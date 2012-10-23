# -*- coding: utf-8 -*-
"""
Created---------------------------------------------------------------------------------------------
		By:
			Muhammed SHEMUNI		Developer
			Yücel KILIÇ				Developer
		at:
			Begin					13.09.2012
			Last update				21.10.2012

Importing things:-----------------------------------------------------------------------------------
	Must have as installed:
		python-2.7
		pyqt4-dev-tools	
		imagemagick(convert)
		iraf					http://www.astro.uson.mx/~favilac/downloads/ubuntu-iraf/iso/
		pyraf					^
		sextractor				http://www.astromatic.net/software/sextractor
		alipy					http://obswww.unige.ch/~tewes/alipy/
		astroasciidata			http://www.stecf.org/software/PYTHONtools/astroasciidata/
		f2n						http://obswww.unige.ch/~tewes/f2n_dot_py/
----------------------------------------------------------------------------------------------------
"""

import sys , os, time, string, math, signal, datetime

today = datetime.datetime.now()

os.system("echo \"-" + str(today) + "\" >>log.my")

try:
	from myraf import Ui_Form
except:
	print("MYRaf is not installed properly.\nTry remove ptraf/, uparm/ and login.cl and remake them with:\n mkiraf\npyraf\ncommands")
	os.system("echo \"--Where is myraf.py file?\">>log.my")
	raise SystemExit
try:
	from PyQt4 import QtGui
	from PyQt4 import QtCore
except:
	print("pyqt4-dev-tools'? To install\nsudo apt-get install pyqt4-dev-tools")
	os.system("echo \"--Where is pyqt4.dev.tools.\">>log.my")
	raise SystemExit

try:
	from pyraf import iraf
	from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom
except:
	print("Did you install Pyraf, IRAF? To information and problems visit:\nhttp://myrafproject.org/page.php?p=ins\nIf you are. delete pyraf/, uparm/ and login.cl. And remake them")
	os.system("echo \"--Where is pyraf?\">>log.my")
	raise SystemExit

try:
	import alipy
	import glob
except:
	print("Did you install 'alipy'? To furter information:\nhttp://obswww.unige.ch/~tewes/alipy/")
	os.system("echo \"--Where is alipy & glob ?\">>log.my")
	raise SystemExit
		
class MyForm(QtGui.QWidget):
  def __init__(self):
    super(MyForm, self).__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
	

	
    os.system("rm -rf ./tmp/*")
    os.system("rm -rf ./alipy_visu")
    os.system("rm -rf ./alipy_out")
    os.system("mkdir -p ./tmp/alipy/")
    os.system("mkdir -p ./tmp/analyzed/")
    
    resolution = QtGui.QDesktopWidget().screenGeometry()
    self.move((resolution.width() / 2) - (self.frameSize().width() / 2),(resolution.height() / 2) - (self.frameSize().height() / 2))

    
    self.ui.tabWidgetCalibration.setTabEnabled(1,False)
    self.ui.tabWidgetCalibration.setTabEnabled(2,False)
    self.ui.tabWidgetCalibration.setTabEnabled(3,False)
    
    f = open('./log.my', 'r')
    a=""
    for line in f:
		li=line.strip()
		a=a+li+"\n"
		
    self.ui.BrowserHelpLog.setText(QtGui.QApplication.translate("Form", a, None, QtGui.QApplication.UnicodeUTF8))
    
    if os.path.isfile("./first/main.py"):
		self.ui.checkBox_4.setChecked(True)
		os.system("python ./first/main.py")
    else:
		self.ui.checkBox_4.setChecked(False)
		
    
    f = open('/iraf/iraf/noao/lib/obsdb.dat', 'r')
    for line in f:
		li=line.strip()
		if li.startswith("observatory"):
			l=line.rstrip()
			a=l.split('=')
			b=a[1].replace(" ","")
			b=b.replace("\"","")
			self.ui.comboBoxOBS_3.addItem(b)
			
	
    self.ui.pushButtonIMGAdd.clicked.connect(self.ImageAdd)
    self.ui.pushButtonBiasAdd.clicked.connect(self.BiasAdd)
    self.ui.pushButtonDarkAdd.clicked.connect(self.DarkAdd)
    self.ui.pushButtonFlatAdd.clicked.connect(self.FlatAdd)
    self.ui.pushButtonEdiorHeditAdd.clicked.connect(self.HeaderAdd)
    self.ui.pushButtonEdiorHeditRemove.clicked.connect(self.HeaderRm)
    self.ui.pushButtonAlignAdd.clicked.connect(self.AlignAdd)
    self.ui.listWidget.clicked.connect(self.DisplayImage)
    self.ui.pushButtonGoCalib.clicked.connect(self.ProGo)
    self.ui.pushButtonIMGRm.clicked.connect(self.ImageRm)
    self.ui.pushButtonBiasRm.clicked.connect(self.BiasRm)
    self.ui.pushButtonDarkRm.clicked.connect(self.DarkRm)
    self.ui.pushButtonFlatRm.clicked.connect(self.FlatRm)
    self.ui.pushButtonAlignRm.clicked.connect(self.AlignRm)
    self.ui.checkBoxBias.clicked.connect(self.unlockBias)
    self.ui.checkBoxDark.clicked.connect(self.unlockDark)
    self.ui.checkBoxFlat.clicked.connect(self.unlockFlat)
    self.ui.checkBoxAlign.clicked.connect(self.unlockAlign)
    self.ui.checkBoxEdiorHeditUseValueEx.clicked.connect(self.ValueFromHeader)
    self.ui.listWidgetEditorHedit.clicked.connect(self.heditShow)
    self.ui.listWidgetEditorHeditheader.clicked.connect(self.getHedit)
    self.ui.pushButtonGoEdiorHedit.clicked.connect(self.headerEditt)
    self.ui.pushButtonGoPhoto.clicked.connect(self.photometry)
    self.ui.label_30.mousePressEvent = self.pixelSelect
    self.ui.pushButton.clicked.connect(self.fh)
    self.ui.pushButton_2.clicked.connect(self.fv)
    self.ui.pushButton_3.clicked.connect(self.nr)
    self.ui.pushButton_4.clicked.connect(self.pr)
    self.ui.checkBox_3.clicked.connect(self.unlockanima)
    self.ui.checkBox_4.clicked.connect(self.showhidehelp)
    self.ui.pushButton_5.clicked.connect(self.reloadlog)
    self.ui.pushButtonLogClear.clicked.connect(self.clearlog)
   
