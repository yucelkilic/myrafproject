# -*- coding: utf-8 -*-
"""
Created:--------------------------------------------------------------------------------------------
		By:
			Muhammed SHEMUNI		Developer
			Yücel KILIÇ				Developer
		at:
			Begin					04.12.2013
			Last update				13.12.2013
Importing things:-----------------------------------------------------------------------------------
		Must have as installed:
			python-2.7
			pyqt4-dev-tools
			imagemagick(convert)
			iraf					http://www.astro.uson.mx/~favilac/downloads/ubuntu-iraf/iso/
			pyraf					^
			sextractor				http://www.astromatic.net/software/sextractor/
			alipy					http://obswww.unige.ch/~tewes/alipy/
			astroasciidata			http://www.stecf.org/software/PYTHONtools/astroasciidata/
			f2n						http://obswww.unige.ch/~tewes/f2n_dot_py/
----------------------------------------------------------------------------------------------------
"""
import sys , os, time, string, math, signal, datetime, ntpath

os.system("echo \"- " + str(datetime.datetime.utcnow()) + " - MYRaf started.\" >>log.my")

try:
	from myraf import Ui_Form
	import function, gui
except:
	print("Can not load MYRaf.")
	os.system("echo \"-- " + str(datetime.datetime.utcnow()) + " - MYRaf is not installed properly.\">>log.my")
	raise SystemExit
try:
	from PyQt4 import QtGui, QtCore
	from PyQt4.QtGui import *
	from PyQt4.QtCore import *
except:
	print("Can not load PyQT4")
	gui.logging(self, "-- %s - Did you install PyQT4?" %(datetime.datetime.utcnow()))
	raise SystemExit

try:
	from pyraf import iraf
	from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom
except:
	print("Can not load PyRAF, iraf")
	gui.logging(self, "-- %s - Did you install PyRAF, iraf?" %(datetime.datetime.utcnow()))
	raise SystemExit

try:
	import alipy
	import glob
except:
	print("Did you install 'alipy'? To furter information:\nhttp://obswww.unige.ch/~tewes/alipy/")
	gui.logging(self, "-- %s - Where is alipy & glob?" %(datetime.datetime.utcnow()))
	raise SystemExit
		
class MyForm(QtGui.QWidget):
  def __init__(self):
    super(MyForm, self).__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    
    me = self.ui
	
    os.system("rm -rf ./tmp/*")
    os.system("rm -rf ./alipy_visu")
    os.system("rm -rf ./alipy_out")
    os.system("mkdir -p ./tmp/alipy/")
    os.system("mkdir -p ./tmp/analyzed/")
      
    f = open('./log.my', 'r')
    it = self.ui.listWidget_10.count()-1
    for line in f:
		li=line.strip()
		li = str(li)
		it = it+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_10.addItem(item)
		item = self.ui.listWidget_10.item(it)
		item.setText(QtGui.QApplication.translate("Form", str(li), None, QtGui.QApplication.UnicodeUTF8))

    it = self.ui.listWidget_12.count()-1
    for files in glob.glob("./obsdat/*"):
		fn = ntpath.basename(str(files))
		it = it+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_12.addItem(item)
		item = self.ui.listWidget_12.item(it)
		item.setText(QtGui.QApplication.translate("Form", str(fn), None, QtGui.QApplication.UnicodeUTF8))
    self.ui.listWidget_12.sortItems()
      
    self.ui.tabWidget_2.setTabEnabled(1,False)
    self.ui.tabWidget_2.setTabEnabled(2,False)
    self.ui.tabWidget_2.setTabEnabled(3,False)


    self.ui.checkBox.clicked.connect(self.unlockBias)
    self.ui.checkBox_2.clicked.connect(self.unlockDark)
    self.ui.checkBox_3.clicked.connect(self.unlockFlat)
    


    self.ui.radioButton.clicked.connect(self.unlockIrafPhot)
    self.ui.radioButton_2.clicked.connect(self.unlockEnsfPhot)
    
    self.ui.pushButton_34.clicked.connect(self.saveSettings)
    
    self.ui.pushButton_3.clicked.connect(self.imgAdd)
    self.ui.pushButton_4.clicked.connect(self.imgRm)
    self.ui.pushButton_5.clicked.connect(self.biasAdd)
    self.ui.pushButton_6.clicked.connect(self.biasRm)
    self.ui.pushButton_10.clicked.connect(self.darkAdd)
    self.ui.pushButton_8.clicked.connect(self.darkRm)
    self.ui.pushButton_13.clicked.connect(self.flatAdd)
    self.ui.pushButton_11.clicked.connect(self.flatRm)
    self.ui.pushButton_15.clicked.connect(self.autAlignAdd)
    self.ui.pushButton_16.clicked.connect(self.autAlignRm)
    self.ui.pushButton_22.clicked.connect(self.manAlignAdd)
    self.ui.pushButton_21.clicked.connect(self.manAlignRm)
    self.ui.pushButton_33.clicked.connect(self.photAdd)
    self.ui.pushButton_32.clicked.connect(self.photRm)
    
    self.ui.pushButton_36.clicked.connect(self.heditAdd)
    self.ui.pushButton_37.clicked.connect(self.heditRm)
    
    self.ui.listWidget_5.clicked.connect(self.displayAutAlign)
    self.ui.graphicsView.wheelEvent = self.zoomAutAlign
    self.ui.pushButton_17.clicked.connect(self.rlAutAlign)
    self.ui.pushButton_18.clicked.connect(self.fhAutAlign)
    self.ui.pushButton_19.clicked.connect(self.fvAutAlign)
    self.ui.pushButton_20.clicked.connect(self.rrAutAlign)
    self.ui.pushButton_14.clicked.connect(self.goAutAlign)
    
    self.ui.listWidget_6.clicked.connect(self.displayManAlign)
    self.ui.graphicsView_2.wheelEvent = self.zoomManAlign
    self.ui.pushButton_23.clicked.connect(self.rlManAlign)
    self.ui.pushButton_24.clicked.connect(self.fhManAlign)
    self.ui.pushButton_25.clicked.connect(self.fvManAlign)
    self.ui.pushButton_27.clicked.connect(self.goManAlign)
    
    self.ui.listWidget_7.clicked.connect(self.displayPhot)
    self.ui.graphicsView_3.wheelEvent = self.zoomPhot
    self.ui.pushButton_28.clicked.connect(self.rlPhot)
    self.ui.pushButton_29.clicked.connect(self.fhPhot)
    self.ui.pushButton_30.clicked.connect(self.fvPhot)
    self.ui.pushButton_31.clicked.connect(self.rrPhot)
    self.ui.checkBox_4.clicked.connect(self.photChange)
    self.ui.pushButton_45.clicked.connect(self.photCooRm)
    self.ui.pushButton_35.clicked.connect(self.goPhot)
    
    self.ui.listWidget_9.clicked.connect(self.getHeader)
    self.ui.listWidget_11.clicked.connect(self.getVlueFromHeader)
    self.ui.checkBox_5.clicked.connect(self.unlockGetHeaderFromValue)
    self.ui.pushButton_39.clicked.connect(self.goHeaderAdd)
    self.ui.pushButton_38.clicked.connect(self.goHeaderDel)
    
    self.ui.listWidget_12.clicked.connect(self.getObservat)
    self.ui.pushButton_41.clicked.connect(self.rmObservatory)
    self.ui.pushButton_40.clicked.connect(self.addObservatory)
    
    self.ui.pushButton_7.clicked.connect(self.masterZero)
    self.ui.pushButton_9.clicked.connect(self.masterDark)
    self.ui.pushButton_12.clicked.connect(self.masterFlat)
    
    self.ui.pushButton.clicked.connect(self.calib)
    
    self.ui.pushButton_44.clicked.connect(self.readStars)
    self.ui.pushButton_46.clicked.connect(self.plotChart)
  
    self.ui.pushButton_34.clicked.connect(self.saveSettings)
    self.applySettings()

