import os
from PyQt4 import QtGui
from PyQt4 import QtCore

from pyraf import iraf
from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom

import alipy
import glob

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

def Rm(self, flist):
	for x in flist.selectedItems():
		flist.takeItem(flist.row(x))
	fnumber = flist.count()
	
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

def fileNamePath(Path):
	countOfSlashs = Path.count("/")
	imgFileNamePath = Path.split("/")
	Name = str(imgFileNamePath[countOfSlashs])
	Path = Path.replace(Name, "")
	return Name, Path

def align(self, ImagePath, RefPath):
	images_to_align = sorted(glob.glob(str(ImagePath)))
	ref_image = str(RefPath)
	try:
		identifications = alipy.ident.run(ref_image, images_to_align, visu=True)
	except:
		os.system("echo \"--Error with aligning " + str(ImagePath) + " is not alignable!\">>log.my")
		QtGui.QMessageBox.critical( self,  ("Error"), ( fileNamePath(ImagePath)[0] + " is not alignable.\nSkipping ..."))
		
	print(ref_image)
	outputshape = alipy.align.shape(ref_image)
	for id in identifications:
		if id.ok == True:
			try:
				print "%20s : %20s, flux ratio %.2f" % (id.ukn.name, id.trans, id.medfluxratio)
				
				alipy.align.irafalign(id.ukn.filepath, id.uknmatchstars, id.refmatchstars, shape=outputshape, makepng=True)
				hd= iraf.images.imutil.hedit
				hd (id.ukn.filepath, "myraf1", "Aligned via MYRaf V1Beta using Alipy V2", add="yes", verify="no", show="no", update="yes")
				da="geomapin"
				
			except:
				os.system("echo \"--Error with aling." + str(id.ukn.filepath.replace) + " is not alignable\">>log.my")
				QtGui.QMessageBox.critical( self,  ("Error"), ("Can not align image " + str(id.ukn.filepath.replace("./tmp/","") + " skipping ...")))
				