#clear log.
  def clearlog(self):
	os.system("echo \"\">log.my")
	self.reloadlog()
#reload the log file.
  def reloadlog(self):
	self.ui.BrowserHelpLog.setText(QtGui.QApplication.translate("Form", "", None, QtGui.QApplication.UnicodeUTF8))
	f = open('./log.my', 'r')
	a=""
	for line in f:
		li=line.strip()
		a=a+li+"\n"
	self.ui.BrowserHelpLog.setText(QtGui.QApplication.translate("Form", a, None, QtGui.QApplication.UnicodeUTF8))
#Show me animation.
  def showhidehelp(self):
	if self.ui.checkBox_4.checkState() == QtCore.Qt.Checked:
		os.system("mv ./gosterme/ ./first/")
	else:
		os.system("mv ./first/ ./gosterme/")
		
#Show me animation.
  def unlockanima(self):
	if self.ui.checkBoxAlign.checkState() != QtCore.Qt.Checked:
		self.ui.checkBox_3.setChecked(False)
		QtGui.QMessageBox.critical( self,  ("Error"), ("You must enable align first!"))
		
#positive rotate
  def pr(self):
	if self.ui.listWidget.currentItem() != None:
		deger=float(self.ui.lineEdit.text())
		deger=(deger+90.0) % 360
		self.ui.lineEdit.setText(QtGui.QApplication.translate("Form", str(deger), None, QtGui.QApplication.UnicodeUTF8))
		self.DisplayImage()
#negative rotate
  def nr(self):
	if self.ui.listWidget.currentItem() != None:
		deger=float(self.ui.lineEdit.text())
		deger=(deger-90.0) %360
		self.ui.lineEdit.setText(QtGui.QApplication.translate("Form", str(deger), None, QtGui.QApplication.UnicodeUTF8))
		self.DisplayImage()
#Flip Vertical
  def fh(self):
	if self.ui.listWidget.currentItem() != None:
		if self.ui.checkBox.checkState() != QtCore.Qt.Checked:
			self.ui.checkBox.setChecked(True)
		else:
			self.ui.checkBox.setChecked(False)
		self.DisplayImage()
#flip horizontal
  def fv(self):
	if self.ui.listWidget.currentItem() != None:
		if self.ui.checkBox_2.checkState() != QtCore.Qt.Checked:
			self.ui.checkBox_2.setChecked(True)
		else:
			self.ui.checkBox_2.setChecked(False)
		self.DisplayImage()
	
#copy files. In case rotate or flip it.
  def copyFits(self, image, des):
	rot=self.ui.lineEdit.text()
	print rot
	print image
	
	say = image.count("/")
	imName=image.split("/")
	print imName[say]
	
	ig = iraf.images.imgeom.imtranspose
	ic = iraf.images.imutil.imcopy
	
	try:
		
		if rot=="90.0":
			ig(image+"[*,-*]", des+"imagerot"+imName[say])
		elif rot=="180.0":
			ic(image+"[-*,-*]", des+"imagerot"+imName[say])
		elif rot=="270.0":
			ig(image+"[-*,*]", des+"imagerot"+imName[say])
		else:
			ic(image+"[*,*]", des+"imagerot"+imName[say])
			
		if self.ui.checkBox.checkState() == QtCore.Qt.Checked:
			ic(des+"imagerot"+imName[say]+"[*,-*]",des+"imagerotflhr"+imName[say])
		else:
			ic(des+"imagerot"+imName[say]+"[*,*]",des+"imagerotflhr"+imName[say])
		
		if self.ui.checkBox_2.checkState() == QtCore.Qt.Checked:
			ic(des+"imagerotflhr"+imName[say]+"[-*,*]",des+"imagerotflhrflv"+imName[say])
		else:
			ic(des+"imagerotflhr"+imName[say]+"[*,*]",des+"imagerotflhrflv"+imName[say])
			
		os.system("cp "+des+"imagerotflhrflv"+imName[say] + " " + des+imName[say])
		os.system("rm "+des+"imagerot*"+imName[say])
	except:
		QtGui.QMessageBox.critical( self,  ("Error"), ("Simple keyword value is not standart for " + imName[say] + " file."))
		os.system("echo \"--Error with copying Simple keyword value is not standart for " + imName[say] + " file!\">>log.my")
	