#Read Stars ID to Graph Tab###################################
  def readStars(self):
      filename = QtGui.QFileDialog.getOpenFileName(self ,"MYRaf Result File...","",("My Files (*.my *.myf)"))
      self.ui.label_43.setText(QtGui.QApplication.translate("Form", "File location: %s" %(filename), None, QtGui.QApplication.UnicodeUTF8))
      # counting stars in result file
      dataCount = os.popen("cat %s |awk '{if ($1 == 1) print $1}'|wc -l" %(filename))
      dataCount=dataCount.readline().replace("\n","")
      lineCount = os.popen("cat %s| wc -l" %(filename))
      lineCount = lineCount.readline().replace("\n","")
      starCount = int(lineCount)/int(dataCount)
      #clearing comboxBoxs
      self.ui.comboBox_11.clear()
      self.ui.comboBox_12.clear()
      self.ui.comboBox_13.clear()
      for i in range(1, starCount+1):
          self.ui.comboBox_11.addItem(str(i))
          self.ui.comboBox_12.addItem(str(i))
          self.ui.comboBox_13.addItem(str(i))
      self.ui.comboBox_14.clear()
      #getting apertures
      for aperture in self.ui.lineEdit_15.text().split(","):
          self.ui.comboBox_14.addItem(aperture.replace("\n", ""))

#Plot Chart#############################################
  def plotChart(self):
      import numpy as np
      # reading form
      varStarID = self.ui.comboBox_11.currentText()
      checkStarID = self.ui.comboBox_12.currentText()
      refStarID = self.ui.comboBox_13.currentText()
      apertureIndex = self.ui.comboBox_14.currentIndex() + 3
      
      # reading result file
      neednt,  filename = self.ui.label_43.text().split(":")
      filename = filename.replace("\n", "")
      function.readResultFile(filename, varStarID, apertureIndex)
      function.readResultFile(filename, checkStarID, apertureIndex)
      function.readResultFile(filename, refStarID, apertureIndex)
      
      # varStar
      filep = open("tmp/idjdmag_%s.my" %(varStarID), "r")
      varDatas = filep.readlines()
      filep.close()
      # checkStar
      filep = open("tmp/idjdmag_%s.my" %(checkStarID), "r")
      checkDatas = filep.readlines()
      filep.close()
      # refStar
      filep = open("tmp/idjdmag_%s.my" %(refStarID), "r")
      refDatas = filep.readlines()
      filep.close()  
      # numpy operations
      varPhase1 = []
      varMag1 = []
      checkMag1 = []
      refMag1 = []
      diffMag = []
      residuMag = []
      # Variable
      for varData in varDatas:
          vData = varData.split()
          try:
              varPhase1.append(((float(vData[1]) - float(self.ui.lineEdit_19.text()))/(float(self.ui.lineEdit_20.text()))) - int(((float(vData[1]) - float(self.ui.lineEdit_19.text()))/(float(self.ui.lineEdit_20.text())))))
              varMag1.append(float(vData[2]))
          except:
              varMag1.append(float(0))
      # Check
      for checkData in checkDatas:
          cData = checkData.split()
          try:
              checkMag1.append(float(cData[2]))
          except:
              checkMag1.append(float(0))
      # Ref
      for refData in refDatas:
          rData = refData.split()
          try:
              refMag1.append(float(rData[2]))
          except:
              refMag1.append(float(0))
          
      varPhase = np.array(varPhase1)
      varMag = np.array(varMag1)
      checkMag = np.array(checkMag1)
      refMag = np.array(refMag1)
      diffMag = varMag - checkMag
      residuMag = checkMag - refMag
      
      #Plot
      gui.PlotFunc(self,  self.ui.disp_chart.canvas, varPhase, diffMag,  residuMag)
  
########################################################

