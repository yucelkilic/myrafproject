# -*- coding: utf-8 -*-
"""
Created:--------------------------------------------------------------------------------------------
		By:
			Muhammed SHEMUNI		Developer
			Yücel KILIÇ				Developer
		at:
			Begin					04.12.2013
			Last update				07.05.2014
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
import sys , os, time, string, math, signal, datetime, ntpath, numpy
from matplotlib.patches import Circle

os.system("echo \"- " + str(datetime.datetime.utcnow()) + " - MYRaf started.\" >>log.my")

try:
	from PyQt4 import QtGui, QtCore
	from PyQt4.QtGui import *
	from PyQt4.QtCore import *
except:
	print("Can not load PyQT4")
	os.system("echo \"- " + str(datetime.datetime.utcnow()) + " -- Did you install PyQT4?\" >>$HOME/.MYRaf2/log.my")
	raise SystemExit

try:
	from myraf import Ui_Form
	import function, gui
except:
	print("Is MYRaf installed?")
	raise SystemExit

try:
    from fPlot import *
    from sexCat import *
except:
	print("Where is fPlot?")
	raise SystemExit

try:
    from pyraf import iraf
    from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom
    from astropy.stats import sigma_clip
    from numpy import mean
    import numpy as np
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
    
    self.ui.pushButton_18.clicked.connect(self.displayCoords)
    
    self.ui.pushButton_34.clicked.connect(self.saveSettings)
    
    self.ui.pushButton_3.clicked.connect(lambda: gui.add(self, self.ui.listWidget))
    self.ui.pushButton_4.clicked.connect(lambda: gui.rm(self, self.ui.listWidget))
    self.ui.pushButton_5.clicked.connect(lambda: gui.add(self, self.ui.listWidget_2))
    self.ui.pushButton_6.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_2))
    self.ui.pushButton_10.clicked.connect(lambda: gui.add(self, self.ui.listWidget_3))
    self.ui.pushButton_8.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_3))
    self.ui.pushButton_13.clicked.connect(lambda: gui.add(self, self.ui.listWidget_4))
    self.ui.pushButton_11.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_4))
    self.ui.pushButton_15.clicked.connect(lambda: gui.add(self, self.ui.listWidget_5))
    self.ui.pushButton_16.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_5))
    self.ui.pushButton_22.clicked.connect(lambda: gui.add(self, self.ui.listWidget_6))
    self.ui.pushButton_21.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_6))
    self.ui.pushButton_33.clicked.connect(lambda: gui.add(self, self.ui.listWidget_7))
    self.ui.pushButton_32.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_7))
    self.ui.pushButton_36.clicked.connect(lambda: gui.add(self, self.ui.listWidget_9))
    self.ui.pushButton_37.clicked.connect(lambda: gui.rm(self, self.ui.listWidget_9))


    self.ui.pushButton_3.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_4.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_5.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_6.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_10.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_8.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_13.clicked.connect(self.displayCalibLabel)
    self.ui.pushButton_11.clicked.connect(self.displayCalibLabel)


    self.ui.listWidget_5.clicked.connect(self.displayAutAlign)
    self.ui.pushButton_14.clicked.connect(self.goAutAlign)
    
    self.ui.listWidget_6.clicked.connect(self.displayManAlign)
    self.ui.pushButton_27.clicked.connect(self.goManAlign)
    
    self.ui.listWidget_7.clicked.connect(self.displayPhot)
    self.ui.pushButton_45.clicked.connect(self.coorDel)
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
    self.ui.pushButton_2.clicked.connect(self.choosePointCol)
    
    self.ui.pushButton.clicked.connect(self.calib)
    
    self.ui.pushButton_44.clicked.connect(self.readStars)
    self.ui.pushButton_46.clicked.connect(self.plotChart)
    
    self.ui.pushButton_17.clicked.connect(self.findStars)
    
    self.ui.checkBox_4.clicked.connect(self.epochUnlock)
    
    self.ui.pushButton_19.clicked.connect(self.chartClear)
  
    self.ui.pushButton_34.clicked.connect(self.saveSettings)
    self.applySettings()
    
    self.ui.horizontalSlider.sliderReleased.connect(lambda:self.reDraw(self.ui.listWidget_5.currentItem(), self.ui.dispAuto.canvas, "horizontalSlider"))
    self.ui.horizontalSlider_2.sliderReleased.connect(lambda:self.reDraw(self.ui.listWidget_6.currentItem(), self.ui.dispManual.canvas, "horizontalSlider_2"))
    self.ui.horizontalSlider_3.sliderReleased.connect(lambda:self.reDraw(self.ui.listWidget_7.currentItem(), self.ui.dispPhoto.canvas, "horizontalSlider_3"))
    self.ui.dispManual.canvas.fig.canvas.mpl_connect('button_press_event',self.mouseClick)
    self.ui.dispPhoto.canvas.fig.canvas.mpl_connect('button_press_event',self.mouseClick)
    self.ui.disp_chart.canvas.fig.canvas.mpl_connect('pick_event', self.onpick)

# Chart point picker
  def onpick(self, event):
  	thisline = event.artist
	xdata = thisline.get_xdata()
	ydata = thisline.get_ydata()
	ind = event.ind
	self.ui.label_9.setText("x=" + str(format(xdata[ind][0], '.3f')) + " y=" + str(format(ydata[ind][0], '.3f')))

  #Chart area clear
  def chartClear(self):
  	data = []
  	self.ui.disp_chart.canvas.ax.hold(False)
	self.ui.disp_chart.canvas.ax.plot(data) 
  	self.ui.disp_chart.canvas.draw()
  	 
#Choose Point Color of Chart###################################
  def choosePointCol(self):
      col = QtGui.QColorDialog.getColor()
      if col:
	      if col.isValid():
	          pcol = self.ui.label_55.setText(QtGui.QApplication.translate("Form", "%s" %(str(col.name())), None, QtGui.QApplication.UnicodeUTF8))
	          return pcol

#other###################################
  def displayCalibLabel(self):
  	imC = self.ui.listWidget.count()
  	biC = self.ui.listWidget_2.count()
  	daC = self.ui.listWidget_3.count()
  	flC = self.ui.listWidget_4.count()
  	self.ui.label_3.setText(QtGui.QApplication.translate("Form", "<b>%s</b> image(s) will calibrate using <b>%s</b> Bias(es), <b>%s</b> Dark(s) and <b>%s</b> Flat(s)." %(imC, biC, daC, flC), None, QtGui.QApplication.UnicodeUTF8))
  	self.ui.label_4.setText(QtGui.QApplication.translate("Form", "<b>%s</b> image(s) will calibrate using <b>%s</b> Bias(es), <b>%s</b> Dark(s) and <b>%s</b> Flat(s)." %(imC, biC, daC, flC), None, QtGui.QApplication.UnicodeUTF8))
  	self.ui.label_5.setText(QtGui.QApplication.translate("Form", "<b>%s</b> image(s) will calibrate using <b>%s</b> Bias(es), <b>%s</b> Dark(s) and <b>%s</b> Flat(s)." %(imC, biC, daC, flC), None, QtGui.QApplication.UnicodeUTF8))
  	self.ui.label_6.setText(QtGui.QApplication.translate("Form", "<b>%s</b> image(s) will calibrate using <b>%s</b> Bias(es), <b>%s</b> Dark(s) and <b>%s</b> Flat(s)." %(imC, biC, daC, flC), None, QtGui.QApplication.UnicodeUTF8))
  	

#Read Stars ID to Graph Tab###################################
  def readStars(self):
  	filename = QtGui.QFileDialog.getOpenFileName(self ,"MYRaf Result File...","",("My Files (*.my *.myf)"))
  	if filename:
  		try:   	
			self.ui.label_43.setText(QtGui.QApplication.translate("Form", "File location: %s" %(filename), None, QtGui.QApplication.UnicodeUTF8))
			# counting stars in result file
			with open(filename) as resultFile:
			    head=[resultFile.next() for x in xrange(3)]
			capStar, starCount = head[0].split(" = ")
			capStar, apertures = head[1].split(" = ")
			#clearing comboxBoxs
			self.ui.comboBox_11.clear()
			self.ui.comboBox_12.clear()
			self.ui.comboBox_13.clear()
			for i in range(1, int(starCount.replace("\n",""))+1):
			    self.ui.comboBox_11.addItem(str(i))
			    self.ui.comboBox_12.addItem(str(i))
			    self.ui.comboBox_13.addItem(str(i))
			self.ui.comboBox_14.clear()
			#getting apertures
			apertures = apertures.replace("\n","")
			for aperture in apertures.split(","):
			    self.ui.comboBox_14.addItem(aperture.replace("\n", ""))
		except:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Error reading MYRaf <b>result file</b>!"))
			gui.logging(self, "--- %s - Error reading MYRaf result file!" %(datetime.datetime.utcnow()))			

#Plot Chart#############################################
  def plotChart(self):
  	# reading form
  	if self.ui.label_43.text():
  		#Checking result file
  		if self.ui.lineEdit_19.text() and self.ui.lineEdit_20.text() and self.ui.lineEdit_21.text() and self.ui.label_55.text() and self.ui.comboBox_11.currentText() and self.ui.comboBox_12.currentText() and self.ui.comboBox_13.currentText() and self.ui.comboBox_14.currentText():
			varStarID = self.ui.comboBox_11.currentText()
			checkStarID = self.ui.comboBox_12.currentText()
			refStarID = self.ui.comboBox_13.currentText()
			apertureIndex = self.ui.comboBox_14.currentIndex() + 3
			legendName = self.ui.lineEdit_21.text().replace(" ",  "")
			
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
			        varMag1.append(np.nan)
			# Check
			for checkData in checkDatas:
			    cData = checkData.split()
			    try:
			        checkMag1.append(float(cData[2]))
			    except:
			        checkMag1.append(np.nan)
			# Ref
			for refData in refDatas:
			    rData = refData.split()
			    try:
			        refMag1.append(float(rData[2]))
			    except:
			        refMag1.append(np.nan)
			 
			# Masking INDEF content
			varPhase = np.array(varPhase1)
			varMag2 = np.array(varMag1)
			varMag = np.ma.masked_array(varMag2, np.isnan(varMag2))
			
			checkMag2 = np.array(checkMag1)
			checkMag = np.ma.masked_array(checkMag2, np.isnan(checkMag2))
			
			refMag2 = np.array(refMag1)
			refMag = np.ma.masked_array(refMag2, np.isnan(refMag2))
			# Rejecting scattered points from array
			diffMag1 = varMag - checkMag
			diffMag = sigma_clip(diffMag1, 3, None, mean, copy=False)
			
			residuMag1 = checkMag - refMag
			residuMag = sigma_clip(residuMag1, 3, None, mean, copy=False)
			
			#Plot
			pointColor = self.ui.label_55.text()
			sp = str(self.ui.comboBox_15.currentText()).split(" ")[0]
			gui.PlotFunc(self,  self.ui.disp_chart.canvas, varPhase, (diffMag*(-1)),  residuMag, pointColor,  legendName, sp)
		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please <b>fill/select</b> the required informations!"))
			gui.logging(self, "--- %s - Please fill/select the required informations!" %(datetime.datetime.utcnow()))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select MYRaf <b>result file</b>!"))
		gui.logging(self, "--- %s - Please select MYRaf result file!" %(datetime.datetime.utcnow()))
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
			self.ui.lineEdit_3.setText(QtGui.QApplication.translate("Form", str(ln).split(" = ")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("name"):
			self.ui.lineEdit_4.setText(QtGui.QApplication.translate("Form", str(ln).split(" = ")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("longitude"):
			self.ui.lineEdit_5.setText(QtGui.QApplication.translate("Form", str(ln).split(" = ")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("latitude"):
			self.ui.lineEdit_6.setText(QtGui.QApplication.translate("Form", str(ln).split(" = ")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("altitude"):
			self.ui.lineEdit_7.setText(QtGui.QApplication.translate("Form", str(ln).split(" = ")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))

		if ln.replace("	","").startswith("timezone"):
			self.ui.lineEdit_8.setText(QtGui.QApplication.translate("Form", str(ln).split(" = ")[1].replace("\"",""), None, QtGui.QApplication.UnicodeUTF8))
			
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
	os.popen("cat obsdat/* > /iraf/iraf/noao/lib/obsdb.dat")

  def addObservatory(self):
	fl = self.ui.listWidget_12.currentItem()
	
	observatory = self.ui.lineEdit_3.text()
	name = self.ui.lineEdit_4.text()
	longitude = self.ui.lineEdit_5.text()
	latitude = self.ui.lineEdit_6.text()
	altitude = self.ui.lineEdit_7.text()
	timeZone = self.ui.lineEdit_8.text()
	other = str(self.ui.plainTextEdit.toPlainText())
	
	f = open("./obsdat/%s" %(observatory), "w")
	f.write("#%s\n" %(other.replace("\n"," ")))
	f.write("observatory = \"%s\"\n" %(observatory))
	f.write("\tname = \"%s\"\n" %(name))
	f.write("\tlongitude = %s\n" %(longitude))
	f.write("\tlatitude = %s\n" %(latitude))
	f.write("\taltitude = %s\n" %(altitude))
	f.write("\ttimezone = %s\n" %(timeZone))
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
	
	os.popen("cat obsdat/* > /iraf/iraf/noao/lib/obsdb.dat")
		
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
		
  def epochUnlock(self):
	if self.ui.checkBox_4.checkState() == QtCore.Qt.Checked:
		self.ui.lineEdit_25.setEnabled(False)
	else:
		self.ui.lineEdit_25.setEnabled(True)

  def goHeaderAdd(self):
	if self.ui.listWidget_9.count() != 0:
		f = self.ui.lineEdit.text()
		if str(f).strip():
			headErr = ""
			it = 0
			for x in xrange(self.ui.listWidget_9.count()):
				it = it + 1
				img = self.ui.listWidget_9.item(x)
				img = str(img.text())
				field = self.ui.lineEdit.text()
				field = str(field).strip()
					
				if self.ui.checkBox_5.checkState() != QtCore.Qt.Checked:
					val = self.ui.lineEdit_2.text()
				else:
					h = self.ui.comboBox.currentText()
					selectedField = h.split(" = ")[0]
					val = str("'(@\"%s\")'" %selectedField)
				
				self.ui.progressBar_4.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_9.count())))))
				self.ui.label_41.setText(QtGui.QApplication.translate("Form", "Header: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
					
				if not function.headerWrite(img, field, val):
					headErr = "%s\n%s" %(headErr, ntpath.basename(str(img)))
						
			if self.ui.listWidget_9.currentIndex():
				self.getHeader()
			if headErr != "" :
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>hedit</b> can not handle this job for images below\n%s" %(headErr)))
		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please fill the \"Field\" section!"))			
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select some <b>images</b>."))
	
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
			self.ui.label_41.setText(QtGui.QApplication.translate("Form", "Header: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))

		if heErr != "":
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>hedit</b> can not handle this job for images below\n%s" %(heErr)))
			
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select some <b>images</b>."))
########################################################
#Pohtometry#############################################
  def displayPhot(self):

	img = self.ui.listWidget_7.currentItem()
	img = img.text()
	plotF = FitsPlot(str(img), self.ui.dispPhoto.canvas, self.ui)
	if plotF.drawim("horizontalSlider_3"):
		self.ui.dispPhoto.canvas.draw()
		#self.displayCoords()
		gui.logging(self, "-- %s - matplotlib succeed." %(datetime.datetime.utcnow()))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>matplotlib</b> can not handle this job."))
		gui.logging(self, "--- %s - imagemagick failed." %(datetime.datetime.utcnow()))

  def coorDel(self):
	gui.rm(self, self.ui.listWidget_8)
	self.displayPhot()
		
  def displayCoords(self):
	if self.ui.listWidget_8.count() != 0:
		self.displayPhot()
		lNumber = 0	
		for x in self.ui.listWidget_8.selectedItems():
			lNumber = lNumber +1
			coo = str(x.text())
			x, y = coo.split("-")
			mean = 0
			ap = str(self.ui.lineEdit_15.text())
			for ape in ap.split(","):
				mean = mean + int(ape)
			Aperture = mean/len(ap.split(","))
			Aperture = mean/len(ap.split(","))
			circAperture = Circle((Aperture, Aperture), Aperture, edgecolor="#00FF00", facecolor="none") 				
			circAnnulus = Circle((Aperture + self.ui.dial.value(), Aperture + self.ui.dial.value()), Aperture + self.ui.dial.value(), edgecolor="#00FFFF", facecolor="none")
			circDannulus = Circle((Aperture + self.ui.dial.value() + self.ui.dial_2.value(), Aperture + self.ui.dial.value() + self.ui.dial_2.value()), Aperture + self.ui.dial.value() + self.ui.dial_2.value(), edgecolor="red", facecolor="none")
			self.ui.dispPhoto.canvas.ax.add_artist(circAnnulus)
			self.ui.dispPhoto.canvas.ax.add_artist(circDannulus)
			self.ui.dispPhoto.canvas.ax.add_artist(circAperture)
			circAperture.center = x, y
			circAnnulus.center = x, y
			circDannulus.center = x, y
			self.ui.dispPhoto.canvas.ax.annotate(lNumber, xy = (x, y), xytext=(int(Aperture/3),int(Aperture/3)), textcoords='offset points', color = "blue", fontsize = 10)
			self.ui.dispPhoto.canvas.draw()
			
  def goPhot(self):
	if self.ui.listWidget_7.count() != 0:
		if self.ui.listWidget_8.count() != 0:
			gui.logging(self, "-- %s - phot started." %(datetime.datetime.utcnow()))
			f = open("./tmp/pc", "w")
			for x in xrange(self.ui.listWidget_8.count()):
				coo = self.ui.listWidget_8.item(x)
				coo = str(coo.text())
				coo = coo.replace("-", " ")
				f.write("%s\n" %(coo))
			f.close()
			
			exp = self.ui.lineEdit_13.text()
			fil = self.ui.lineEdit_14.text()
			ann = self.ui.dial.value()
			dan = self.ui.dial_2.value()
			cbo = self.ui.dial_3.value()
			ape = self.ui.lineEdit_15.text()
			zma = self.ui.lineEdit_16.text()
			obs = self.ui.lineEdit_18.text()
			print(obs)
			obt = self.ui.lineEdit_17.text()
			obd = self.ui.lineEdit_24.text()
			ra = self.ui.lineEdit_22.text()
			dec = self.ui.lineEdit_23.text()
			epo = self.ui.lineEdit_25.text()
			
			apert = self.ui.lineEdit_15.text()
			staCount = self.ui.listWidget_8.count()
			
			ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save MYRaf file', 'res.my', 'my (*.my)')
			if ofile != "":
				if os.path.exists(ofile):
					os.popen("rm %s" %(ofile))
				f = open(ofile, "w")
				f.write("# STAR = %s\n" %(str(staCount)))
				f.write("# APERTURE = %s\n" %(str(apert)))
				f.write("# DO NOT EDIT PARAMETRES ABOVE. You can add comments starts with '#' below ths line.\n")
				f.write("# If you don't have any experience before, DO NOT EDIT THIS FILE!\n")
				f.write("# id\tTIME\tMAG%s\tMERR%s\tAIRMASS\n"%(self.ui.lineEdit_15.text().replace(",","\tMAG"), self.ui.lineEdit_15.text().replace(",","\tMERR")))
				f.close()
				it = 0
				err = ""
				errJD = ""
				errSid = ""
				errAir = ""
				errTM = ""
				errOB = ""
				errORA = ""
				errODEC = ""
				errdt = ""
				errOBSERVAT = ""
				errEpoch = ""
				for x in xrange(self.ui.listWidget_7.count()):
					it = it + 1
					img = self.ui.listWidget_7.item(x)
					img = str(img.text())
					tm = function.headerRead(img, obt)
					ob = function.headerRead(img, obs)
					dt = function.headerRead(img, obd)
					ora = function.headerRead(img, ra)
					odec = function.headerRead(img, dec)
					observatory = function.headerRead(img, obs)
					if self.ui.checkBox_4.checkState() == QtCore.Qt.Checked:
						epo = function.epoch(img, obd, obt)
					function.headerWrite(img, "epoch", epo)
					if errEpoch != "":
						if os.path.isfile("%s/obsdat/%s" %(self.HOME, ob)):
							if dt !="":
								if ob !="":
									if tm != "":
										if ora != "":
											if odec != "":
												if function.JD(img, str(obs), str(obd), str(obt), str(ra), str(dec), str("epoch"), str(exp)):
													if function.sideReal(self, img, ob, obd, obt):
														if function.airmass(img, observatory, ra, dec, "epoch", "st", obt, obd, exp):
															if function.phot(self, img, "%s/tmp/analyzed/" %(self.HOME), "%s/tmp/pc" %(self.HOME), expTime = exp, Filter = fil, centerBOX = cbo, annulus = ann, dannulus = dan, apertur = ape, zmag = zma):
																if function.txDump("%s/tmp/analyzed/%s.mag.1"  %(self.HOME, ntpath.basename(img)), "%s/tmp/analyzed/%s"  %(self.HOME, ntpath.basename(img))):
																	#os.popen("echo '#ap=%s'"%(str()))
																	os.popen("rm %s/tmp/analyzed/%s.mag.1" %(self.HOME, ntpath.basename(img)))
																	os.popen("cat %s/tmp/analyzed/%s >> %s"  %(self.HOME, ntpath.basename(img), ofile))
																	os.popen("rm %s/tmp/analyzed/%s" %(self.HOME, ntpath.basename(img)))
															else:
																err = "%s, %s" %(err, ntpath.basename(img))
														else:
															errAir = "%s, %s" %(errAir, ntpath.basename(img))
													else:
														errSid = "%s, %s" %(errSid, ntpath.basename(img))
												else:
													errJD = "%s, %s" %(errJD, ntpath.basename(img))
											else:
												errODEC = "%s, %s" %(errODEC, ntpath.basename(img))
										else:
											errORA = "%s, %s" %(errORA, ntpath.basename(img))
									else:
										errTM = "%s, %s" %(errTM, ntpath.basename(img))
								else:
									errOB = "%s, %s" %(errOB, ntpath.basename(img))
							else:
								errdt = "%s, %s" %(errdt, ntpath.basename(img))
						else:
							errOBSERVAT = "%s, %s" %(errOBSERVAT, ntpath.basename(img))
					
					self.ui.progressBar_5.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_7.count())))))
					self.ui.label_14.setText(QtGui.QApplication.translate("Form", "Photometry: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
				if errOBSERVAT != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Can't find Observatory in <b>obsdb</b> for images below:\n%s\nYou can add your observatory using editor." %(errOBSERVAT)))
					
				if errTM != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>%s</b> header on images below:\n%s" %(obt, errTM)))
				if errEpoch != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Time format is not correct for images below:\n%s\nYou can change value from header or choose manual epoch from setting tab." %(errEpoch)))
				if errOB != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>%s</b> header on images below:\n%s" %(obs, errOB)))
				if errORA != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>%s</b> header on images below:\n%s" %(ra, errORA)))
				if errODEC != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>%s</b> header on images below:\n%s" %(dec, errODEC)))
				if errdt != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>%s</b> header on images below:\n%s" %(obd, errdt)))
				if errJD != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>setjd</b> can not handle images below\n%s." %(errJD)))
				if errSid != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error can not calculate <b>sidereal</b> time for images below\n%s." %(errSid)))
				if errAir != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>setairmass</b> can not handle images below\n%s." %(errAir)))
				if err != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>phot</b> can not handle images below\n%s." %(err)))
				
		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select some <b>sources</b>."))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>image</b> for Photometry."))
		
########################################################
#Manual Align############################################
  def displayManAlign(self):
	
	img = self.ui.lisstWidget_6.currentItem()
	img = img.text()
	plotF = FitsPlot(str(img), self.ui.dispManual.canvas, self.ui)
	c = function.headerRead(img, "MYRAFCOR")
	print c
	if plotF.drawim("horizontalSlider_2"):
		gui.logging(self, "-- %s - matplotlib succeed." %(datetime.datetime.utcnow()))
		coors = function.headerRead(img, "MYRafCor")
		self.ui.label_11.setText(QtGui.QApplication.translate("Form", "%s" %(coors), None, QtGui.QApplication.UnicodeUTF8))
		if c!="":
			print "Coor is there"
			x, y = c.split("-")
			print x
			print y
			mean = 0
			ap = str(self.ui.lineEdit_15.text())
			for ape in ap.split(","):
				mean = mean + int(ape)
			Aperture = mean/len(ap.split(","))
			circAperture = Circle((Aperture, Aperture), Aperture, edgecolor="#00FF00", facecolor="none")
			circAnnulus = Circle((Aperture + self.ui.dial.value(), Aperture + self.ui.dial.value()), Aperture + self.ui.dial.value(), edgecolor="#00FFFF", facecolor="none")
			circDannulus = Circle((Aperture + self.ui.dial.value() + self.ui.dial_2.value(), Aperture + self.ui.dial.value() + self.ui.dial_2.value()), Aperture + self.ui.dial.value() + self.ui.dial_2.value(), edgecolor="red", facecolor="none")
			self.ui.dispManual.canvas.ax.add_artist(circAnnulus)
			self.ui.dispManual.canvas.ax.add_artist(circDannulus)
			self.ui.dispManual.canvas.ax.add_artist(circAperture)
			circAperture.center = x, y
			circAnnulus.center = x, y
			circDannulus.center = x, y
			self.ui.label_11.setText(str(format(float(x), '.2f')) + " - " + str(format(float(y), '.2f')))
			self.ui.dispManual.canvas.draw()
		
  def goManAlign(self):
	if self.ui.listWidget_6.count() != 0:
		if self.ui.listWidget_6.currentItem() != None:
			img = self.ui.listWidget_6.currentItem()
			img = img.text()
			coorRef = function.headerRead(img, "MYRafCor").split("-")
			if str(coorRef) != "['']":
				xref = coorRef[0]
				yref = coorRef[1]
				odir = QtGui.QFileDialog.getExistingDirectory( self, 'Select Directory to Save Aligned File(s)')
				if os.path.exists(odir):
					it = 0
					err = ""
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
							print x, y
							if not function.manAlign(img, x, y, ofile):
								err = "%s, %s" %(err, ntpath.basename(str(img)))
								gui.logging(self, "--- %s - imshift failed." %(datetime.datetime.utcnow()))
						self.ui.label_10.setText(QtGui.QApplication.translate("Form", "Aligning:%s" %(ntpath.basename(img)), None, QtGui.QApplication.UnicodeUTF8))
						self.ui.progressBar_3.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_6.count())))))
				
					if err!="":
						QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>imshift</b> can not align images below\n%s." %(err)))
			
			else:
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select coordinates for reference image."))
		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select a reference image first."))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please add some <b>Image</b> files."))
	
########################################################
  def mouseClick(self, event):
  	if self.ui.tabWidget.currentIndex() == 1:
	  	if self.ui.tabWidget_3.currentIndex() == 1:
		  	if self.ui.checkBox_6.isChecked():
		   		if event.ydata != None and event.xdata != None:
		  			rows = self.ui.listWidget_6.count()
		  			row = self.ui.listWidget_6.currentRow()
					img = self.ui.listWidget_6.currentItem()
					img = img.text()
					height = function.headerRead(img, "i_naxis2")
					x = event.xdata
					y = event.ydata
					function.headerWrite(img, "MYRafCor", "%s-%s" %(str(x), str(y)))
		  			if row < rows-1:
						self.ui.listWidget_6.setCurrentRow(row+1)
					else:
						self.ui.listWidget_6.setCurrentRow(0)
					self.displayManAlign()
  	elif self.ui.tabWidget.currentIndex() == 2:
  		if self.ui.checkBox_7.isChecked():		
	   		print event.ydata
	   		if event.ydata != None and event.xdata != None:
  				self.ui.listWidget_8.addItem(str(format(event.xdata, '.4f')) + " - " + str(format(event.ydata, '.4f')))
  				self.displayCoords()

#Auto Align#############################################
  def findStars(self):
  	if self.ui.tabWidget.currentIndex() == 2:
  		if self.ui.listWidget_7.currentItem():
			if self.ui.dial_5.value() > self.ui.dial_6.value():
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("<b>Min FWHM</b> can not be bigger than <b>Max FWHM</b>"))
			else:
				img = self.ui.listWidget_7.currentItem()
				img = str(img.text())
				
				minFWHM = self.ui.dial_5.value()
				maxFWHM = self.ui.dial_6.value()
				FluxRadi = self.ui.dial_4.value()
				maxStar = self.ui.dial_7.value()
				
				
				sex = runSex(img)
				stars = sex.run(FluxRadi, minFWHM, maxFWHM, maxStar)
				
				c=self.ui.listWidget_8.count()
				for i in xrange(c):
					self.ui.listWidget_8.takeItem(0)
				
				it = -1
				for x in stars:
					it = it+1
					coo = "%s-%s" %(x[0],x[1])
					item = QtGui.QListWidgetItem()
					self.ui.listWidget_8.addItem(item)
					item = self.ui.listWidget_8.item(it)
					item.setText(QtGui.QApplication.translate("Form", coo, None, QtGui.QApplication.UnicodeUTF8))

  def reDraw(self, listObject, dispObject, horizontalSlider):
  	if listObject:
		img = listObject.text()
		plotF = FitsPlot(str(img), dispObject, self.ui)
		plotF.drawim(horizontalSlider)
		#tab denetle....
		#self.displayCoords()

  def displayAutAlign(self):
	gui.logging(self, "-- %s - image conversion started." %(datetime.datetime.utcnow()))
	img = self.ui.listWidget_5.currentItem()
	img = img.text()
	plotF = FitsPlot(str(img), self.ui.dispAuto.canvas, self.ui)
	if plotF.drawim("horizontalSlider"):
		self.ui.dispAuto.canvas.draw()
		gui.logging(self, "--- %s - matplotlib succeed." %(datetime.datetime.utcnow()))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>matplotlib</b> can not handle this job."))
		gui.logging(self, "--- %s - matplotlib failed." %(datetime.datetime.utcnow()))

  def goAutAlign(self):
	if self.ui.listWidget_5.count() != 0:
		if self.ui.listWidget_5.currentItem() != None:
			gui.logging(self, "-- %s - AutoAlign started." %(datetime.datetime.utcnow()))
			ref = self.ui.listWidget_5.currentItem()
			ref = str(ref.text())
			it = 0
			odir = QtGui.QFileDialog.getExistingDirectory( self, 'Select Directory to Save Aligned File(s)')
			if os.path.exists(odir):
				aliErr = ""
				for x in xrange(self.ui.listWidget_5.count()):
					it = it + 1
					img = self.ui.listWidget_5.item(x)
					img = str(img.text())
					self.ui.label_7.setText(QtGui.QApplication.translate("Form", "Aligning: %s" %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
					if not function.autoAlign(img, ref, odir):
						aliErr = "%s, %s" %(aliErr, ntpath.basename(str(img)))
						gui.logging(self, "--- %s - alipy failed." %(datetime.datetime.utcnow()))
					self.ui.progressBar_2.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget_5.count())))))
					os.popen("rm -rf ./alipy_cats/ ./alipy_out/")
				gui.logging(self, "-- %s - AutoAlign finished aligning." %(datetime.datetime.utcnow()))
				if aliErr != "":
					QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>alipy</b> can not align images below\n%s") %(aliErr))

		else:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please select a <b>reference image</b> first."))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Please add some <b>Image</b> files."))
########################################################
#Calibration############################################
  def calib(self):
	if self.ui.listWidget.count() != 0:
		if self.ui.checkBox.checkState() != QtCore.Qt.Checked and self.ui.checkBox_2.checkState() != QtCore.Qt.Checked and self.ui.checkBox_3.checkState() != QtCore.Qt.Checked:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Nothing to do!"))
		else:
			gui.logging(self, "-- %s - Calibration started." %(datetime.datetime.utcnow()))
			go = True
			
			os.popen("rm -rf ./tmp/dark.fits ./tmp/dark.fits ./tmp/flat_*.fits")
				
			b, d, f="","",""
			if self.ui.checkBox.checkState() == QtCore.Qt.Checked and self.ui.listWidget_2.count() == 0: b = "Bias\n"
			if self.ui.checkBox_2.checkState() == QtCore.Qt.Checked and self.ui.listWidget_3.count() == 0: d = "Dark\n"
			if self.ui.checkBox_3.checkState() == QtCore.Qt.Checked and self.ui.listWidget_4.count() == 0: f = "Flat\n"
			
			if b != "" or d != "" or f != "":
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Add file(s) to\n%s%s%s" %(b,d,f)))
			else:
				print "basla"
				zeroFilePath, darkFilePath, flatFilePath = "", "", ""
				
				if self.ui.checkBox.checkState() == QtCore.Qt.Checked:
					self.ui.label.setText(QtGui.QApplication.translate("Form", "Creating Masster Bias.", None, QtGui.QApplication.UnicodeUTF8))
					gui.logging(self, "--- %s - zerocombine started for calibration." %(datetime.datetime.utcnow()))
					lst = gui.lisFromLW(self, self.ui.listWidget_2)
					gui.list2file(lst, "./tmp/zeroLST")
					comb = self.ui.comboBox_4.currentText()
					rejb = self.ui.comboBox_5.currentText()
					ctyb = self.ui.lineEdit_10.text()
					if not function.zeroCombine("./tmp/zeroLST", "./tmp/zero.fits", com=comb, rej=rejb, cty=ctyb):
						QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>zerocombine</b> can not handle this job."))
						gui.logging(self, "--- %s - zerocombine failed." %(datetime.datetime.utcnow()))
					else:
						gui.logging(self, "--- %s - zerocombine succeed." %(datetime.datetime.utcnow()))
						zeroFilePath = "./tmp/zero.fits"
					os.popen("rm -rf ./tmp/zeroLST")
				
				if self.ui.checkBox_2.checkState() == QtCore.Qt.Checked:
					self.ui.label.setText(QtGui.QApplication.translate("Form", "Creating Masster Dark.", None, QtGui.QApplication.UnicodeUTF8))
					gui.logging(self, "--- %s - darkcombine started for calibration." %(datetime.datetime.utcnow()))
					lst = gui.lisFromLW(self, self.ui.listWidget_3)
					gui.list2file(lst, "./tmp/darkLST")
					comd = self.ui.comboBox_4.currentText()
					rejd = self.ui.comboBox_5.currentText()
					scld = self.ui.comboBox_8.currentText()
					ctyd = self.ui.lineEdit_10.text()
					if not function.darkCombine("./tmp/darkLST", "./tmp/dark.fits", com=comd, rej=rejd, cty=ctyd, scl=scld):
						QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>darkcombine</b> can not handle this job."))
						gui.logging(self, "--- %s - darkcombine failed." %(datetime.datetime.utcnow()))
					else:
						gui.logging(self, "--- %s - darkcombine succeed." %(datetime.datetime.utcnow()))
						darkFilePath = "./tmp/dark.fits"
					os.popen("rm -rf ./tmp/darkLST")
			
				if self.ui.checkBox_3.checkState() == QtCore.Qt.Checked:
					self.ui.label.setText(QtGui.QApplication.translate("Form", "Creating Masster Flat.", None, QtGui.QApplication.UnicodeUTF8))
					gui.logging(self, "--- %s - flatcombine started for calibration." %(datetime.datetime.utcnow()))
					lst = gui.lisFromLW(self, self.ui.listWidget_4)
					gui.list2file(lst, "./tmp/flatLST")
					comf = self.ui.comboBox_6.currentText()
					rejf = self.ui.comboBox_7.currentText()
					subf = self.ui.comboBox_10.currentText()
					ctyf = self.ui.lineEdit_11.text()
					
					f = open("./tmp/flatLST", "r")
					it = 0
					sname = self.ui.lineEdit_14.text()
						
					for i in f:
						fn = i.replace("\n","")
						if function.headerRead(fn,sname) == "":
							it = it + 1
					f.close()
					
					if subf == "yes" and it != 0:
						QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Subset classification is enabled but one or more images have no <b>%s</b> field in header.\nAdd <b>%s</b> field to headers." %(sname, sname)))
						go = False
					else:
						function.headerWrite("@./tmp/flatLST", "subset", str("'(@\"%s\")'" %sname))
						if not function.flatCombine("./tmp/flatLST", "./tmp", com=comf, rej=rejf, cty=ctyf, sub=subf):
							QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>flatcombine</b> can not handle this job."))
							gui.logging(self, "--- %s - flatcombine failed." %(datetime.datetime.utcnow()))
						else:
							gui.logging(self, "--- %s - flatcombine succeed." %(datetime.datetime.utcnow()))
							flatFilePath = "./tmp/flat_*.fits"
						os.popen("rm -rf ./tmp/flatLST")
				
				if go:	
					odir = QtGui.QFileDialog.getExistingDirectory(self, 'Select Directory to Save calibrated files')
					err = ""
					errs = ""
					subc = self.ui.comboBox_10.currentText()
					ctyc = self.ui.lineEdit_12.text()
					if os.path.isdir(odir):
						pit = 0
						gui.logging(self, "--- %s - ccdproc started for calibration." %(datetime.datetime.utcnow()))
						for x in xrange(self.ui.listWidget.count()):
							pit = pit + 1
							ln = self.ui.listWidget.item(x)
							img = ln.text()
							if function.headerRead(img, sname) == "" and subc == "yes":
								errs = "%s, %s" %(errs, ntpath.basename(str(img)))
							else:
								function.headerWrite(img, "subset", str("'(@\"%s\")'" %sname))
								if not function.calibration(img, zeroFilePath, darkFilePath, flatFilePath, odir, sub=subc, cty=ctyc):
									err = "%s, %s" %(err, ntpath.basename(str(img)))
							self.ui.label.setText(QtGui.QApplication.translate("Form", "Calibration: %s." %(ntpath.basename(str(img))), None, QtGui.QApplication.UnicodeUTF8))
							self.ui.progressBar.setProperty("value", math.ceil(100*(float(float(pit)/float(self.ui.listWidget.count())))))
						
						if err != "":
							QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("<b>ccdproc</b> failed on:\n%s" %(err)))
						if errs:
							QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Images below have no <b>%s</b> field in header:\n%s\nSkipped!" %(sname, errs)))
						
						gui.logging(self, "--- %s - ccdproc finished calibration." %(datetime.datetime.utcnow()))
						os.popen("rm -rf ./tmp/flatLS ./tmp/zeroLST ./tmp/darkLST %s %s %s" %(zeroFilePath, darkFilePath, flatFilePath))
	else:
		QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("No <b>image</b> to calibrate."))
########################################################
#Create master files####################################
  def masterZero(self):
	gui.logging(self, "-- %s - zerocombine started." %(datetime.datetime.utcnow()))
	lst = gui.lisFromLW(self, self.ui.listWidget_2)
	gui.list2file(lst, "./tmp/zeroLST")
	ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save Master Bias file', 'zero.fits', 'Fit or Fits (*.fits *.fit)')
	if ofile != "":
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
	if ofile != "":
		com = self.ui.comboBox_4.currentText()
		rej = self.ui.comboBox_5.currentText()
		scl = self.ui.comboBox_8.currentText()
		cty = self.ui.lineEdit_10.text()
		if not function.darkCombine("./tmp/darkLST", ofile, com=com, rej=rej, cty=cty, scl=scl):
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
	f = open("./tmp/flatLST", "r")
	it = 0
	sname = self.ui.lineEdit_14.text()
	
	for i in f:
		fn = i.replace("\n","")
		if function.headerRead(fn,sname) == "":
			it = it + 1
	f.close()
	
	com = self.ui.comboBox_6.currentText()
	rej = self.ui.comboBox_7.currentText()
	sub = self.ui.comboBox_9.currentText()
	cty = self.ui.lineEdit_11.text()
	
	if os.path.isdir(odir):
		if sub == "yes" and it != 0:
			QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Subset classification is enabled but one or more images have no <b>%s</b> field in header.\nAdd <b>%s</b> field to headers." %(sname, sname)))
		else:
			
			function.headerWrite("@./tmp/flatLST", "subset", str("'(@\"%s\")'" %sname))
			if not function.flatCombine("./tmp/flatLST", odir, com=com, rej=rej, cty=cty, sub=sub):
				QtGui.QMessageBox.critical( self,  ("MYRaf Error"), ("Due to an error <b>flatcombine</b> can not handle this job."))
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
			  
		  if l.startswith("oRa"):
			  oRa = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_22.setText(QtGui.QApplication.translate("Form", str(oRa), None, QtGui.QApplication.UnicodeUTF8))
		
		  if l.startswith("oDec"):
			  oDec = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_23.setText(QtGui.QApplication.translate("Form", str(oDec), None, QtGui.QApplication.UnicodeUTF8))

		  if l.startswith("obser"):
			  obser = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_18.setText(QtGui.QApplication.translate("Form", str(obser), None, QtGui.QApplication.UnicodeUTF8))
		
		  if l.startswith("obsti"):
			  obsti = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_17.setText(QtGui.QApplication.translate("Form", str(obsti), None, QtGui.QApplication.UnicodeUTF8))

		  if l.startswith("obsda"):
			  obsda = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_24.setText(QtGui.QApplication.translate("Form", str(obsda), None, QtGui.QApplication.UnicodeUTF8))
			  
		  if l.startswith("epoc"):
			  epoc = l.split(":")[1].replace("\n","")
			  self.ui.lineEdit_25.setText(QtGui.QApplication.translate("Form", str(epoc), None, QtGui.QApplication.UnicodeUTF8))

		  if l.startswith("chepoc"):
			  chepoc = l.split(":")[1].replace("\n","")
			  if chepoc == "t":
				  self.ui.checkBox_4.setChecked(True)
				  self.ui.lineEdit_25.setEnabled(False)
			  else:
				  self.ui.checkBox_4.setChecked(False)
				  self.ui.lineEdit_25.setEnabled(True)


 		  if l.startswith("sfMaxStar"):
			  sfMaxStar = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial_7.setValue(sfMaxStar)

 		  if l.startswith("sMaxFWHM"):
			  sMaxFWHM = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial_6.setValue(sMaxFWHM)

 		  if l.startswith("sMinFWHM"):
			  sMinFWHM = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial_5.setValue(sMinFWHM)

 		  if l.startswith("sFluxradi"):
			  sFluxradi = int(l.split(":")[1].replace("\n",""))
			  self.ui.dial_4.setValue(sFluxradi)



				  
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

	f.write("dpExpTime:%s\n" %self.ui.lineEdit_13.text())
	f.write("dpFilter:%s\n" %self.ui.lineEdit_14.text())

	f.write("fspAnnulus:%s\n" %self.ui.dial.value())
	f.write("fspDannulus:%s\n" %self.ui.dial_2.value())
	f.write("fspCBox:%s\n" %self.ui.dial_3.value())
	
	f.write("ppApertur:%s\n" %self.ui.lineEdit_15.text())
	f.write("ppZMag:%s\n" %self.ui.lineEdit_16.text())
	
	f.write("oRa:%s\n" %self.ui.lineEdit_22.text())
	f.write("oDec:%s\n" %self.ui.lineEdit_23.text())
	
	f.write("obser:%s\n" %self.ui.lineEdit_18.text())
	f.write("obsti:%s\n" %self.ui.lineEdit_17.text())
	f.write("obsda:%s\n" %self.ui.lineEdit_24.text())
	
	f.write("epoc:%s\n" %self.ui.lineEdit_25.text())
	if self.ui.checkBox_4.checkState() == QtCore.Qt.Checked:
		f.write("chepoc:t\n")
	else:
		f.write("chepoc:f\n")
	
	f.write("sfMaxStar:%s\n" %self.ui.dial_7.value())
	f.write("sMaxFWHM:%s\n" %self.ui.dial_6.value())
	f.write("sMinFWHM:%s\n" %self.ui.dial_5.value())
	f.write("sFluxradi:%s\n" %self.ui.dial_4.value())
		
	
	f.close()
#########################################################
#Unlock calibration tabs.################################
  def unlockBias(self):
	gui.unlocCali(self, self.ui.checkBox, 1)
  def unlockDark(self):
	gui.unlocCali(self, self.ui.checkBox_2, 2)
  def unlockFlat(self):
	gui.unlocCali(self, self.ui.checkBox_3, 3)
########################################################
  def closeEvent(self, event):
	gui.logging(self, "- %s - MYRaf closed." %(datetime.datetime.utcnow()))
	exit(0)
########################################################
app = QtGui.QApplication(sys.argv)
f = MyForm()
f.show()
app.exec_()
