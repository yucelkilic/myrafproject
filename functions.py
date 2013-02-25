import os
from PyQt4 import QtGui
from PyQt4 import QtCore

from pyraf import iraf
from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom

def add(self, flist):
	filename = QtGui.QFileDialog.getOpenFileNames(self ,"Images...","",("Fit or Fits (*.fits *.fit)"))
	a = flist.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		flist.addItem(item)
		item = flist.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
	fnumber = flist.count()

def Rm(self, flist, display):
	for x in flist.selectedItems():
		flist.takeItem(flist.row(x))
	fnumber = flist.count()
	display.setText(QtGui.QApplication.translate("Form", str(fnumber) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	
def ImgCopyDisplay(self,ImgPath):
	os.popen("convert -normalize " + ImgPath + " ./tmp/display.png")

def display(self, FilePath, displayDevice):
	if os.path.isfile(FilePath):
		scene = QtGui.QGraphicsScene()
		scene.addPixmap(QtGui.QPixmap(FilePath))
		displayDevice.setScene(scene)

def zoom(self, display, val):
	display.scale(val, val)

def headerDisplay(self, ImagePath):
	if os.path.isfile("./tmp/head"):
		os.remove("./tmp/head")
	rh = iraf.hedit(ImagePath, "*", ".", Stdout="./tmp/head")
	RowCount = self.ui.listWidget_8.count()
	for i in xrange(RowCount):
		self.ui.listWidget_8.takeItem(0)
	i=-1
	f = open('./tmp/head', 'r')
	for x in f:
		RowValue = x.split(",")
		i=i+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_8.addItem(item)
		item = self.ui.listWidget_8.item(i)
		item.setText(QtGui.QApplication.translate("Form", RowValue[1].strip("\n"), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.comboBox_2.addItem(RowValue[1].strip("\n"))