#photometry.
  def photometry(self):
	
	QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
	if self.ui.lineEdit_2.text() != "" and self.ui.lineEdit_3.text() != "":
		ch=0
		self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Checking header information...", None, QtGui.QApplication.UnicodeUTF8))
		for x in xrange(self.ui.listWidget.count()):
			d=self.ui.listWidget.item(x)
			img = d.text()
			hd = iraf.images.imutil.hselect	
			s=hd (img, "ra,dec,epoch,subset,date-obs,time-obs, observat", "yes", Stdout=1)
			stab = s[0].count("\t",0,len(s[0]))
			if str(stab) != "6":
				if ch==0:
					ch=ch+1
					QtGui.QMessageBox.critical( self,  ("Error"), ("Please add to your these keyword values:\n\tra\n\tdec\n\tepoch\n\tsubset\n\tdate-obs\n\ttime-obs\n\tobservat."))
		
		if ch ==0:
			
			if self.ui.checkBox_3.checkState() == QtCore.Qt.Checked:
				mkpng=True
			else:
				mkpng=False
				
			a=self.ui.comboBox.currentText()
			dene=False
			if a == "Variant 1":
				dene=True
			
			if self.ui.checkBoxAlign.checkState() == QtCore.Qt.Checked:
								
				os.system("rm -f ./tmp/alipy/*.fit*")
				i=0
				for x in xrange(self.ui.listWidget.count()):
					i=i+1
					self.ui.progressBarPhoto.setProperty("value", math.ceil(50*(i+1)/self.ui.listWidget.count()))
					d=self.ui.listWidget.item(x)
					img = d.text()
					self.copyFits(str(img), "./tmp/alipy/")
					
					c_slash_say=img.count("/")
					imgFileName=img.split("/")
					
					images_to_align = sorted(glob.glob("./tmp/alipy/"+str(imgFileName[c_slash_say])))
					self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Aligning " + str(images_to_align[0].replace("./tmp/alipy/","")), None, QtGui.QApplication.UnicodeUTF8))
					ref_image = "./tmp/display.fit"
					try:
						identifications = alipy.ident.run(ref_image, images_to_align, visu=False)
					except:
						os.system("echo \"--Error with aligning " + str(images_to_align[0].replace("./tmp/alipy/","")) + " is not alignable!\">>log.my")
						QtGui.QMessageBox.critical( self,  ("Error"), ( str(images_to_align[0].replace("./tmp/alipy/","")) + " is not alignable.\nSkipping ..."))
					
					outputshape = alipy.align.shape(ref_image)
					for id in identifications:
						self.ui.progressBarPhoto.setProperty("value", math.ceil(50*(x+1)/self.ui.listWidget.count()))
						if id.ok == True:
							try:
								print "%20s : %20s, flux ratio %.2f" % (id.ukn.name, id.trans, id.medfluxratio)
								if dene:
									alipy.align.affineremap(id.ukn.filepath, id.trans, shape=outputshape, makepng=mkpng)
									hd= iraf.images.imutil.hedit
									hd (id.ukn.filepath, "myraf1", "Aligned via MYRaf V1Beta using Alipy V2", add="yes", verify="no", show="no", update="yes")
									da="affineremap"
								else:
									alipy.align.irafalign(id.ukn.filepath, id.uknmatchstars, id.refmatchstars, shape=outputshape, makepng=mkpng)
									hd= iraf.images.imutil.hedit
									hd (id.ukn.filepath, "myraf1", "Aligned via MYRaf V1Beta using Alipy V2", add="yes", verify="no", show="no", update="yes")
									da="geomapin"
							except:
								os.system("echo \"--Error with aling." + str(id.ukn.filepath.replace("./tmp/","")) + " is not alignable\">>log.my")
								QtGui.QMessageBox.critical( self,  ("Error"), ("Can not align image " + str(id.ukn.filepath.replace("./tmp/","")) + " skipping ..."))

						
				
				os.system("ls ./tmp/alipy/*.fit* > ./tmp/headReplace")
				f=open("./tmp/headReplace")
				for x in f:
					l=x.strip()
					d=l.split("/")
					filenamme=d[3].split(".")
					mkh=iraf.artdata.mkheader
					self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Repairing header for " + filenamme[0] + ".fits", None, QtGui.QApplication.UnicodeUTF8))
					mkh(str("./alipy_out/" + filenamme[0] + "_" + da + ".fits"), str(l))
				
				va=self.ui.lineEdit_2.text()
				vax, vay = va.split(" - ")
				vs, vx=vax.split(":")
				vs, vy=vay.split(":")
				
				ca=self.ui.lineEdit_3.text()
				cax, cay = ca.split(" - ")
				cs, cx=cax.split(":")
				cs, cy=cay.split(":")
				

				os.system("echo " + str(vx) + " " + str(vy) + " > ./tmp/coo")
				os.system("echo " + str(cx) + " " + str(cy) + " >> ./tmp/coo")
				

			
				os.system('echo astcalc > ./tmp/st.cl')
				os.system("echo \"	observatory=\\\"" + str(self.ui.comboBoxOBS_3.currentText()) + "\\\"\" >> ./tmp/st.cl")
				os.system("echo \"	st=mst(@'DATE-OBS',@'TIME-OBS',obsdb(observatory,\\\"longitude\\\"))\" >> ./tmp/st.cl")
				os.system("echo quit >> ./tmp/st.cl")


				os.system("rm -f ./alipy_out/display*.fits")
				os.system("ls ./alipy_out/*.fits > ./tmp/photoList")
				
			

				
				##setjd, asthedit and airmass
				sd = iraf.noao.astutil.setjd
				ss = iraf.setairmass
				at = iraf.noao.astutil.asthedit
				f = open('./tmp/photoList', 'r')
				for line in f:
					li=line.strip()
					self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Processing setjd, asthedit, setairmass for image " + li , None, QtGui.QApplication.UnicodeUTF8))
					sd (li, observatory = str(self.ui.comboBoxOBS_3.currentText()), time = "time-obs")
					at (li, commands = "./tmp/st.cl", update = "yes", verbose = "yes")
					ss (li, observatory = str(self.ui.comboBoxOBS_3.currentText()), intype = "middle", ut = "time-obs")
								
				##datapar
				iraf.datapars.setParam("exposur", "exptime")
				iraf.datapars.setParam("airmass", "airmass")
				iraf.datapars.setParam("filter", "subset")
				iraf.datapars.setParam("obstime", "hjd")
				iraf.datapars.saveParList(filename="./uparm/aptdataps.par")
				##centerpar
				iraf.centerpars.setParam("cbox", "10.0")
				iraf.centerpars.saveParList(filename="./uparm/aptcentes.par")
				##fitskypars
				iraf.fitskypars.setParam("annulus", "25")
				iraf.fitskypars.setParam("dannulus", "5")
				iraf.fitskypars.saveParList(filename="./uparm/aptfitsks.par")
				##photpars
				iraf.photpars.setParam("apertur", "10,15,20,25,30")
				iraf.photpars.setParam("zmag", "25")
				iraf.photpars.saveParList(filename="./uparm/aptphot.par")	
				##phot

				os.system("rm -f ./tmp/analyzed/*.mag*")
				i=0
				pt = iraf.phot
				hd= iraf.images.imutil.hedit

				f = open('./tmp/photoList', 'r')
				for line in f:
					i=i+1
					self.ui.progressBarPhoto.setProperty("value", math.ceil(50+50*(i+1)/self.ui.listWidget.count()))
					li=line.strip()
					hd (li, "observat", str(self.ui.comboBoxOBS_3.currentText()) , add="yes", verify="no", show="no", update="yes")
					self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Phot task is working for " + li, None, QtGui.QApplication.UnicodeUTF8))
					pt (li, coords =  "./tmp/coo", output = "./tmp/analyzed/" , interac = "no", verify = "no", Stdout=1)

					
				os.system("rm -f ./tmp/result.my")
				tx=iraf.txdump
				tx ("./tmp/analyzed/*.mag.1", "id, otime, mag , merr, xairmass", "yes", Stdout= "./tmp/result.my")
				self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Please wait. Copying selected file(s)...", None, QtGui.QApplication.UnicodeUTF8))
				ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save photometry result file', 'result.my', 'MYRaf Result File (*.my)')
				os.popen("cat ./title_head.my ./tmp/result.my >" + str(ofile))
				if mkpng:
					giffile = QtGui.QFileDialog.getSaveFileName( self, 'Save photometry result file', 'result.gif', 'MYRaf Result File (*.gif)')
					os.system("mkdir " + str(giffile) + "/MYRafResultPNG")
					os.system("cp ./alipy_out/*.png " + str(giffile) + "/MYRafResultPNG")
				self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "The End...", None, QtGui.QApplication.UnicodeUTF8))	
				
			else:
								
				va=self.ui.lineEdit_2.text()
				vax, vay = va.split(" - ")
				vs, vx=vax.split(":")
				vs, vy=vay.split(":")
				
				ca=self.ui.lineEdit_3.text()
				cax, cay = ca.split(" - ")
				cs, cx=cax.split(":")
				cs, cy=cay.split(":")
				
				os.system("echo " + str(vx) + " " + str(vy) + " > ./tmp/coo")
				os.system("echo " + str(cx) + " " + str(cy) + " >> ./tmp/coo")
				
				os.system('echo astcalc > ./tmp/st.cl')
				os.system("echo \"	observatory=\\\"" + str(self.ui.comboBoxOBS_3.currentText()) + "\\\"\" >> ./tmp/st.cl")
				os.system("echo \"	st=mst(@'DATE-OBS',@'TIME-OBS',obsdb(observatory,\\\"longitude\\\"))\" >> ./tmp/st.cl")
				os.system("echo quit >> ./tmp/st.cl")
				
				os.system("ls ./tmp/*.fits > ./tmp/photoList")
				
				self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Please wait. Processing setjd, asthedit, setairmass your image file(s)...", None, QtGui.QApplication.UnicodeUTF8))
				##setjd, asthedit and airmass
				sd = iraf.noao.astutil.setjd
				ss = iraf.setairmass
				at = iraf.noao.astutil.asthedit
				
				##datapar
				iraf.datapars.setParam("exposur", "exptime")
				iraf.datapars.setParam("airmass", "airmass")
				iraf.datapars.setParam("filter", "subset")
				iraf.datapars.setParam("obstime", "hjd")
				iraf.datapars.saveParList(filename="./uparm/aptdataps.par")
				##centerpar
				iraf.centerpars.setParam("cbox", "10.0")
				iraf.centerpars.saveParList(filename="./uparm/aptcentes.par")
				##fitskypars
				iraf.fitskypars.setParam("annulus", "25")
				iraf.fitskypars.setParam("dannulus", "5")
				iraf.fitskypars.saveParList(filename="./uparm/aptfitsks.par")
				##photpars
				iraf.photpars.setParam("apertur", "10,15,20,25,30")
				iraf.photpars.setParam("zmag", "25")
				iraf.photpars.saveParList(filename="./uparm/aptphot.par")
				##phot
				pt = iraf.phot
				i=0
				hd= iraf.images.imutil.hedit
				os.system("rm -f ./tmp/alipy/*")
				for x in xrange(self.ui.listWidget.count()):
					i=i+1
					d=self.ui.listWidget.item(x)
					img=d.text()
					self.copyFits(str(img), "./tmp/alipy/")
					cslash = img.count("/")
					imgg=img.split("/")
					hd ("./tmp/alipy/"+str(imgg[cslash]), "observat", str(self.ui.comboBoxOBS_3.currentText()) , add="yes", verify="no", show="no", update="yes")
					self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Phot task is working for " + str(imgg[cslash]), None, QtGui.QApplication.UnicodeUTF8))
					sd ("./tmp/alipy/"+str(imgg[cslash]), observatory = str(self.ui.comboBoxOBS_3.currentText()), time = "time-obs")
					at ("./tmp/alipy/"+str(imgg[cslash]), commands = "./tmp/st.cl", update = "yes", verbose = "yes")
					ss ("./tmp/alipy/"+str(imgg[cslash]), observatory = str(self.ui.comboBoxOBS_3.currentText()), intype = "middle", ut = "time-obs")
					self.ui.progressBarPhoto.setProperty("value", math.ceil(100*(i+1)/self.ui.listWidget.count()))
					pt ("./tmp/alipy/"+str(imgg[cslash]), coords =  "./tmp/coo", output = "./tmp/analyzed/" , interac = "no", verify = "no", Stdout=1)
					
				os.system("rm -f ./tmp/result.my")
				tx=iraf.txdump
				tx ("./tmp/analyzed/*.mag.1", "id, otime, mag , merr, xairmass", "yes", Stdout= "./tmp/result.my")
				self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Please wait. Copying selected file(s)...", None, QtGui.QApplication.UnicodeUTF8))
				ofile = QtGui.QFileDialog.getSaveFileName( self, 'Save photometry result file', 'result.my', 'MYRaf Result File (*.my)')
				os.popen("cat ./title_head.my ./tmp/result.my >" + str(ofile))
				self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "The End...", None, QtGui.QApplication.UnicodeUTF8))	
				
	else:
		QtGui.QMessageBox.critical( self,  ("Error"), ("Please select Variable (V) and Check (C) stars."))
			
	QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
		