#Pohtometry#############################################
  def getObservat(self):
	fl = self.ui.listWidget_12.currentItem()
	fl = fl.text()
	
	self.ui.lineEdit_3.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEdit_4.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEdit_5.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEdit_6.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEdit_7.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEdit_8.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.plainTextEdit.setPlainText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	
	f = open("obsdat/%s" %str(fl), "r")
	for i in f:
		ln = i.replace("\n","")
		if ln.replace("	","").startswith("observatory"):
			self.ui.lineEdit_3.setText(QtGui.QApplication.translate("Form", str(ln).split("=")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("name"):
			self.ui.lineEdit_4.setText(QtGui.QApplication.translate("Form", str(ln).split("=")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("longitude"):
			self.ui.lineEdit_5.setText(QtGui.QApplication.translate("Form", str(ln).split("=")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("latitude"):
			self.ui.lineEdit_6.setText(QtGui.QApplication.translate("Form", str(ln).split("=")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("altitude"):
			self.ui.lineEdit_7.setText(QtGui.QApplication.translate("Form", str(ln).split("=")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("timezone"):
			self.ui.lineEdit_8.setText(QtGui.QApplication.translate("Form", str(ln).split("=")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))
			
		if ln.replace("	","").startswith("#"):
			self.ui.plainTextEdit.setPlainText(QtGui.QApplication.translate("Form", "%s" %(ln.replace("#","")), None, QtGui.QApplication.UnicodeUTF8))
			
	
  def rmObservatory(self):
	fl = self.ui.listWidget_12.currentItem()
	fl = fl.text()
	os.popen("rm -rf ./obsdat/%s" %(str(fl)))
	c=self.ui.listWidget_12.count()
	for i in xrange(c):
		self.ui.listWidget_12.takeItem(0)
	
	it = self.ui.listWidget_12.count()-1
	for files in glob.glob("./obsdat/*"):
		fn = ntpath.basename(str(files))
		it = it+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_12.addItem(item)
		item = self.ui.listWidget_12.item(it)
		item.setText(QtGui.QApplication.translate("Form", str(fn), None, QtGui.QApplication.UnicodeUTF8))
	self.ui.listWidget_12.sortItems()

  def addObservatory(self):
	fl = self.ui.listWidget_12.currentItem()
	
	observatory = self.ui.lineEdit_3.text()
	name = self.ui.lineEdit_4.text()
	longitude = self.ui.lineEdit_5.text()
	latitude = self.ui.lineEdit_6.text()
	altitude = self.ui.lineEdit_7.text()
	timeZone = self.ui.lineEdit_8.text()
	other = self.ui.plainTextEdit.toPlainText
	
	f = open("./obsdat/%s" %observatory, "w")
	f.write("#%s\n" %other.replace("\n"," "))
	f.write("observatory=\"%s\"\n" %observatory)
	f.write("\tname=\"%s\"\n" %name)
	f.write("\tlongitude=%s\n" %longitude)
	f.write("\tlatitude=%s\n" %latitude)
	f.write("\taltitude=%s\n" %altitude)
	f.write("\ttimezone=%s\n" %timeZone)
	f.close()
	
	c=self.ui.listWidget_12.count()
	for i in xrange(c):
		self.ui.listWidget_12.takeItem(0)
	
	it = self.ui.listWidget_12.count()-1
	for files in glob.glob("./obsdat/*"):
		fn = ntpath.basename(str(files))
		it = it+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_12.addItem(item)
		item = self.ui.listWidget_12.item(it)
		item.setText(QtGui.QApplication.translate("Form", str(fn), None, QtGui.QApplication.UnicodeUTF8))
	self.ui.listWidget_12.sortItems()
		
########################################################
#Header Editor##########################################
  def getHeader(self):
	
	img = self.ui.listWidget_9.currentItem()
	img = img.text()
	h = iraf.hedit(img, "*", ".", Stdout=1)
	
	c=self.ui.listWidget_11.count()
	for i in xrange(c):
		self.ui.listWidget_11.takeItem(0)
		
	it = self.ui.listWidget_11.count()-1
	for i in h:
		it = it+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_11.addItem(item)
		item = self.ui.listWidget_11.item(it)
		item.setText(QtGui.QApplication.translate("Form", i.split(",")[1], None, QtGui.QApplication.UnicodeUTF8))
		self.ui.comboBox.addItem(i.split(",")[1])
		
  def getVlueFromHeader(self):
	hed = self.ui.listWidget_11.currentItem()
	hed = hed.text()
	field, val = hed.split(" = ")
	self.ui.lineEdit.setText(QtGui.QApplication.translate("Form", str(field), None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEdit_2.setText(QtGui.QApplication.translate("Form", str(val), None, QtGui.QApplication.UnicodeUTF8))
	
  def unlockGetHeaderFromValue(self):
	if self.ui.checkBox_5.checkState() == QtCore.Qt.Checked:
		self.ui.lineEdit_2.setEnabled(False)
		self.ui.comboBox.setEnabled(True)
	else:
		self.ui.lineEdit_2.setEnabled(True)
		self.ui.comboBox.setEnabled(False)
		
  def goHeaderAdd(self):
	if self.ui.listWidget_9.count() != 0:
		headErr = ""
		it = 0
		for x in xrange(self.ui.listWidget_9.count()):
			it = it + 1
			img = self.ui.listWidget_9.item(x)
			img = str(img.text())
			field = self.ui.lineEdit.text()
			if self.ui.checkBox_5.checkState() != QtCore.Qt.Checked:
				val = self.ui.lineEdit_2.text()
			else:
				h = self.ui.comboBox.currentText()
				selectedField = h.split(" = ")[0]
				val = str("'(@\"%s\")'" %selectedField)
			
			self.ui.progressBar_4.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_9.count())))))
			self.ui.label_41.setText(QtGui.QApplication.translate("Form", "Header delete: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
				
			if function.headerWrite(img, field, val):
				self.getHeader()
			else:
				headErr = "%s\n%s" %(headErr, ntpath.basename(str(img)))
					
		if headErr != "" :
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>hedit</b> can not handle this job for images below\n%s" %(headErr)))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select some images."))
	
  def goHeaderDel(self):
	if self.ui.listWidget_9.count() != 0:
		f = self.ui.listWidget_11.currentItem()
		f = f.text()
		field = f.split(" = ")[0]
		heErr = ""
		it = 0
		for x in xrange(self.ui.listWidget_9.count()):
			it = it + 1
			img = self.ui.listWidget_9.item(x)
			img = str(img.text())
			if function.headerDel(img, field):
				self.getHeader()
			else:
				heErr = "%s\n%s" %(headErr, ntpath.basename(str(img)))					
				
			self.ui.progressBar_4.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_9.count())))))
			self.ui.label_41.setText(QtGui.QApplication.translate("Form", "Header delete: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))

		if heErr != "":
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>hedit</b> can not handle this job for images below\n%s" %(heErr)))
			
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select some images."))
########################################################
#Pohtometry#############################################
  def displayPhot(self):
	if self.ui.checkBox_4.checkState() == QtCore.Qt.Checked:
		img = self.ui.listWidget_7.currentItem()
		img = img.text()
		if not function.autoAlign(str(img), str(img), "./tmp", False, True):
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>alipy</b> can not handle this job."))
		else:
			os.popen("rm -rf tmp/%s" %(ntpath.basename(str(img))))
			
		coorFile = "alipy_cats/%s.pysexcat" %(ntpath.basename(str(img)).split(".")[0])
		dotPic = "alipy_visu/%s_stars.png" %(ntpath.basename(str(img)).split(".")[0])
		print(dotPic)
		os.popen("cp " + dotPic + " ./tmp/display.png")
		gui.display(self, "./tmp/display.png", self.ui.graphicsView_3)
		os.popen("cat %s | grep -v '#' | awk '{print $1,$2}' > tmp/photCoo" %(coorFile))
		os.popen("rm -rf ./alipy_cats/ ./alipy_out/ ./alipy_visu/")
	else:
		gui.logging(self, "-- %s - image conversion started." %(datetime.datetime.utcnow()))
		img = self.ui.listWidget_7.currentItem()
		img = img.text()
		if not function.fits2png(img, "./tmp/display.png"):
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>imagemagick</b> can not handle this job."))
			gui.logging(self, "--- %s - imagemagick failed." %(datetime.datetime.utcnow()))
		else:
			gui.logging(self, "--- %s - imagemagick succeed." %(datetime.datetime.utcnow()))
			self.display("./tmp/display.png", self.ui.graphicsView_3)
			
  def zoomPhot(self, ev):
	if ev.delta() < 0:
		gui.zoom(self, self.ui.graphicsView_3, 0.9)
	else:
		 gui.zoom(self, self.ui.graphicsView_3, 1.1)
		 
  def rlPhot(self):
	gui.rot(self, self.ui.graphicsView_3, -90)
	
  def rrPhot(self):
	gui.rot(self, self.ui.graphicsView_3, 90)
	
  def fvPhot(self):
	gui.flip(self, self.ui.graphicsView_3, "v")

  def fhPhot(self):
	gui.flip(self, self.ui.graphicsView_3, "h")
	
  def pixelSelectPhot(self, event):
	if self.ui.checkBox_4.checkState() != QtCore.Qt.Checked:
		img = self.ui.listWidget_7.currentItem()
		img = img.text()
		height = function.headerRead(img, "i_naxis2")
		x = event.pos().x()
		y = float(height) - event.pos().y()
		it = self.ui.listWidget_8.count()
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_8.addItem(item)
		item = self.ui.listWidget_8.item(it)
		item.setText(QtGui.QApplication.translate("Form", "%s-%s" %(x, y), None, QtGui.QApplication.UnicodeUTF8))
		
		if not os.path.exists("./tmp/photCoo"):
			os.popen("rm -rf ./tmp/photCoo")
			
		f = open("./tmp/photCoo", "w")
		for x in xrange(self.ui.listWidget_8.count()):
			coo = self.ui.listWidget_8.item(x)
			coo = coo.text()
			f.write("%s\n" %coo.replace("-"," "))
		f.close()
			
  def photChange(self):
	if self.ui.listWidget_7.currentItem() != None:
		if self.ui.checkBox_4.checkState() != QtCore.Qt.Checked:
			self.ui.listWidget_8.setEnabled(True)
		else:
			self.ui.listWidget_8.setEnabled(False)
		self.displayPhot()	
	else:
		if self.ui.checkBox_4.checkState() != QtCore.Qt.Checked:
			self.ui.listWidget_8.setEnabled(True)
		else:
			self.ui.listWidget_8.setEnabled(False)
			
  def goPhot(self):
	if self.ui.radioButton.isChecked():		
		if os.path.exists("./tmp/photCoo"):
			gui.logging(self, "-- %s - phot started." %(datetime.datetime.utcnow()))
			if self.ui.listWidget_7.count() != 0:
				it = 0
				for x in xrange(self.ui.listWidget_7.count()):
					it = it + 1
					img = self.ui.listWidget_7.item(x)
					img = str(img.text())
					OBS = function.headerRead(img, "observat").split("-")[0]
					jdErr=""
					srErr=""
					amErr=""
					phErr=""
					exp = str(self.ui.lineEdit_13.text())
					fil = str(self.ui.lineEdit_14.text())
					ann = str(self.ui.dial.value())
					dan = str(self.ui.dial_2.value())
					cbo = str(self.ui.dial_3.value())
					ape = str(self.ui.lineEdit_15.text())
					zma = str(self.ui.lineEdit_16.text())
					observatory = str(self.ui.lineEdit_18.text())
					oti = str(self.ui.lineEdit_17.text())
					print(zma)
					if function.JD(img, OBS, time=oti):
						if function.sideReal(img, OBS):
							if function.airmass(img, OBS, time=oti):
								if function.phot(img, "./tmp/analyzed/", "./tmp/photCoo", expTime = exp, Filter = fil, centerBOX = cbo, annulus = ann, dannulus = dan, apertur = ape, zmag = zma):
									if function.txDump("./tmp/analyzed/%s.mag.1" %(ntpath.basename(str(img))), "./tmp/out%s" %str(it)):
										os.popen("cat ./tmp/out%s >> tmp/res.my" %str(it))
										os.popen("rm -rf ./tmp/out%s" %str(it))
								else:
									phErr = "%s\n%s" %(phErr, ntpath.basename(str(img)))
									gui.logging(self, "--- %s - phot failed with %s." %(datetime.datetime.utcnow(), ntpath.basename(str(img))))
							else:
								amErr = "%s\%s" %(amErr, ntpath.basename(str(img)))
								gui.logging(self, "--- %s - airmass failed with %s." %(datetime.datetime.utcnow(), ntpath.basename(str(img))))
						else:
							srErr = "%s\%s" %(srErr, ntpath.basename(str(img)))
							gui.logging(self, "--- %s - sidereal time calculator failed with %s." %(datetime.datetime.utcnow(), ntpath.basename(str(img))))
					else:
						jdErr = "%s\%s" %(ahErr, ntpath.basename(str(img)))
						gui.logging(self, "--- %s - JD failed with %s." %(datetime.datetime.utcnow(), ntpath.basename(str(img))))
					
					self.ui.progressBar_5.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_7.count())))))
					self.ui.label_14.setText(QtGui.QApplication.translate("Form", "Phpotometry: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
					
				if phErr != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>phot</b> can not handle this job for images below\n%s" %(phErr)))

				if amErr != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>airmass</b> can not handle this job for images below\n%s" %(amErr)))

				if srErr != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>AstHedit</b> can not handle this job for images below\n%s" %(srErr)))

				if jdErr != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>JD</b> can not handle this job for images below\n%s" %(jdErr)))
			
				ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save resoult file', 'res.my', 'Text (*.my)')
				os.popen("mv ./tmp/res.my %s" %ofile)
			
			else:
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select some images."))
		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select coordinates for photometry."))
	else:
		print("ens phot")
		
########################################################
#Manual Align############################################
  def displayManAlign(self):
	gui.logging(self, "-- %s - image conversion started." %(datetime.datetime.utcnow()))
	img = self.ui.listWidget_6.currentItem()
	img = img.text()
	if not function.fits2png(img, "./tmp/display.png"):
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>imagemagick</b> can not handle this job."))
		gui.logging(self, "--- %s - imagemagick failed." %(datetime.datetime.utcnow()))
	else:
		gui.logging(self, "--- %s - imagemagick succeed." %(datetime.datetime.utcnow()))
		coors = function.headerRead(img, "MYRafCor")
		print("coors are:" + coors)
		self.ui.label_11.setText(QtGui.QApplication.translate("Form", "%s" %(coors), None, QtGui.QApplication.UnicodeUTF8))
		self.display("./tmp/display.png", self.ui.graphicsView_2)
	
  def zoomManAlign(self, ev):
	if ev.delta() < 0:
		gui.zoom(self, self.ui.graphicsView_2, 0.9)
	else:
		 gui.zoom(self, self.ui.graphicsView_2, 1.1)

  def rlManAlign(self):
	gui.rot(self, self.ui.graphicsView_2, -90)
	
  def rrManAlign(self):
	gui.rot(self, self.ui.graphicsView_2, 90)
	
  def fvManAlign(self):
	gui.flip(self, self.ui.graphicsView_2, "v")

  def fhManAlign(self):
	gui.flip(self, self.ui.graphicsView_2, "h")
	
  def pixelManAlign(self, event):
	rows = self.ui.listWidget_6.count()
	row = self.ui.listWidget_6.currentRow()
	if row < rows-1:
		img = self.ui.listWidget_6.currentItem()
		img = img.text()
		height = function.headerRead(img, "i_naxis2")
		print(height)
		x = event.pos().x()
		y = float(height) - event.pos().y()
		function.headerWrite(img, "MYRafCor", "%s-%s" %(str(x), str(y)))
		self.ui.listWidget_6.setCurrentRow(row+1)
		img = self.ui.listWidget_6.currentItem()
		img = img.text()
		self.displayManAlign()
	elif row == rows-1:
		img = self.ui.listWidget_6.currentItem()
		img = img.text()
		height = function.headerRead(img, "i_naxis2")
		print(height)
		x = event.pos().x()
		y = float(height) - event.pos().y()
		function.headerWrite(img, "MYRafCor", "%s-%s" %(str(x), str(y)))
		self.ui.listWidget_6.setCurrentRow(0)
		img = self.ui.listWidget_6.currentItem()
		img = img.text()
		self.displayManAlign()
		
  def goManAlign(self):
	if self.ui.listWidget_6.count() != 0:
		if self.ui.listWidget_6.currentItem() != None:
			img = self.ui.listWidget_6.currentItem()
			img = img.text()
			coorRef = function.headerRead(img, "MYRafCor").split("-")
			print("evet:" + str(coorRef))
			if str(coorRef) != "['']":
				xref = coorRef[0]
				yref = coorRef[1]
				odir = QtGui.QFileDialog.getExistingDirectory( self, 'Select Directory to Save Aligned File(s)')
				it = 0
				for x in xrange(self.ui.listWidget_6.count()):
					it = it + 1
					img = self.ui.listWidget_6.item(x)
					img = str(img.text())
					self.ui.label_10.setText(QtGui.QApplication.translate("Form", "Aligning: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
					ofile = "%s/%s" %(odir, ntpath.basename(str(img)))
					coorImg = function.headerRead(img, "MYRafCor").split("-")
					if str(coorImg) != "['']":
						ximg = coorImg[0]
						yimg = coorImg[1]
						x = float(xref) - float(ximg)
						y = float(yref) - float(yimg)
						if not function.manAlign(img, x, y, ofile):
							QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>imshift</b> can not handle this job."))
							gui.logging(self, "--- %s - imshift failed." %(datetime.datetime.utcnow()))
				
					self.ui.progressBar_3.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_6.count())))))
			else:
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select coordinates for reference image."))
		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select a reference image first."))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please add some <b>Image</b> files."))
	
