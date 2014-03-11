import os, datetime, ntpath, alipy, glob
from pyraf import iraf
from pyraf.iraf import noao, imred, ccdred, darkcombine, flatcombine, ccdproc ,astutil, setjd, setairmass, asthedit, digiphot, apphot, phot, ptools, txdump, artdata, imgeom
from astropy.time import Time
from time import gmtime, strftime


def readResultFile(filename,  starID, apIndex):
    try:
        os.popen("cat %s |awk '{if ($1 == %s) print $1, $2, $%s}' > tmp/idjdmag_%s.my" %(filename, starID, apIndex, starID))
        print "Result file is succesfuly read."
        return True
    except:
        print "Result file did not read"
        return False
        
def headerRead(filename, field):
	res = iraf.hedit(filename, field, ".", Stdout=1)
	if res != []:
		res = res[0]
		return res.split("=")[1].replace(" ","")
	else:
		return ""
	
def headerWrite(filename, field, text):
	try:
		hd= iraf.images.imutil.hedit
		hd (filename, field, text, add="yes", verify="no", show="no", update="yes")
		return True
		print("Hedit succeed")
	except:
		return False
		print("Hedit failed")
	
def headerDel(filename, field):
	try:
		hd= iraf.images.imutil.hedit
		hd (filename, field, delete="yes", verify="no", show="no")
		return True
		print("Hedit succeed")
	except:
		return False
		print("Hedit failed")
		
def zeroCombine(fileList, out, com="median", rej="none", cty=""):
	zc = iraf.noao.imred.ccdred.zerocombine
	zc.input = "@%s" %(fileList)
	zc.output = out
	zc.combine = com
	zc.reject = rej
	zc.ccdtype = cty
	zc.process = "no"
	try:
		zc._runCode()
		print("zerocombine succeed.")
		return True
	except:
		print("zerocombine failed.")
		return False

def darkCombine(fileList, out, com="median", rej="none", cty="", scl="exposure"):
	dc = iraf.noao.imred.ccdred.darkcombine
	dc.input = "@%s" %(fileList)
	dc.output = out
	dc.combine = com
	dc.reject = rej
	dc.ccdtype = cty
	dc.scale = scl
	dc.process = "no"
	try:
		dc._runCode()
		print("darkcombine succeed.")
		return True
	except:
		print("darkcombine failed.")
		return False

def flatCombine(fileList, out, com="median", rej="none", cty="", sub="yes"):
	fc = iraf.noao.imred.ccdred.flatcombine
	fc.input = "@%s" %(fileList)
	fc.output = "%s/flat_" %(out)
	fc.process = "no"
	fc.combine = com
	fc.reject = rej
	fc.ccdtype = cty
	fc.subsets = sub
	try:
		fc	._runCode()
		print("flatcombine succeed.")
		return True
	except:
		print("flatcombine failed.")
		return False

def calibration(image, bias, dark, flat, odir, cty="", sub="yes"):

	if sub =="no":
		headerWrite(image, "tmp", headerRead(image, "SUBSET"))
		headerWrite(image, "SUBSET", "MYRAF")
		headerWrite(flat, "tmp", headerRead(flat, "SUBSET"))		
		headerWrite(flat, "SUBSET", "MYRAF")

	bia, dar, fla = "yes", "yes", "yes"
	if bias == "": bia = "no"
	if dark == "": dar = "no"
	if flat == "": fla = "no"
	bia2="%s(%s)" %(bia, bias)
	dar2="%s(%s)" %(dar, dark)
	fla2="%s(%s)" %(fla, flat)
	print("Starting Calibration:Image=%s Bias=%s, Dark=%s, Flat=%s" %(ntpath.basename(str(image)), bia2, dar2, fla2))
	cp = iraf.noao.imred.ccdred.ccdproc
	cp.images = str(image)
	cp.output = "%s/%s" %(str(odir), ntpath.basename(str(image)))
	cp.ccdtype = cty
	cp.fixpix = "no"
	cp.overscan = "no"
	cp.trim = "no"
	cp.zerocor = bia
	cp.darkcor = dar
	cp.flatcor = fla
	cp.zero = bias
	cp.dark = dark
	cp.flat = flat

	cp(images = str(image))
	headerWrite("%s/%s" %(str(odir), ntpath.basename(str(image))), "MYRafCAL", "Calibrated Via MYRaf V2.0 Beta @ %s" %(datetime.datetime.utcnow()))
	print("Calibration succeed.")
	
	if sub =="no":
		print "Geri gel" 
		headerWrite(image, "SUBSET", headerRead(image, "tmp"))
		headerDel(image, "tmp")
		headerWrite("%s/%s" %(odir, ntpath.basename(str(image))), "SUBSET", headerRead("%s/%s" %(odir, ntpath.basename(str(image))), "tmp"))
		headerDel("%s/%s" %(odir, ntpath.basename(str(image))), "tmp")
		headerWrite(flat, "SUBSET", headerRead(flat, "tmp"))
		headerDel(flat, "tmp")
		
	return True

		
def fits2png(inFile, outFile):
	try:
		os.popen("convert -normalize %s %s" %(inFile, outFile))			
		print("Conversion succeed.")
		return True
	except:
		print("Conversion failed.")
		return False