#Edit header
  def headerEditt(self):
	
	if self.ui.listWidgetEditorHedit.count() == 0:
		
		QtGui.QMessageBox.critical( self,  ("Error"), ("Please select files for header edit."))
		
	else:
		ch=self.ui.lineEditEdiorHeditFeild.text()
		if str(ch).strip() == "":
			
			QtGui.QMessageBox.critical( self,  ("Error"), ("Please fill the field."))
			
		else:
			f=self.ui.lineEditEdiorHeditFeild.text()
			f=f.replace(" ", "")
			if self.ui.checkBoxEdiorHeditUseValueEx.checkState() != QtCore.Qt.Checked:
				v=self.ui.lineEditEdiorHeditValue.text()
				hd= iraf.images.imutil.hedit
				for x in xrange(self.ui.listWidgetEditorHedit.count()):
					d=self.ui.listWidgetEditorHedit.item(x)
					img = d.text()
					QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
					hd (str(img), str(f), str(v), add="yes", verify="no", show="no", update="yes")
					self.ui.progressBarEdiorHedit.setProperty("value", math.ceil(100*(x+1)/self.ui.listWidgetEditorHedit.count()))

			else:
				h=self.ui.comboBoxEdiorHeditValueExist.currentText()
				selectedField, selectedValue=h.split(" = ")
				hd= iraf.images.imutil.hedit
				for x in xrange(self.ui.listWidgetEditorHedit.count()):
					d=self.ui.listWidgetEditorHedit.item(x)
					img = d.text()
					QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
					hd (str(img), str(f), str("'(@\""+selectedField+"\")'"), add="yes", verify="no", show="no", update="yes")
					self.ui.progressBarEdiorHedit.setProperty("value", math.ceil(100*(x+1)/self.ui.listWidgetEditorHedit.count()))
			self.heditShow()
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#get selected header value and field
  def getHedit(self):
	a=self.ui.listWidgetEditorHeditheader.currentItem()
	a=a.text()
	field, balue = a.split(" = ")
	balue=balue.replace("\"","")
	self.ui.lineEditEdiorHeditFeild.setText(QtGui.QApplication.translate("Form", field, None, QtGui.QApplication.UnicodeUTF8))
	self.ui.lineEditEdiorHeditValue.setText(QtGui.QApplication.translate("Form", balue, None, QtGui.QApplication.UnicodeUTF8))