########################################################
#Auto Align#############################################
  def displayAutAlign(self):
	gui.logging(self, "-- %s - image conversion started." %(datetime.datetime.utcnow()))
	img = self.ui.listWidget_5.currentItem()
	img = img.text()
	if not function.fits2png(img, "./tmp/display.png"):
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>imagemagick</b> can not handle this job."))
		gui.logging(self, "--- %s - imagemagick failed." %(datetime.datetime.utcnow()))
	else:
		gui.logging(self, "--- %s - imagemagick succeed." %(datetime.datetime.utcnow()))
		gui.display(self, "./tmp/display.png", self.ui.graphicsView)

  def zoomAutAlign(self, ev):
	if ev.delta() < 0:
		gui.zoom(self, self.ui.graphicsView, 0.9)
	else:
		 gui.zoom(self, self.ui.graphicsView, 1.1)
		 
  def rlAutAlign(self):
	gui.rot(self, self.ui.graphicsView, -90)
	
  def rrAutAlign(self):
	gui.rot(self, self.ui.graphicsView, 90)
	
  def fvAutAlign(self):
	gui.flip(self, self.ui.graphicsView, "v")

  def fhAutAlign(self):
	gui.flip(self, self.ui.graphicsView, "h")

  def goAutAlign(self):
	if self.ui.listWidget_5.count() != 0:
		if self.ui.listWidget_5.currentItem() != None:
			gui.logging(self, "-- %s - AutoAlign started." %(datetime.datetime.utcnow()))
			ref = self.ui.listWidget_5.currentItem()
			ref = str(ref.text())
			it = 0
			odir = QtGui.QFileDialog.getExistingDirectory( self, 'Select Directory to Save Aligned File(s)')
			aliErr = ""
			for x in xrange(self.ui.listWidget_5.count()):
				it = it + 1
				img = self.ui.listWidget_5.item(x)
				img = str(img.text())
				self.ui.label_7.setText(QtGui.QApplication.translate("Form", "Aligning: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
				if not function.autoAlign(img, ref, odir):
					aliErr = "%s\%s" %(aliErr, ntpath.basename(str(img)))
					gui.logging(self, "--- %s - alipy failed." %(datetime.datetime.utcnow()))					
				self.ui.progressBar_2.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_5.count())))))
				os.popen("rm -rf ./alipy_cats/ ./alipy_out/")
			gui.logging(self, "-- %s - AutoAlign finished aligning." %(datetime.datetime.utcnow()))
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>alipy</b> can not align images below\n%s") %aliErr)

		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select a reference image first."))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please add some <b>Image</b> files."))
