# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:54:39 2018

@author: mshem
"""

from os import name as osname

from myraf import Ui_Form
from PyQt5 import QtWidgets
import sys

#Importing myraf's GUI
import gui as g
from fPlot import FitsPlot

#Importing myraf's needed modules
from myraflib import myEnv
from myraflib import myAst
from myraflib import myCos

class MyForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyForm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.verb = True
        self.srttings_file = "./set.myc"
        
        self.etc = myEnv.etc(verb=self.verb)
        self.fop = myEnv.file_op(verb=self.verb)
        self.fit = myAst.fits(verb=self.verb)
        
        self.etc.log("Loading settings.")
        #Load settings
        self.read_settings()
        
        self.etc.log("Resetting Gui for Log tab.")
        #set Log tab
        self.ui.label_19.setProperty("text", "")
        self.ui.label_19.setProperty("text",
                                     "Log file is stored: {}".format(
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
        self.align_disp = FitsPlot(self.ui.disp_align.canvas)
        
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
        self.phot_disp = FitsPlot(self.ui.disp_photometry.canvas)
        
        self.etc.log("Creating triggers for Photometry tab.")
        #add triggers for photometry
        self.ui.pushButton_15.clicked.connect(lambda: (
                g.add_files(self, self.ui.listWidget_2),
                self.phot_annotation()))
        self.ui.pushButton_14.clicked.connect(lambda: (
                g.rm(self, self.ui.listWidget_2),
                self.phot_annotation()))
        
        self.ui.pushButton_16.clicked.connect(lambda: (self.do_phot()))
        self.ui.listWidget_2.clicked.connect(lambda: (self.display_phot()))
        
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
        self.cocmicC_disp = FitsPlot(self.ui.disp_cosmicC.canvas)
        
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
            print("Do dark combine")
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
            #Display the file
            self.cocmicC_disp.load(str(img))
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Disp cosmicC)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
       
    #Display fit file on Align Tab
    def display_align(self):
        #Find the possible file name
        img = self.ui.listWidget.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
            #Display the file
            self.align_disp.load(str(img))
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
            #Display the file
            self.phot_disp.load(str(img))
        else:
            #Log and display an error about not existing file
            self.et.log("No such (Disp Photometry)file({})".format(img))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("Please add some files"))
            
        #Reload log file to log view
        self.reload_log()
    
    #Get a header key and it's value to textEdit fields 
    def get_the_header(self):
        #Get the header's line
        line = self.ui.listWidget_4.currentItem().text()
        #Split the line by "=>" so the field and value is obtaned
        field, value = line.split("=>")
        #Set (value)text of field textEdit
        self.ui.lineEdit.setProperty("text", field)
        #Set (value)text of value textEdit
        self.ui.lineEdit_2.setProperty("text", value)
        
        #Reload log file to log view
        self.reload_log()
        
    #Get whole list of headers of a fits file
    def header_list(self):
        #Get file's name
        img = self.ui.listWidget_3.currentItem().text()
        #Check if file does exist
        if self.fop.is_file(img):
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
                print("Do manual align")
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
                print("Pure Photometry")
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
        
    #Do Hedit's Operation
    def do_hedit(self, update_add=True):
        #Check if listWidget is empty
        if not g.is_list_empty(self, self.ui.listWidget_3):
            #Check if any field was specified
            if not self.ui.lineEdit.text() == "":
                #Get field value
                field = self.ui.lineEdit.text()
                #Start an iteration for prgressBar
                it = 0.
                #Start a loop for each file name
                for i in range(self.ui.listWidget_3.count()):
                    #Increase iteration
                    it += 1
                    #Find the possible file name
                    img = self.ui.listWidget_3.item(i).text()
                    #Check if file exist
                    if self.fop.is_file(img):
                        #Check if header must be updated/added or removed
                        if update_add:
                            #Header must be updated/added
                            #Check if using an existion value
                            if self.ui.checkBox_5.isChecked():
                                #Using an existing value
                                #Get the "key=>value" for existing value
                                combo = self.ui.comboBox_12.currentText()
                                #Find wanted key by spliting it by "=>"
                                wanted_filed = combo.split("=>")[0].strip()
                                #Get the value of wanted key in header
                                value = self.fit.header(img, wanted_filed)[1]
                            else:
                                #Using a static value
                                #Getting the value value
                                value = self.ui.lineEdit_2.text()
                            try:
                                #Updating the header
                                self.fit.update_header(img, field, value)
                            except Exception as e:
                                #Log the exception if it happened
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
                        #Log an error about empty not existing file
                        self.etc.log("No such (Hedit)file({})".format(img))
                        
                    #Advance ProgressBar
                    g.proc(self, self.ui.progressBar_3, it/g.list_lenght(
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
            #Start an iteration for prgressBar
            it = 0.
            #Start a loop for each file name
            for i in range(self.ui.listWidget_5.count()):
                #Increase iteration
                it += 1
                #Find the possible file name
                img = self.ui.listWidget_5.item(i).text()
                #Check if file exist
                if self.fop.is_file(img):
                    #Split file name and the path
                    pth, name = self.fop.get_base_name(img)
                    #User file name and path given to create new file path
                    ofile = self.fop.abs_path("{}/{}".format(odir, name))
                    #User file name and path given to create mask file path
                    mfile = self.fop.abs_path("{}/mask_{}".format(odir, name))
                    #Start cosmic clean
                    data, header = myCos.fromfits(img)
                    c = myCos.cosmicsimage(data, gain=gain, readnoise=readN,
                                             sigclip=sigmC, sigfrac=sigmF,
                                             objlim=objeL)
                    
                    c.run(maxiter=max_it)
                    if not self.fop.is_file(ofile):
                        myCos.tofits(ofile, c.cleanarray, header)
                    if self.ui.checkBox_3.isChecked():
                        if not self.fop.is_file(mfile):
                            myCos.tofits(mfile, c.mask, header)
                    #Cosmic clean done
                else:
                    #Log an error about empty not existing file
                    self.et.log("No such (Cosmic Clean)file({})".format(img))
                
                #Advance ProgressBar
                g.proc(self, self.ui.progressBar_5, it/g.list_lenght(
                                                self, self.ui.listWidget_5))
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
        
    #Change annotation of WCS Tab
    def wcs_annotation(self):
        #Just find how many files were given for WCS
        img = g.list_lenght(self, self.ui.listWidget_11)
        self.ui.label_14.setProperty(
                "text",
                "Cosmic Cleaning will be applied for {0} files".format(img))
        
    #Save Settings to File
    def save_seetings(self):
        #Photometry settings
        if self.ui.groupBox_6.isChecked():
            photometry_ens = "yes"
        else:
            photometry_ens = "no"
            
        photometry_ens_catalog = self.ui.comboBox.currentIndex()
        photometry_ens_filter = self.ui.comboBox_11.currentIndex()
        
        photometry_sfp_anbulus = self.ui.doubleSpinBox_2.value()
        photometry_sfp_danbulus = self.ui.doubleSpinBox.value()
        photometry_sfp_cbox =self.ui.doubleSpinBox_3.value()
        
        photometry_dap_exposur = self.ui.lineEdit_13.text()
        photometry_dap_filter = self.ui.lineEdit_14.text()
        
        photometry_php_apertur = self.ui.lineEdit_15.text()
        photometry_php_zmag = self.ui.doubleSpinBox_8.value()
        photometry_php_gain = self.ui.lineEdit_26.text()
        
        photometry_wcs_ra = self.ui.lineEdit_22.text()
        photometry_wcs_dec = self.ui.lineEdit_23.text()
        
        if self.ui.checkBox_4.isChecked():
            photometry_lot_autoEpoch = "yes"
        else:
            photometry_lot_autoEpoch = "no"
            
        photometry_lot_observat = self.ui.lineEdit_18.text()
        photometry_lot_time = self.ui.lineEdit_17.text()
        photometry_lot_epoch = self.ui.lineEdit_25.text()
        
        photometry_stf_fluxrad = self.ui.doubleSpinBox_4.value()
        photometry_stf_minfwhm = self.ui.doubleSpinBox_5.value()
        photometry_stf_maxfwhm = self.ui.doubleSpinBox_6.value()
        photometry_stf_max2fnd = self.ui.spinBox.value()
        
        #Calibration settings
        calibration_zc_combine = self.ui.comboBox_2.currentIndex()
        calibration_zc_reject = self.ui.comboBox_3.currentIndex()
        
        calibration_zc_combine = self.ui.comboBox_2.currentIndex()
        calibration_zc_reject = self.ui.comboBox_3.currentIndex()
        
        calibration_dc_combine = self.ui.comboBox_4.currentIndex()
        calibration_dc_reject = self.ui.comboBox_5.currentIndex()
        calibration_dc_scale = self.ui.comboBox_8.currentIndex()
        
        calibration_fc_combine = self.ui.comboBox_6.currentIndex()
        calibration_fc_reject = self.ui.comboBox_7.currentIndex()
        calibration_fc_subset = self.ui.comboBox_9.currentIndex()
        
        calibration_ca_combine = self.ui.comboBox_10.currentIndex()
        
        #Cosmic Cleaner settings
        cosmicC_all_gain = self.ui.doubleSpinBox_20.value()
        cosmicC_all_readNoise = self.ui.doubleSpinBox_21.value()
        cosmicC_all_sigmaClip = self.ui.doubleSpinBox_22.value()
        cosmicC_all_SigmaFrac = self.ui.doubleSpinBox_23.value()
        cosmicC_all_objLim = self.ui.doubleSpinBox_24.value()
        
        #WCS settings
        if self.ui.groupBox_5.isChecked():
            wcs_all_goOnline = "yes"
        else:
            wcs_all_goOnline = "no"
            
            
        if self.ui.checkBox_2.isChecked():
            wcs_all_comp = "yes"
        else:
            wcs_all_comp = "no"
            
        wcs_all_server = self.ui.lineEdit_27.text()
        wcs_all_apikey = self.ui.lineEdit_28.text()
        
        try:
            self.etc.log("Settings will be saved in {}".format(
                    self.srttings_file))
            f_set = open(self.srttings_file, "w")
            
            f_set.write("photometry_ens|{0}\n".format(photometry_ens))
            f_set.write("photometry_ens_catalog|{0}\n".format(
                    photometry_ens_catalog))
            f_set.write("photometry_ens_filter|{0}\n".format(
                    photometry_ens_filter))
            
            f_set.write("photometry_sfp_anbulus|{0}\n".format(
                    photometry_sfp_anbulus))
            f_set.write("photometry_sfp_danbulus|{0}\n".format(
                    photometry_sfp_danbulus))
            f_set.write("photometry_sfp_cbox|{0}\n".format(
                    photometry_sfp_cbox))
            
            f_set.write("photometry_dap_exposur|{0}\n".format(
                    photometry_dap_exposur))
            f_set.write("photometry_dap_filter|{0}\n".format(
                    photometry_dap_filter))
            
            f_set.write("photometry_php_apertur|{0}\n".format(
                    photometry_php_apertur))
            f_set.write("photometry_php_zmag|{0}\n".format(
                    photometry_php_zmag))
            f_set.write("photometry_php_gain|{0}\n".format(
                    photometry_php_gain))
            
            f_set.write("photometry_wcs_ra|{0}\n".format(photometry_wcs_ra ))
            f_set.write("photometry_wcs_dec|{0}\n".format(photometry_wcs_dec))
            
            f_set.write("photometry_lot_autoEpoch|{0}\n".format(
                    photometry_lot_autoEpoch))
            f_set.write("photometry_lot_observat|{0}\n".format(
                    photometry_lot_observat))
            f_set.write("photometry_lot_time|{0}\n".format(
                    photometry_lot_time))
            f_set.write("photometry_lot_epoch|{0}\n".format(
                    photometry_lot_epoch))
            
            f_set.write("photometry_stf_fluxrad|{0}\n".format(
                    photometry_stf_fluxrad))
            f_set.write("photometry_stf_minfwhm|{0}\n".format(
                    photometry_stf_minfwhm))
            f_set.write("photometry_stf_maxfwhm|{0}\n".format(
                    photometry_stf_maxfwhm))
            f_set.write("photometry_stf_max2fnd|{0}\n".format(
                    photometry_stf_max2fnd))
            
            f_set.write("calibration_zc_combine|{0}\n".format(
                    calibration_zc_combine))
            f_set.write("calibration_zc_reject|{0}\n".format(
                    calibration_zc_reject))
    
            f_set.write("calibration_dc_combine|{0}\n".format(
                    calibration_dc_combine))
            f_set.write("calibration_dc_reject|{0}\n".format(
                    calibration_dc_reject))
            f_set.write("calibration_dc_scale|{0}\n".format(
                    calibration_dc_scale))
            
            f_set.write("calibration_fc_combine|{0}\n".format(
                    calibration_fc_combine))
            f_set.write("calibration_fc_reject|{0}\n".format(
                    calibration_fc_reject))
            f_set.write("calibration_fc_subset|{0}\n".format(
                    calibration_fc_subset))
            
            
            
            f_set.write("calibration_ca_combine|{0}\n".format(
                    calibration_ca_combine))
            
            
            f_set.write("cosmicC_all_gain|{0}\n".format(cosmicC_all_gain))
            f_set.write("cosmicC_all_readNoise|{0}\n".format(
                    cosmicC_all_readNoise))
            f_set.write("cosmicC_all_sigmaClip|{0}\n".format(
                    cosmicC_all_sigmaClip))
            f_set.write("cosmicC_all_SigmaFrac|{0}\n".format(
                    cosmicC_all_SigmaFrac))
            f_set.write("cosmicC_all_objLim|{0}\n".format(cosmicC_all_objLim))
            
            
            f_set.write("wcs_all_goOnline|{0}\n".format(wcs_all_goOnline))
            f_set.write("wcs_all_comp|{0}\n".format(wcs_all_comp))
            f_set.write("wcs_all_server|{0}\n".format(wcs_all_server))
            f_set.write("wcs_all_apikey|{0}\n".format(wcs_all_apikey))
            
            f_set.close()
        except Exception as e:
            self.etc.log(e)
        
        self.reload_log()
        
    #Read and apply settings From File
    def read_settings(self):
        try:
            self.etc.log("Settings will be applied from {}".format(
                    self.srttings_file))
            f_set = open(self.srttings_file, "r")
            for i in f_set:
                ln = i.replace("\n", "")
                if ln.startswith("photometry_ens|"):
                    val = ln.split("|")[1]
                    if val == "yes":
                        self.ui.groupBox_6.setChecked(True)
                    else:
                        self.ui.groupBox_6.setChecked(False)
                        
                if ln.startswith("photometry_ens_catalog|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox.setCurrentIndex(int(val))
                    
                if ln.startswith("photometry_sfp_anbulus|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_2.setValue(float(val))
                    
                if ln.startswith("photometry_sfp_danbulus|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox.setValue(float(val))
                    
                if ln.startswith("photometry_sfp_cbox|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_3.setValue(float(val))
                    
                if ln.startswith("photometry_dap_exposur|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_13.setText(str(val))
                    
                if ln.startswith("photometry_dap_filter|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_14.setText(str(val))
                    
                if ln.startswith("photometry_php_apertur|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_15.setText(str(val))
                    
                if ln.startswith("photometry_php_zmag|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_8.setValue(float(val))
                    
                if ln.startswith("photometry_php_gain|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_26.setText(str(val))
                    
                if ln.startswith("photometry_wcs_ra|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_22.setText(str(val))
                    
                if ln.startswith("photometry_wcs_dec|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_23.setText(str(val))
                    
                if ln.startswith("photometry_lot_autoEpoch|"):
                    val = ln.split("|")[1]
                    if val == "yes":
                        self.ui.checkBox_4.setChecked(True)
                    else:
                        self.ui.checkBox_4.setChecked(False)
                        
                if ln.startswith("photometry_lot_observat|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_18.setText(str(val))
                    
                if ln.startswith("photometry_lot_time|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_17.setText(str(val))
                    
                if ln.startswith("photometry_lot_epoch|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_25.setText(str(val))
                    
                if ln.startswith("photometry_stf_fluxrad|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_4.setValue(float(val))
                    
                if ln.startswith("photometry_stf_minfwhm|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_5.setValue(float(val))
                    
                if ln.startswith("photometry_stf_maxfwhm|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_6.setValue(float(val))
                    
                if ln.startswith("photometry_stf_max2fnd|"):
                    val = ln.split("|")[1]
                    self.ui.spinBox.setValue(int(val))
                    
                if ln.startswith("calibration_zc_combine|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_2.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_zc_reject|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_3.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_dc_combine|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_4.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_dc_reject|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_5.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_dc_scale|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_8.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_fc_combine|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_6.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_fc_reject|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_7.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_fc_subset|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_9.setCurrentIndex(int(val))
                    
                if ln.startswith("calibration_ca_combine|"):
                    val = ln.split("|")[1]
                    self.ui.comboBox_10.setCurrentIndex(int(val))
                    
                if ln.startswith("cosmicC_all_gain|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_20.setValue(float(val))
                    
                if ln.startswith("cosmicC_all_readNoise|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_21.setValue(float(val))
                    
                if ln.startswith("cosmicC_all_sigmaClip|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_22.setValue(float(val))
                    
                if ln.startswith("cosmicC_all_SigmaFrac|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_23.setValue(float(val))
                    
                if ln.startswith("cosmicC_all_objLim|"):
                    val = ln.split("|")[1]
                    self.ui.doubleSpinBox_24.setValue(float(val))
                    
                if ln.startswith("wcs_all_goOnline|"):
                    val = ln.split("|")[1]
                    if val == "yes":
                        self.ui.groupBox_5.setChecked(True)
                    else:
                        self.ui.groupBox_5.setChecked(False)
                        
                if ln.startswith("wcs_all_comp|"):
                    val = ln.split("|")[1]
                    if val == "yes":
                        self.ui.checkBox_2.setChecked(True)
                    else:
                        self.ui.checkBox_2.setChecked(False)
                        
                if ln.startswith("wcs_all_server|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_27.setText(str(val))
                    
                if ln.startswith("wcs_all_apikey|"):
                    val = ln.split("|")[1]
                    self.ui.lineEdit_28.setText(str(val))
        except Exception as e:
            self.etc.log(e)
                
        self.reload_log()
        
    def astrometrynet_check(self):
        if osname == 'nt':
            QtWidgets.QMessageBox.critical(self, ("MYRaf Error"), ("The Astrometry.net does not support your os.\nYou HAVE to use online version."))
            self.ui.groupBox_5.setChecked(True)
            self.etc.log("No Astrometry.new for Windows.")
        else:
            print("other")
            
        self.reload_log()
        
    def load_observat(self):
        obs_files = self.fop.list_of_fiels(self.fop.abs_path("./observat"), ext="*")
        new_list = []
        for i in obs_files:
            new_list.append(self.fop.get_base_name(i)[1])
        g.replace_list_con(self, self.ui.listWidget_12, new_list)
        
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
                    
            
            self.ui.plainTextEdit.setPlainText(QtWidgets.QApplication.translate("Form", "\n".join(comm.split('\n')[1:]), None))
                    
        else:
            self.etc.log("No such Observatory({})".format(obs_name))
        self.reload_log()
    
    def rm_obs(self):
        obs_name = self.ui.listWidget_12.currentItem().text()
        obs_path = self.fop.abs_path("./observat/{}".format(obs_name))
        if self.fop.is_file(obs_path):
            self.fop.rm(obs_path)
        else:
            #Log and display an error about about not existing observatory name
            self.etc.log("No such Observatory({})".format(obs_name))
            QtWidgets.QMessageBox.critical(
                    self, ("MYRaf Error"), ("No observatory was specified"))
            
        self.load_observat()
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
        
    def reload_log(self):
        g.rm_all(self, self.ui.listWidget_10)
        g.add_line_by_line(self, self.ui.listWidget_10, self.etc.mini_log_file)
        
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
    app = QtWidgets.QApplication(sys.argv)
    f = MyForm()
    f.show()
    app.exec_()