#get coordinate of clicked pixel
  def pixelSelect(self, event):
	
	
	s=self.ui.label_30.height()
	hs=iraf.images.imutil.hselect
	size=hs("./tmp/display.fit","naxis1,naxis2","yes",Stdout=1)
	ix,ye=size[0].split("\t")
	if ix == "" or ye == "":
		QtGui.QMessageBox.critical( self,  ("Error"), ("There is no naxis1 and naxis2 fields on this image's header.\nnaxis1: number of x pixels\nnaxis2:number of x pixels."))
	else:
		
		a=True
		if ix > ye:
			dispY=436
			dispX=436*float(ix)/float(ye)
		else:
			dispY=436*float(ye)/float(ix)
			dispX=436
			
		if float(event.pos().x()) > dispX:
			a=False
		if float(436-event.pos().y()) > dispY:
			a=False

		if a:
			if self.ui.radioButton.isChecked():
				cor="x:" + str(round(float(event.pos().x())*float(ix)/float(dispX),2)) + " - y:" + str(round((436-float(event.pos().y()))*float(ye)/float(dispY),2))
				self.ui.lineEdit_2.setText(QtGui.QApplication.translate("Form", str(cor), None, QtGui.QApplication.UnicodeUTF8))
				self.ui.radioButton_2.setChecked(True)
			else:
				cor="x:" + str(round(float(event.pos().x())*float(ix)/float(dispX),2)) + " - y:" + str(round((436-float(event.pos().y()))*float(ye)/float(dispY),2))
				self.ui.lineEdit_3.setText(QtGui.QApplication.translate("Form", str(cor), None, QtGui.QApplication.UnicodeUTF8))
				self.ui.radioButton.setChecked(True)
	