########################################################
#Calibration############################################
  def calib(self):
	if self.ui.listWidget.count() != 0:
		gui.logging(self, "-- %s - Calibration started." %(datetime.datetime.utcnow()))
		b, d, f="","",""
		if self.ui.checkBox.checkState() == QtCore.Qt.Checked and self.ui.listWidget_2.count() == 0: b = "Bias"
		if self.ui.checkBox_2.checkState() == QtCore.Qt.Checked and self.ui.listWidget_3.count() == 0: d = "Dark"
		if self.ui.checkBox_3.checkState() == QtCore.Qt.Checked and self.ui.listWidget_4.count() == 0: f = "Flat"
		
		if b != "" or d != "" or f != "":
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("You left \n%s\n%s\n%s\nblank." %(b,d,f)))
		else:
			zeroFilePath, darkFilePath, flatFilePath = "", "", ""
			if self.ui.checkBox.checkState() == QtCore.Qt.Checked:
				self.ui.label.setText(QtGui.QApplication.translate("Form", "Creating Masster Bias.", None, QtGui.QApplication.UnicodeUTF8))
				gui.logging(self, "--- %s - zerocombine started for calibration." %(datetime.datetime.utcnow()))
				lst = gui.lisFromLW(self, self.ui.listWidget_2)
				gui.list2file(lst, "./tmp/zeroLST")
				com = self.ui.comboBox_4.currentText()
				rej = self.ui.comboBox_5.currentText()
				scl = self.ui.comboBox_8.currentText()
				cty = self.ui.lineEdit_10.text()
				if not function.zeroCombine("./tmp/zeroLST", "./tmp/zero.fits", com=com, rej=rej, cty=cty):
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>zerocombine</b> can not handle this job."))
					gui.logging(self, "--- %s - zerocombine failed." %(datetime.datetime.utcnow()))
				else:
					gui.logging(self, "--- %s - zerocombine succeed." %(datetime.datetime.utcnow()))
					zeroFilePath = "./tmp/zero.fits"
					
			if self.ui.checkBox_2.checkState() == QtCore.Qt.Checked:
				self.ui.label.setText(QtGui.QApplication.translate("Form", "Creating Masster Dark.", None, QtGui.QApplication.UnicodeUTF8))
				gui.logging(self, "--- %s - darkcombine started for calibration." %(datetime.datetime.utcnow()))
				lst = gui.lisFromLW(self, self.ui.listWidget_3)
				gui.list2file(lst, "./tmp/darkLST")
				com = self.ui.comboBox_4.currentText()
				rej = self.ui.comboBox_5.currentText()
				scl = self.ui.comboBox_8.currentText()
				cty = self.ui.lineEdit_10.text()
				if not function.darkCombine("./tmp/darkLST", "./tmp/dark.fits", com=com, rej=rej, cty=cty, scl=scl):
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>darkcombine</b> can not handle this job."))
					gui.logging(self, "--- %s - darkcombine failed." %(datetime.datetime.utcnow()))
				else:
					gui.logging(self, "--- %s - darkcombine succeed." %(datetime.datetime.utcnow()))
					darkFilePath = "./tmp/dark.fits"
				
			if self.ui.checkBox_3.checkState() == QtCore.Qt.Checked:
				self.ui.label.setText(QtGui.QApplication.translate("Form", "Creating Masster Flat.", None, QtGui.QApplication.UnicodeUTF8))
				gui.logging(self, "--- %s - flatcombine started for calibration." %(datetime.datetime.utcnow()))
				lst = gui.lisFromLW(self, self.ui.listWidget_4)
				gui.list2file(lst, "./tmp/flatLST")
				com = self.ui.comboBox_6.currentText()
				rej = self.ui.comboBox_7.currentText()
				sub = self.ui.comboBox_9.currentText()
				cty = self.ui.lineEdit_11.text()
				if not function.flatCombine("./tmp/flatLST", "./tmp", com=com, rej=rej, cty=cty, sub=sub):
					QtGui.QMessageBox.critical( self,  ("MYRaf Error") ("Due to an error <b>flatcombine</b> can not handle this job."))
					gui.logging(self, "--- %s - flatcombine failed." %(datetime.datetime.utcnow()))
				else:
					gui.logging(self, "--- %s - flatcombine succeed." %(datetime.datetime.utcnow()))
					flatFilePath = "./tmp/flat_*.fits"
			
			odir = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory to Save calibrated files')
			err=""
			it=0
			gui.logging(self, "--- %s - ccdproc started for calibration." %(datetime.datetime.utcnow()))
			for x in xrange(self.ui.listWidget.count()):
				it = it + 1
				ln = self.ui.listWidget.item(x)
				img = ln.text()
				self.ui.label.setText(QtGui.QApplication.translate("Form", "Calibration: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
				function.calibration(img, zeroFilePath, darkFilePath, flatFilePath, odir)
					
				self.ui.progressBar.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget.count())))))
			if err != "":
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("ccdproc failed with:\n%s." %(err)))
		gui.logging(self, "--- %s - ccdproc finished calibration." %(datetime.datetime.utcnow()))
		os.popen("rm -rf ./tmp/flatLS ./tmp/zeroLST ./tmp/darkLST %s %s %s" %(zeroFilePath, darkFilePath, flatFilePath))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please add some <b>Image</b> files."))
