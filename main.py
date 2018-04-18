# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:54:39 2018

@author: mshem
"""

from matplotlib.patches import Circle

from myraf import Ui_Form
from PyQt5 import QtWidgets
from sys import argv

#Importing myraf's GUI
import gui as g
from fPlot import FitsPlot

#Importing myraf's needed modules
from myraflib import myEnv
from myraflib import myAst
from myraflib import myCos

class MyForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, verb=True):
        super(MyForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.verb = verb
        self.srttings_file = "./set.myc"
        
        self.etc = myEnv.etc(verb=self.verb)
        self.fop = myEnv.file_op(verb=self.verb)
        self.fit = myAst.fits(verb=self.verb)
        self.sex = myAst.sextractor(verb=self.verb)
        self.pht = myAst.phot(verb=self.verb)
        self.clc = myAst.calc(verb=self.verb)
        
        #self.etc.log("Loading settings.")
        #Load settings
        #self.read_settings()
        
        self.etc.log("Resetting Gui for Log tab.")
        #set Log tab
        self.ui.label_19.setProperty("text",
                                     "Logs are stoed in: {} & {}".format(
                                             self.etc.log_file,
                                             self.etc.mini_log_file))
        
        self.etc.log("Resetting Gui for Calibration tab.")
        #set calibration tab
        self.ui.progressBar.setProperty("value", 0)
        self.ui.label_3.setProperty("text", "")
        self.ui.label_4.setProperty("text", "")
        self.ui.label_5.setProperty("text", "")
        self.ui.label_6.setProperty("text", "")
        self.ui.label.setProperty("text", "")
        self.calibration_annotation()
        
        self.etc.log("Creating triggers for Calibration tab.")
        #add triggers for Calibration
        self.ui.pushButton_6.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_6),
                self.calibration_annotation()))
        self.ui.pushButton_5.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_6),
                self.calibration_annotation()))
        
        self.ui.pushButton_8.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_7),
                self.calibration_annotation()))
        self.ui.pushButton_7.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_7),
                self.calibration_annotation()))
        self.ui.pushButton_37.clicked.connect(lambda: (self.zero_combine()))
        
        self.ui.pushButton_10.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_8),
                self.calibration_annotation()))
        self.ui.pushButton_9.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_8),
                self.calibration_annotation()))
        self.ui.pushButton_40.clicked.connect(lambda: (self.dark_combine()))
        
        self.ui.pushButton_12.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_9),
                self.calibration_annotation()))
        self.ui.pushButton_11.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_9),
                self.calibration_annotation()))
        self.ui.pushButton_41.clicked.connect(lambda: (self.flat_combine()))
        
        self.ui.pushButton.clicked.connect(lambda: (self.do_calibration()))
        
        self.etc.log("Resetting Gui for Align tab.")
        #set align tab
        self.ui.progressBar_2.setProperty("value", 0)
        self.ui.label_2.setProperty("text", "")
        self.align_annotation()
        self.align_disp = FitsPlot(self.ui.disp_align.canvas, verb=self.verb)
        
        self.etc.log("Creating triggers for Align tab.")
        #add triggers for align
        self.ui.pushButton_3.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget),
                self.align_annotation()))
        self.ui.pushButton_4.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget),
                self.align_annotation()))
        
        self.ui.pushButton_2.clicked.connect(lambda: (self.do_align()))
        self.ui.listWidget.clicked.connect(lambda: (self.display_align()))
        
        self.etc.log("Resetting Gui for Photometry tab.")
        #set photometry tab
        self.ui.progressBar_4.setProperty("value", 0)
        self.ui.label_8.setProperty("text", "")
        self.phot_annotation()
        self.phot_disp = FitsPlot(
                self.ui.disp_photometry.canvas, verb=self.verb)
        
        self.etc.log("Creating triggers for Photometry tab.")
        #add triggers for photometry
        self.ui.pushButton_15.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_2),
                self.phot_annotation()))
        self.ui.pushButton_14.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_2),
                self.phot_annotation()))
        self.ui.pushButton_36.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_14),
                self.phot_annotation()))
        
        self.ui.pushButton_35.clicked.connect(lambda: (
                self.display_coors_phot()))
        
        self.ui.pushButton_34.clicked.connect(lambda: (self.run_sex()))
        self.ui.pushButton_16.clicked.connect(lambda: (self.do_phot()))
        self.ui.listWidget_2.clicked.connect(lambda: (self.display_phot()))
        
        self.etc.log("Resetting Gui for A-Track tab.")
        #set a-track tab
        self.ui.progressBar_7.setProperty("value", 0)
        self.ui.label_27.setProperty("text", "")
        self.atrack_annotation()
        self.atrack_disp = FitsPlot(self.ui.disp_atrack.canvas, verb=self.verb)
        
        self.etc.log("Creating triggers for A-Track tab.")
        #add triggers for atrack
        self.ui.pushButton_33.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_13),
                self.atrack_annotation()))
        self.ui.pushButton_32.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_13),
                self.atrack_annotation()))
        
        self.ui.listWidget_13.clicked.connect(lambda: (self.display_atrack()))
        self.ui.pushButton_42.clicked.connect(lambda: (self.a_track()))
        
        self.etc.log("Resetting Gui for Hedit tab.")
        #set header editor tab
        self.ui.progressBar_3.setProperty("value", 0)
        self.ui.label_10.setProperty("text", "")
        self.heditor_annotation()
        
        self.etc.log("Creating triggers for Hedit tab.")
        #add triggers for header editor
        self.ui.pushButton_20.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_3),
                self.heditor_annotation()))
        self.ui.pushButton_19.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_3),
                self.heditor_annotation()))
        
        self.ui.checkBox_5.clicked.connect(lambda: (
                self.use_existing_header()))
                
        
        self.ui.pushButton_39.clicked.connect(lambda: (
                self.do_hedit(update_add=True)))
        self.ui.pushButton_38.clicked.connect(lambda: (
                self.do_hedit(update_add=False)))
                
        self.ui.listWidget_3.clicked.connect(lambda: (self.header_list()))
        self.ui.listWidget_4.clicked.connect(lambda: (self.get_the_header()))
        
        self.etc.log("Resetting Gui for CosmicC tab.")
        #set Cosmic Cleaner tab
        self.ui.progressBar_5.setProperty("value", 0)
        self.ui.label_11.setProperty("text", "")
        self.cosmicC_annotation()
        self.cocmicC_disp = FitsPlot(
                self.ui.disp_cosmicC.canvas, verb=self.verb)
        
        self.etc.log("Creating triggers for CosmicC tab.")
        #add triggers for Cosmic Cleaner
        self.ui.pushButton_22.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_5),
                self.cosmicC_annotation()))
        self.ui.pushButton_21.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_5),
                self.cosmicC_annotation()))
        
        self.ui.pushButton_23.clicked.connect(lambda: (self.do_cosmicC()))
        self.ui.listWidget_5.clicked.connect(lambda: (self.display_cosmicC()))
        
        self.etc.log("Resetting Gui for WCS tab.")
        #set WCS Editor tab
        self.ui.progressBar_6.setProperty("value", 0)
        self.ui.label_17.setProperty("text", "")
        self.ui.label_14.setProperty("text", "")
        self.wcs_annotation()
        
        
        self.etc.log("Resetting Gui for Calculator tab.")
        #set Caloculator tab
        self.ui.progressBar_9.setProperty("value", 0)
        self.ui.label_49.setProperty("text", "")
        self.calculator_annotation()
        
        self.etc.log("Creating triggers for Calculator.")
        #add triggers for Calculator
        self.ui.groupBox_33.clicked.connect(lambda: (
                self.calculator_annotation()))
        self.ui.groupBox_34.clicked.connect(lambda: (
                self.calculator_annotation()))
        self.ui.groupBox_35.clicked.connect(lambda: (
                self.calculator_annotation()))
        
        self.ui.pushButton_47.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_16),
                self.calculator_annotation()))
        self.ui.pushButton_46.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_16),
                self.calculator_annotation()))
        
        self.ui.pushButton_48.clicked.connect(lambda: (self.do_calculator()))
        self.ui.listWidget_16.clicked.connect(lambda: (self.header_list_calculator()))
        
        
        self.etc.log("Creating triggers for WCS tab.")
        #add triggers for WCS Editor
        self.ui.pushButton_24.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_11),
                self.wcs_annotation()))
        self.ui.pushButton_25.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_11),
                self.wcs_annotation()))
        
        self.ui.pushButton_26.clicked.connect(lambda: (self.do_wcs()))
        
        self.etc.log("Creating triggers for Sttings tab.")
        #add triggers for Settings
        self.ui.pushButton_17.clicked.connect(lambda: (self.save_seetings()))
        self.ui.groupBox_5.clicked.connect(lambda: (
                self.astrometrynet_check()))
                
        self.etc.log("Creating triggers for Observatory Editor tab.")
        #add triggers for Observatory Editor
        self.ui.pushButton_30.clicked.connect(lambda: (self.add_obs()))
        self.ui.pushButton_29.clicked.connect(lambda: (self.rm_obs()))
        self.ui.listWidget_12.clicked.connect(lambda: (
                        self.get_observat_prop()))
        self.load_observat()
        
        self.etc.log("Creating triggers for Log tab.")
        #add triggers for Logs
        self.ui.pushButton_28.clicked.connect(lambda: (self.reload_log()))
        self.ui.pushButton_18.clicked.connect(lambda: (self.save_log()))
        self.ui.pushButton_27.clicked.connect(lambda: (self.clear_log()))
        self.reload_log()
        
        self.etc.log("Resetting Gui for Graph tab.")
        #set WCS Editor tab
        self.ui.label_31.setProperty("text", "")
        
        self.etc.log("Creating triggers for Graph tab.")
        
        self.ui.pushButton_44.clicked.connect(lambda: (
                self.get_graph_file_path()))
        self.ui.disp_align.canvas.fig.canvas.mpl_connect(
                'button_press_event',self.mouseClick)

    def header_list_calculator(self):
        #Get file's name
        img = self.ui.listWidget_16.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            try:
                #Get all headers of give file
                all_header = self.fit.header(img)
                #convert [key, value] to "key=>value" format in an array
                header_list = []
                for i in all_header:
                    header_list.append("{}=>{}".format(i[0], i[1]))
                
                #Replace whole combo with header list
                g.c_replace_list_con(self, self.ui.comboBox_16, header_list)
                g.c_replace_list_con(self, self.ui.comboBox_18, header_list)
                g.c_replace_list_con(self, self.ui.comboBox_17, header_list)
                g.c_replace_list_con(self, self.ui.comboBox_19, header_list)
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Header List)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                self, ("MYRaf Error"), ("File not found."))
    
        #Reload log file to log view
        self.reload_log()
    
    
    def do_calculator(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_16):
            #Start Calculator
            do_jd = self.ui.groupBox_33.isChecked()
            do_airmass = self.ui.groupBox_34.isChecked()
            do_imexam = self.ui.groupBox_35.isChecked()
            if do_jd or do_airmass or do_imexam:
                pref = self.ui.lineEdit_9.text()
                for i in range(self.ui.listWidget_16.count()):
                    img = self.ui.listWidget_16.item(i).text()
                    if self.fop.is_file(img):
                        if do_jd:
                            try:
                                #Get the "key=>value" for existing value
                                combo_time_jd = self.ui.comboBox_16.currentText()
                                #Find wanted key by spliting it by "=>"
                                field_time_jd = combo_time_jd.split("=>")[0].strip()
                                time_jd = self.fit.header(img, field_time_jd)
                            except Exception as e:
                                self.etc.log(e)
                                continue
                            
                            if time_jd is not None:
                                try:
                                    the_time = time_jd[1]
                                    the_jd = self.clc.jd(the_time)
                                    the_mjd = self.clc.mjd(the_time)
                                except Exception as e:
                                    self.etc.log(e)
                                    continue
                                try:
                                    if type(the_jd) == float:
                                        val_jd = the_jd
                                        self.fit.update_header(img, "{}JD".format(pref), val_jd)
                                        
                                    if type(the_mjd) == float:
                                        val_mjd = the_mjd
                                        self.fit.update_header(img, "{}MJD".format(pref), val_mjd)
                                    
                                except Exception as e:
                                    self.etc.log(e)
                                    continue
                            else:
                                #Log an error about not existing header
                                self.etc.log("No such (Calc)header({})".format(field_time_jd))
                                continue
                                
                        if do_imexam:
                            try:
                                imex = self.clc.imexamine(img)
                            except Exception as e:
                                self.etc.log(e)
                                continue
                            
                            if imex is not None:
                                try:
                                    if self.ui.checkBox_8.isChecked():
                                        self.fit.update_header(img, "{}mean".format(pref), imex[0])
                                    if self.ui.checkBox_9.isChecked():
                                        self.fit.update_header(img, "{}medi".format(pref), imex[1])
                                    if self.ui.checkBox_10.isChecked():
                                        self.fit.update_header(img, "{}stdv".format(pref), imex[2])
                                    if self.ui.checkBox_11.isChecked():
                                        self.fit.update_header(img, "{}min".format(pref), imex[3])
                                    if self.ui.checkBox_12.isChecked():
                                        self.fit.update_header(img, "{}max".format(pref), imex[4])
                                except Exception as e:
                                    self.etc.log(e)
                                    continue   
                            
                    else:
                        #Log an error about not existing file
                        self.etc.log("No such (Calc)file({})".format(img))
            else:
                #Log and display an error about no operation
                self.etc.log("Nothing to do.")
                QtWidgets.QMessageBox.critical(
                        self, ("MYRaf Error"), ("Please select operation(s)"))
                
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to Calculator.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))

        #Reload log file to log view
        self.reload_log()

    #Change annotation of Calculator Tab
    def calculator_annotation(self):
        #Just find how many files were given for align
        img = g.list_lenght(self, self.ui.listWidget_16)
        proc = ""
        if self.ui.groupBox_33.isChecked():
            proc = "JD, {}".format(proc)
        
        if self.ui.groupBox_34.isChecked():
            proc = "Airmass, {}".format(proc)
            
        if self.ui.groupBox_35.isChecked():
            proc = "Imexamine, {}".format(proc)
            
        if len(proc) == 0:
            proc = "Nothing, "
        self.ui.label_49.setProperty("text",
                                    "{0} will be done to {1} files".format(proc[:-2], img))

        #Reload log file to log view
        self.reload_log()

    def mouseClick(self, event):
        print(event)
        if self.ui.tabWidget.currentIndex() == 1:
            if event.ydata != None and event.xdata != None:
                rows = self.ui.listWidget.count()
                row = self.ui.listWidget.currentRow()
                img = self.ui.listWidget.currentItem()
                if img is not None:
                    img = img.text()
                    x = event.xdata
                    y = event.ydata
                    self.fit.update_header(img, "mymancoo", "{}, {}".format(
                                                                    x, y))
                    if row < rows-1:
                        self.ui.listWidget.setCurrentRow(row+1)
                    else:
                        self.etc.beep()
                        self.ui.listWidget.setCurrentRow(0)
                        
            self.display_align()
            
        #Reload log file to log view
        self.reload_log()

    def get_graph_file_path(self):
        pth = self.fop.abs_path(g.get_graph_file_path(self))
        self.ui.label_31.setProperty("text", pth)
        
        #Reload log file to log view
        self.reload_log()
    
    #Zero Combine Method
    def zero_combine(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_7):
            #Start Zero Combine
            print("Do zero combine")
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to (z)combine.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
           
    #Dark Combine Method
    def dark_combine(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_8):
            #Start Dark Combine
            print("Do dark combine")
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to (d)combine.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
            
    #Flat Combine Method
    def flat_combine(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_9):
            #Start Flat Combine
            print("Do flat combine")
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to (f)combine.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
            
    #Display fit file on Cosmic Cleaner Tab
    def display_cosmicC(self):
        #Check if file does exist
        img = self.ui.listWidget_5.currentItem().text()
        #Find the possible file name
        if self.fop.is_file(img):
            try:
                #Display the file
                self.cocmicC_disp.load(str(img))
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Disp cosmicC)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
       
    def get_man_coo(self):
        #Find the possible file name
        img = self.ui.listWidget.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            the_coo = self.fit.header(img, field="mymancoo")[1]
            if the_coo is not None:
                try:
                    #Split x, y coordinates by ", "
                    x, y = the_coo.split(", ")
                    #Convert x coordinate to float dtype
                    x = float(x)
                    #Convert y coordinate to float dtype
                    y = float(y)
                    #Get the aperture value
                    ap = float(self.ui.doubleSpinBox_2.value())
                    #Make a circle with x, y coordinates and ap aperture value
                    circ = Circle((x, y), ap * 1.3,
                                  edgecolor="#00FFFF", facecolor="none")
                    #Add circle to canvas
                    self.ui.disp_align.canvas.fig.gca().add_artist(circ)
                    #Make the circle's center x, y
                    circ.center = x, y
                    
                    #Add iteration value as label
                    self.ui.disp_align.canvas.fig.gca().annotate(
                            "Ref", xy = (x, y), xytext=(int(ap)/3,int(ap)/3),
                            textcoords='offset points', color = "red",
                            fontsize = 10) 
                    self.ui.disp_align.canvas.draw()
                except Exception as e:
                    self.etc.log(e)
            else:
                self.etc.log("No Manual Align coordinate found")
        else:
            #Log an error about not existing file
            self.et.log("No such (Disp Align Coor)file({})".format(img))
            
        
        #Reload log file to log view
        self.reload_log()
        
    #Display fit file on Align Tab
    def display_align(self):
        #Find the possible file name
        img = self.ui.listWidget.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            try:
                #Display the file
                self.align_disp.load(str(img))
                self.get_man_coo()
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Disp Align)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
        
    #Display fit file on Photometry Tab
    def display_phot(self):
        #Find the possible file name
        img = self.ui.listWidget_2.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            try:
                #Display the file
                self.phot_disp.load(str(img))
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Disp Photometry)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
        
    #Display fit file on A-Track Tab
    def display_atrack(self):
        #Find the possible file name
        img = self.ui.listWidget_13.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            try:
                #Display the file
                self.atrack_disp.load(str(img))
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Disp A-Track)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
    
    #Get a header key and it's value to textEdit fields 
    def get_the_header(self):
        if self.ui.listWidget_4.currentItem() is not None:
            #Get the header's line
            line = self.ui.listWidget_4.currentItem().text()
            #Split the line by "=>" so the field and value is obtaned
            field, value = line.split("=>")
            #Set (value)text of field textEdit
            self.ui.lineEdit.setProperty("text", field)
            #Set (value)text of value textEdit
            self.ui.lineEdit_2.setProperty("text", value)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Get the header)header (-_-)")
            QtWidgets.QMessageBox.critical(self, ("MYRaf Error"), ("I don't know how you managed that.\nBut No header was selected."))
        
        #Reload log file to log view
        self.reload_log()
        
    #Get whole list of headers of a fits file
    def header_list(self):
        #Get file's name
        img = self.ui.listWidget_3.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            try:
                #Get all headers of give file
                all_header = self.fit.header(img)
                #convert [key, value] to "key=>value" format in an array
                header_list = []
                for i in all_header:
                    header_list.append("{}=>{}".format(i[0], i[1]))
                
                #Replace whole list with header list
                g.replace_list_con(self, self.ui.listWidget_4, header_list)
                #Replace whole combo with header list
                g.c_replace_list_con(self, self.ui.comboBox_12, header_list)
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Header List)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                self, ("MYRaf Error"), ("File not found."))
    
        #Reload log file to log view
        self.reload_log()
        
    #Start Calibration
    def do_calibration(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_6):
            #Check if any file was given as Bias
            do_zc = not g.is_list_empty(self, self.ui.listWidget_7)
            #Check if any file was given as Dark
            do_dc = not g.is_list_empty(self, self.ui.listWidget_8)
            #Check if any file was given as Flat
            do_fc = not g.is_list_empty(self, self.ui.listWidget_9)
            
            #Check if any task was set
            if do_zc or do_dc or do_fc:
                #Find which taskes were given
                if do_zc:
                    #Zero Correction wanted
                    print("Create Master Zero")
                    
                if do_dc:
                    #Dark Correction wanted
                    print("Create Master Dark")
                
                if do_fc:
                    #Flat Correction wanted
                    print("Create Master Flat")
            else:
                #Log and display an error about not given operation
                self.etc.log("No operation was set for Calibration.")
                QtWidgets.QMessageBox.critical(
                        self,  ("MYRaf Error"), ("Nothing to do."))
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to calibrate.")
            QtWidgets.QMessageBox.critical(self,  ("MYRaf Error"), ("Please add some files.\nUnless you have a sick sense of humour and you really want calibrate no files."))
            
        #Reload log file to log view
        self.reload_log()
        
    #Change annotation of Calibration Tab
    def calibration_annotation(self):
        #Just find how many files were given as BDF and images
        img = g.list_lenght(self, self.ui.listWidget_6)
        zer = g.list_lenght(self, self.ui.listWidget_7)
        dar = g.list_lenght(self, self.ui.listWidget_8)
        fla = g.list_lenght(self, self.ui.listWidget_9)
        self.ui.label.setProperty("text", "{0} File(s) will be calibrated using {1} Bias(es), {2} Dark(s) and {3} Flat(s)".format(img, zer, dar, fla))
    
    #Start Alignment
    def do_align(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget):
            #Check if Auto Align is selected
            if self.ui.checkBox.isChecked():
                #Do Auto Align
                print("Do auto align")
            else:
                #Do Manual Align
                if self.ui.listWidget.currentItem() is not None:
                    ref = self.ui.listWidget.currentItem().text()
                    if self.fop.is_file(ref):
                        ref_coors = self.fit.header(ref, "mymancoo")
                        if ref_coors is not None:
                            ref_coors = ref_coors[1]
                            odir = str(
                                    QtWidgets.QFileDialog.getExistingDirectory(
                                            self, "Select Directory"))
                            if self.fop.is_dir(odir):
                                for i in range(self.ui.listWidget.count()):
                                    img = self.ui.listWidget.item(i).text()
                                    if self.fop.is_file(img):
                                        coors = self.fit.header(img, "mymancoo")
                                        if coors is not None:
                                            coors = coors[1]
                                            fp, fn = self.fop.get_base_name(img)
                                            new_path = self.fop.abs_path("{}/{}".format(odir, fn))
                                            ry = float(ref_coors.split(", ")[0])
                                            rx = float(ref_coors.split(", ")[1])
                                            ty = float(coors.split(", ")[0])
                                            tx = float(coors.split(", ")[1])
                                            x = rx - tx
                                            y = ry - ty
                                            self.fit.shift(new_path, img, x, y)
                                            
                                        else:
                                            #Log an error about Not
                                            #existing coor
                                            self.etc.log("No coordinate was selected for file({})".format(img))
                                    else:
                                        #Log an error about Not existing file
                                        self.etc.log("No image found({})".format(img))
                                        
                                    g.proc(self, self.ui.progressBar_2, (i + 1)/g.list_lenght(self, self.ui.listWidget))
                            else:
                                #Log an error about Not existing out dir
                                self.etc.log("No out dir found({})".format(odir))
                        else:
                            #Log and display an error about Not existing ref coors
                            self.etc.log("Referance image has no coordinates.")
                            QtWidgets.QMessageBox.critical(
                                    self,  ("MYRaf Error"),
                                    ("Please select Coor on Ref image."))
                    else:
                        #Log and display an error about Not existing ref image
                        self.etc.log("No Referance image() found".format(ref))
                        QtWidgets.QMessageBox.critical(
                                self,  ("MYRaf Error"),
                                ("No reference image found."))
                else:
                    #Log and display an error about not selected ref image
                    self.etc.log("No Reference image was selected.")
                    QtWidgets.QMessageBox.critical(
                            self,  ("MYRaf Error"),
                            ("No reference image selected."))
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to align.")
            QtWidgets.QMessageBox.critical(
                    self,  ("MYRaf Error"), ("Please add some files"))
    
        #Reload log file to log view
        self.reload_log()
    
    #Change annotation of Align Tab
    def align_annotation(self):
        #Just find how many files were given for align
        img = g.list_lenght(self, self.ui.listWidget)
        self.ui.label_2.setProperty("text",
                                    "{0} file(s) will be aligned".format(img))
    
    def a_track(self):
        if not g.is_list_empty(self, self.ui.listWidget_13):
            for i in range(self.ui.listWidget_14.count()):
                img = self.ui.listWidget_13.item(i).text()
                if self.fop.is_file(img):
                    print(img)
                else:
                    self.et.log("No such (a-track)file({})".format(img))
        else:
            self.etc.log("Nothing to track.")
            QtWidgets.QMessageBox.critical(
                    self,  ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
        
    def display_coors_phot(self):
        #Refresh display
        self.display_phot()
        #Check if any specific coordinate was selected
        if len(self.ui.listWidget_14.selectedItems()) != 0:
            #User selected some coordinates to display
            self.etc.log("Displaying selected coordinates")
            #Loop in all coordinates
            for it, coo in enumerate(self.ui.listWidget_14.selectedItems()):
                try:
                    #Convfert coodinate line to string dtype
                    the_coo = str(coo.text())
                    #Split x, y coordinates by ", "
                    x, y = the_coo.split(", ")
                    #Convert x coordinate to float dtype
                    x = float(x)
                    #Convert y coordinate to float dtype
                    y = float(y)
                    #Get the aperture value
                    ap = float(self.ui.doubleSpinBox_2.value())

                    #Make a circle with x, y coordinates and ap aperture value
                    circ = Circle((x, y), ap * 1.3, edgecolor="#00FFFF",
                                  facecolor="none")
                    #Add circle to canvas
                    self.ui.disp_photometry.canvas.fig.gca().add_artist(circ)
                    #Make the circle's center x, y
                    circ.center = x, y
                    #Add iteration value as label
                    self.ui.disp_photometry.canvas.fig.gca().annotate(
                            it, xy = (x, y), xytext=(int(ap)/3,int(ap)/3),
                            textcoords='offset points', color = "red",
                            fontsize = 10)
                except Exception as e:
                    #Log error if any occurs
                    self.etc.log(e)
            try:
                self.etc.log("Drawing coordinates")
                #Draw all coordinates
                self.ui.disp_photometry.canvas.draw()
            except Exception as e:
                #Log error if any occurs
                self.etc.log(e)
        else:
            #User did not select any coordinates to display. Drawing all
            self.etc.log("Displaying all coordinates")
            #Check if coordinates list is empty
            if not g.is_list_empty(self, self.ui.listWidget_14):
                #List is not empty
                #Loop in all coordinates
                for it, i in enumerate(range(self.ui.listWidget_14.count())):
                    #Get coordinate from the item
                    coo = self.ui.listWidget_14.item(i).text()
                    try:
                        the_coo = str(coo)
                        #Split x, y coordinates by ", "
                        x, y = the_coo.split(", ")
                        #Convert x coordinate to float dtype
                        x = float(x)
                        #Convert y coordinate to float dtype
                        y = float(y)
                        #Get the aperture value
                        ap = float(self.ui.doubleSpinBox_2.value())

                        #Make a circle with x, y coordinates and ap
                        #                               aperture value
                        circ = Circle((x, y), ap * 1.3, edgecolor="#00FFFF",
                                      facecolor="none")
                        #Add circle to canvas
                        self.ui.disp_photometry.canvas.fig.gca().add_artist(
                                circ)
                        #Make the circle's center x, y
                        circ.center = x, y
                        #Add iteration value as label
                        self.ui.disp_photometry.canvas.fig.gca().annotate(
                                it, xy = (x, y), xytext=(int(ap)/3,int(ap)/3),
                                textcoords='offset points', color = "red",
                                fontsize = 10)
                    except Exception as e:
                        #Log any error if any occurs
                        self.etc.log(e)
                try:
                    self.etc.log("Drawing coordinates")
                    #Draw all coordinates
                    self.ui.disp_photometry.canvas.draw()
                except Exception as e:
                    #Log any error if any occurs
                    self.etc.log(e)
            else:
                self.etc.log("No coordinate was given")
                QtWidgets.QMessageBox.critical(
                        self, ("MYRaf Error"), ("No coordinate was given"))
                
        #Reload log file to log view
        self.reload_log()
        
    def run_sex(self):
        #Check if any image file was selected
        if self.ui.listWidget_2.currentItem() is not None:
            #File was selected
            #Get file's name
            img = self.ui.listWidget_2.currentItem().text()
            #Check if file exist
            if self.fop.is_file(img):
                try:
                    #Get data from file
                    data = self.fit.data(img, table=False)
                    #Get maximum object count to find
                    lim = int(self.ui.spinBox.value())
                    #Get coordinates from the img file
                    coors = self.sex.find_limited(data, max_sources=lim)
                    #Declare a list variable
                    sex_coors = []
                    for i in coors:
                        #Add all coordinates to list as string
                        #with "X, Y" format
                        sex_coors.append("{:0.4f}, {:0.4f}".format(
                                                            i['x'], i['y']))
                    #Add coordinate list to listwidget
                    g.replace_list_con(self, self.ui.listWidget_14, sex_coors)
                except Exception as e:
                    #Log error if any occurs
                    self.etc.log(e)
            else:
                #Log and display an error about not existing file
                self.etc.log("No such (Run Sex)file({}).".format(img))
                QtWidgets.QMessageBox.critical(
                        self, ("MYRaf Error"), ("No Such file"))
        else:
            #Log and display an error about empty listWidget
           self.etc.log("No File was selected(Run Sex)")
           QtWidgets.QMessageBox.critical(
                   self, ("MYRaf Error"), ("No file was selected"))
           
        #Reload log file to log view
        self.reload_log()
        
    #Start Photometry
    def do_phot(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_2):
            #Check if Ensemble Photometry is selected
            if self.ui.groupBox_6.isChecked():
                #Do Ensemble Photometry
                print("Ensemble Photometry")
            else:
                #Do Photometry
                if not g.is_list_empty(self, self.ui.listWidget_14):
                    odir = str(QtWidgets.QFileDialog.getExistingDirectory(
                                    self, "Select Directory"))
                    if self.fop.is_dir(odir):
                        for i in range(self.ui.listWidget_2.count()):
                            img = self.ui.listWidget_2.item(i).text()
                            if self.fop.is_file(img):
                                
                                data = self.fit.data(img, table=False)
                                aper = float(self.ui.doubleSpinBox_5.value())
                                gain = self.ui.lineEdit_26.text()
                                jd = self.ui.lineEdit_17.text()
                                
                                h_gain = self.fit.header(img, field=gain)
                                
                                if h_gain is not None:
                                    try:
                                        the_gain = float(h_gain[1])
                                    except Exception as e:
                                        self.etc.log("Bad GAIN value ({})".format(e))
                                        continue
                                else:
                                    self.etc.log("No Gain value found in header({})".format(img))
                                    continue
                                
                                h_jd = self.fit.header(img, field=jd)
                                
                                if h_jd is not None:
                                    try:
                                        the_jd = float(h_jd[1])
                                    except Exception as e:
                                        self.etc.log("Bad JD value ({})".format(e))
                                        continue
                                else:
                                    self.etc.log("No JD value found in header({})".format(img))
                                    continue
                                
                                a_file = []
                                for u in range(self.ui.listWidget_14.count()):
                                    coo = self.ui.listWidget_14.item(u).text()
                                    x = float(coo.split(", ")[0])
                                    y = float(coo.split(", ")[1])
                                    
                                    try:
                                        mag, merr = self.pht.do_mag(data, x, y, aper, the_gain)
                                        a_file.append([the_jd, x, y, mag, merr])
                                    except Exception as e:
                                        self.etc.log(e)
                                    
                                try:
                                    pn, fn = self.fop.get_base_name(img)
                                    of = self.fop.abs_path("{}/{}.mmm".format(odir, fn))
                                    self.fop.write_array(of, a_file, dm=" ", h="jd x y mag merr")
                                except Exception as e:
                                    self.etc.log(e)
                            else:
                                #Log an error about not existing file
                                self.etc.log("No such (Phot)file({})".format(img))
                                
                            g.proc(self, self.ui.progressBar_4, (i + 1)/g.list_lenght(self, self.ui.listWidget_2))
                            
                    else:
                        #Log an error about Not existing out dir
                        self.etc.log("No out dir found({})".format(odir))
                else:
                    #Log and display an error about empty listWidget
                    self.etc.log("No coordinate was given to do photometry.")
                    QtWidgets.QMessageBox.critical(
                            self,  ("MYRaf Error"),
                            ("Please add some coordinates"))
        else:
            #Log and display an error about empty listWidget
            self.etc.log("No file was given to do photometry.")
            QtWidgets.QMessageBox.critical(
                    self,  ("MYRaf Error"), ("Please add some files"))
    
        #Reload log file to log view
        self.reload_log()
    
    #Change annotation of Photometry Tab
    def phot_annotation(self):
        #Just find how many files were given for photometry
        img = g.list_lenght(self, self.ui.listWidget_2)
        self.ui.label_8.setProperty(
                "text", "Photometry will be done for {0} file(s)".format(img))
        
    #Change annotation of Photometry Tab
    def atrack_annotation(self):
        #Just find how many files were given for photometry
        img = g.list_lenght(self, self.ui.listWidget_13)
        self.ui.label_27.setProperty(
                "text", "A-Track will be done for {0} file(s)".format(img))
        
    #Do Hedit's Operation
    def do_hedit(self, update_add=True):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_3):
            #Check if any field was specified
            if not self.ui.lineEdit.text() == "":
                #Get field value
                field = self.ui.lineEdit.text()
                #Start an iteration for prgressBar
                for i in range(self.ui.listWidget_3.count()):
                    #Find the possible file name
                    img = self.ui.listWidget_3.item(i).text()
                    #Check if file exist
                    if self.fop.is_file(img):
                        #Check if header must be updated/added or removed
                        if update_add:
                            #Header must be updated/added
                            try:
                                #Check if using an existion value
                                if self.ui.checkBox_5.isChecked():
                                    #Using an existing value
                                    #Get the "key=>value" for existing value
                                    combo = self.ui.comboBox_12.currentText()
                                    #Find wanted key by spliting it by "=>"
                                    wanted_filed = combo.split("=>")[0].strip()
                                    #Get the value of wanted key in header
                                    value = self.fit.header(
                                            img, wanted_filed)[1]
                                else:
                                    #Using a static value
                                    #Getting the value value
                                    value = self.ui.lineEdit_2.text()
    
                                #Updating the header
                                self.fit.update_header(img, field, value)
                            except Exception as e:
                                #Log error if any occurs
                                self.etc.log(e)

                        else:
                            #Header must be removed
                            try:
                                #Remove header
                                self.fit.delete_header(img, field)
                            except Exception as e:
                                #Log the exception if it happened
                                self.etc.log(e)
                    else:
                        #Log and display an error about not existing file
                        self.etc.log("No such (Hedit)file({})".format(img))
                        
                    #Advance ProgressBar
                    g.proc(self, self.ui.progressBar_3, (i + 1)/g.list_lenght(
                                                self, self.ui.listWidget_3))
                #Reload header list in hedit view
                self.header_list()
            else:
                #Log and display an error about empty field
                self.etc.log("No field was specified.")
                QtWidgets.QMessageBox.critical(
                        self, ("MYRaf Error"), ("No field was specified"))
        else:
            #Log and display an error about empty listWidget
            self.etc.log("No file was given to Header Editor.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
    
    #Change Usage of Existing Header
    def use_existing_header(self):
        #Check if using an existing value
        if self.ui.checkBox_5.isChecked():
            #Using an existing value
            #Disable lineEdit and Enable Combobox
            self.ui.lineEdit_2.setEnabled(False)
            self.ui.comboBox_12.setEnabled(True)
        else:
            #Using a static value
            #Enable lineEdit and Disable Combobox
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.comboBox_12.setEnabled(False)
    
        self.reload_log()
    #Change annotation of Header Editor Tab
    def heditor_annotation(self):
        img = g.list_lenght(self, self.ui.listWidget_3)
        self.ui.label_10.setProperty(
                "text", "header for {0} files will be updated".format(img))
        
        #Reload log file to log view
        self.reload_log()
       
    #Start Cosmic Cleaning
    def do_cosmicC(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_5):
            #Get gain value from settings tab
            gain = float(self.ui.doubleSpinBox_20.value())
            #Get Readout Noise value from settings tab
            readN = float(self.ui.doubleSpinBox_21.value())
            #Get Sigma Clip value from settings tab
            sigmC = float(self.ui.doubleSpinBox_22.value())
            #Get Sigma Frac value from settings tab
            sigmF = float(self.ui.doubleSpinBox_23.value())
            #Get Object Limit value from settings tab
            objeL = float(self.ui.doubleSpinBox_24.value())
            #Get Maximum iteration value from settings tab
            max_it = int(self.ui.spinBox_2.value())
            #Get the output directory path from user
            odir = str(QtWidgets.QFileDialog.getExistingDirectory(
                        self, "Select Directory"))
            if self.fop.is_dir(odir):
                #Start a loop for each file name
                for i in range(self.ui.listWidget_5.count()):
                    #Find the possible file name
                    img = self.ui.listWidget_5.item(i).text()
                    #Check if file exist
                    if self.fop.is_file(img):
                        try:
                            #Split file name and the path
                            pth, name = self.fop.get_base_name(img)
                            #User file name and path given to create new file path
                            ofile = self.fop.abs_path("{}/{}".format(odir, name))
                            #User file name and path given to create mask file path
                            mfile = self.fop.abs_path("{}/mask_{}".format(odir, name))
                            #Start cosmic clean
                            data, header = myCos.fromfits(img)
                            c = myCos.cosmicsimage(data, gain=gain, readnoise=readN, sigclip=sigmC, sigfrac=sigmF, objlim=objeL)
                            
                            c.run(maxiter=max_it)
                            if not self.fop.is_file(ofile):
                                myCos.tofits(ofile, c.cleanarray, header)
                            if self.ui.checkBox_3.isChecked():
                                if not self.fop.is_file(mfile):
                                    myCos.tofits(mfile, c.mask, header)
                            #Cosmic clean done
                        except Exception as e:
                            #Log error if any occurs
                            self.etc.log(e)
                    else:
                        #Log and display an error about not existing file
                        self.et.log("No such (Cosmic Clean)file({})".format(img))
                    
                    #Advance ProgressBar
                    g.proc(self, self.ui.progressBar_5, (i + 1)/g.list_lenght(self, self.ui.listWidget_5))
            else:
                #Log an error about empty listWidget
                self.etc.log("No out dir found({})".format(odir))
        else:
            #Log and display an error about empty listWidget
            self.etc.log("Nothing to Cosimc Clean.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
    
    #Change annotation of Cosmic Cleaning Tab
    def cosmicC_annotation(self):
        #Just find how many files were given for Cosmic Cleaner
        img = g.list_lenght(self, self.ui.listWidget_5)
        self.ui.label_11.setProperty(
                "text", 
                "Cosmic Cleaning will be applied for {0} files".format(img))
        
    #Satrt WCS Operation
    def do_wcs(self):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_11):
            print("Start WCS")
        else:
            #Log and display an error about empty listWidget
            self.etc.log("No file was given to WCS Editor.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
        
    #Change annotation of WCS Tab
    def wcs_annotation(self):
        #Just find how many files were given for WCS
        img = g.list_lenght(self, self.ui.listWidget_11)
        self.ui.label_14.setProperty(
                "text",
                "Cosmic Cleaning will be applied for {0} files".format(img))
        
    def astrometrynet_check(self):
        if self.etc.is_it_windows:
            self.etc.log("No Astrometry.new for Windows.")
            QtWidgets.QMessageBox.critical(self, ("MYRaf Error"), ("The Astrometry.net does not support your os.\nYou HAVE to use online version."))
            self.ui.groupBox_5.setChecked(True)
        else:
            print("other")
            
        #Reload log file to log view
        self.reload_log()
        
    def load_observat(self):
        obs_files = self.fop.list_of_fiels(self.fop.abs_path(
                            "./observat"), ext="*")
        new_list = []
        for i in obs_files:
            new_list.append(self.fop.get_base_name(i)[1])
        g.replace_list_con(self, self.ui.listWidget_12, new_list)
        
        g.c_replace_list_con(self, self.ui.comboBox_22, new_list)
        
        #Reload log file to log view
        self.reload_log()
        
    def get_observat_prop(self):
        obs_name = self.ui.listWidget_12.currentItem().text()
        obs_path = self.fop.abs_path("./observat/{}".format(obs_name))
        if self.fop.is_file(obs_path):
            f_obs = open(obs_path, "r")
            comm = ""
            for i in f_obs:
                ln = i.replace("\n", "")
                
                if ln.startswith("observatory|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_3.setText(str(val))
                    
                if ln.startswith("name|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_4.setText(str(val))
                    
                if ln.startswith("longitude|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_5.setText(str(val))
                    
                if ln.startswith("latitude|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_6.setText(str(val))
                    
                if ln.startswith("altitude|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_7.setText(str(val))
                    
                if ln.startswith("timezone|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_8.setText(str(val))
                    
                if ln.startswith("#"):
                    comm = "{}\n{}".format(comm, ln.replace("#", ""))
                    
            
            self.ui.plainTextEdit.setPlainText(
                    QtWidgets.QApplication.translate(
                            "Form", "\n".join(comm.split('\n')[1:]), None))
                    
        else:
            self.etc.log("No such Observatory({})".format(obs_name))
        
        #Reload log file to log view
        self.reload_log()
    
    def rm_obs(self):
        if self.ui.listWidget_12.currentItem() is not None:
            obs_name = self.ui.listWidget_12.currentItem().text()
            obs_path = self.fop.abs_path("./observat/{}".format(obs_name))
            if self.fop.is_file(obs_path):
                self.fop.rm(obs_path)
            else:
                #Log and display an error about about not existing
                #observatory name
                self.etc.log("No such Observatory({})".format(obs_name))
                QtWidgets.QMessageBox.critical(
                        self, ("MYRaf Error"),
                        ("Couldn't find the observatory"))
        else:
            #Log and display an error about about not existing observatory name
                self.etc.log("No Observatory was choosen")
                QtWidgets.QMessageBox.critical(self, ("MYRaf Error"),
                                               ("No Observatory was choosen"))
        self.load_observat()
        #Reload log file to log view
        self.reload_log()
    
    def add_obs(self):
        if not self.ui.lineEdit_3.text() == "":
            observatory = self.ui.lineEdit_3.text()
            name = self.ui.lineEdit_4.text()
            longitude = self.ui.lineEdit_5.text()
            latitude = self.ui.lineEdit_6.text()
            altitude = self.ui.lineEdit_7.text()
            timezone = self.ui.lineEdit_8.text()
            comm = str(self.ui.plainTextEdit.toPlainText())
            
            file_name = self.fop.abs_path("./observat/{}".format(observatory))        
            f = open(file_name, "w")
            f.write("#{}\n".format(comm.replace("\n", "\n#")))
            f.write("observatory|{}\n".format(observatory))
            f.write("name|{}\n".format(name))
            f.write("longitude|{}\n".format(longitude))
            f.write("latitude|{}\n".format(latitude))
            f.write("altitude|{}\n".format(altitude))
            f.write("timezone|{}\n".format(timezone))
            f.close()
            
            self.ui.lineEdit_3.setText("")
            self.ui.lineEdit_4.setText("")
            self.ui.lineEdit_5.setText("")
            self.ui.lineEdit_6.setText("")
            self.ui.lineEdit_7.setText("")
            self.ui.lineEdit_8.setText("")
            self.ui.plainTextEdit.setPlainText("")
            
            self.load_observat()
        else:
            #Log and display an error about empty observatory name
            self.etc.log("No observatory was specified.")
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("No observatory was specified"))
            
        #Reload log file to log view
        self.reload_log()
        
    def reload_log(self):
        g.rm_all(self, self.ui.listWidget_10)
        g.add_line_by_line(self, self.ui.listWidget_10, self.etc.mini_log_file)
        self.ui.listWidget_10.scrollToBottom()
        
    def save_log(self):
        out_file = g.save_log_file(self)
        self.fop.cp(self.etc.mini_log_file, out_file)
        self.reload_log()
        
    def clear_log(self):
        answ = g.question(self, "Are you sure you want to clear log?")
        if answ == QtWidgets.QMessageBox.Yes:
            self.etc.dump_mlog()
        self.reload_log()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)        
    f = MyForm(verb=True)
    f.show()
    app.exec_()