#get all header of an image
  def heditShow(self):
	img=self.ui.listWidgetEditorHedit.currentItem()
	img=img.text()
	if os.path.isfile("./tmp/head"):
		os.system("rm -f ./tmp/head")
	s = iraf.hedit(img, "*", ".", Stdout="./tmp/head")
	say=self.ui.listWidgetEditorHeditheader.count()
	for i in xrange(say):
		self.ui.listWidgetEditorHeditheader.takeItem(0)
	a=-1
	f = open('./tmp/head', 'r')
	for x in f:
		b=x.split(",")
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidgetEditorHeditheader.addItem(item)
		item = self.ui.listWidgetEditorHeditheader.item(a)
		item.setText(QtGui.QApplication.translate("Form", b[1].strip("\n"), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.comboBoxEdiorHeditValueExist.addItem(b[1].strip("\n"))
#Remove images from Calibration list
  def ImageRm(self):
	for x in self.ui.listWidgetIMG.selectedItems():
		self.ui.listWidgetIMG.takeItem(self.ui.listWidgetIMG.row(x))
		
	self.ui.labelShowIMG.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetIMG.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Remove images from Bias list
  def BiasRm(self):
	for x in self.ui.listWidgetIMGBias.selectedItems():
		self.ui.listWidgetIMGBias.takeItem(self.ui.listWidgetIMGBias.row(x))
		
	self.ui.labelShowBias.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetIMGBias.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Remove images from Dark list
  def DarkRm(self):
	for x in self.ui.listWidgetDark.selectedItems():
		self.ui.listWidgetDark.takeItem(self.ui.listWidgetDark.row(x))
		
	self.ui.labelShowDark.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetDark.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Remove images from Flat list
  def FlatRm(self):
	for x in self.ui.listWidgetFlat.selectedItems():
		self.ui.listWidgetFlat.takeItem(self.ui.listWidgetFlat.row(x))
		
	self.ui.labelShowFlat.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetFlat.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Remove images from Header list
  def HeaderRm(self):
	for x in self.ui.listWidgetEditorHedit.selectedItems():
		self.ui.listWidgetEditorHedit.takeItem(self.ui.listWidgetEditorHedit.row(x))
#Remove images from Align list
  def AlignRm(self):
	for x in self.ui.listWidget.selectedItems():
		self.ui.listWidget.takeItem(self.ui.listWidget.row(x))
		
	self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidget.count()) + "</b> Files will using for photometry", None, QtGui.QApplication.UnicodeUTF8))
#Add images from Calibration list
  def ImageAdd(self):
	filename=QtGui.QFileDialog.getOpenFileNames(self,"Images...","",("Fit or Fits (*.fits *.fit)"))
	a=self.ui.listWidgetIMG.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidgetIMG.addItem(item)
		item = self.ui.listWidgetIMG.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
		
	self.ui.labelShowIMG.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetIMG.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Add images from Biass list
  def BiasAdd(self):
	filename=QtGui.QFileDialog.getOpenFileNames(self,"Bias...","",("Fit or Fits (*.fits *.fit)"))
	a=self.ui.listWidgetIMGBias.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidgetIMGBias.addItem(item)
		item = self.ui.listWidgetIMGBias.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
	
	self.ui.labelShowBias.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetIMGBias.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Add images from Dark list
  def DarkAdd(self):
	filename=QtGui.QFileDialog.getOpenFileNames(self,"Dark...","",("Fit or Fits (*.fits *.fit)"))
	a=self.ui.listWidgetDark.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidgetDark.addItem(item)
		item = self.ui.listWidgetDark.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
		
	self.ui.labelShowDark.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetDark.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Add images from Flat list
  def FlatAdd(self):
	filename=QtGui.QFileDialog.getOpenFileNames(self,"Flat...","",("Fit or Fits (*.fits *.fit)"))
	a=self.ui.listWidgetFlat.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidgetFlat.addItem(item)
		item = self.ui.listWidgetFlat.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
		
	self.ui.labelShowFlat.setText(QtGui.QApplication.translate("Form", str(self.ui.listWidgetFlat.count()) + " Files selected", None, QtGui.QApplication.UnicodeUTF8))
	self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidgetIMG.count()) + "</b> Files will calibrate by uisng, <b>" + str(self.ui.listWidgetIMGBias.count()) + "</b> Bias files, <b>" + str(self.ui.listWidgetDark.count()) + "</b> Dark files and <b>" + str(self.ui.listWidgetFlat.count()) + "</b> Flat files.", None, QtGui.QApplication.UnicodeUTF8))
#Add images from Align list
  def AlignAdd(self):
	filename=QtGui.QFileDialog.getOpenFileNames(self,"Images...","./",("Fit or Fits (*.fit *.fits)"))
	a=self.ui.listWidget.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidget.addItem(item)
		item = self.ui.listWidget.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "<b>" + str(self.ui.listWidget.count()) + "</b> File(s) will using for photometry", None, QtGui.QApplication.UnicodeUTF8))
#Add images from Header list
  def HeaderAdd(self):
	filename=QtGui.QFileDialog.getOpenFileNames(self,"Images...","",("Fit or Fits (*.fits *.fit)"))
	a=self.ui.listWidgetEditorHedit.count()-1
	for x in filename:
		a=a+1
		item = QtGui.QListWidgetItem()
		self.ui.listWidgetEditorHedit.addItem(item)
		item = self.ui.listWidgetEditorHedit.item(a)
		item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
#Unlocking Bias tab and enabling bias corraction for calibration
  def unlockBias(self):
	if self.ui.checkBoxBias.checkState() == QtCore.Qt.Checked:
		self.ui.tabWidgetCalibration.setTabEnabled(1,True)
	else:
		self.ui.tabWidgetCalibration.setTabEnabled(1,False)
