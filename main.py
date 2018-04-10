# -*- coding: utf-8 -*-


from myraflib import myEnv
from myraflib import myFit
from myraflib import mySta

import sys
import sip
try:
    apis = ["QDate", "QDateTime", "QString",
        "QTextStream", "QTime", "QUrl", "QVariant"]
    for api in apis:
        sip.setapi(api, 2)
except ValueError:
    # API has already been set so we can't set it again.
    pass

from PyQt4 import QtGui
from PyQt4 import QtCore
import gui as g
import functions as f

from fPlot import *

from uis.main import Ui_MainWindow
from uis.error import Ui_MainWindowErr


#Temporary...
from os import system as temp_sys


class MyForm(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, verb=True):
        super(MyForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.verb = verb
        self.ggui = g.Gui(verb=self.verb)
        self.meetc = myEnv.etc(verb=self.verb)
        self.mefo = myEnv.file_operation(verb=self.verb)
        self.fset = f.settings(verb=self.verb)
        self.mfst = myFit.statistics_operation(verb=self.verb)
        self.mffo = myFit.fits_operation(verb=self.verb)
        self.mfho = myFit.header_operation(verb=self.verb)
        self.msetc = mySta.etc(verb=self.verb)

        self.phot_r_click_coor = [0.0, 0.0]

        #Add icon files.
        icon_app = QtGui.QIcon()
        icon_app.addFile('icons/app/myraf/16x16.png',
            QtCore.QSize(16, 16))
        icon_app.addFile('icons/app/myraf/24x24.png',
            QtCore.QSize(24, 24))
        icon_app.addFile('icons/app/myraf/32x32.png',
            QtCore.QSize(32, 32))
        icon_app.addFile('icons/app/myraf/48x48.png',
            QtCore.QSize(48, 48))
        icon_app.addFile('icons/app/myraf/256x256.png',
            QtCore.QSize(256, 256))
        app.setWindowIcon(icon_app)

        #Desible not ready features
        self.ui.tabWidget.setTabEnabled(5, False)
        self.ui.tabWidget_5.setTabEnabled(4, False)
        self.ui.tabWidget_6.setTabEnabled(0, False)

        #Set display items
        self.cosmic_disp = FitsPlot(self.ui.disp_cosmic_clean.canvas)
        self.manali_disp = FitsPlot(self.ui.disp_man_align.canvas)
        self.autali_disp = FitsPlot(self.ui.disp_aut_align.canvas)
        self.phot_disp = FitsPlot(self.ui.disp_phot.canvas)

        #Popups
        #Bias
        self.popMenu_bias_stat = QtGui.QMenu(self)
        self.popMenu_bias_stat.addAction('Show Stats', lambda:
            self.show_stats(self.ui.listWidget_10))
        self.popMenu_bias_stat.addAction('Show All Stats', lambda:
            self.show_infos_for_all(self.ui.listWidget_10, "Bias Combin"))
        self.popMenu_bias_stat.setEnabled(False)

        self.ui.listWidget_10.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.listWidget_10, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                self.on_context_menu_bias)

        #Dark
        self.popMenu_dark_stat = QtGui.QMenu(self)
        self.popMenu_dark_stat.addAction('Show Stats', lambda:
            self.show_stats(self.ui.listWidget_11))
        self.popMenu_dark_stat.addAction('Show All Stats', lambda:
            self.show_infos_for_all(self.ui.listWidget_11, "Dark Combin"))
        self.popMenu_dark_stat.setEnabled(False)

        self.ui.listWidget_11.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.listWidget_11, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                self.on_context_menu_dark)

        #Flat
        self.popMenu_flat_stat = QtGui.QMenu(self)
        self.popMenu_flat_stat.addAction('Show Stats', lambda:
            self.show_stats(self.ui.listWidget_12))
        self.popMenu_flat_stat.addAction('Show All Stats', lambda:
            self.show_infos_for_all(self.ui.listWidget_12, "Flat Combin"))
        self.popMenu_flat_stat.setEnabled(False)

        self.ui.listWidget_12.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.listWidget_12, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                self.on_context_menu_flat)

        #RunSex
        self.popMenu_run_sex = QtGui.QMenu(self)
        self.popMenu_run_sex.addAction('Run SEX!', lambda:
            self.auto_source_finder())
        self.popMenu_run_sex.addAction('Find MOs', lambda:
            self.run_atrack())
        self.popMenu_run_sex.addAction('Get FWHM', lambda:
            self.show_phot_source_stats())
        self.popMenu_run_sex.setEnabled(False)

        self.ui.disp_phot.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.disp_phot, QtCore.SIGNAL(
            'customContextMenuRequested(const QPoint&)'),
                self.on_context_menu_run_sex)

        #Settings->Load settings
        self.ui.pushButton_70.clicked.connect(lambda: (
            self.load_selected_settings()))
        #Settings->Save settings
        self.ui.pushButton_60.clicked.connect(lambda: (self.save_settings()))

        #Help->Save log
        self.ui.pushButton_10.clicked.connect(lambda: (self.save_logs()))
        #Help->Delete log
        self.ui.pushButton_11.clicked.connect(lambda: (self.delete_log_file()))

        #add to and remove from list triggers
        #Calibration->Data
        self.ui.pushButton_22.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_9)))
        self.ui.pushButton_21.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_9)))
        #Calibration->Bias
        self.ui.pushButton_23.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_10)))
        self.ui.pushButton_24.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_10)))
        #Calibration->Dark
        self.ui.pushButton_27.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_11)))
        self.ui.pushButton_26.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_11)))
        #Calibration->Flat
        self.ui.pushButton_30.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_12)))
        self.ui.pushButton_29.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_12)))
        #Align->Auto
        self.ui.pushButton_2.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget)))
        self.ui.pushButton_3.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget)))
        #Align->Manual
        self.ui.pushButton_6.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_2)))
        self.ui.pushButton_5.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_2)))
        #Photometry->Apperture
        self.ui.pushButton_9.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_3)))
        self.ui.pushButton_8.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_3)))
        #Photometry->Remove from source list
        self.ui.pushButton_32.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_4)))
        #Editor->Header
        self.ui.pushButton_36.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_14)))
        self.ui.pushButton_37.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_14)))
        #Editor->Cosmic Cleaner
        self.ui.pushButton_42.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_16)))
        self.ui.pushButton_41.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_16)))
        #Editor->Convert to Fits
        self.ui.pushButton_45.clicked.connect(lambda: (
            self.add_files_imh(self.ui.listWidget_17)))
        self.ui.pushButton_44.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_17)))
        #Scheduler->Data
        self.ui.pushButton_52.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_19)))
        self.ui.pushButton_51.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_19)))
        #Scheduler->Bias
        self.ui.pushButton_54.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_20)))
        self.ui.pushButton_53.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_20)))
        #Scheduler->Dark
        self.ui.pushButton_56.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_21)))
        self.ui.pushButton_55.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_21)))
        #Scheduler->Flat
        self.ui.pushButton_58.clicked.connect(lambda: (
            self.add_files(self.ui.listWidget_22)))
        self.ui.pushButton_57.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_22)))
        #Scheduler->Remove from source list
        self.ui.pushButton_59.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_23)))
        #Scheduler->Remove from task list
        self.ui.pushButton_48.clicked.connect(lambda: (
            self.rm_files(self.ui.listWidget_18)))

        #Editor->Header->Display headers
        self.ui.listWidget_14.clicked.connect(lambda: (self.load_header()))
        #Editor->Header->Select header
        self.ui.listWidget_13.clicked.connect(lambda: (self.select_header()))
        #Editor->Header->Unlock existing header value
        self.ui.checkBox.clicked.connect(lambda: (
            self.unlock_get_value_from_existing_header()))
        #Editor->Header->Add update header
        self.ui.pushButton_38.clicked.connect(lambda: (
            self.add_update_header()))
        #Editor->Header->Delete header
        self.ui.pushButton_35.clicked.connect(lambda: (self.delete_header()))
        #Editor->Convert to fits
        self.ui.pushButton_46.clicked.connect(lambda: (self.convert_files()))
        #Editor->Cosmic cleaner
        self.ui.pushButton_31.clicked.connect(lambda: (self.save_flat()))
        self.ui.listWidget_16.clicked.connect(lambda: (self.display_cc()))
        #Editor->Load values from observatory file
        self.ui.listWidget_15.clicked.connect(lambda: (self.load_observatory()))
        #Editor->Delete from observatory file
        self.ui.pushButton_39.clicked.connect(lambda: (
            self.delete_observatory()))
        #Editor->Add/Update from observatory file
        self.ui.pushButton_40.clicked.connect(lambda: (
            self.add_update_observatory()))

        #Save Combine
        #Save Zerocombine
        self.ui.pushButton_25.clicked.connect(lambda: (self.save_zero()))
        #Save Darkcombine
        self.ui.pushButton_28.clicked.connect(lambda: (self.save_dark()))
        #Save Flatcombine
        self.ui.pushButton_43.clicked.connect(lambda: (self.cosmic_clean()))

        #Clibration
        self.ui.pushButton.clicked.connect(lambda: (self.calibration()))

        #Align
        #Manual Align display
        self.ui.listWidget_2.clicked.connect(lambda: (self.display_ma()))
        #Manual Align get coord
        self.ui.disp_man_align.canvas.fig.canvas.mpl_connect(
            'button_press_event', self.get_manali_coors)
        #Manual Align Do the harlem shake
        self.ui.pushButton_7.clicked.connect(lambda: (self.manual_align()))
        #Auto Alin display
        self.ui.listWidget.clicked.connect(lambda: (self.display_aa()))
        #Auto Align
        self.ui.pushButton_4.clicked.connect(lambda: (self.auto_align()))

        #Photometry
        #Photometry Display
        self.ui.listWidget_3.clicked.connect(lambda: (self.display_ph()))
        #Photometry Display coordinates
        self.ui.pushButton_33.clicked.connect(lambda: (
            self.display_phot_coor()))
        #Photometry get coord
        self.ui.disp_phot.canvas.fig.canvas.mpl_connect(
            'button_press_event', self.get_phot_coors)
        #Photometry go
        self.ui.pushButton_34.clicked.connect(lambda: (self.ap_photometry()))

        self.initial()

    def run_atrack(self):
        ays = True
        file_count = self.ggui.get_count_of_list(self.ui.listWidget_3)
        if file_count[0]:
            if file_count[1] > 0:
                if file_count[1] > 7:
                    ays = self.ggui.show_are_you_sure(self,
                        "We strongly recommend you to use less then 8 files")
                if ays:
                    file_list = self.ggui.get_all_items_from_list(
                        self.ui.listWidget_3)
                    atrack_dir = self.mefo.get_atrack_dir()
                    myraf_dir = self.mefo.get_myraf_dir()
                    if atrack_dir[0]:
                        if file_list[0]:
                            for i in file_list[1]:
                                self.mefo.cp_file(i, atrack_dir[1])
                            temp_sys(
                                "python3 atrack.py --skip-pngs %s" %
                                (atrack_dir[1]))
                            coor_file = open("%s/atrack/results.txt" % (
                                atrack_dir[1]))
                            mos_coors = []
                            for i in coor_file:
                                mos_coors.append(i.replace("\n", "").split())
                            mos_to_use = []
                            for i in mos_coors:
                                if not i[0] in mos_to_use:
                                    mos_to_use.append(i[0])

                            if not len(mos_coors) == 0:
                                self.show_error_form(title="Info",
                                    owner="Atrack-Moving objects below found.",
                                    disp=mos_to_use)

                        else:
                            self.ggui.show_dialog(self,
                                "critic", "Photometry", "Can not get file list")
            else:
                self.ggui.show_dialog(self, "critic",
                    "Photometry", "Add some files first")
        else:
            self.ggui.show_dialog(self, "critic",
                "Photometry", "Can not get file count")

    def ap_photometry(self):
        do_phot = False
        file_count = self.ggui.get_count_of_list(self.ui.listWidget_3)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_3)
                if file_list[0]:
                    coor_count = self.ggui.get_count_of_list(
                        self.ui.listWidget_4)
                    if coor_count[0]:
                        if coor_count[1] > 0:
                            do_phot = True
                        else:
                            self.ggui.show_dialog(self, "critic",
                                "Photometry", "Add some sources first")
                    else:
                        self.ggui.show_dialog(self, "critic", "Photometry",
                            "Can not get source count")
                else:
                    self.ggui.show_dialog(self, "critic", "Photometry",
                        "Can not get file list")
            else:
                self.ggui.show_dialog(self, "critic", "Photometry",
                    "Add some files first")
        else:
            self.ggui.show_dialog(self, "critic", "Photometry",
                "Can not get file count")

        if do_phot:
            annu = "25"
            dann = "5"
            cbox = "10"
            expt = "exptime"
            aper = "10,15,20,25,30"
            zmag = "25"
            gain = "gain"
            tobs = "time-obs",
            subs = "filter"

            set_file_name = self.current_set_file_name()
            if set_file_name[0]:
                current_set_file = "./sessions/%s.set" % (set_file_name[1])
                pfsp_set = self.fset.read_settings_phot_fitskypar(
                    current_set_file)
                if pfsp_set[0]:
                    annu = pfsp_set[1]["phot_fsp_annu"]
                    dann = pfsp_set[1]["phot_fsp_dann"]
                    cbox = pfsp_set[1]["phot_fsp_cbox"]

                pdp_set = self.fset.read_settings_phot_datapar(current_set_file)
                if pdp_set[0]:
                    expt = pdp_set[1]["phot_dap_expo"]
                    subs = pdp_set[1]["phot_dap_fltr"]

                ppp_set = self.fset.read_settings_phot_photpar(current_set_file)
                if ppp_set[0]:
                    aper = ppp_set[1]["phot_php_aper"]
                    zmag = ppp_set[1]["phot_php_zmag"]
                    gain = ppp_set[1]["phot_php_gain"]

                plt_set = self.fset.read_settings_phot_locTime(current_set_file)
                if plt_set[0]:
                    tobs = plt_set[1]["phot_loti_tmob"]

        if do_phot:
            has_header = []
            no_header = []
            for i in file_list[1]:
                if not self.mfho.does_header_exist(i, expt):
                    no_header.append("%s Has not %s header" % (i, expt))
                else:
                    if not self.mfho.does_header_exist(i, gain):
                        no_header.append("%s Has not %s header" % (i, gain))
                    else:
                        if not self.mfho.does_header_exist(i, tobs):
                            no_header.append("%s Has not %s header" % (i, tobs))
                        else:
                            if not self.mfho.does_header_exist(i, subs):
                                no_header.append(
                                    "%s Has not %s header" % (i, subs))
                            else:
                                has_header.append(i)
            coors = self.ggui.get_all_items_from_list(self.ui.listWidget_4)
            last_coor = []
            if coors[0]:
                for i in coors[1]:
                    last_coor.append(i.replace(" - ", " "))

                out_file = self.ggui.get_file(self, "res.my", "my")
                file_count = len(has_header)
                it = 0
                if out_file[0]:
                    wtf = open(out_file[1], "w")
                    atrack_dir = self.mefo.get_atrack_dir()
                    for i in has_header:
                        it = it + 1
                        final_coor = []
                        for z in last_coor:
                            if len(z.split(" ")) < 2:
                                if atrack_dir[0]:
                                    mos_coors = open(
                                        "%s/atrack/results.txt" % (
                                            atrack_dir[1]), "r")
                                    for u in mos_coors:
                                        ln = u.replace("\n", "")
                                        if ln.startswith(z):
                                            line_splt = ln.split()
                                            if int(line_splt[1]) == int(it - 1):
                                                final_coor.append(
                                                    "%s %s" % (line_splt[3],
                                                        line_splt[4]))
                                    mos_coors.close()
                            else:
                                final_coor.append(z)

                        mags = self.mffo.photometry(i, out_file[1], final_coor,
                            aper, annu, dann, cbox, tobs, expt,
                            zmag, gain, subs)
                        final_coor = []
                        if mags[0]:
                            for u in mags[1]:
                                wtf.write("%s %s\n" % (i, u))

                        self.ui.progressBar_4.setValue(
                            self.ggui.calc_percentage(it, file_count))

                    wtf.close()

        if not len(no_header) == 0:
            self.show_error_form(
                title="Error", owner="Photometry", disp=no_header)
        self.ui.progressBar_4.setValue(0)

    def show_phot_source_stats(self):
        coors = self.phot_r_click_coor
        file_name = self.ggui.get_item_from_list(self.ui.listWidget_3)
        if file_name[0]:
            stats = self.mfst.get_stats_object(file_name[1], coors)
            if stats[0]:
                self.ggui.show_dialog(self, "info", "Statics For Object",
                    "File: %s\nx:%s, y:%s\nFWHM:%s" % (file_name[1],
                    stats[1][0], stats[1][1], stats[1][2]))
                use_it = self.ggui.show_are_you_sure(self,
                    "Do you want me to use FWHM*2.5 as Aperture?")
                if use_it:
                    self.ui.lineEdit_35.setText("%s,%s,%s" % (
                        int(abs(-5 + float(stats[1][2]) * 2.5)),
                        int(abs(float(stats[1][2]) * 2.5)),
                        int(abs(5 + float(stats[1][2]) * 2.5))))
            else:
                self.ggui.show_dialog(self, "critic",
                    "Photometry", "Can not get statistics")
        else:
            self.ggui.show_dialog(self, "critic",
                "Photometry", "Can not get file")

    def auto_source_finder(self):
        count = 25
        set_file_name = self.current_set_file_name()
        if set_file_name[0]:
            current_set_file = "./sessions/%s.set" % (set_file_name[1])
            stfn_set = self.fset.read_settings_phot_starfind(current_set_file)
            count = float(stfn_set[1]["phot_stfi_mstf"])

        file_name = self.ggui.get_item_from_list(self.ui.listWidget_3)
        if file_name[0]:
            src = self.mfst.get_sources(file_name[1], count=count)
            if src[0]:
                send_it = []
                for i in src[1]:
                    send_it.append("%s - %s - %s" % (i[2], i[0], i[1]))
                self.show_error_form(title="Detected Objects",
                    owner="Photometry", disp=send_it)
            else:
                self.ggui.show_dialog(self, "critic",
                    "Photometry", "Auto Source Finder Failed")
        else:
            self.ggui.show_dialog(self, "critic",
                "Photometry", "Can not get file")

    def display_phot_coor(self):
        file_name = self.ggui.get_item_from_list(self.ui.listWidget_3)
        if file_name[0]:
            self.display_ph()
            coors_count = self.ggui.get_count_of_list(self.ui.listWidget_4)
            if coors_count[0]:
                if coors_count[1] > 0:
                    coors = self.ggui.get_selected_items_from_list(
                        self.ui.listWidget_4)
                    if coors[0]:
                        set_file_name = self.current_set_file_name()
                        if set_file_name[0]:
                            current_set_file = "./sessions/%s.set" % (
                                set_file_name[1])
                            phot_set = self.fset.read_settings_phot_photpar(
                                current_set_file)
                            app = 20.0
                            if phot_set[0]:
                                appers = phot_set[1]["phot_php_aper"].split(",")
                                all_appers = 0
                                for i in appers:
                                    all_appers = all_appers + float(i)
                                app = all_appers / len(appers)

                            phot_set = self.fset.read_settings_phot_fitskypar(
                                current_set_file)
                            ann = 25
                            dan = 5
                            if phot_set[0]:
                                ann = float(phot_set[1]["phot_fsp_annu"])
                                dan = float(phot_set[1]["phot_fsp_dann"])
                            it = 0
                            for i in coors[1]:
                                it = it + 1
                                x = float(i.split(" - ")[0])
                                y = float(i.split(" - ")[1])
                                self.ggui.draw_a_circle(self.ui.disp_phot, x, y,
                                    app, "#ffff00")
                                self.ggui.draw_a_circle(self.ui.disp_phot, x, y,
                                    app + ann, "#ff00ff")
                                self.ggui.draw_a_circle(self.ui.disp_phot, x, y,
                                    app + ann + dan, "#00ffff", label=it)
                                self.ui.progressBar_4.setValue(
                                    self.ggui.calc_percentage(
                                        it, len(coors[1])))
        self.ui.progressBar_4.setValue(0)

    def get_phot_coors(self, event):
        if event.button == 1:
            if event.ydata is not None and event.xdata is not None:
                file_name = self.ggui.get_item_from_list(self.ui.listWidget_3)
                if file_name[0]:
                    x = event.xdata
                    y = event.ydata
                    coor_line = "%s - %s" % (x, y)
                    self.ggui.set_values_to_list(
                        self, self.ui.listWidget_4, [coor_line])
        else:
            x = event.xdata
            y = event.ydata
            self.phot_r_click_coor = [x, y]

    def display_ph(self):
        file_name = self.ggui.get_item_from_list(self.ui.listWidget_3)
        if file_name[0]:
            self.ggui.display(str(file_name[1]), self.phot_disp)

        coor_list = self.ggui.get_all_items_from_list(self.ui.listWidget_4)
        if coor_list[0]:
            if coor_list[1] > 0:
                atrack_dir = self.mefo.get_atrack_dir()
                width = self.mfho.get_header(str(file_name[1]), "i_naxis1")
                if width[0]:
                    radi = int(int(width[1]) / 50)
                else:
                        radi = 30

                for i in coor_list[1]:
                    if len(i.split(" - ")) < 2:
                        cur_index = self.ggui.get_current_index_from_list(
                            self.ui.listWidget_3)
                        if atrack_dir[0]:
                            mos_coors = open("%s/atrack/results.txt" % (
                                atrack_dir[1]), "r")
                            for u in mos_coors:
                                ln = u.replace("\n", "")
                                if u.startswith(i):
                                    ln = u.split()
                                    if cur_index[0]:
                                        if int(cur_index[1]) == int(ln[1]):
                                            self.ggui.draw_a_circle(
                                                self.ui.disp_phot, ln[3], ln[4],
                                                        radi, "#FF0000",
                                                        label="MO%s" % (
                                                            ln[0]))

                            mos_coors.close()
                    else:
                        x, y = i.split(" - ")
                        self.ggui.draw_a_circle(self.ui.disp_phot,
                            x, y, radi, "#00FFFF")

        self.update_info()

    def auto_align(self):
        file_count = self.ggui.get_count_of_list(self.ui.listWidget)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget)
                if file_list[0]:
                    ref_image = self.ggui.get_current_item_from_list(
                        self.ui.listWidget)
                    if ref_image[0]:
                        failed_files = []
                        it = 0
                        out_dir = self.ggui.get_folder(self)
                        if out_dir[0]:
                            for i in file_list[1]:
                                it = it + 1
                                if not self.mffo.auto_align(str(i),
                                    str(ref_image[1]), str(out_dir[1])):
                                    failed_files.append(
                                        "Can not align file(%s)" % (i))
                                self.ui.label_2.setText(i)
                                self.ui.progressBar_2.setValue(
                                    self.ggui.calc_percentage(
                                        it, file_count[1]))
                            if not len(failed_files) == 0:
                                self.show_error_form(title="Error",
                                    owner="%s - %s" % ("Manual Align",
                                        "Failed with files below"),
                                            disp=failed_files)
                            self.ui.progressBar_2.setValue(0)

                    else:
                        self.ggui.show_dialog(self, "critic", "Auto Align",
                            "Please select a reference image")
                else:
                    self.ggui.show_dialog(self, "critic", "Auto Align",
                        "Can not get file list")
            else:
                self.ggui.show_dialog(self, "critic", "Auto Align",
                    "Add some files first")
        else:
            self.ggui.show_dialog(self, "critic", "Auto Align",
                "Can not get file count")

    def manual_align(self):
        file_count = self.ggui.get_count_of_list(self.ui.listWidget_2)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_2)
                if file_list[0]:
                    ref_image = self.ggui.get_current_item_from_list(
                        self.ui.listWidget_2)
                    if ref_image[0]:
                        ref_coor = self.mfho.get_header(ref_image[1], "MYCOOR")
                        if ref_coor[0]:
                            x_ref, y_ref = ref_coor[1].replace(
                                "\"", "").split("-")
                            x_ref = float(x_ref)
                            y_ref = float(y_ref)
                            it = 0
                            failed_files = []
                            out_dir = self.ggui.get_folder(self)
                            if out_dir[0]:
                                for i in file_list[1]:
                                    pfn = self.mefo.get_base_name(i)
                                    if pfn:
                                        it = it + 1
                                        coor = self.mfho.get_header(i, "MYCOOR")
                                        if coor[0]:
                                            x, y = coor[1].replace(
                                                "\"", "").split("-")
                                            x = float(x)
                                            y = float(y)

                                            x_diif = x_ref - x
                                            y_diif = y_ref - y

                                            if not self.mffo.manual_align(i,
                                                x_diif, y_diif, "%s/%s" %
                                                (out_dir[1], pfn[1][1])):
                                                failed_files.append(
                                                    "Can not align dile(%s)" % (
                                                        i))
                                        else:
                                            failed_files.append(
                                                "No coor found for file(%s)" % (
                                                    i))
                                    self.ui.label_4.setText(i)
                                    self.ui.progressBar_3.setValue(
                                        self.ggui.calc_percentage(
                                            it, file_count[1]))

                                if not len(failed_files) == 0:
                                    self.show_error_form(title="Error",
                                        owner="%s - %s" % ("Manual Align",
                                            "Failed with files below"),
                                                disp=failed_files)
                                self.ui.progressBar_3.setValue(0)

                        else:
                            self.ggui.show_dialog(self, "critic",
                                "Manual Align",
                                "Can not get referance image's coordinates")
                    else:
                        self.ggui.show_dialog(self, "critic",
                            "Manual Align", "Select a reference image first!")

            else:
                self.ggui.show_dialog(self, "critic",
                    "Cosmic Cleaner", "Add some files first.")
        else:
            self.ggui.show_dialog(self, "critic",
                "Cosmic Cleaner", "Can not get file list")

    def get_manali_coors(self, event):
        if event.button == 1:
            if event.ydata is not None and event.xdata is not None:
                file_count = self.ggui.get_count_of_list(self.ui.listWidget_2)
                if file_count[0]:
                    if file_count[1] > 0:
                        total_rows = file_count[1] - 1
                        cuurent_row = self.ggui.get_current_index_from_list(
                            self.ui.listWidget_2)
                        file_name = self.ggui.get_current_item_from_list(
                            self.ui.listWidget_2)
                        if file_name[0]:
                            if self.mefo.is_file(file_name[1]):
                                x = event.xdata
                                y = event.ydata
                                self.mfho.add_update_header(file_name[1],
                                    "MYCOOR", '%s - %s' % (x, y))
                                if cuurent_row[0]:
                                    if total_rows > cuurent_row[1]:
                                        self.ggui.set_current_index_to_list(
                                            self.ui.listWidget_2,
                                            cuurent_row[1] + 1)
                                    else:
                                        self.ggui.set_current_index_to_list(
                                            self.ui.listWidget_2, 0)

                                    self.display_ma()

    def display_aa(self):
        file_name = self.ggui.get_item_from_list(self.ui.listWidget)
        if file_name[0]:
            self.ggui.display(str(file_name[1]), self.autali_disp)

    def display_ma(self):
        file_name = self.ggui.get_item_from_list(self.ui.listWidget_2)
        if file_name[0]:
            self.ggui.display(str(file_name[1]), self.manali_disp)
            if self.mfho.does_header_exist(str(file_name[1]), "MYCOOR"):
                coors = self.mfho.get_header(str(file_name[1]), "MYCOOR")
                if coors[0]:
                    self.ui.label_3.setText(coors[1].replace("\"", ""))
                    x, y = coors[1].replace("\"", "").split("-")
                    width = self.mfho.get_header(str(file_name[1]), "i_naxis1")
                    if width[0]:
                        radi = int(int(width[1]) / 50)
                    else:
                        radi = 30
                    self.ggui.draw_a_circle(self.ui.disp_man_align, x, y,
                        radi, "#00FFFF")
            else:
                self.ui.label_3.setText("")

    def add_update_observatory(self):
        observat = self.ui.lineEdit_3.text().strip()
        name = self.ui.lineEdit_4.text().strip()
        longitude = self.ui.lineEdit_5.text().strip()
        latitude = self.ui.lineEdit_6.text().strip()
        altitude = self.ui.lineEdit_7.text().strip()
        timezone = self.ui.lineEdit_8.text().strip()

        if (observat == "") or (name == "") or (longitude == "") or (
            latitude == "") or (altitude == "") or (timezone == ""):
            self.ggui.show_dialog(self, "critic",
                "Observatory Editor - Add/Update", "Fill all fields first!")
        else:
            comm = self.ui.plainTextEdit.toPlainText()
            if self.mefo.create_obs_file(observat, name, longitude, latitude,
                altitude, timezone, comm=comm):
                self.load_observatories()

    def delete_observatory(self):
        selected_item = self.ggui.get_item_from_list(self.ui.listWidget_15)
        if selected_item[0]:
            obs_file = "./observatories/%s" % (selected_item[1])
            if self.mefo.is_file(obs_file):
                if self.mefo.delete_file(obs_file):
                    self.load_observatories()
        else:
            self.ggui.show_dialog(self, "critic",
                "Observatory Editor - Delete", "Choose an Observatory first!")

    def load_observatory(self):
        selected_item = self.ggui.get_item_from_list(self.ui.listWidget_15)
        if selected_item[0]:
            vals = self.mefo.get_values_from_obs_file(selected_item[1])
            if vals[0]:
                self.ui.lineEdit_3.setText(str(vals[1]["observatory"]))
                self.ui.lineEdit_4.setText(str(vals[1]["name"]))
                self.ui.lineEdit_5.setText(str(vals[1]["longitude"]))
                self.ui.lineEdit_6.setText(str(vals[1]["latitude"]))
                self.ui.lineEdit_7.setText(str(vals[1]["altitude"]))
                self.ui.lineEdit_8.setText(str(vals[1]["timezone"]))
                self.ui.plainTextEdit.setPlainText(str(vals[1]["commands"]))

    def load_observatories(self):
        all_files = self.mefo.get_file_name_list("./observatories/", "*")
        if all_files[0]:
            self.ggui.reload_list_with_new_items(self,
                self.ui.listWidget_15, all_files[1])
            self.ui.listWidget_15.sortItems()

    def calibration(self):
        set_file_name = self.current_set_file_name()
        if set_file_name[0]:
            current_set_file = "./sessions/%s.set" % (set_file_name[1])

        do_bias = False
        do_dark = False
        do_flat = False
        err_bias = []
        err_dark = []
        err_flat = []
        err_all = []
        it = 0

        bias_file_count = self.ggui.get_count_of_list(self.ui.listWidget_10)
        if bias_file_count[0]:
            if bias_file_count[1] > 0:
                do_bias = True
                bias_set = self.fset.read_settings_calib_zerocombine(
                    current_set_file)

        dark_file_count = self.ggui.get_count_of_list(self.ui.listWidget_11)
        if dark_file_count[0]:
            if dark_file_count[1] > 0:
                do_dark = True
                dark_set = self.fset.read_settings_calib_darkcombine(
                    current_set_file)

        flat_file_count = self.ggui.get_count_of_list(self.ui.listWidget_12)
        if flat_file_count[0]:
            if flat_file_count[1] > 0:
                do_flat = True
                flat_set = self.fset.read_settings_calib_flatcombine(
                    current_set_file)

        cali_set = self.fset.read_settings_calib_calib(current_set_file)

        out_dir = self.mefo.get_tmp_dir()

        if do_bias:

            do_bias = False

            b_comb = "median"
            b_reje = "minmax"
            b_ccdt = ""

            if bias_set[0]:
                if bias_set[1]["cali_zero_comb"] == '0':
                    b_comb = "median"
                elif bias_set[1]["cali_zero_comb"] == '1':
                    b_comb = "average"
                else:
                    b_comb = "average"

                if bias_set[1]["cali_zero_reje"] == '0':
                    b_reje = "none"
                elif bias_set[1]["cali_zero_reje"] == '1':
                    b_reje = "minmax"
                elif bias_set[1]["cali_zero_reje"] == '2':
                    b_reje = "ccdclip"
                elif bias_set[1]["cali_zero_reje"] == '3':
                    b_reje = "crreject"
                elif bias_set[1]["cali_zero_reje"] == '4':
                    b_reje = "sigclip"
                elif bias_set[1]["cali_zero_reje"] == '5':
                    b_reje = "avsigclip"
                elif bias_set[1]["cali_zero_reje"] == '6':
                    b_reje = "pclip"
                else:
                    b_reje = "none"

                b_ccdt = bias_set[1]["cali_zero_ccty"]

                b_data_count = self.ggui.get_count_of_list(
                    self.ui.listWidget_10)
                if b_data_count[0]:
                    if b_data_count[1] > 0:
                        b_data_list = self.ggui.get_all_items_from_list(
                            self.ui.listWidget_10)
                        if b_data_list[0]:
                            if out_dir[0]:
                                out_file = "%s/%s" % (out_dir[1],
                                    "zero.fits")
                                if self.mffo.zerocombine(b_data_list[1],
                                    out_file, combine=b_comb, reject=b_reje,
                                    ccdtype=b_ccdt):
                                    do_bias = True
                                else:
                                    err_bias = ["Zerocombine failed"]

        if do_dark:

            do_dark = False

            d_comb = "median"
            d_reje = "minmax"
            d_scal = "exposure"
            d_ccdt = ""

            if dark_set[0]:
                if dark_set[1]["cali_dark_comb"] == '0':
                    d_comb = "median"
                elif dark_set[1]["cali_dark_comb"] == '1':
                    d_comb = "average"
                else:
                    d_comb = "average"

                if dark_set[1]["cali_dark_reje"] == '0':
                    d_reje = "none"
                elif dark_set[1]["cali_dark_reje"] == '1':
                    d_reje = "minmax"
                elif dark_set[1]["cali_dark_reje"] == '2':
                    d_reje = "ccdclip"
                elif dark_set[1]["cali_dark_reje"] == '3':
                    d_reje = "crreject"
                elif dark_set[1]["cali_dark_reje"] == '4':
                    d_reje = "sigclip"
                elif dark_set[1]["cali_dark_reje"] == '5':
                    d_reje = "avsigclip"
                elif dark_set[1]["cali_dark_reje"] == '6':
                    d_reje = "pclip"
                else:
                    d_reje = "none"

                if dark_set[1]["cali_dark_scal"] == '0':
                    d_scal = "exposure"
                elif dark_set[1]["cali_dark_scal"] == '1':
                    d_scal = "none"
                elif dark_set[1]["cali_dark_scal"] == '2':
                    d_scal = "mode"
                elif dark_set[1]["cali_dark_scal"] == '3':
                    d_scal = "median"
                elif dark_set[1]["cali_dark_scal"] == '4':
                    d_scal = "mean"
                else:
                    d_scal = "none"

                d_ccdt = dark_set[1]["cali_dark_ccty"]

                d_data_count = self.ggui.get_count_of_list(
                    self.ui.listWidget_11)
                if d_data_count[0]:
                    if d_data_count[1] > 0:
                        d_data_list = self.ggui.get_all_items_from_list(
                            self.ui.listWidget_11)
                        if d_data_list[0]:
                            if out_dir[0]:
                                out_file = "%s/%s" % (out_dir[1],
                                "dark.fits")
                                if self.mffo.darkcombine(d_data_list[1],
                                    out_file, combine=d_comb, reject=d_reje,
                                    scale=d_scal, ccdtype=d_ccdt):
                                    do_dark = True
                                else:
                                    err_dark = ["Darkcombine Failed"]

        if do_flat:

            do_flat = False

            f_comb = "median"
            f_reje = "minmax"
            f_subset = "no"
            f_ccdt = ""

            if cali_set[0]:
                if cali_set[1]["cali_cali_subs"] == '0':
                    f_subset = "yes"
                elif cali_set[1]["cali_cali_subs"] == '1':
                    f_subset = "no"
                else:
                    f_subset = "no"

            if flat_set[0]:
                if flat_set[1]["cali_flat_comb"] == '0':
                    f_comb = "median"
                elif flat_set[1]["cali_flat_comb"] == '1':
                    f_comb = "average"
                else:
                    f_comb = "average"

                if flat_set[1]["cali_flat_reje"] == '0':
                    f_reje = "none"
                elif flat_set[1]["cali_flat_reje"] == '1':
                    f_reje = "minmax"
                elif flat_set[1]["cali_flat_reje"] == '2':
                    f_reje = "ccdclip"
                elif flat_set[1]["cali_flat_reje"] == '3':
                    f_reje = "crreject"
                elif flat_set[1]["cali_flat_reje"] == '4':
                    f_reje = "sigclip"
                elif flat_set[1]["cali_flat_reje"] == '5':
                    f_reje = "avsigclip"
                elif flat_set[1]["cali_flat_reje"] == '6':
                    f_reje = "pclip"
                else:
                    f_reje = "none"

                f_ccdt = flat_set[1]["cali_flat_ccty"]

                f_data_count = self.ggui.get_count_of_list(
                    self.ui.listWidget_12)
                if f_data_count[0]:
                    if f_data_count[1] > 0:
                        flt_files = self.ggui.get_all_items_from_list(
                            self.ui.listWidget_12)
                        if flt_files[0]:
                            if f_subset == "yes":
                                dp_set = self.fset.read_settings_phot_datapar(
                                    current_set_file)
                                if dp_set[0]:
                                    fltr_value = dp_set[1]["phot_dap_fltr"]
                                    has_header = []
                                    for i in flt_files[1]:
                                        if self.mfho.does_header_exist(i,
                                            fltr_value):
                                            if self.mfho.add_update_header(i,
                                                "subset", "'(@\"%s\")'" % (
                                                    fltr_value)):
                                                has_header.append(i)
                                            else:
                                                err_all.append(
                                                    "%s Can't add header(%s)"
                                                    % (i, fltr_value))
                                        else:
                                            err_all.append(
                                                "%s header not found(%s)" % (
                                                    i, fltr_value))

                                    if out_dir[0]:
                                        out_files = out_dir[1]
                                        if self.mffo.flatcombine(has_header,
                                            out_files, combine=f_comb,
                                            reject=f_reje, subset="yes",
                                            ccdtype=f_ccdt):
                                            do_flat = True
                                        else:
                                            err_flat = ["Flatcombine Failed"]

                            else:
                                if out_dir[0]:
                                    out_file = "%s/%s" % (out_dir[1],
                                        "myraf_flat.fit")
                                    if self.mffo.flatcombine(flt_files[1],
                                        out_file, combine=f_comb,
                                        reject=f_reje, subset="no",
                                        ccdtype=f_ccdt):
                                        do_flat = True
                                    else:
                                        err_flat = ["Flatcombine Failed"]

        data_count = self.ggui.get_count_of_list(self.ui.listWidget_9)
        if data_count[0]:
            if data_count[1] > 0:
                all_data = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_9)
                subset = "no"
                ccdty = ""
                if all_data[0]:
                    if cali_set[0]:
                        if cali_set[1]["cali_cali_subs"] == '0':
                            subset = "yes"
                        elif cali_set[1]["cali_cali_subs"] == '1':
                            subset = "no"
                        else:
                            subset = "no"

                        if do_bias:
                            the_bias_file = "%s/%s" % (out_dir[1], "zero.fits")
                        else:
                            the_bias_file = ""

                        if do_dark:
                            the_dark_file = "%s/%s" % (out_dir[1], "dark.fit")
                        else:
                            the_dark_file = ""

                        if do_flat:
                            the_flat_file = "%s/%s" % (out_dir[1],
                                "flat_*.fits")
                        else:
                            the_flat_file = ""

                        if do_bias or do_dark or do_flat:
                            ccdty = cali_set[1]["cali_cali_ccty"]
                            cal_has_header = []
                            cal_out_dir = self.ggui.get_folder(self)
                            if cal_out_dir[0]:
                                if subset == "yes":
                                    dp_set = \
                                    self.fset.read_settings_phot_datapar(
                                        current_set_file)
                                    if dp_set[0]:
                                        fltr_value = dp_set[1]["phot_dap_fltr"]
                                        for i in all_data[1]:
                                            if self.mfho.does_header_exist(
                                                i, fltr_value):
                                                if self.mfho.add_update_header(
                                                    i, "subset", "'(@\"%s\")'"
                                                    % (fltr_value)):
                                                    cal_has_header.append(i)
                                                else:
                                                    err_all.append("%s%s" % (i,
                                                    "Can not add header(%s)" % (
                                                        fltr_value)))
                                            else:
                                                err_all.append(
                                                    "%s header not found(%s)" %
                                                    (i, fltr_value))

                                        for i in cal_has_header:
                                            pfn = self.mefo.get_base_name(i)
                                            if pfn:
                                                it = it + 1
                                                if not self.mffo.calibration(i,
                                                    "%s/%s" % (cal_out_dir[1],
                                                        pfn[1][1]),
                                                    bias_file=the_bias_file,
                                                    dark_file=the_dark_file,
                                                    flat_file=the_flat_file,
                                                    ccdty=ccdty, subs="yes"):
                                                    err_all.append(
                                                        "Calibration Failed(%s)"
                                                        % (i))
                                                self.ui.label.setText(i)
                                                self.ui.progressBar_6.setValue(
                                                    self.ggui.calc_percentage(
                                                        it,
                                                        len(cal_has_header)))
                                if subset == "no":
                                    for i in cal_has_header:
                                        pfn = self.mefo.get_base_name(i)
                                        if pfn:
                                            it = it + 1
                                            if not self.mffo.calibration(i,
                                                "%s/%s" % (cal_out_dir[1],
                                                    pfn[1][1]),
                                                bias_file=the_bias_file,
                                                dark_file=the_dark_file,
                                                flat_file=the_flat_file,
                                                ccdty=ccdty, subs="no"):
                                                err_all.append("%s%s" % (i,
                                                "Can not do the calibration"))

                                        self.ui.label.setText(i)
                                        self.ui.progressBar_6.setValue(
                                            self.ggui.calc_percentage(it,
                                                len(cal_has_header)))

                        else:
                            self.ggui.show_dialog(self, "info",
                                "Calibration", "Nothing to do")

                if not len(err_bias) == 0:
                    err_all.append(err_bias)
                if not len(err_dark) == 0:
                    err_all.append(err_dark)
                if not len(err_flat) == 0:
                    err_all.append(err_flat)

                if not len(err_all) == 0:
                    self.show_error_form(title="Error", owner="%s - %s" % (
                        "Calibration", "Failed with files below"),
                            disp=err_all)

            else:
                self.ggui.show_dialog(self, "critic",
                    "Calibration", "Add some files first.")
        else:
            self.ggui.show_dialog(self, "critic",
                "Calibration", "Can not get file list")

    def display_cc(self):
        file_name = self.ggui.get_item_from_list(self.ui.listWidget_16)
        if file_name[0]:
            self.ggui.display(str(file_name[1]), self.cosmic_disp)

    def cosmic_clean(self):
        set_file_name = self.current_set_file_name()
        if set_file_name[0]:
            current_set_file = "./sessions/%s.set" % (set_file_name[1])
            the_set = self.fset.read_settings_ccleaner(current_set_file)
            acmf = False
            gain = 2.2
            read_noise = 10
            sigma_clip = 5
            sigma_frac = 0.3
            object_lim = 5
            if the_set[0]:
                if the_set[1]['coce_acmf'] == "t":
                    acmf = True
                else:
                    acmf = False
                gain = float(the_set[1]['coce_gain'])
                read_noise = float(the_set[1]['coce_reno'])
                sigma_clip = float(the_set[1]['coce_sicl'])
                sigma_frac = float(the_set[1]['coce_sifr'])
                object_lim = float(the_set[1]['coce_obli'])

        file_count = self.ggui.get_count_of_list(self.ui.listWidget_16)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_16)
                if file_list[0]:
                    it = 0
                    failed_files = []
                    out_dir = self.ggui.get_folder(self)
                    if out_dir[0]:
                        for i in file_list[1]:
                            pfn = self.mefo.get_base_name(i)
                            if pfn:
                                it = it + 1
                                self.ggui.display(str(i), self.cosmic_disp)
                                if not self.mffo.cosmic_clean(str(i),
                                    "%s/%s" % (out_dir[1], pfn[1][1]),
                                    mask=acmf, gain=gain, readnoise=read_noise,
                                    sigclip=sigma_clip, sigfrac=sigma_frac,
                                    objlim=object_lim):
                                    failed_files.append(i)
                            self.ui.label_17.setText(i)
                            self.ui.progressBar_6.setValue(
                                self.ggui.calc_percentage(it, file_count[1]))

                        if not len(failed_files) == 0:
                            self.show_error_form(title="Error",
                                owner="%s - %s" % ("Cosmic Cleaner",
                                    "Failed with files below"),
                                        disp=failed_files)
                        self.ui.progressBar_6.setValue(0)
            else:
                self.ggui.show_dialog(self, "critic",
                    "Cosmic Cleaner", "Add some files first.")
        else:
            self.ggui.show_dialog(self, "critic",
                "Cosmic Cleaner", "Can not get file list")

    def convert_files(self):
        file_count = self.ggui.get_count_of_list(self.ui.listWidget_17)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_17)
                if file_list[0]:
                    it = 0
                    failed_files = []
                    out_dir = self.ggui.get_folder(self)
                    if out_dir[0]:
                        for i in file_list[1]:
                            pfn = self.mefo.get_base_name(i)
                            if pfn:
                                it = it + 1
                                if not self.mffo.convert_to_fits(
                                    str(i), "%s/%s" % (out_dir[1], pfn[1][1])):
                                    failed_files.append(i)
                                self.ui.label_18.setText(i)
                                self.ui.progressBar_7.setValue(
                                    self.ggui.calc_percentage(
                                        it, file_count[1]))

                    if not len(failed_files) == 0:
                        self.show_error_form(title="Error",
                            owner="Convert tp Fits - Failed with files below",
                            disp=failed_files)

                    self.ui.progressBar_7.setValue(0)
            else:
                self.ggui.show_dialog(self, "critic",
                    "Fits Coverter", "Add some files first.")
        else:
            self.ggui.show_dialog(self, "critic",
                "Fits Coverter", "Can not get file list")

    def delete_header(self):
        file_count = self.ggui.get_count_of_list(self.ui.listWidget_14)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_14)
                if file_list[0]:
                    key = self.ui.lineEdit.text()
                    failed_files = []
                    it = 0
                    for i in file_list[1]:
                        it = it + 1
                        if not self.mfho.delete_header(i, key):
                            failed_files.append(i)
                        self.ui.label_16.setText(i)
                        self.ui.progressBar_5.setValue(
                            self.ggui.calc_percentage(it, file_count[1]))

                    if not len(failed_files) == 0:
                        self.show_error_form(title="Error",
                            owner="Header Editor - Failed with files below",
                            disp=failed_files)

                    self.ui.progressBar_5.setValue(0)
                    self.load_header()
            else:
                self.ggui.show_dialog(self, "critic",
                    "Header Editor", "Add some files first.")
        else:
            self.ggui.show_dialog(self, "critic",
                "Header Editor", "Can not get file list")

    def add_update_header(self):
        file_count = self.ggui.get_count_of_list(self.ui.listWidget_14)
        if file_count[0]:
            if file_count[1] > 0:
                file_list = self.ggui.get_all_items_from_list(
                    self.ui.listWidget_14)
                if file_list[0]:
                    key = self.ui.lineEdit.text()

                    failed_files = []
                    if self.ggui.is_checked(self.ui.checkBox):
                        selected_header_key = self.ggui.get_item_from_combo(
                            self.ui.comboBox)
                        if selected_header_key[0]:
                            header_source = str(
                                selected_header_key[1].split("=")[0].strip())
                            it = 0
                            for i in file_list[1]:
                                it = it + 1
                                val = self.mfho.get_header(i, header_source)
                                if val[0]:
                                    self.mfho.add_update_header(i, key, val[1])
                                else:
                                    failed_files.append(i)
                        else:
                            failed_files.append(i)
                    else:
                        val = self.ui.lineEdit_2.text()

                        it = 0
                        for i in file_list[1]:
                            it = it + 1
                            if not self.mfho.add_update_header(i, key, val):
                                failed_files.append(i)
                            self.ui.label_16.setText(i)
                            self.ui.progressBar_5.setValue(
                                self.ggui.calc_percentage(it, file_count[1]))

                    if not len(failed_files) == 0:
                        self.show_error_form(title="Error",
                            owner="Header Editor - Failed with files below",
                            disp=failed_files)

                    self.ui.progressBar_5.setValue(0)
                    self.load_header()
            else:
                self.ggui.show_dialog(self, "critic",
                    "Header Editor", "Add some files first.")
        else:
            self.ggui.show_dialog(self, "critic",
                "Header Editor", "Can not get file list")

    def unlock_get_value_from_existing_header(self):
        self.ggui.set_enabled(self.ui.comboBox,
            self.ggui.is_checked(self.ui.checkBox))
        self.ggui.set_enabled(self.ui.lineEdit_2,
            not self.ggui.is_checked(self.ui.checkBox))

    def select_header(self):
        header_and_value = self.ggui.get_item_from_list(self.ui.listWidget_13)
        if header_and_value[0]:
            h = header_and_value[1].split("=")[0].strip()
            v = header_and_value[1].split("=")[1].strip()
            self.ui.lineEdit.setText(h)
            self.ui.lineEdit_2.setText(v)

    def list_headers(self, file_name):
        headers = self.mfho.get_list_header(file_name)
        hlist = []
        if headers[0]:
            for i in headers[1]:
                hlist.append("%s = %s" % (i[0], i[1]))
            self.ggui.reload_list_with_new_items(self,
                self.ui.listWidget_13, hlist)
            self.ggui.reload_combo_with_new_items(self,
                self.ui.comboBox, hlist)
        else:
            self.ggui.show_dialog(self, "critic", "Header Editor",
            "Can not get header from file")

    def load_header(self):
        file_name = self.ggui.get_item_from_list(self.ui.listWidget_14)
        if file_name[0]:
            self.list_headers(file_name[1])

    def save_flat(self):
        set_file_name = self.current_set_file_name()
        if set_file_name[0]:
            current_set_file = "./sessions/%s.set" % (set_file_name[1])
            the_set = self.fset.read_settings_calib_flatcombine(
                current_set_file)
            comb = "median"
            reje = "minmax"
            subset = "no"
            ccdt = ""
            if the_set[0]:

                if the_set[1]["cali_flat_comb"] == '0':
                    comb = "median"
                elif the_set[1]["cali_flat_comb"] == '1':
                    comb = "average"
                else:
                    comb = "average"

                if the_set[1]["cali_flat_reje"] == '0':
                    reje = "none"
                elif the_set[1]["cali_flat_reje"] == '1':
                    reje = "minmax"
                elif the_set[1]["cali_flat_reje"] == '2':
                    reje = "ccdclip"
                elif the_set[1]["cali_flat_reje"] == '3':
                    reje = "crreject"
                elif the_set[1]["cali_flat_reje"] == '4':
                    reje = "sigclip"
                elif the_set[1]["cali_flat_reje"] == '5':
                    reje = "avsigclip"
                elif the_set[1]["cali_flat_reje"] == '6':
                    reje = "pclip"
                else:
                    reje = "none"

                if the_set[1]["cali_flat_subs"] == '0':
                    subset = "yes"
                elif the_set[1]["cali_flat_subs"] == '1':
                    subset = "no"
                else:
                    subset = "no"

                ccdt = the_set[1]["cali_flat_ccty"]

                data_count = self.ggui.get_count_of_list(self.ui.listWidget_12)
                if data_count[0]:
                    if data_count[1] > 0:
                        flt_files = self.ggui.get_all_items_from_list(
                            self.ui.listWidget_12)
                        if flt_files[0]:
                            if subset == "yes":
                                dp_set = self.fset.read_settings_phot_datapar(
                                    current_set_file)
                                if dp_set[0]:
                                    fltr_value = dp_set[1]["phot_dap_fltr"]
                                    no_header = []
                                    has_header = []
                                    for i in flt_files[1]:
                                        if self.mfho.does_header_exist(
                                            i, fltr_value):
                                            if self.mfho.add_update_header(i,
                                                "subset", "'(@\"%s\")'" % (
                                                    fltr_value)):
                                                has_header.append(i)
                                            else:
                                                no_header.append(i)
                                        else:
                                            no_header.append(i)

                                    out_dir = self.ggui.get_folder(self)
                                    if out_dir[0]:
                                        out_file = out_dir[1]
                                        if not self.mffo.flatcombine(has_header,
                                            out_file, combine=comb, reject=reje,
                                            subset="yes", ccdtype=ccdt):
                                            self.ggui.show_dialog(self,
                                                "critic", "Flatcombine",
                                                "Can not create master flats.")

                                    if len(no_header):
                                        self.show_error_form(
                                            title="Flatcombine",
                                            owner="No (%s) found. Skiped" % (
                                                fltr_value), disp=no_header)

                            else:
                                out_file = self.ggui.get_file(self, "flat.fit",
                                    "fit")
                                if out_file[0]:
                                    if not self.mffo.flatcombine(flt_files[1],
                                        out_file[1], combine=comb, reject=reje,
                                        subset="no", ccdtype=ccdt):
                                        self.ggui.show_dialog(self, "critic",
                                            "Flatcombine",
                                            "Can not create master flat.")

    def save_dark(self):
        set_file_name = self.current_set_file_name()
        if set_file_name[0]:
            current_set_file = "./sessions/%s.set" % (set_file_name[1])
            the_set = self.fset.read_settings_calib_darkcombine(
                current_set_file)
            comb = "median"
            reje = "minmax"
            scal = "exposure"
            ccdt = ""
            if the_set[0]:

                if the_set[1]["cali_dark_comb"] == '0':
                    comb = "median"
                elif the_set[1]["cali_dark_comb"] == '1':
                    comb = "average"
                else:
                    comb = "average"

                if the_set[1]["cali_dark_reje"] == '0':
                    reje = "none"
                elif the_set[1]["cali_dark_reje"] == '1':
                    reje = "minmax"
                elif the_set[1]["cali_dark_reje"] == '2':
                    reje = "ccdclip"
                elif the_set[1]["cali_dark_reje"] == '3':
                    reje = "crreject"
                elif the_set[1]["cali_dark_reje"] == '4':
                    reje = "sigclip"
                elif the_set[1]["cali_dark_reje"] == '5':
                    reje = "avsigclip"
                elif the_set[1]["cali_dark_reje"] == '6':
                    reje = "pclip"
                else:
                    reje = "none"

                if the_set[1]["cali_dark_scal"] == '0':
                    scal = "exposure"
                elif the_set[1]["cali_dark_scal"] == '1':
                    scal = "none"
                elif the_set[1]["cali_dark_scal"] == '2':
                    scal = "mode"
                elif the_set[1]["cali_dark_scal"] == '3':
                    scal = "median"
                elif the_set[1]["cali_dark_scal"] == '4':
                    scal = "mean"
                else:
                    scal = "none"

                ccdt = the_set[1]["cali_dark_ccty"]

                data_count = self.ggui.get_count_of_list(self.ui.listWidget_11)
                if data_count[0]:
                    if data_count[1] > 0:
                        data_list = self.ggui.get_all_items_from_list(
                            self.ui.listWidget_11)
                        if data_list[0]:
                            out_file = self.ggui.get_file(self,
                                "dark.fit", "fit")
                            if out_file[0]:
                                if not self.mffo.darkcombine(data_list[1],
                                    out_file[1], combine=comb, reject=reje,
                                    scale=scal, ccdtype=ccdt):
                                    self.ggui.show_dialog(self, "critic",
                                    "Darkcombine",
                                    "Can not create master dark.")
                        else:
                            self.ggui.show_dialog(self, "critic",
                                "Darkcombine", "Can not get file list.")
                    else:
                        self.ggui.show_dialog(self, "critic",
                            "Darkcombine", "No file found.")
                else:
                    self.ggui.show_dialog(self, "critic",
                        "Darkcombine", "Add some files first.")

    def save_zero(self):
        set_file_name = self.current_set_file_name()
        if set_file_name[0]:
            current_set_file = "./sessions/%s.set" % (set_file_name[1])
            the_set = self.fset.read_settings_calib_zerocombine(
                current_set_file)
            comb = "median"
            reje = "minmax"
            ccdt = ""
            if the_set[0]:

                if the_set[1]["cali_zero_comb"] == '0':
                    comb = "median"
                elif the_set[1]["cali_zero_comb"] == '1':
                    comb = "average"
                else:
                    comb = "average"

                if the_set[1]["cali_zero_reje"] == '0':
                    reje = "none"
                elif the_set[1]["cali_zero_reje"] == '1':
                    reje = "minmax"
                elif the_set[1]["cali_zero_reje"] == '2':
                    reje = "ccdclip"
                elif the_set[1]["cali_zero_reje"] == '3':
                    reje = "crreject"
                elif the_set[1]["cali_zero_reje"] == '4':
                    reje = "sigclip"
                elif the_set[1]["cali_zero_reje"] == '5':
                    reje = "avsigclip"
                elif the_set[1]["cali_zero_reje"] == '6':
                    reje = "pclip"
                else:
                    reje = "none"

                ccdt = the_set[1]["cali_zero_ccty"]

                data_count = self.ggui.get_count_of_list(self.ui.listWidget_10)
                if data_count[0]:
                    if data_count[1] > 0:
                        data_list = self.ggui.get_all_items_from_list(
                            self.ui.listWidget_10)
                        if data_list[0]:
                            out_file = self.ggui.get_file(
                                self, "zero.fit", "fit")
                            if out_file[0]:
                                if not self.mffo.zerocombine(data_list[1],
                                    out_file[1], combine=comb,
                                    reject=reje, ccdtype=ccdt):
                                    self.ggui.show_dialog(self, "critic",
                                    "Zerocombine",
                                    "Can not create master zero.")
                        else:
                            self.ggui.show_dialog(self, "critic",
                                "Zerocombine", "Can not get file list.")
                    else:
                        self.ggui.show_dialog(self, "critic",
                            "Zerocombine", "No file found.")
                else:
                    self.ggui.show_dialog(self, "critic",
                        "Zerocombine", "Add some files first.")

    def save_settings(self):
        set_name = str(self.ui.lineEdit_47.text())

        gen_cpus = str(self.ui.dial_2.value())

        cal_zero_comb = str(self.ui.comboBox_12.currentIndex())
        cal_zero_rejc = str(self.ui.comboBox_13.currentIndex())
        cal_zero_ccdt = str(self.ui.lineEdit_21.text())

        cal_dark_comb = str(self.ui.comboBox_14.currentIndex())
        cal_dark_rejc = str(self.ui.comboBox_15.currentIndex())
        cal_dark_scale = str(self.ui.comboBox_16.currentIndex())
        cal_dark_ccdt = str(self.ui.lineEdit_30.text())

        cal_flat_comb = str(self.ui.comboBox_17.currentIndex())
        cal_flat_rejc = str(self.ui.comboBox_18.currentIndex())
        cal_flat_subs = str(self.ui.comboBox_19.currentIndex())
        cal_flat_ccdt = str(self.ui.lineEdit_31.text())

        cal_cali_subs = str(self.ui.comboBox_20.currentIndex())
        cal_cali_ccdt = str(self.ui.lineEdit_32.text())

        phot_fsp_anna = str(self.ui.doubleSpinBox_8.value())
        phot_fsp_dand = str(self.ui.doubleSpinBox_9.value())
        phot_fsp_cbox = str(self.ui.doubleSpinBox_15.value())

        phot_dpe_xpti = str(self.ui.lineEdit_33.text())
        phot_dpt_filt = str(self.ui.lineEdit_34.text())

        phot_php_aper = str(self.ui.lineEdit_35.text())
        phot_php_zmag = str(self.ui.lineEdit_36.text())
        phot_php_gain = str(self.ui.lineEdit_37.text())
        phot_php_fxpx = str(self.ui.lineEdit_38.text())

        phot_wcs_raa = str(self.ui.lineEdit_39.text())
        phot_wcs_dec = str(self.ui.lineEdit_40.text())

        phot_lot_obse = str(self.ui.lineEdit_42.text())
        if self.ggui.is_checked(self.ui.checkBox_13):
            phot_lot_tmsp = "t"
        else:
            phot_lot_tmsp = "f"

        phot_lot_time = str(self.ui.lineEdit_43.text())
        phot_lot_date = str(self.ui.lineEdit_44.text())
        if self.ggui.is_checked(self.ui.checkBox_5):
            phot_lot_epca = "t"
        else:
            phot_lot_epca = "f"

        phot_lot_epch = str(self.ui.lineEdit_41.text())

        phot_stf_fxra = str(self.ui.doubleSpinBox_16.value())
        phot_stf_mnfh = str(self.ui.doubleSpinBox_17.value())
        phot_stf_mxfh = str(self.ui.doubleSpinBox_18.value())
        phot_stf_mstf = str(self.ui.doubleSpinBox_19.value())

        phot_hex = ""
        all_items = self.ggui.get_all_items_from_list(self.ui.listWidget_26)
        if all_items[0]:
            for i in all_items[1]:
                phot_hex = "%s,%s" % (phot_hex, i)

        if self.ggui.is_checked(self.ui.checkBox_17):
            phot_ccl_acmf = "t"
        else:
            phot_ccl_acmf = "f"

        phot_ccl_gain = str(self.ui.doubleSpinBox_20.value())
        phot_ccl_rnoi = str(self.ui.doubleSpinBox_21.value())
        phot_ccl_scli = str(self.ui.doubleSpinBox_22.value())
        phot_ccl_sfra = str(self.ui.doubleSpinBox_23.value())
        phot_ccl_olim = str(self.ui.doubleSpinBox_24.value())

        phot_wct_serv = str(self.ui.lineEdit_45.text())
        phot_wct_apke = str(self.ui.lineEdit_46.text())

        phot_wct_befl = ""
        if self.ui.radioButton_4.isChecked():
            phot_wct_befl = "Nothing"
        elif self.ui.radioButton_5.isChecked():
            phot_wct_befl = "Compress"
        elif self.ui.radioButton_6.isChecked():
            phot_wct_befl = "Binary"
        else:
            phot_wct_befl = "Nothing"

        if self.ggui.is_checked(self.ui.checkBox_20):
            phot_wct_abap = "t"
        else:
            phot_wct_abap = "f"

        if self.ggui.is_checked(self.ui.checkBox_21):
            phot_wct_scli = "t"
        else:
            phot_wct_scli = "f"

        self.fset.create_settings(set_name, gen_cpus=gen_cpus,
            cal_zero_comb=cal_zero_comb, cal_zero_rejc=cal_zero_rejc,
            cal_zero_ccdt=cal_zero_ccdt, cal_dark_comb=cal_dark_comb,
            cal_dark_rejc=cal_dark_rejc, cal_dark_scale=cal_dark_scale,
            cal_dark_ccdt=cal_dark_ccdt, cal_flat_comb=cal_flat_comb,
            cal_flat_rejc=cal_flat_rejc, cal_flat_subs=cal_flat_subs,
            cal_flat_ccdt=cal_flat_ccdt, cal_cali_subs=cal_cali_subs,
            cal_cali_ccdt=cal_cali_ccdt, phot_fsp_anna=phot_fsp_anna,
            phot_fsp_dand=phot_fsp_dand, phot_fsp_cbox=phot_fsp_cbox,
            phot_dpe_xpti=phot_dpe_xpti, phot_dpt_filt=phot_dpt_filt,
            phot_php_aper=phot_php_aper, phot_php_zmag=phot_php_zmag,
            phot_php_gain=phot_php_gain, phot_php_fxpx=phot_php_fxpx,
            phot_wcs_raa=phot_wcs_raa, phot_wcs_dec=phot_wcs_dec,
            phot_lot_obse=phot_lot_obse, phot_lot_tmsp=phot_lot_tmsp,
            phot_lot_time=phot_lot_time, phot_lot_date=phot_lot_date,
            phot_lot_epca=phot_lot_epca, phot_lot_epch=phot_lot_epch,
            phot_stf_fxra=phot_stf_fxra, phot_stf_mnfh=phot_stf_mnfh,
            phot_stf_mxfh=phot_stf_mxfh, phot_stf_mstf=phot_stf_mstf,
            phot_hex=phot_hex, phot_ccl_acmf=phot_ccl_acmf,
            phot_ccl_gain=phot_ccl_gain, phot_ccl_rnoi=phot_ccl_rnoi,
            phot_ccl_scli=phot_ccl_scli, phot_ccl_sfra=phot_ccl_sfra,
            phot_ccl_olim=phot_ccl_olim, phot_wct_serv=phot_wct_serv,
            phot_wct_apke=phot_wct_apke, phot_wct_befl=phot_wct_befl,
            phot_wct_abap=phot_wct_abap, phot_wct_scli=phot_wct_scli)

    def add_files_imh(self, list_widget):
        files = self.ggui.get_file_list(self,
        "All Files (*.*);;FIT or FITS (*.fits *.fit *.fits);;IMH (*.img)",
        check_fits=False)
        if files[0]:
            self.ggui.set_values_to_list(self, list_widget, files[1])
        else:
            self.ggui.show_dialog(self, "info",
                "File Problem", "No file selected!")

        self.load_logs()
        self.update_info()

    def add_files(self, list_widget):
        files = self.ggui.get_file_list(self,
        "FIT or FITS (*.fits *.fit *.fits)")
        if files[0]:
            self.ggui.set_values_to_list(self, list_widget, files[1])
        else:
            self.ggui.show_dialog(self, "info",
                "File Problem", "No file selected!")

        self.load_logs()
        self.update_info()

    def delete_log_file(self):
        if self.ggui.show_are_you_sure(self, "%s\n%s" % (
            "Are you sure you want to dlete log files?",
            "We highly recommend you to save the log files first.")):
            self.mefo.delete_log_files()
        self.load_logs()

    def rm_files(self, list_widget):
        self.ggui.remove_values_from_list(list_widget)
        self.update_info()

    def load_selected_settings(self):
        set_name = self.ggui.get_current_item_from_combo(self.ui.comboBox_21)
        if set_name[0]:
            self.load_settings(set_name[1])

        self.load_logs()

    def initial(self):
        self.refresh_settings_list()
        csfn = self.current_set_file_name()
        if csfn[0]:
            self.load_settings(csfn[1])

        self.load_logs()
        self.update_info()
        self.load_observatories()

    def refresh_settings_list(self):
        set_file_list = self.mefo.get_file_name_list("./sessions/", "*.set")
        if set_file_list[0]:
            self.ggui.reload_combo_with_new_items(self,
                self.ui.comboBox_21, set_file_list[1])
        self.load_logs()

    def current_set_file_name(self):
        ret = [False, None]
        try:
            cur_set = open("sessions/current")
            for i in cur_set:
                ret = [True, i.strip()]
        except Exception as e:
            self.meetc.print_if(e)

        self.load_logs()
        return ret

    def load_logs(self):
        list_of_logs = self.meetc.get_mini_log_file()
        if list_of_logs[0]:
            self.ggui.reload_list_with_new_items(self,
                self.ui.listWidget_28, list_of_logs[1])

        log_file_size = self.mefo.get_total_log_file_size()
        if log_file_size[0]:
            self.ui.label_6.setText(
                "Total Log file size is: %s" % (log_file_size[1]))

    def load_settings(self, set_file_name):
        current_set_file = "./sessions/%s.set" % (set_file_name)

        self.ui.lineEdit_47.setText(set_file_name)

        set_cpu_num = self.fset.read_settings_general_cpu(current_set_file)
        if set_cpu_num[0]:
            self.ui.dial_2.setValue(int(set_cpu_num[1]["cpus"]))

        cur_cal_set = self.fset.read_settings_calibration(current_set_file)
        if cur_cal_set[0]:
            self.ui.comboBox_12.setCurrentIndex(
                int(cur_cal_set[1]["cali_zero_comb"]))
            self.ui.comboBox_13.setCurrentIndex(
                int(cur_cal_set[1]["cali_zero_reje"]))
            self.ui.lineEdit_21.setText(
                cur_cal_set[1]["cali_zero_ccty"].strip())

            self.ui.comboBox_17.setCurrentIndex(
                int(cur_cal_set[1]["cali_flat_comb"]))
            self.ui.comboBox_18.setCurrentIndex(
                int(cur_cal_set[1]["cali_flat_reje"]))
            self.ui.comboBox_19.setCurrentIndex(
                int(cur_cal_set[1]["cali_flat_subs"]))
            self.ui.lineEdit_31.setText(
                cur_cal_set[1]["cali_flat_ccty"].strip())

            self.ui.comboBox_14.setCurrentIndex(
                int(cur_cal_set[1]["cali_dark_comb"]))
            self.ui.comboBox_15.setCurrentIndex(
                int(cur_cal_set[1]["cali_dark_reje"]))
            self.ui.comboBox_16.setCurrentIndex(
                int(cur_cal_set[1]["cali_dark_scal"]))
            self.ui.lineEdit_30.setText(
                cur_cal_set[1]["cali_dark_ccty"].strip())

            self.ui.comboBox_20.setCurrentIndex(
                int(cur_cal_set[1]["cali_cali_subs"]))
            self.ui.lineEdit_32.setText(
                cur_cal_set[1]["cali_cali_ccty"].strip())

        cur_phot_set = self.fset.read_settings_photometry(current_set_file)
        if cur_phot_set[0]:
            self.ui.doubleSpinBox_8.setValue(
                float(cur_phot_set[1]["phot_fsp_annu"]))
            self.ui.doubleSpinBox_9.setValue(
                float(cur_phot_set[1]["phot_fsp_dann"]))
            self.ui.doubleSpinBox_15.setValue(
                float(cur_phot_set[1]["phot_fsp_cbox"]))

            self.ui.lineEdit_33.setText(
                cur_phot_set[1]["phot_dap_expo"])
            self.ui.lineEdit_34.setText(
                cur_phot_set[1]["phot_dap_fltr"])

            self.ui.lineEdit_35.setText(
                cur_phot_set[1]["phot_php_aper"])
            self.ui.lineEdit_36.setText(
                cur_phot_set[1]["phot_php_zmag"])
            self.ui.lineEdit_37.setText(
                cur_phot_set[1]["phot_php_gain"])
            self.ui.lineEdit_38.setText(
                cur_phot_set[1]["phot_php_fxpx"])

            self.ui.lineEdit_39.setText(
                cur_phot_set[1]["phot_pwcs_rias"])
            self.ui.lineEdit_40.setText(
                cur_phot_set[1]["phot_pwcs_decl"])

            self.ui.lineEdit_42.setText(
                cur_phot_set[1]["phot_loti_obsv"])
            self.ui.lineEdit_43.setText(
                cur_phot_set[1]["phot_loti_tmob"])
            self.ui.lineEdit_44.setText(
                cur_phot_set[1]["phot_loti_dtob"])
            self.ui.lineEdit_41.setText(
                cur_phot_set[1]["phot_loti_epoc"])

            if cur_phot_set[1]["phot_loti_tmsp"] == "t":
                self.ui.checkBox_13.setChecked(True)
                self.ggui.timestamp_checked(self, True)
            else:
                self.ui.checkBox_13.setChecked(False)
                self.ggui.timestamp_checked(self, False)

            if cur_phot_set[1]["phot_loti_epca"] == "t":
                self.ggui.epoch_calculator(self, True)
            else:
                self.ggui.epoch_calculator(self, False)

            self.ui.doubleSpinBox_16.setValue(
                float(cur_phot_set[1]["phot_stfi_flra"]))
            self.ui.doubleSpinBox_17.setValue(
                float(cur_phot_set[1]["phot_stfi_mifh"]))
            self.ui.doubleSpinBox_18.setValue(
                float(cur_phot_set[1]["phot_stfi_mafh"]))
            self.ui.doubleSpinBox_19.setValue(
                float(cur_phot_set[1]["phot_stfi_mstf"]))

            extraction = []
            for i in cur_phot_set[1]["phot_heex_extr"].split(","):
                extraction.append(i)

            self.ggui.reload_list_with_new_items(self,
                self.ui.listWidget_26, extraction)

        cur_cclean_set = self.fset.read_settings_ccleaner(current_set_file)
        if cur_cclean_set[0]:
            if cur_cclean_set[1]["coce_acmf"] == "t":
                self.ggui.set_state(self.ui.checkBox_17, True)
            else:
                self.ggui.set_state(self.ui.checkBox_17, False)

            self.ui.doubleSpinBox_20.setValue(
                float(cur_cclean_set[1]["coce_gain"]))
            self.ui.doubleSpinBox_21.setValue(
                float(cur_cclean_set[1]["coce_reno"]))
            self.ui.doubleSpinBox_22.setValue(
                float(cur_cclean_set[1]["coce_sicl"]))
            self.ui.doubleSpinBox_23.setValue(
                float(cur_cclean_set[1]["coce_sifr"]))
            self.ui.doubleSpinBox_24.setValue(
                float(cur_cclean_set[1]["coce_obli"]))

        cur_wcs_set = self.fset.read_settings_wcs(current_set_file)
        if cur_wcs_set[0]:
            self.ui.lineEdit_45.setText(cur_wcs_set[1]["wcs_serv"])
            self.ui.lineEdit_46.setText(cur_wcs_set[1]["wcs_apke"])

            if cur_wcs_set[1]["wcs_belo"] == "Nothing":
                self.ui.radioButton_4.setChecked(True)
            elif cur_wcs_set[1]["wcs_belo"] == "Compress":
                self.ui.radioButton_5.setChecked(True)
            elif cur_wcs_set[1]["wcs_belo"] == "Binary":
                self.ui.radioButton_6.setChecked(True)
            else:
                self.ui.radioButton.setChecked(True)

            if cur_wcs_set[1]["wcs_abap"] == "t":
                self.ggui.set_state(self.ui.checkBox_20, True)
            else:
                self.ggui.set_state(self.ui.checkBox_20, False)

            if cur_wcs_set[1]["wcs_cwhs"] == "t":
                self.ggui.set_state(self.ui.checkBox_21, True)
            else:
                self.ggui.set_state(self.ui.checkBox_21, False)

        self.mefo.write_to_file("sessions/current",
            set_file_name, "w", force=True)

        self.load_logs()

    def show_stats(self, list_dev):
        file_name = self.ggui.get_current_item_from_list(list_dev)
        if file_name[0]:
            stat = self.mfst.get_stats([file_name[1]])
            if stat[0]:
                    pfn = self.mefo.get_base_name(stat[1][0][0])
                    if pfn[0]:
                        self.ggui.show_dialog(self, "info", "stats",
                            "File Name: %s\nStddev: %s\nMean: %s" % (
                                pfn[1][1], stat[1][0][3], stat[1][0][2]))
        self.load_logs()

    def show_infos_for_all(self, lst_dev, owner):
        res = []
        it = 0
        list_of_files = self.ggui.get_all_items_from_list(lst_dev)
        cou = self.ggui.get_count_of_list(lst_dev)
        if cou[0]:
            if list_of_files[0]:
                for i in list_of_files[1]:
                    it = it + 1
                    stats = self.mfst.get_stats([i])
                    if stats[0]:
                        res.append(
                            "%s, MEAN:%s, STDDEV:%s, MIN:%s, MAX:%s" % (
                                stats[1][0][0], stats[1][0][2], stats[1][0][3],
                                stats[1][0][4], stats[1][0][5]))
                    self.ui.progressBar.setValue(
                        self.ggui.calc_percentage(float(it), float(cou[1])))
        self.ui.progressBar.setValue(0)
        self.show_error_form(title="Resoullt of imstatistics", owner=owner,
            disp=res)

        self.load_logs()

    def on_context_menu_bias(self, point):
        self.popMenu_bias_stat.exec_(self.ui.listWidget_10.mapToGlobal(point))

    def on_context_menu_dark(self, point):
        self.popMenu_dark_stat.exec_(self.ui.listWidget_11.mapToGlobal(point))

    def on_context_menu_flat(self, point):
        self.popMenu_flat_stat.exec_(self.ui.listWidget_12.mapToGlobal(point))

    def on_context_menu_run_sex(self, point):
        self.popMenu_run_sex.exec_(self.ui.disp_phot.mapToGlobal(point))

    def save_logs(self):
        file_to_save = self.ggui.get_file(self, "MYRaf.log", "log")
        all_lines = self.ggui.get_all_items_from_list(self.ui.listWidget_28)
        if file_to_save[0]:
            if all_lines[0]:
                self.mefo.save_1d_array_to_file(file_to_save[1], all_lines[1])
        self.load_logs()

    def show_error_form(self, title="Error",
    owner="No one", disp=["Noting to show"]):
        self.load_logs()
        err_dia = MyFormErr(self,
            verb=True, header=title, who_sent=owner, values=disp)
        err_dia.setParent(form2load)
        flags = QtCore.Qt.Tool
        err_dia.setWindowFlags(flags)

        position = self.pos()
        self_height = err_dia.height()
        self_width = err_dia.width()
        pos_x = position.x()
        pos_y = position.y()
        err_pos_y = (pos_y + self_height / 2)
        err_pos_x = (pos_x + self_width / 2)
        err_dia.setGeometry(err_pos_x, err_pos_y, 500, 300)

        err_dia.show()

    def update_info(self):
        cou_data = 0
        data = self.ggui.get_count_of_list(self.ui.listWidget_9)
        cou_bias = 0
        bias = self.ggui.get_count_of_list(self.ui.listWidget_10)
        cou_dark = 0
        dark = self.ggui.get_count_of_list(self.ui.listWidget_11)
        cou_flat = 0
        flat = self.ggui.get_count_of_list(self.ui.listWidget_12)

        if data[0]:
            cou_data = data[1]
        if bias[0]:
            cou_bias = bias[1]
        if dark[0]:
            cou_dark = dark[1]
        if flat[0]:
            cou_flat = flat[1]

        pho_file = self.ggui.get_current_item_from_list(self.ui.listWidget_3)

        if pho_file[0]:
            self.popMenu_run_sex.setEnabled(True)
        else:
            self.popMenu_run_sex.setEnabled(False)

        if cou_bias == 0:
            self.popMenu_bias_stat.setEnabled(False)
        else:
            self.popMenu_bias_stat.setEnabled(True)

        if cou_dark == 0:
            self.popMenu_dark_stat.setEnabled(False)
        else:
            self.popMenu_dark_stat.setEnabled(True)

        if cou_flat == 0:
            self.popMenu_flat_stat.setEnabled(False)
        else:
            self.popMenu_flat_stat.setEnabled(True)

        self.ui.label_10.setText("%s file(s) selected" % (cou_data))
        self.ui.label_11.setText("%s file(s) selected" % (cou_bias))
        self.ui.label_12.setText("%s file(s) selected" % (cou_dark))
        self.ui.label_13.setText("%s file(s) selected" % (cou_flat))

        self.ui.label.setText("%s %s %s Bias(es), %s Dark(s), %s Flat(s)" % (
            cou_data, "file(s) will be calibrated using",
            cou_bias, cou_dark, cou_flat))


