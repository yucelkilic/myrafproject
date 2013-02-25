import os
from PyQt4 import QtGui
from PyQt4 import QtCore

def add(self, flist, display):
	filename = QtGui.QFileDialog.getOpenFileNames(self ,"Images...","",("Fit or Fits (*.fits *.fit)"))
	a = flist.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		flist.addItem(item)
		item = flist.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
	fnumber = flist.count()
	display.setText(QtGui.QApplication.translate("Form", str(fnumber) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))

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