########################################################
#Create master files####################################
  def masterZero(self):
	gui.logging(self, "-- %s - zerocombine started." %(datetime.datetime.utcnow()))
	lst = gui.lisFromLW(self, self.ui.listWidget_2)
	gui.list2file(lst, "./tmp/zeroLST")
	ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save Master Bias file', 'zero.fits', 'Fit or Fits (*.fits *.fit)')
	com = self.ui.comboBox_2.currentText()
	rej = self.ui.comboBox_3.currentText()
	cty = self.ui.lineEdit_9.text()
	if not function.zeroCombine("./tmp/zeroLST", ofile, com=com, rej=rej, cty=cty):
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>zerocombine</b> can not handle this job."))
		gui.logging(self, "-- %s - zerocombine failed." %(datetime.datetime.utcnow()))
	else:
		gui.logging(self, "-- %s - zerocombine succeed." %(datetime.datetime.utcnow()))
		os.popen("rm -rf ./tmp/zeroLST")

  def masterDark(self):
	gui.logging(self, "-- %s - darkcombine started." %(datetime.datetime.utcnow()))
	lst = gui.lisFromLW(self, self.ui.listWidget_3)
	gui.list2file(lst, "./tmp/darkLST")
	ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save Master Dark file', 'dark.fits', 'Fit or Fits (*.fits *.fit)')
	com = self.ui.comboBox_4.currentText()
	rej = self.ui.comboBox_5.currentText()
	scl = self.ui.comboBox_8.currentText()
	cty = self.ui.lineEdit_10.text()
	if not function.darkCombine("./tmp/darkLST", foile, com=com, rej=rej, cty=cty, scl=scl):
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>darkcombine</b> can not handle this job."))
		gui.logging(self, "-- %s - darkcombine failed." %(datetime.datetime.utcnow()))
	else:
		gui.logging(self, "-- %s - darkcombine succeed." %(datetime.datetime.utcnow()))
		os.popen("rm -rf ./tmp/darkLST")
		
  def masterFlat(self):
	gui.logging(self, "-- %s - flatcombine started." %(datetime.datetime.utcnow()))
	lst = gui.lisFromLW(self, self.ui.listWidget_4)
	gui.list2file(lst, "./tmp/flatLST")
	odir = QtGui.QFileDialog.getExistingDirectory( self, 'Select Directory to Save Flat(s)')
	com = self.ui.comboBox_6.currentText()
	rej = self.ui.comboBox_7.currentText()
	sub = self.ui.comboBox_9.currentText()
	cty = self.ui.lineEdit_11.text()
	if not function.flatCombine("./tmp/flatLST", odir, com=com, rej=rej, cty=cty, sub=sub):
		QtGui.QMessageBox.critical( self,  ("MYRaf Error") ("Due to an error <b>flatcombine</b> can not handle this job."))
		gui.logging(self, "-- %s - flatcombine failed." %(datetime.datetime.utcnow()))
	else:
		gui.logging(self, "-- %s - flatcombine succeed." %(datetime.datetime.utcnow()))
		os.popen("rm -rf ./tmp/flatLST")
		