class MyFormErr(QtGui.QMainWindow, Ui_MainWindowErr):
    def __init__(self, parent=None, verb=True, header="Error",
        who_sent="Unknown", values=["Nothing to show"]):
        super(MyFormErr, self).__init__()
        self.ui = Ui_MainWindowErr()
        self.ui.setupUi(self)
        self.verb = verb
        self.ggui = g.Gui(verb=self.verb)
        self.mefo = myEnv.file_operation(verb=self.verb)
        self.who_sent = who_sent

        self.setWindowTitle("MYRaf 3 - %s" % (header))
        self.ui.Err_label.setText(who_sent)
        self.ggui.reload_list_with_new_items(
            self, self.ui.Err_listWidget, values)

        self.ui.Err_pushButton.clicked.connect(lambda:
            self.save_res(self.ui.Err_listWidget))

        self.ui.Err_pushButton_2.clicked.connect(lambda: self.close_me())

        if who_sent == "Bias Combin":
            self.popMenu_dark_stat_select_over_bias = QtGui.QMenu(self)
            self.popMenu_dark_stat_select_over_bias.addAction(
                'Select on Bias Combin', lambda: self.re_select(
                    parent.ui.listWidget_10, self.ui.Err_listWidget))

            self.ui.Err_listWidget.setContextMenuPolicy(
                QtCore.Qt.CustomContextMenu)
            self.connect(self.ui.Err_listWidget, QtCore.SIGNAL(
                'customContextMenuRequested(const QPoint&)'),
                    self.on_context_menu_select_over_bias)

        if who_sent == "Dark Combin":
            self.popMenu_dark_stat_select_over_dark = QtGui.QMenu(self)
            self.popMenu_dark_stat_select_over_dark.addAction(
                'Select on Dark Combin', lambda: self.re_select(
                    parent.ui.listWidget_11, self.ui.Err_listWidget))

            self.ui.Err_listWidget.setContextMenuPolicy(
                QtCore.Qt.CustomContextMenu)
            self.connect(self.ui.Err_listWidget, QtCore.SIGNAL(
                'customContextMenuRequested(const QPoint&)'),
                    self.on_context_menu_select_over_dark)

        if who_sent == "Flat Combin":
            self.popMenu_dark_stat_select_over_flat = QtGui.QMenu(self)
            self.popMenu_dark_stat_select_over_flat.addAction(
                'Select on Flat Combin', lambda: self.re_select(
                    parent.ui.listWidget_12, self.ui.Err_listWidget))

            self.ui.Err_listWidget.setContextMenuPolicy(
                QtCore.Qt.CustomContextMenu)
            self.connect(self.ui.Err_listWidget, QtCore.SIGNAL(
                'customContextMenuRequested(const QPoint&)'),
                    self.on_context_menu_select_over_flat)

        if who_sent == "Photometry":
            self.popMenu_display_on_image = QtGui.QMenu(self)
            self.popMenu_display_on_image.addAction(
                'Show me', lambda: self.show_on_phot(parent))
            self.popMenu_display_on_image.addAction(
                'Add to Sources List', lambda: self.get_coors(parent))

            self.ui.Err_listWidget.setContextMenuPolicy(
                QtCore.Qt.CustomContextMenu)
            self.connect(self.ui.Err_listWidget, QtCore.SIGNAL(
                'customContextMenuRequested(const QPoint&)'),
                    self.on_context_menu_show_on_phot)

        if who_sent == "Atrack-Moving objects below found.":
            self.popMenu_add_mos_source = QtGui.QMenu(self)
            self.popMenu_add_mos_source.addAction(
                'Add to list', lambda: self.add_mos_to_list(parent))

            self.ui.Err_listWidget.setContextMenuPolicy(
                QtCore.Qt.CustomContextMenu)
            self.connect(self.ui.Err_listWidget, QtCore.SIGNAL(
                'customContextMenuRequested(const QPoint&)'),
                    self.on_context_menu_add_mos_source)

    def add_mos_to_list(self, parent):
        coors = self.ggui.get_selected_items_from_list(self.ui.Err_listWidget)
        if coors[0]:
            self.ggui.set_values_to_list(
                parent, parent.ui.listWidget_4, coors[1])

    def get_coors(self, parent):
        coors = self.ggui.get_selected_items_from_list(self.ui.Err_listWidget)
        add_coors = []
        if coors[0]:
            for i in coors[1]:
                x = float(i.split(" - ")[1])
                y = float(i.split(" - ")[2])
                add_coors.append("%s - %s" % (x, y))

            self.ggui.set_values_to_list(parent,
                parent.ui.listWidget_4, add_coors)

    def show_on_phot(self, parent):
        parent.display_ph()
        coors = self.ggui.get_selected_items_from_list(self.ui.Err_listWidget)
        app = 20
        ann = 25
        dan = 5
        it = 0
        if coors[0]:
            for i in coors[1]:
                it = it + 1
                flux = float(i.split(" - ")[0])
                x = float(i.split(" - ")[1])
                y = float(i.split(" - ")[2])
                self.ggui.draw_a_circle(parent.ui.disp_phot, x, y,
                    app, "#ffff00")
                self.ggui.draw_a_circle(parent.ui.disp_phot, x, y,
                    app + ann, "#ff00ff")
                self.ggui.draw_a_circle(parent.ui.disp_phot, x, y,
                    app + ann + dan, "#00ffff", label=flux)

                parent.ui.progressBar_4.setValue(
                    self.ggui.calc_percentage(it, len(coors[1])))
        parent.ui.progressBar_4.setValue(0)

    def save_res(self, lst_dev):
        file_to_save = self.ggui.get_file(self, "%s.txt" % (
            self.who_sent), "txt")
        all_lines = self.ggui.get_all_items_from_list(lst_dev)
        if file_to_save[0]:
            if all_lines[0]:
                self.mefo.save_1d_array_to_file(file_to_save[1], all_lines[1])

    def re_select(self, remote_list_dev, local_list_dev):
        list_of_indexes = self.ggui.get_list_index_of_selected_items_from_list(
            local_list_dev)
        if list_of_indexes[0]:
            self.ggui.select_given_range_in_list(remote_list_dev,
                list_of_indexes[1])

    def on_context_menu_add_mos_source(self, point):
        self.popMenu_add_mos_source.exec_(
            self.ui.Err_listWidget.mapToGlobal(point))

    def on_context_menu_select_over_bias(self, point):
        self.popMenu_dark_stat_select_over_bias.exec_(
            self.ui.Err_listWidget.mapToGlobal(point))

    def on_context_menu_select_over_dark(self, point):
        self.popMenu_dark_stat_select_over_dark.exec_(
            self.ui.Err_listWidget.mapToGlobal(point))

    def on_context_menu_select_over_flat(self, point):
        self.popMenu_dark_stat_select_over_flat.exec_(
            self.ui.Err_listWidget.mapToGlobal(point))

    def on_context_menu_show_on_phot(self, point):
        self.popMenu_display_on_image.exec_(
            self.ui.Err_listWidget.mapToGlobal(point))

    def close_me(self):
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form2load = MyForm()
    form2load.show()
    app.exec_()