#Unlocking Dark tab and enabling dark corraction for calibration
  def unlockDark(self):
	if self.ui.checkBoxDark.checkState() == QtCore.Qt.Checked:
		self.ui.tabWidgetCalibration.setTabEnabled(2,True)
	else:
		self.ui.tabWidgetCalibration.setTabEnabled(2,False)
#Unlocking Flat tab and enabling flat corraction for calibration
  def unlockFlat(self):
	if self.ui.checkBoxFlat.checkState() == QtCore.Qt.Checked:
		self.ui.tabWidgetCalibration.setTabEnabled(3,True)
	else:
		self.ui.tabWidgetCalibration.setTabEnabled(3,False)	
#get value from header for update or adding a field to header
  def ValueFromHeader(self):
	if self.ui.checkBoxEdiorHeditUseValueEx.checkState() == QtCore.Qt.Checked:
		self.ui.comboBoxEdiorHeditValueExist.setEnabled(True)
		self.ui.lineEditEdiorHeditValue.setEnabled(False)
	else:
		self.ui.comboBoxEdiorHeditValueExist.setEnabled(False)
		self.ui.lineEditEdiorHeditValue.setEnabled(True)
# Chacking conformity for calibration
  def ProGo(self):
      bias=False
      dark=False
      flat=False
      if self.ui.checkBoxBias.checkState() == QtCore.Qt.Checked:
          bias=True
      
      if self.ui.checkBoxDark.checkState() == QtCore.Qt.Checked:
          dark=True
      
      if self.ui.checkBoxFlat.checkState() == QtCore.Qt.Checked:
          flat=True
      
      if self.ui.listWidgetIMG.count() == 0:
		  QtGui.QMessageBox.critical( self,  ("Error"), ("Please select images(s)..."))
      else:
		  
		  if bias==False and dark==False and flat==False:
			  QtGui.QMessageBox.critical( self,  ("Error"), ("There is no proccess selected"))
		  else:
			  
			  if bias and self.ui.listWidgetIMGBias.count() == 0:
				  QtGui.QMessageBox.critical( self,  ("Error"), ("Please select Bias file(s)..."))
			  elif dark and self.ui.listWidgetDark.count() == 0:
				  QtGui.QMessageBox.critical( self,  ("Error"), ("Please select Dark file(s)..."))
			  elif flat and self.ui.listWidgetFlat.count() == 0:
				  QtGui.QMessageBox.critical( self,  ("Error"), ("Please select Flat file(s)..."))
			  else:
				  self.red()

