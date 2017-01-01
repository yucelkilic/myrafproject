# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
MYRaf FIT/FITS Module.
Note that all modules with name started by 'my' such as myFit, myEnv are MYRaf's third party modules.
For further information:

	from myraflib import myCal
	help(myCal)
"""

import myEnv
import myFit

envos = myEnv.oOP()
fitdata = myFit.dOP()
fitstat = myFit.sOP()
fithead = myFit.hOP()

__all__ = ["combine", "zerocombine"]

def combine(inFiles, oFile, method, rejection, skp=True, verb=False):
	"""
	combine(self, inFiles, oFile, method, rejection, verb=verb) -> None
	Creates a combine of a list of images.
	
	@param inFiles: List of input files name.
	@type inFiles: string
	@param oFile: Path for output file.
	@type oFile: string
	@param method: Combine type. 'MEDIAN', 'AVERAGE', 'SUM', 'MEAN', 'EXTRACT'.
	@type method: string
	@param rejection: Rejection type. 'MINMAX' or 'NONE'.
	@type rejection: string
	@param skp: Skip files not exist.
	@type skp: boolean (Optional, False by True)
	@param verb: Get information while operation (Optional, False by default).
	@type verb: boolean
	@return: None
	"""
	fitstat.imcom(inFiles, method, rejection, oFile, skp=skp, verb=verb)

def hreject(inFiles, head, verb=False):
	if type(inFiles) == list:
		if type(head) == list:
			if len(head) == 2:
				lst = []
				for i in inFiles:
					if len(fithead.imhead(i, key=head[0])) == 2:
						if head[1] == fithead.imhead(i, key=head[0])[1]:
							lst.append(i)
				return lst
			else:
				if verb:
					print "head have to be 1D with 2 elements. Got %s element(s)" %(len(head))
		else:
			if verb:
				print "Unexpected input type for head value. Array expected. Received: %s" %(type(head))
	else:
		if verb:
			print "Unexpected input type for inFiles value. Array expected. Received: %s" %(type(inFiles))

def zerocombine(inFiles, oFile, method, rejection, ccdType=[], skp=True, verb=False):
	"""
	zerocombine(self, inFiles, oFile, method, rejection, verb=verb) -> None
	Creates a combine of a list of zero images.
	
	@param inFiles: List of input files name.
	@type inFiles: list
	@param oFile: Path for output file.
	@type oFile: string
	@param method: Combine type. 'MEDIAN', 'AVERAGE'.
	@type method: string
	@param rejection: Rejection type. 'MINMAX' or 'NONE'.
	@type rejection: string
	@param ccdType: Looks for a value in given header for Image Type to decide to use the image or not. skp will be activated with this option.
	@type ccdType: list
	@param skp: Skip not existing input files (Optional, True by default).
	@type skp: boolean
	@param verb: Get information while operation (Optional, False by default).
	@type verb: boolean
	@return: None
	"""
	if ccdType == []:
		fitstat.imcom(inFiles, method, rejection, None, oFile, skp=skp, verb=verb)
	else:
		
		lst = hreject(inFiles, ccdType, verb=False)
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, None, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."

def flatcombine(inFiles, oFile, method, rejection, ccdType=[], subset=[], skp=True, verb=False):
	"""
	flatcombine(inFiles, oFile, method, rejection, verb=verb) -> None
	Creates a combine of a list of flat images.
	
	@param inFiles: List of input files name.
	@type inFiles: list
	@param oFile: Path for output file.
	@type oFile: string
	@param method: Combine type. 'MEDIAN', 'AVERAGE'.
	@type method: string
	@param rejection: Rejection type. 'MINMAX' or 'NONE'.
	@type rejection: string
	@param ccdType: Looks for a value in given header for Image Type to decide to use the image or not. skp will be activated with this option.
	@type ccdType: list
	@param subset: Looks for a value in given header for Filter Value to decide to use the image or not. skp will be activated with this option.
	@type subset: list
	@param skp: Skip not existing input files (Optional, True by default).
	@type skp: boolean
	@param verb: Get information while operation (Optional, False by default).
	@type verb: boolean
	@return: None
	"""
	if ccdType == [] and subset == []:
		fitstat.imcom(inFiles, method, rejection, None, oFile, skp=skp, verb=verb)
		
	elif ccdType != [] and subset == []:
		lst = hreject(inFiles, ccdType, verb=verb)
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, None, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."
				
	elif ccdType == [] and subset != []:
		lst = hreject(inFiles, subset, verb=verb)
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, None, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."
				
	else:
		lst = hreject(inFiles, ccdType, verb=verb)
		print lst
		lst = hreject(lst, subset, verb=verb)
		print lst
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, None, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."


def darkcombine(inFiles, oFile, method, rejection, ccdType=[], scale=None, skp=True, verb=False):
	"""
	darkcombine(inFiles, oFile, method, rejection, verb=verb) -> None
	Creates a combine of a list of dark images.
	
	@param inFiles: List of input files name.
	@type inFiles: list
	@param oFile: Path for output file.
	@type oFile: string
	@param method: Combine type. 'MEDIAN', 'AVERAGE'.
	@type method: string
	@param rejection: Rejection type. 'MINMAX' or 'NONE'.
	@type rejection: string
	@param ccdType: Looks for a value in given header for Image Type to decide to use the image or not. skp will be activated with this option.
	@type ccdType: list
	@param scale: Scale with exposure time with given card (Optional, True by default).
	@type scale: None or string
	@param skp: Skip not existing input files (Optional, True by default).
	@type skp: boolean
	@param verb: Get information while operation (Optional, False by default).
	@type verb: boolean
	@return: None
	"""
	if ccdType == [] and subset == []:
		if scale == None or type(scale) == str:
			fitstat.imcom(inFiles, method, rejection, scale, oFile, skp=skp, verb=verb)
		else:
			if verb:
				print "scale must be None or string."
		
	elif ccdType != [] and subset == []:
		lst = hreject(inFiles, ccdType, verb=verb)
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, scale, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."
				
	elif ccdType == [] and subset != []:
		lst = hreject(inFiles, subset, verb=verb)
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, scale, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."
				
	else:
		lst = hreject(inFiles, ccdType, verb=verb)
		print lst
		lst = hreject(lst, subset, verb=verb)
		print lst
		if len(lst) !=0:					
			if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
				fitstat.imcom(lst, method, rejection, scale, oFile, skp=False, verb=verb)
			else:
				if verb:
					print "Unknown combine type:%s" %(method)
		else:
			if verb:
				print "All input files rejected. Check ccdType and try again."