########################################################
#Load and set set########################################
  def applySettings(self):
	  f = open("set/setting", "r")
	  for l in f:
		  #print(l.replace("\n",""))
		  
		  if l.startswith("zCombine"):
			  zCombine = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_2.setCurrentIndex(zCombine)

		  if l.startswith("zReject"):
			  zReject = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_3.setCurrentIndex(zReject)
			  
		  if l.startswith("zccdtype"):
			  zccdtype = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_9.setText(QtGui.QApplication.translate("Form", str(zccdtype), None, QtGui.QApplication.UnicodeUTF8))

		  if l.startswith("dCombine"):
			  dCombine = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_4.setCurrentIndex(dCombine)

		  if l.startswith("dReject"):
			  dReject = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_5.setCurrentIndex(dReject)

		  if l.startswith("dScale"):
			  dScale = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_8.setCurrentIndex(dScale)

		  if l.startswith("dccdtype"):
			  dccdtype = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_10.setText(QtGui.QApplication.translate("Form", str(dccdtype), None, QtGui.QApplication.UnicodeUTF8))

		  if l.startswith("fCombine"):
			  fCombine = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_6.setCurrentIndex(dCombine)

		  if l.startswith("fReject"):
			  fReject = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_7.setCurrentIndex(fReject)

		  if l.startswith("fSubset"):
			  fSubset = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_9.setCurrentIndex(fSubset)

		  if l.startswith("fccdtype"):
			  fccdtype = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_11.setText(QtGui.QApplication.translate("Form", str(fccdtype), None, QtGui.QApplication.UnicodeUTF8))
			  
		  if l.startswith("cSubset"):
			  cSubset = int(l.split(":")[1].replace("\n",""))
			  self.ui.comboBox_10.setCurrentIndex(cSubset)
			  
		  if l.startswith("cccdtype"):
			  cccdtype = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_12.setText(QtGui.QApplication.translate("Form", str(cccdtype), None, QtGui.QApplication.UnicodeUTF8))
			  
		  if l.startswith("dpExpTime"):
			  dpExpTime = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_13.setText(QtGui.QApplication.translate("Form", str(dpExpTime), None, QtGui.QApplication.UnicodeUTF8))
			  
		  if l.startswith("dpFilter"):
			  dpFilter = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_14.setText(QtGui.QApplication.translate("Form", str(dpFilter), None, QtGui.QApplication.UnicodeUTF8))
		  
		  
		  if l.startswith("fspAnnulus"):
			  fspAnnulus = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial.setValue(fspAnnulus)
			  
		  if l.startswith("fspDannulus"):
			  fspDannulus = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial_2.setValue(fspDannulus)
			  
		  if l.startswith("fspCBox"):
			  fspCBox = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial_3.setValue(fspCBox)
			  
		  if l.startswith("ppApertur"):
			  ppApertur = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_15.setText(QtGui.QApplication.translate("Form", str(ppApertur), None, QtGui.QApplication.UnicodeUTF8))
			  
		  if l.startswith("ppZMag"):
			  ppZMag = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_16.setText(QtGui.QApplication.translate("Form", str(ppZMag), None, QtGui.QApplication.UnicodeUTF8))
	
			  
		  if l.startswith("photType"):
			  photType = l.split(":")[1].replace("\n","")
			  if photType == "iraf":
				  self.ui.radioButton.setChecked(True)
				  self.ui.scrollArea_11.setEnabled(True)
				  self.ui.scrollArea_12.setEnabled(False)
			  elif photType == "ense":
				  self.ui.radioButton_2.setChecked(True)
				  self.ui.scrollArea_11.setEnabled(False)
				  self.ui.scrollArea_12.setEnabled(True)

  def saveSettings(self):
	
	f = open("set/setting", "w")
	
	f.write("zCombine:%s\n" %self.ui.comboBox_2.currentIndex())
	f.write("zReject:%s\n" %self.ui.comboBox_3.currentIndex())
	f.write("zccdtype:%s\n" %self.ui.lineEdit_9.text())
	
	f.write("dCombine:%s\n" %self.ui.comboBox_4.currentIndex())
	f.write("dReject:%s\n" %self.ui.comboBox_5.currentIndex())
	f.write("dScale:%s\n" %self.ui.comboBox_8.currentIndex())
	f.write("dccdtype:%s\n" %self.ui.lineEdit_10.text())
	
	f.write("fCombine:%s\n" %self.ui.comboBox_6.currentIndex())
	f.write("fReject:%s\n" %self.ui.comboBox_7.currentIndex())
	f.write("fSubset:%s\n" %self.ui.comboBox_9.currentIndex())
	f.write("fccdtype:%s\n" %self.ui.lineEdit_11.text())
	
	f.write("cSubset:%s\n" %self.ui.comboBox_10.currentIndex())
	f.write("ccdtype:%s\n" %self.ui.lineEdit_12.text())
	
	if self.ui.radioButton.isChecked():
		f.write("photType:iraf\n" )
	else:
		f.write("photType:ense\n")

	f.write("dpExpTime:%s\n" %self.ui.lineEdit_13.text())
	f.write("dpFilter:%s\n" %self.ui.lineEdit_14.text())

	f.write("fspAnnulus:%s\n" %self.ui.dial.value())
	f.write("fspDannulus:%s\n" %self.ui.dial_2.value())
	f.write("fspCBox:%s\n" %self.ui.dial_3.value())
	
	f.write("ppApertur:%s\n" %self.ui.lineEdit_15.text())
	f.write("ppZMag:%s\n" %self.ui.lineEdit_16.text())
	
	f.close()