#calibration
  def red(self):

      bias=""
      dark=""
      flat=""
      bi="no"
      da="no"
      fa="no"
      
      for x in xrange(self.ui.listWidgetIMGBias.count()):
          a=self.ui.listWidgetIMGBias.item(x)
          bias = a.text()
          dosya = open("tmp/biasList", "a")
          dosya.write(bias+"\n")
          dosya.close()

      for x in xrange(self.ui.listWidgetDark.count()):
          b=self.ui.listWidgetDark.item(x)
          dark = b.text()
          dosya = open("tmp/darkList", "a")
          dosya.write(dark+"\n")
          dosya.close()
          
      for x in xrange(self.ui.listWidgetFlat.count()):
          c=self.ui.listWidgetFlat.item(x)
          flat = c.text()
          dosya = open("tmp/flatList", "a")
          dosya.write(flat+"\n")
          dosya.close()
          
      os.system("rm -f .tmp/Zero.fits")
      if self.ui.checkBoxBias.checkState() == QtCore.Qt.Checked:
          bi="yes"
          zc = iraf.noao.imred.ccdred.zerocombine
          zc.input = "@tmp/biasList"
          zc.output = "tmp/Zero.fits"
          zc.process = "no"
          zc.ccdtype = ""
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Processing bias files...", None, QtGui.QApplication.UnicodeUTF8))
          try:
			  zc._runCode()
          except:
			  QtGui.QMessageBox.critical( self,  ("Error"), ("Check your Bias/Zero file(s)."))
			  os.system("echo \"--Error With Zero Files. There is a problem Bias file(s).\">>log.my")
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Bias files processed...", None, QtGui.QApplication.UnicodeUTF8))

      os.system("rm -f .tmp/Dark.fits")
      if self.ui.checkBoxDark.checkState() == QtCore.Qt.Checked:
          da="yes"
          dc = iraf.noao.imred.ccdred.darkcombine
          dc.input = "@tmp/darkList"
          dc.output = "tmp/Dark.fits"
          dc.process = "no"
          dc.ccdtype = ""
          dc.scale = "exposure"
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Processing dark files...", None, QtGui.QApplication.UnicodeUTF8))
          try:
			  dc._runCode()
          except:
			  os.system("echo \"--Error with Dark Files. There is a problem Dark file(s).\">>log.my")
			  QtGui.QMessageBox.critical( self,  ("Error"), ("Check your Dark file(s)."))
          
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Dark files processed...", None, QtGui.QApplication.UnicodeUTF8)) 
          
      os.system("rm -f .tmp/Flat.fits")
      if self.ui.checkBoxFlat.checkState() == QtCore.Qt.Checked:
          fa="yes"
          fc = iraf.noao.imred.ccdred.flatcombine
          fc.input = "@tmp/flatList"
          fc.output = "tmp/Flat.fits"
          fc.process = "no"
          fc.subsets = "no"
          fc.ccdtype = ""
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Processing flat files...", None, QtGui.QApplication.UnicodeUTF8))
          try:
			  fc._runCode()
          except:
			  os.system("echo \"--Error With Flat files. There is a problem Flat file(s).\">>log.my")
			  QtGui.QMessageBox.critical( self,  ("Error"), ("Check your Flat file(s)."))
			  
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Flat files Processed...", None, QtGui.QApplication.UnicodeUTF8))
         
      QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
      for x in xrange(self.ui.listWidgetIMG.count()):
          d=self.ui.listWidgetIMG.item(x)
          img = d.text()
          cp = iraf.noao.imred.ccdred.ccdproc
          cp.images = img
          cp.output = ""
          cp.ccdtype = ""
          cp.fixpix = "no"
          cp.overscan = "no"
          cp.trim = "no"
          cp.zerocor = bi
          cp.darkcor = da
          cp.flatcor = fa
          cp.zero = "tmp/Zero.fits"
          cp.dark = "tmp/Dark.fits"
          cp.flat = "tmp/Flat.fits"
          self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Processing " + str(img) + " file...", None, QtGui.QApplication.UnicodeUTF8))
          try:
			  
			  hd= iraf.images.imutil.hedit
			  hd (id.ukn.filepath, "myraf2", "Calibrated via MYRaf V1Beta", add="yes", verify="no", show="no", update="yes")
			  cp(images = img)
          except:
			  QtGui.QMessageBox.critical( self,  ("Error"), ("Check your Image(s). Maybe restarting will help!"))
			  os.system("echo \"--Error with images, master Bias, Dark or flat\">>log.my")
          self.ui.progressBarCalib.setProperty("value", math.ceil(100*(x+1)/self.ui.listWidgetIMG.count()))
	  self.ui.labelCalibPro.setText(QtGui.QApplication.translate("Form", "Process calibrated " + str((x+1)) + " file(s)...", None, QtGui.QApplication.UnicodeUTF8))		
      QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#Enabling align
  def unlockAlign(self):
	a=self.ui.listWidget.currentItem()
	
	if a == None:
		self.ui.checkBoxAlign.setChecked(False)
		QtGui.QMessageBox.critical( self,  ("Error"), ("Please select a reference image first..."))
	else:
		if self.ui.checkBoxAlign.checkState() == QtCore.Qt.Checked:
			self.ui.widget.setEnabled(False)
			self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Please wait. Choosing stars...", None, QtGui.QApplication.UnicodeUTF8))
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
			images_to_align = sorted(glob.glob("./tmp/display.fit"))
			ref_image = "./tmp/display.fit"
			try:
				identifications = alipy.ident.run(ref_image, images_to_align, visu=True)
				for id in identifications:
					if id.ok == True:
						print "%20s : %20s, flux ratio %.2f" % (id.ukn.name, id.trans, id.medfluxratio)
						
				h=self.ui.label_30.height()
				w=self.ui.label_30.width()
				os.system(str("convert -normalize -resize " + str(w) + "x" + str(h) + " ./alipy_visu/display_stars.png ./tmp/display.png"))
				self.ui.label_30.setPixmap(QtGui.QPixmap("./tmp/display.png"))
				self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Process done.", None, QtGui.QApplication.UnicodeUTF8))
				
			except:
				self.ui.checkBoxAlign.setChecked(False)
				QtGui.QMessageBox.critical( self,  ("Error"), ("Image is not usable. Going to remove it from list.\nPlease select another image."))
				os.system("echo \"--Stars in this image probably are not exist.\">>log.my")
				self.AlignRm()
				self.ui.label_30.setPixmap(QtGui.QPixmap(""))
			self.ui.widget.setEnabled(True)
			QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
#displaying image for photometry
  def DisplayImage(self):
	  QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
	  self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Please wait. Choosing stars...", None, QtGui.QApplication.UnicodeUTF8))
	  h=self.ui.label_30.height()
	  w=self.ui.label_30.width()
	  a=self.ui.listWidget.currentItem()
	  self.copyFits(str(a.text()),"./tmp/")
	  res=a.text()
	  say = res.count("/")
	  imgname=res.split("/")
	  os.system("mv ./tmp/" + str(imgname[say]) + " ./tmp/display.fit")
	  os.system(str("convert -normalize -resize " + str(w) + "x" + str(h) + " ./tmp/display.fit ./tmp/display.png"))
	  self.ui.label_30.setPixmap(QtGui.QPixmap("./tmp/display.png"))

	  self.ui.label_30.setEnabled(True)
	  
	  
	  if self.ui.checkBoxAlign.checkState() == QtCore.Qt.Checked:
		  self.ui.widget.setEnabled(False)
		  QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		  images_to_align = sorted(glob.glob("./tmp/display.fit"))
		  ref_image = "./tmp/display.fit"
		  try:
			identifications = alipy.ident.run(ref_image, images_to_align, visu=True)
							
			for id in identifications:
			  if id.ok == True:
				  print "%20s : %20s, flux ratio %.2f" % (id.ukn.name, id.trans, id.medfluxratio)
				  
			h=self.ui.label_30.height()
			w=self.ui.label_30.width()
			os.system(str("convert -normalize -resize " + str(w) + "x" + str(h) + " ./alipy_visu/display_stars.png ./tmp/display.png"))
			self.ui.label_30.setPixmap(QtGui.QPixmap("./tmp/display.png"))
			self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Process done.", None, QtGui.QApplication.UnicodeUTF8))
		  except:
			self.ui.checkBoxAlign.setChecked(False)
			
			QtGui.QMessageBox.critical( self,  ("Error"), ("Image is not usable. It will be removed from list.\nPlease select another image."))
			self.AlignRm()
			self.ui.label_30.setPixmap(QtGui.QPixmap(""))
	
		  self.ui.widget.setEnabled(True)
			
	  QtGui.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
	  self.ui.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Process done.", None, QtGui.QApplication.UnicodeUTF8))
	  
###################
	
	
app = QtGui.QApplication(sys.argv)
f = MyForm()
f.show()
app.exec_()
