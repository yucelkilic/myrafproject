# -*- coding: utf-8 -*-
"""
Created---------------------------------------------------------------------------------------------
		By:
			Muhammed SHEMUNI		Developer
			Yücel KILIÇ				Developer
		at:
			Begin					24.02.2013
			Last update				24.02.2013

Importing things:-----------------------------------------------------------------------------------
	Must have as installed:
		python-2.7
		pyqt4-dev-tools	
		imagemagick(convert)
		iraf						http://www.astro.uson.mx/~favilac/downloads/ubuntu-iraf/iso/
		pyraf						^
		sextractor					http://www.astromatic.net/software/sextractor
		alipy						http://obswww.unige.ch/~tewes/alipy/
		astroasciidata				http://www.stecf.org/software/PYTHONtools/astroasciidata/
		f2n							http://obswww.unige.ch/~tewes/f2n_dot_py/

MYRaf:----------------------------------------------------------------------------------------------
		For further imformation:	http://myrafproject.org/
----------------------------------------------------------------------------------------------------
"""

import sys , os, time, string, math, signal, datetime

today = datetime.datetime.now()
os.system("echo ----------------------------------------------------------------------------------- >>log.my")
os.system("echo \"- Try to start at: " + str(today) + "\" >>log.my")

try:
	from myraf import Ui_Form
	os.system("echo -- MYRaf GUI imported >>log.my")
except:
	print("MYRaf is not installed properly.\nTry remove pyraf/, uparm/ and login.cl\nrm -rf pyraf/ uparm/ login.cl\n and remake them with:\n mkiraf\npyraf\ncommands")
	os.system("echo \"-- Error: Where is myraf.py file?\">>log.my")
	raise SystemExit
try:
	from PyQt4 import QtGui
	from PyQt4 import QtCore
	os.system("echo -- PyQT4 stuff imported >>log.my")
except:
	print("pyqt4-dev-tools'? To install\nsudo apt-get install pyqt4-dev-tools")
	os.system("echo \"-- Error: Where is pyqt4.dev.tools.\">>log.my")
	raise SystemExit

try:
	from pyraf import iraf
	from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom
	os.system("echo -- IRAF stuff imported >>log.my")
except:
	print("Did you install Pyraf, IRAF? To information and problems visit:\nhttps://code.google.com/p/myrafproject/w/list\nIf you did. Try remove pyraf/, uparm/ and login.cl\nrm -rf pyraf/ uparm/ login.cl\n and remake them with:\n mkiraf\npyraf\ncommands")
	os.system("echo \"-- Erro: Where is pyraf?\">>log.my")
	raise SystemExit

try:
	import alipy
	import glob
	os.system("echo -- alipy and glob imported >>log.my")
	
except:
	print("Did you install 'alipy'? For furter information:\nhttp://obswww.unige.ch/~tewes/alipy/")
	os.system("echo \"-- Error: Where is alipy & glob ?\">>log.my")
	raise SystemExit
	
import functions
	
os.system("echo \"- Startup succeed: " + str(today) + "\" >>log.my")
		
