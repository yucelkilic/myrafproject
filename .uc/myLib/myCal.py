# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
MYRaf FIT/FITS Module.
Note that all modules with name started by 'my' such as myFit, myEnv are MYRaf's third party modules.
For further information:

	From myLib import myFit
	help(myFit)
"""

import myEnv
import myFit

class cOP():
	"""
	cOP stands for CALIBRATION OPERATIONS.
	This class contains functions to hanlding header of FIT/FITS files.
	"""
	__all__ = ["__init__"]

	def __init__(self, verb=False):
		"""
		__init__(self, verb=False) -> None
		Initial function. Welcome the user.
		
		@param verb: Get information while operations (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		self.envos = myEnv.oOP(verb=verb)
		self.fitdata = myFit.dOP(verb=verb)
		self.fitstat = myFit.sOP(verb=verb)
		self.fithead = myFit.hOP(verb=verb)
		
		if verb:
			print "Welcome to data Operation class of myFit."

	def combine(self, inFiles, oFile, method, rejection, skp=True, verb=False):
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
		self.fitstat.imcom(inFiles, method, rejection, oFile, skp=skp, verb=verb)
		
	def zerocombine(self, inFiles, oFile, method, rejection, ccdType=[], skp=True, verb=False):
		"""
		zerocombine(self, inFiles, oFile, method, rejection, verb=verb) -> None
		Creates a combine of a list of zero images.
		
		@param inFiles: List of input files name.
		@type inFiles: string
		@param oFile: Path for output file.
		@type oFile: string
		@param method: Combine type. 'MEDIAN', 'AVERAGE'.
		@type method: string
		@param rejection: Rejection type. 'MINMAX' or 'NONE'.
		@type rejection: string
		@param ccdType: Looks for a value in given header to decide to use the image or not.
		@type ccdType: list
		@param skp: Skip files not exist.
		@type skp: boolean (Optional, False by True)
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		if ccdType == []:
			self.fitstat.imcom(inFiles, method, rejection, oFile, skp=skp, verb=verb)
		else:
			if type(ccdType) == list:
				if len(ccdType) == 2:
					lst = []
					for i in inFiles:
						if ccdType[1] == self.fithead.imhead(i, key=ccdType[0])[1]:
							lst.append(i)
					if "MEDIAN".startswith(method.upper()) or "AVERAGE".startswith(method.upper()):
						self.fitstat.imcom(lst, method, rejection, oFile, skp=False, verb=verb)
					else:
						if verb:
							print "Unknown combine type:%s" %(method)
				else:
					if verb:
						print "ccdType have to contein ['keyname', 'key Value']."
			else:
				if verb:
					print "Unexpected input type for ccdType value. Array expected. Received: %s" %(type(ccdType))