def autoAlign(inFile, refImage, outFile, mkPNG=False, visu=False):
	print("image = %s, ref = %s " %(inFile, refImage))
	mkh=iraf.artdata.mkheader
	directory = os.path.dirname("./alipy_out/")
	if not os.path.exists(directory):
		os.popen("rm -rf ./alipy_out/")
	try:
		images_to_align = sorted(glob.glob(inFile))
		ref_image = refImage
		identifications = alipy.ident.run(ref_image, images_to_align, visu=visu)
		outputshape = alipy.align.shape(ref_image)
		for id in identifications:
			if id.ok == True:
				print "%20s : %20s, flux ratio %.2f" % (id.ukn.name, id.trans, id.medfluxratio)
				alipy.align.affineremap(id.ukn.filepath, id.trans, shape=outputshape, makepng=mkPNG)
				
		alipy_out = "./alipy_out/%s_affineremap.fits" %(ntpath.basename(str(inFile)).split(".")[0])
		mkh(alipy_out, inFile)
		headerWrite(alipy_out, "MYRafALI", "Aligned Via MYRaf V2.0 Beta using Alipy @ %s" %(datetime.datetime.utcnow()))
		os.popen("mv %s %s/%s" %(alipy_out, outFile, ntpath.basename(str(inFile))))
		print("alipy succeed.")
		return True
	except:
		print("alipy failed.")
		return False
		
def manAlign(inFile, x, y, outFile):
	imsh = iraf.images.imgeom.imshift
	try:
		print("%s image will align via x:%s y:%s" %(ntpath.basename(str(inFile)), x, y))
		imsh (inFile, outFile, int(x), int(y))
		return True
	except:
		return False

def JD(inFile, OBS, date="date-obs", time = "time-obs", r="ra", d = "dec", epo="epoch", expTime="exptime"):
	print("JD calculation for %s image" %(ntpath.basename(str(inFile))))
	print("JD F(%s) OBSERVAT(%s) DATE(%s) TIME(%s) Ra(%s) Dec(%s) Epo(%s) Exp(%s)" %(inFile, OBS, date, time, r, d, epo, expTime))
	try:
		sd = iraf.noao.astutil.setjd
		sd (inFile, observatory = str(OBS), date=date, time = time, ra=r, dec=d, epoch=epo, exposur=expTime, jd="jd", hjd="hjd", ljd="ljd")
		return True
		print("JD succeed.")
	except:
		return False
		print("JD failed.")
		
def epoch(inFile, date, time):
	t = Time(strftime('%s %s'  %(headerRead(inFile, date), headerRead(inFile, time))), format='iso', scale='utc')
	return t.byear
	
def sideReal(inFile, OBS, date, time):
	print("sidereal time calculation for %s image" %(ntpath.basename(str(inFile))))
	try:
		os.system('echo astcalc > ./tmp/st.cl')
		os.system("echo \"	observatory=\\\"%s\\\"\" >> ./tmp/st.cl" %(OBS))
		os.system("echo \"	st=mst(@'%s',@'%s',obsdb(observatory,\\\"longitude\\\"))\" >> ./tmp/st.cl" %(date, time))
		os.system("echo quit >> ./tmp/st.cl")
		at = iraf.noao.astutil.asthedit
		at(inFile, commands = "./tmp/st.cl", update = "yes", verbose = "yes")
		os.popen("rm -rf ./tmp/st.cl")
		return True
		print("Sidereal calculator succeed.")
	except:
		return False
		print("Sidereal calculator failed.")
		

def airmass(inFile, OBS="observat", r="ra", d="dec", equ="epoch", s="st", u="ut", dat="date", exp="exptime"):
	print("Setairmass for %s image" %(ntpath.basename(str(inFile))))
	try:
		sam = iraf.setairmass
		sam(inFile, observatory=OBS ,intype ="middle" ,outtype="effective", ra=r, dec=d, equinox=equ, st= s, ut=u, date=dat, exposur=exp)
		return True
		print("Setairmass succeed.")
	except:
		return False
		print("Setairmass failed.")

def phot(inFile, outPath, cooFile, expTime = "exptime", Filter = "subset", centerBOX = "10.0", annulus = "25.0", dannulus = "5.0", apertur = "10,15,20,25,30", zmag = "25", airmass = "airmass", otime = "hjd"):
	print("setParam started via: \n\timg=%s \n\tOutfile=%s \n\tcooFile=%s \n\texpTime=%s \n\tFilter=%s \n\tcenterBOX=%s \n\tannulus=%s \n\tdannulus=%s \n\tapertur=%s \n\tzmag=%s \n\tairmass=%s \n\tobstime=%s" %(inFile, outPath, cooFile, expTime, Filter, centerBOX, annulus, dannulus, apertur, zmag, airmass, otime))
	try:
		iraf.datapars.setParam("exposur", expTime)
		iraf.datapars.setParam("filter", Filter)
		iraf.datapars.setParam("airmass", airmass)
		iraf.datapars.setParam("obstime", otime)
		iraf.datapars.saveParList(filename="./uparm/aptdataps.par")
		
		iraf.centerpars.setParam("cbox", centerBOX)
		iraf.centerpars.saveParList(filename="./uparm/aptcentes.par")
		
		iraf.fitskypars.setParam("annulus", annulus)
		iraf.fitskypars.setParam("dannulus", dannulus)
		iraf.fitskypars.saveParList(filename="./uparm/aptfitsks.par")
		
		iraf.photpars.setParam("apertur", apertur)
		iraf.photpars.setParam("zmag", zmag)
		iraf.photpars.saveParList(filename="./uparm/aptphot.par")
		
		pt = iraf.phot
		pt(inFile, coords =  cooFile, output = outPath , interac = "no", verify = "no", Stdout=1)

		return True
		print("setParam succeed.")
	except:
		return False
		print("setParam failed.")

def txDump(inFile, outFile, fields="id, otime, mag , merr, xairmass"):
	print("txDump started.")
	print inFile
	try:
		tx=iraf.txdump
		tx (inFile, fields, "yes", Stdout= outFile)
		return True
		print("txDump succeed.")
	except:
		return False
		print("txDump failed.")
