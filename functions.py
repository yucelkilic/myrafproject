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
				
def biasCombine(self, BiasListDevice):
	if os.path.isfile("./tmp/biasList"):
		os.popen("rm -rf ./tmp/biasList")
		
	if os.path.isfile("./tmp/Zero.fits"):
		os.popen("rm -rf ./tmp/Zero.fits")
		
	for x in xrange(BiasListDevice.count()):
		BiasName = BiasListDevice.item(x)
		BiasName = BiasName.text()
		BiasListFile = open("./tmp/darkList", "a")
		BiasListFile.write(str(BiasName) + "\n")
		BiasListFile.close()
		
	zc = iraf.noao.imred.ccdred.zerocombine
	zc.input = "@tmp/darkList"
	zc.output = "tmp/Zero.fits"
	zc.process = "no"
	zc.ccdtype = ""
	zc._runCode()
		
def darkCombine(self, DarakListDevice):
	if os.path.isfile("./tmp/darkList"):
		os.popen("rm -rf ./tmp/darkList")

	if os.path.isfile("./tmp/Dark.fits"):
		os.popen("rm -rf ./tmp/Dark.fits")
		
	for x in xrange(DarakListDevice.count()):
		DarkName = DarakListDevice.item(x)
		DarkName = DarkName.text()
		DarkListFile = open("./tmp/darkList", "a")
		DarkListFile.write(str(DarkName) + "\n")
		DarkListFile.close()
		
	dc = iraf.noao.imred.ccdred.darkcombine
	dc.input = "@tmp/darkList"
	dc.output = "tmp/Dark.fits"
	dc.process = "no"
	dc.ccdtype = ""
	dc.scale = "exposure"
	dc._runCode()
			
			
def flatCombine(self, FlatListDevice):
	if os.path.isfile("./tmp/flatList"):
		os.popen("rm -rf ./tmp/flatList")
		
	if os.path.isfile("./tmp/Flat.fits"):
		os.popen("rm -rf ./tmp/Flat.fits")
		
	for x in xrange(FlatListDevice.count()):
		FlatName = FlatListDevice.item(x)
		FlatName = FlatName.text()
		FlatListFile = open("./tmp/flatList", "a")
		FlatListFile.write(str(FlatName) + "\n")
		FlatListFile.close()
		
	fc = iraf.noao.imred.ccdred.flatcombine
	fc.input = "@tmp/flatList"
	fc.output = "tmp/Flat.fits"
	fc.process = "no"
	fc.subsets = "no"
	fc.ccdtype = ""
	fc._runCode()
		
def calibration(self, Image, BiasFile, DarkFile, FlatFile):
	isBias = "no"
	isDark = "no"
	isFlat = "no"
	
	if os.path.isfile(str(BiasFile)):
		isBias = "yes"
		
	if os.path.isfile(str(DarkFile)):
		isDark = "yes"
		
	if os.path.isfile(str(FlatFile)):
		isFlat = "yes"
	
	cp = iraf.noao.imred.ccdred.ccdproc
	cp.images = Image
	cp.output = ""
	cp.ccdtype = ""
	cp.fixpix = "no"
	cp.overscan = "no"
	cp.trim = "no"
	cp.zerocor = isBias
	cp.darkcor = isDark
	cp.flatcor = isFlat
	cp.zero = str(BiasFile)
	cp.dark = str(DarkFile)
	cp.flat = str(FlatFile)
	cp(images = Image)

def observatRefresh(self):
	
	count = self.ui.listWidget_10.count()
	for i in xrange(count):
		self.ui.listWidget_10.takeItem(0)
	
	if os.path.isfile("./tmp/obsdb.dat"):
		os.popen("rm ./tmp/obsdb.dat")
	
	for files in os.popen("ls ./obsdat"):
		files = files.replace("\n","")
		f = open("./obsdat/" + files)
		for line in f:
			if line.startswith("name") or line.startswith("longitude") or line.startswith("latitude") or line.startswith("altitude") or line.startswith("timezone"):
				line = "\t" + line

				dosya = open("tmp/obsdb.dat", "a")
				dosya.write(line)
				dosya.close()


			if line.startswith("observatory"):
				line = "\n" + line
				
				dosya = open("tmp/obsdb.dat", "a")
				dosya.write(line)
				dosya.close()
	
	if os.path.isfile("./tmp/obs"):
		os.popen("rm ./tmp/obs")
		
	i=-1
	for files in os.popen("ls ./obsdat"):
		i = i+ 1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget_10.addItem(item)
		item = self.ui.listWidget_10.item(i)
		files = files.replace("\n","")
		item.setText(QtGui.QApplication.translate("Form", str(files), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.comboBox.addItem(str(files))
					
def bringObservatory(self, Name):
	f = open("./obsdat/" + Name)
	first = ""
	for line in f:
		li=line.strip()
		if li.startswith("#"):
			li = li.replace("#","\n")
			first = str(first) + str(li)
			self.ui.textEdit.setHtml(QtGui.QApplication.translate("Form", first + "</br>", None, QtGui.QApplication.UnicodeUTF8))
			
		if li.startswith("name"):
			left, right = li.split("=")
			right = right.replace("\"","")
			self.ui.lineEdit_10.setText(QtGui.QApplication.translate("Form", str(right), None, QtGui.QApplication.UnicodeUTF8))
			
		if li.startswith("longitude"):
			left, right = li.split("=")
			right = right.replace("\"","")
			self.ui.lineEdit_11.setText(QtGui.QApplication.translate("Form", str(right), None, QtGui.QApplication.UnicodeUTF8))
			
		if li.startswith("latitude"):
			left, right = li.split("=")
			right = right.replace("\"","")
			self.ui.lineEdit_12.setText(QtGui.QApplication.translate("Form", str(right), None, QtGui.QApplication.UnicodeUTF8))
			
		if li.startswith("altitude"):
			left, right = li.split("=")
			right = right.replace("\"","")
			self.ui.lineEdit_13.setText(QtGui.QApplication.translate("Form", str(right), None, QtGui.QApplication.UnicodeUTF8))
			
		if li.startswith("timezone"):
			left, right = li.split("=")
			right = right.replace("\"","")
			self.ui.lineEdit_14.setText(QtGui.QApplication.translate("Form", str(right), None, QtGui.QApplication.UnicodeUTF8))
			
		if li.startswith("observatory"):
			left, right = li.split("=")
			right = right.replace("\"","")
			self.ui.lineEdit_9.setText(QtGui.QApplication.translate("Form", str(right), None, QtGui.QApplication.UnicodeUTF8))
			
			