#########################################################
#Photometry Settings Unlock##############################
  def unlockIrafPhot(self):
	if self.ui.radioButton.isChecked():
		self.ui.scrollArea_11.setEnabled(True)
		self.ui.scrollArea_12.setEnabled(False)
	else:
		self.ui.scrollArea_11.setEnabled(False)
		self.ui.scrollArea_12.setEnabled(True)
		
  def unlockEnsfPhot(self):
	if self.ui.radioButton_2.isChecked():
		self.ui.scrollArea_11.setEnabled(False)
		self.ui.scrollArea_12.setEnabled(True)
	else:
		self.ui.scrollArea_11.setEnabled(True)
		self.ui.scrollArea_12.setEnabled(False)
#########################################################
#Unlock calibration tabs.################################
  def unlockBias(self):
	gui.unlocCali(self, self.ui.checkBox, 1)
  def unlockDark(self):
	gui.unlocCali(self, self.ui.checkBox_2, 2)
  def unlockFlat(self):
	gui.unlocCali(self, self.ui.checkBox_3, 3)
########################################################
#Add/Remove Files From Listes###########################
  def imgAdd(self):
	gui.add(self, self.ui.listWidget)
  def imgRm(self):
	gui.rm(self, self.ui.listWidget)
  def biasAdd(self):
	gui.add(self, self.ui.listWidget_2)
  def biasRm(self):
	gui.rm(self, self.ui.listWidget_2)
  def biasAdd(self):
	gui.add(self, self.ui.listWidget_2)
  def biasRm(self):
	gui.rm(self, self.ui.listWidget_2)
  def flatAdd(self):
	gui.add(self, self.ui.listWidget_4)
  def flatRm(self):
	gui.rm(self, self.ui.listWidget_4)
  def darkAdd(self):
	gui.add(self, self.ui.listWidget_3)
  def darkRm(self):
	gui.rm(self, self.ui.listWidget_3)
  def autAlignAdd(self):
	gui.add(self, self.ui.listWidget_5)
  def autAlignRm(self):
	gui.rm(self, self.ui.listWidget_5)
  def manAlignAdd(self):
	gui.add(self, self.ui.listWidget_6)
  def manAlignRm(self):
	gui.rm(self, self.ui.listWidget_6)
  def photAdd(self):
	gui.add(self, self.ui.listWidget_7)
  def photRm(self):
	gui.rm(self, self.ui.listWidget_7)
  def photCooRm(self):
	gui.rm(self, self.ui.listWidget_8)
  def heditAdd(self):
	gui.add(self, self.ui.listWidget_9)
  def heditRm(self):
	gui.rm(self, self.ui.listWidget_9)
########################################################
########################################################
  def display(self, FilePath, displayDevice):
	self.ui.local_image = QImage(FilePath)
	self.ui.local_scenePhot = QGraphicsScene()
	self.ui.pixMapItemPhot = QGraphicsPixmapItem(QPixmap(self.ui.local_image), None, self.ui.local_scenePhot)
	displayDevice.setScene( self.ui.local_scenePhot)
	if displayDevice == self.ui.graphicsView_2:
		self.ui.pixMapItemPhot.mousePressEvent = self.pixelManAlign
	elif displayDevice == self.ui.graphicsView_3:
		self.ui.pixMapItemPhot.mousePressEvent = self.pixelSelectPhot
		
########################################################
#Close##################################################
  def closeEvent(self, event):
	gui.logging(self, "- %s - MYRaf closed." %(datetime.datetime.utcnow()))
########################################################
app = QtGui.QApplication(sys.argv)
f = MyForm()
f.show()
app.exec_()