class MyForm(QtGui.QWidget):
  def __init__(self):
    super(MyForm, self).__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    
    self.ui.tabWidget_2.setTabEnabled(1,False)
    self.ui.tabWidget_2.setTabEnabled(2,False)
    self.ui.tabWidget_2.setTabEnabled(3,False)
    
    self.ui.pushButton_2.clicked.connect(self.ImageAdd)
    self.ui.pushButton_4.clicked.connect(self.BiasAdd)
    self.ui.pushButton_6.clicked.connect(self.DarkAdd)
    self.ui.pushButton_8.clicked.connect(self.FlatAdd)
    self.ui.pushButton_49.clicked.connect(self.AlignAdd)
    self.ui.pushButton_57.clicked.connect(self.AlignManAdd)
    self.ui.pushButton_35.clicked.connect(self.PhotAdd)
    self.ui.pushButton_59.clicked.connect(self.HeaderAdd)
    
    self.ui.pushButton_3.clicked.connect(self.ImageRm)
    self.ui.pushButton_5.clicked.connect(self.BiasRm)
    self.ui.pushButton_7.clicked.connect(self.DarkRm)
    self.ui.pushButton_9.clicked.connect(self.FlatRm)
    self.ui.pushButton_50.clicked.connect(self.AlignRm)
    self.ui.pushButton_56.clicked.connect(self.AlignManRm)
    self.ui.pushButton_36.clicked.connect(self.PhotRm)
    self.ui.pushButton_60.clicked.connect(self.HeaderRm)
    
    self.ui.checkBox.clicked.connect(self.UnlockBias)
    self.ui.checkBox_2.clicked.connect(self.UnlockDark)
    self.ui.checkBox_3.clicked.connect(self.UnlockFlat)
    self.ui.checkBox_5.clicked.connect(self.HeaderGetVal)
    
    self.ui.pushButton.clicked.connect(self.PhotometryGo)
  
  def PhotometryGo(self):
	
	if self.ui.listWidget.count() == 0:
		QtGui.QMessageBox.critical( self,  ("Error"), ("Select IMAGE..."))
	else:
	
		biaSta = self.ui.checkBox.checkState()
		biaCou = self.ui.listWidget_2.count()
		
		darSta = self.ui.checkBox_2.checkState()
		darCou = self.ui.listWidget_3.count()
		
		flaSta = self.ui.checkBox_3.checkState()
		flaCou = self.ui.listWidget_4.count()
		
		if biaSta != QtCore.Qt.Checked and darSta != QtCore.Qt.Checked and flaSta != QtCore.Qt.Checked:
			QtGui.QMessageBox.critical( self,  ("Error"), ("Nothing to do..."))
		
		err = ""
		
		if biaSta == QtCore.Qt.Checked and biaCou == 0:
			err = err + "---Bias\n"
			isBia = False
		else:
			isBia =True
			
		if darSta == QtCore.Qt.Checked and darCou == 0:
			err = err + "---Dark\n"
			isDar = False
		else:
			isDar = True
			
		if flaSta == QtCore.Qt.Checked and flaCou == 0:
			err = err + "---Flat\n"
			isFla = False
		else:
			isFla=True
			
		if isBia and isDar and isFla:
			print("Do fotometry.")
		else:
			QtGui.QMessageBox.critical( self,  ("Error"), ("Oops\nSelect \n" + err + "and retry..."))
	
  def HeaderGetVal(self):
	if self.ui.checkBox_5.checkState() == QtCore.Qt.Checked:
		self.ui.lineEdit_4.setEnabled(False)
		self.ui.comboBox_2.setEnabled(True)
	else:
		self.ui.lineEdit_4.setEnabled(True)
		self.ui.comboBox_2.setEnabled(False)
    
  def UnlockBias(self):
	if self.ui.checkBox.checkState() == QtCore.Qt.Checked:
		self.ui.tabWidget_2.setTabEnabled(1,True)
	else:
		self.ui.tabWidget_2.setTabEnabled(1,False)
		
  def UnlockDark(self):
	if self.ui.checkBox_2.checkState() == QtCore.Qt.Checked:
		self.ui.tabWidget_2.setTabEnabled(2,True)
	else:
		self.ui.tabWidget_2.setTabEnabled(2,False)
		
  def UnlockFlat(self):
	if self.ui.checkBox_3.checkState() == QtCore.Qt.Checked:
		self.ui.tabWidget_2.setTabEnabled(3,True)
	else:
		self.ui.tabWidget_2.setTabEnabled(3,False)
    
#Image Add functions. Take a look to add function under functions.py file.
  def ImageAdd(self):
	functions.add(self, self.ui.listWidget, self.ui.label_26)
  def BiasAdd(self):
	functions.add(self, self.ui.listWidget_2, self.ui.label_27)
  def DarkAdd(self):
	functions.add(self, self.ui.listWidget_3, self.ui.label_28)
  def FlatAdd(self):
	functions.add(self, self.ui.listWidget_4, self.ui.label_29)
  def AlignAdd(self):
	functions.add(self, self.ui.listWidget_13, self.ui.label_32)
  def AlignManAdd(self):
	functions.add(self, self.ui.listWidget_7, self.ui.label_31)
  def PhotAdd(self):
	functions.add(self, self.ui.listWidget_5, self.ui.label_33)
  def HeaderAdd(self):
	functions.add(self, self.ui.listWidget_9, self.ui.label_34)
	
	
#Image Remove functions. Take a look to Rm function under functions.py file.
  def ImageRm(self):
	functions.Rm(self, self.ui.listWidget, self.ui.label_26)
  def BiasRm(self):
	functions.Rm(self, self.ui.listWidget_2, self.ui.label_27)
  def DarkRm(self):
	functions.Rm(self, self.ui.listWidget_3, self.ui.label_28)
  def FlatRm(self):
	functions.Rm(self, self.ui.listWidget_4, self.ui.label_29)
  def AlignRm(self):
	functions.Rm(self, self.ui.listWidget_13, self.ui.label_32)
  def AlignManRm(self):
	functions.Rm(self, self.ui.listWidget_7, self.ui.label_31)
  def PhotRm(self):
	functions.Rm(self, self.ui.listWidget_5, self.ui.label_33)
  def HeaderRm(self):
	functions.Rm(self, self.ui.listWidget_9, self.ui.label_34)
	
	  
###################
	
	
app = QtGui.QApplication(sys.argv)
f = MyForm()
f.show()
app.exec_()
