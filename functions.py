from PyQt4 import QtGui
from PyQt4 import QtCore

def add(self, flist):
	filename=QtGui.QFileDialog.getOpenFileNames(self ,"Images...","",("Fit or Fits (*.fits *.fit)"))
	a=flist.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		flist.addItem(item)
		item = flist.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))

def Rm(self, flist):
	for x in flist.selectedItems():
		flist.takeItem(flist.row(x))
