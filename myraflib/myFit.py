# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
MYRaf FIT/FITS Module.
Note that all modules with name started by 'my' such as myFit, myEnv are MYRaf's third party modules.
For further information:

	From myraflib import myFit
	help(myFit)
"""

import myEnv
import pyfits
import numpy
import itertools

__all__ = ["dOP", "hOP", "sOP"]
class hOP():
	"""
	hOP stands for HEADER OPERATIONS.
	This class contains functions to hanlding header of FIT/FITS files.
	"""
	__all__ = ["__init__", "hopen", "hcopy", "hcount", "hdel", "hedit", "hlist", "hopen", "hupdate", "imhead", "imheadARR", "imeahINT", "imheadSTR"]
	
	def __init__(self, verb=False):
		"""
		__init__(self, verb=False) -> None
		Initial function. Welcome the user.
	
		@param verb: Get information while operations (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		self.envos = myEnv.oOP()
		self.sOP = sOP()
		if verb:
			print "Welcome to Header Operation class of myFit."
			
	def hopen(self, fileName, met, verb=False):
		"""
		hopen(self, fileName, met, verb=False) -> HDU
		Opens a FIT/FITS file.
		
		@param fileName: Input file path.
		@type fileName: string
		@param met: Mode for file to open. 'copyonwrite', 'readonly', 'update', 'append', or 'ostream'.
		@type met: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: HDU
		"""
		if self.envos.isFile(fileName, verb=verb):
			try:
				img = pyfits.open(fileName, mode=met)
				return img
			except:
				if verb:
					print "%s: Corrupted file." %(fileName)
		else:
			if verb:
				print "No such file."

	def hlist(self, fileName, verb=False):
		"""
		hlist(self, fileName, verb=False) -> list
		Returns a list of header keys.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		img = self.hopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			h = img[0].header
			img.close()
			if verb:
				print "'hlist' done."
			return h.keys()
	
	def hcount(self, fileName, verb=False):
		"""
		hcount(self, fileName, verb=False) -> list
		Returns count of header keys.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		if type(self.hlist(fileName, verb=verb)) == list:
			if verb:
				print "'hcound' done."
			return len(self.hlist(fileName, verb=verb))
			
	def imheadSTR(self, fileName, key, verb=False):
		"""
		imheadSTR(self, fileName, key, verb=False) -> list
		Returns header name and value for given header name.
	
		@param fileName: Input file path.
		@type fileName: string
		@param key: Value for wanted card name.
		@type key: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		if type(key) == str:
			img = self.hopen(fileName, "readonly", verb=verb)
			if type(img) == pyfits.hdu.hdulist.HDUList:
				if key in img[0].header:
					hd = [key, img[0].header[key]]
				else:
					hd = [key, "Err"]
				if verb:
					print "'imheadSTR' done."
				img.close()
				return hd
		else:
			if verb:
				print "Unexpected input type for key value.\nString expected.\nReceived %s" %(type(key))
			
	def imheadINT(self, fileName, key, verb=False):
		"""
		imheadINT(self, fileName, key, verb=False) -> list
		Returns header name and value for given header ordery.
		
		@param fileName: Input file path.
		@type fileName: string
		@param key: Value for wanted card order.
		@type key: integer
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		if type(key) == int:
			img = self.hopen(fileName, "readonly", verb=verb)
			if type(img) == pyfits.hdu.hdulist.HDUList:
				if key < self.hcount(fileName, verb=verb) and key >= 0:
					hd = [self.hlist(fileName, verb=verb)[key], img[0].header[key]]
				else:
					if str(key)[-1] == "1":
						tail = "st"
					elif str(key)[-1] == "2":
						tail = "nd"
					elif str(key)[-1] == "3":
						tail = "rd"
					else:
						tail = "th"
					hd = ["%s%s" %(str(key), tail), "Err"]
				if verb:
					print "'imheadINT' done."
				img.close()
				return hd
		else:
			if verb:
				print "Unexpected input type for key value.\nInteger expected.\nReceived %s" %(type(key))
			
	def imheadARR(self, fileName, key, verb=False):
		"""
		imheadARR(self, fileName, key, verb=False) -> list
		Returns header names and values for given header orders or names.
		
		@param fileName: Input file path.
		@type fileName: string
		@param key: Values for wanted cards.
		@type key: list
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		if type(key) == list:
			hd = []
			for i in key:
				if type(i) == str:
					he = self.imheadSTR(fileName, i, verb=verb)
					if type(he) == list:
						hd.append(he)
				elif type(i) == int:
					he = self.imheadINT(fileName, i, verb=verb)
					if type(he):
						hd.append(he)
			if verb:
				print "'imheadARR' done."
			return hd
		else:
			if verb:
				print "Unexpected input type for key value.\nArray expected.\nReceived %s" %(type(key))
			
	def imhead(self, fileName, key="i", verb=False):
		"""
		imhead(self, fileName, key="i", verb=False) -> list
		Resultant of imheadSTR, imheadINT and imheadARR.
		
		@param fileName: Input file path.
		@type fileName: string
		@param key: Value for name or order or both of name and order. 'i': For short description. '*': For whole headers cards.
		@type key: string, integer or list
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		if self.envos.isFile(fileName):
			hd = []
			if key == "i":
				sh = self.sOP.shape("../../d/2.fit")
				if type(sh) == tuple:
					hd.append([fileName, sh])
					if verb:
						print "'imhead' done."
				else:
					hd.append(["Err","Err"])
			
			if key == "*":
				hl = self.hlist(fileName)
				if type(hl) == list:
					for i in hl:
						if i != "":
							hd.append(self.imheadSTR(fileName, i, verb=verb))
					return hd
					if verb:
						print "'imhead' done."
						
			if type(key) == str and key != "i" and key != "*":
				hd = self.imheadSTR(fileName, key, verb=verb)
				if verb:
					print "'imhead' done."	
				return hd

			elif type(key) == int:
				hd = self.imheadINT(fileName, key, verb=verb)
				if verb:
					print "'imhead' done."	
				return hd

			elif type(key) == list:
				hd = self.imheadARR(fileName, key, verb=verb)
				if verb:
					print "'imhead' done."	

				return hd
				if verb:
					print "'imhead' done."	
			else:
				if verb:
					print "Unexpected input type for key value.\nString, Integer or Array expected.\nReceived %s" %(type(key))
		else:
			if verb:
				print "%s: No such file." %(fileName)
			return []
		
	def hedit(self, fileName, key, value, comm="", upd=False, verb=False):
		"""
		hedit(self, fileName, key, value, comm="", upd=False, verb=False) -> list
		Creates a field, adds a value and adds a comment (optionally) by given arguments.
				
		@param fileName: Input file path.
		@type fileName: string
		@param key: Name or order of a card to add.
		@type key: string, integer
		@param value: New value for card.
		@type value: boolean, integer or string
		@param comm: Value for comment (Optional, "" by default).
		@type comm: string
		@param upd: Value for Update if card exist (Optional).
		@type upd: boolean
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		if type(key) == str:
			img = self.hopen(fileName, "update", verb=verb)
			if type(img) == pyfits.hdu.hdulist.HDUList:
				if len(key) > 8:
					if verb:
						print "lenght of a key value can't be more than 8 characters. Going to use first 8 characters. Thus field name will be '%s'" %(key[:8])
					key = key[:8]
				if value == True:
					value = 'T'
				elif value == False:
					value = 'F'
				h = img[0].header
				if key in h:
					if verb:
						print "'%s' feild does exist." %(key)
					if upd:
						if verb:
							print "Going to update it."
						self.hupdate(key, value, comm=str(comm), verb=verb)
				else:
					h.append((key, value, str(comm)), end=False)
				if verb:
					print "'hedit' done."
				img.flush()
				img.close()
		else:
			if verb:
				print "Unexpected input type for key value.\nString expected.\nReceived %s" %(type(key))
			
	def hupdate(self, fileName, key, value, comm="", add=False, verb=False):
		"""
		hupdate(self, fileName, key, value, comm="", add=False, verb=False) -> None
		Updates a fields value in image header by field name as STRING or field order as INTEGER.
		
		@param fileName: Input file path.
		@type fileName: string
		@param key: Name or order of a card to update.
		@type key: integer or string
		@param value: Value for card tobe update.
		@type value: string, integer or boolean
		@param comm: Value for comment for card tobe updaate(Optional, "" by default).
		@type comm: string
		@param add: Value for add if card don't exist (Optional).
		@type add: boolean
		@param verb: Get information while operation.
		@type verb: boolean
		@return: None
		"""
		img = self.hopen(fileName, "update", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			h = img[0].header
			if type(key) == str:
				if len(key) > 8:
					if verb:
						print "lenght of a key value can't be more than 8 characters.\nGoing to use first 8 characters. Thus field name will be '%s'" %(key[:8])
					key = key[:8]
				if key in h:
					h[str(key)] = (value, str(comm))
					if verb:
						print "'hupdate' done."
					img.flush()
					img.close()
				else:
					if verb:
						print "No such header field"
					if add:
						if verb:
							print "Going to add it."
						self.hedit(fileName, key, value, comm=str(comm), verb=verb)
						if verb:
							print "'hupdate' done."
						img.flush()
						img.close()
			elif type(key) == int:
				if self.hcount(fileName, verb=verb) <= key or key < 0:
					if verb:
						print "Field number is [0, %s]" %(self.hcount()-1)
				else:
					h[int(key)] = (value, str(comm))
					if verb:
						print "'hupdate' done."
					img.flush()
					img.close()
		else:
			if verb:
				print "Unexpected input type for key value.\nString or Integer expected.\nReceived %s" %(type(key))

	def hdel(self, fileName, key, verb=False):
		"""
		hdel(self, fileName, key, verb=False) -> None
		Deletes a fieldsin image header by field name as STRING or field order as INTEGER.
				
		@param fileName: Input file path.
		@type fileName: string
		@param key: Name or order of card to delete.
		@type key: string or integer.
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		img = self.hopen(fileName, "update", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			h = img[0].header
			if type(key) == str:
				if len(key) > 8:
					if verb:
						print "lenght of a key value can't be more than 8 characters.\nGoing to use first 8 characters. Thus field name will be '%s'" %(key[:8])
					key = key[:8]
				if key in h:
					del h[str(key)]
					if verb:
						print "'hdel' done."
					img.flush()
					img.close()
				else:
					print "No such field"
			elif type(key) == int:
				if self.hcount(fileName, verb=verb) <= key or key < 0:
					if verb:
						print "Field number is [0, %s]" %(self.hcount(fileName, verb=verb)-1)
				else:
					del h[int(key)]
					if verb:
						print "'hdel' done."
					img.flush()
					img.close()
		else:
			if verb:
				print "Unexpected input type for key value.\nString or Integer expected.\nReceived %s" %(type(key))

	def hcopy(self, inFileName, tarFileName, verb=False):
		"""
		hcopy(self, inFileName, tarFileName, verb=False) -> None
		Copies whole header from a file to another.
				
		@param inFileName: Input file to copy header from.
		@type inFileName: string
		@param tarFileName: Target file to copy header to.
		@type tarFileName: string.
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		imgI = self.hopen(inFileName, "readonly", verb=verb)
		if type(imgI) == pyfits.hdu.hdulist.HDUList:
			hI = imgI[0].header
			for i in hI:
				ht = self.imheadSTR(inFileName, i)
				self.hupdate(tarFileName, self.imheadSTR(inFileName, i)[0], self.imheadSTR(inFileName, i)[1])

class sOP():
	"""
	sOP stands for STATISTICAL OPERATIONS.
	This class contains functions for FIT/FITS files.
	"""
	__all__ = ["__init__", "sopen", "ave", "imave", "imcom", "immean", "immed", "imsub", "imsum", "max", "mean", "median", "min", "minmaxrej", "shape", "stat", "stddv"]
	
	def __init__(self, verb=False):
		"""
		__init__(self, verb=False) -> None
		Initial function. Welcome the user.
	
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		self.envos = myEnv.oOP()
		if verb:
			print "Welcome to statistical Operations class of myFit.."

	def sopen(self, fileName, met, verb=False):
		"""
		sopen(self, fileName, met, verb=False) -> HDU
		Opens a FIT/FITS file.
		
		@param fileName: Input file path.
		@type fileName: string
		@param met: Mode for file to open. 'copyonwrite', 'readonly', 'update', 'append', or 'ostream'.
		@type met: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: HDU
		"""
		if self.envos.isFile(fileName, verb=verb):
			try:
				img = pyfits.open(fileName, mode=met)
				return img
			except:
				if verb:
					print "%s: Corrupted file." %(fileName)
		else:
			if verb:
				print "No such file."

	def stat(self, fileName, verb=False):
		"""
		stat(self, fileName, verb=False) -> list
		Returns statistical informations for given fits file.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			st = [['Image', fileName], ['Shape', self.shape("a.fit", verb=verb)], ['Mean', self.mean("a.fit", verb=verb)], ['STDDEV', self.stddv("a.fit", verb=verb)], ['MIN', self.min("a.fit", verb=verb)], ['MAX', self.max("a.fit", verb=verb)]]
			if verb:
				print "'imstat' done."
			img.close()
			return st
		
	def shape(self, fileName, verb=False):
		"""
		shape(self, fileName, verb=False) -> list
		Returns shape of a given image as array.
				
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: list
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			data = img[0].data
			if verb:
				print "'imshape' done."
			img.close()
			return data.shape

	def ave(self, fileName, verb=False):
		"""
		ave(self, fileName, verb=False) -> integer
		Returns average vale of all counts on image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: integer
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			ave = numpy.average(img[0].data)
			if verb:
				print "'imave' done."
			img.close()
			return ave

	def mean(self, fileName, verb=False):
		"""
		mean(self, fileName, verb=False) -> integer
		Returns mean vale of all counts on image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: integer
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			mea = img[0].data.mean()
			if verb:
				print "'immean' done."
			img.close()
			return mea

	def min(self, fileName, verb=False):
		"""
		min(self, fileName, verb=False) -> integer
		Returns minimum vale of all counts on image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: integer
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			mini = img[0].data.min()
			if verb:
				print "'immin' done."
			img.close()
			return mini

	def max(self, fileName, verb=False):
		"""
		max(self, fileName, verb=False) -> integer
		Returns maximum vale of all counts on image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: integer
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			maxi = img[0].data.max()
			if verb:
				print "'immax' done."
			img.close()
			return maxi
		
	def stddv(self, fileName, verb=False):
		"""
		stddv(self, fileName, verb=False) -> integer
		Returns standard deviation vale of all counts on image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: integer
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			stddv = img[0].data.std()
			if verb:
				print "'imstddv' done."
			img.close()
			return stddv

	def median(self, fileName, verb=False):
		"""
		median(self, fileName, verb=False) -> integer
		Returns median vale of all counts on image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: integer
		"""
		img = self.sopen(fileName, "readonly", verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			stddv = numpy.median(img[0].data)
			if verb:
				print "'immedian' done."
			img.close()
			return stddv


	def minmaxrej(self, inArray, verb=False):
		"""
		minmaxrej(self, inArray, verb=False) -> numpy.ndarray
		Returns all images minmax rejected.
		
		@param inArray: All arrays to reject minmax. It'll return a reverced array.
		@type inArray: numpy.ndarray
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: numpy.ndarray
		"""
		if type(inArray) == numpy.ndarray:
			if len(inArray.shape) == 3:
				if inArray.shape[0] > 2:
					poi = []
					ln = []
					lst = []
					
					for i in xrange(inArray.shape[1]):
						for u in xrange(inArray.shape[2]):
							for k in xrange(inArray.shape[0]):
								poi.append(inArray[k][i][u])
							poi = numpy.sort(poi)
							ln.append(poi)
							poi = []
						lst.append(ln)
						ln = []
					lst = numpy.asarray(lst)
					if verb:
						print "'minmaxrej' done."
					return lst
					
				else:
					if verb:
						print "Min-Max rejection requires at least 3 arrays. Got %s." %(inArray.shape[0])
			else:
				if verb:
					print "Wrong array shape. Expected array type: %s" %(inArray.shape)
		else:
			if verb:
				print "Unexpected input type for input arrays.Array expected.Received %s" %(type(inArray))

	def immed(self, inArray, axis, verb=False):
		"""
		immed(self, inArray, axis, verb=False) -> numpy.ndarray
		Returns median of some arrays.
		
		@param inArray: A list of arrays.
		@type inArray: numpy.ndarray
		@param axis: Getting median using which axis. Can't be equal or larger than inArray's axis count.
		@type axis: integer
		@return: numpy.ndarray
		"""
		if type(inArray) == numpy.ndarray:
			if len(inArray.shape) > axis:
				if inArray.shape[axis] > 2:
					if verb:
						print "'immed' done."
					return numpy.median(inArray, axis)
				else:
					if verb:
						print "Median method needs at least three arrays."
			else:
				if verb:
					print "No such axis. Axis value can't be equal or larger than inArray dimensions."
		else:
			if verb:
				print "Unexpected input type for input arrays.numpy.array expected.Received %s" %(type(inArray))

	def imsum(self, inArray, axis, verb=False):
		"""
		imsum(self, inArray, axis, verb=False) -> numpy.ndarray
		Returns sum of some arrays.
		
		@param inArray: A list of arrays.
		@type inArray: numpy.ndarray
		@param axis: Getting sum using which axis. Can't be equal or larger than inArray's axis count.
		@type axis: integer
		@return: numpy.ndarray
		"""
		if type(inArray) == numpy.ndarray:
			if len(inArray) > axis:
				if verb:
					print "'immed' done."
				return numpy.sum(inArray, axis)
			else:
				if verb:
					print "No such axis. Axis value can't be equal or larger than inArray dimensions."
		else:
			if verb:
				print "Unexpected input type for input arrays.numpy.array expected.Received %s" %(type(inArray))

	def imave(self, inArray, axis, verb=False):
		"""
		imave(self, inArray, axis, verb=False) -> numpy.ndarray
		Returns average of some arrays.
		
		@param inArray: A list of arrays.
		@type inArray: numpy.ndarray
		@param axis: Getting average using which axis. Can't be equal or larger than inArray's axises count.
		@type axis: integer
		@return: numpy.ndarray
		"""
		if type(inArray) == numpy.ndarray:
			if len(inArray) > axis:
				if verb:
					print "'immed' done."
				return numpy.average(inArray, axis)
			else:
				if verb:
					print "No such axis. Axis value can't be equal or larger than inArray dimensions."
		else:
			if verb:
				print "Unexpected input type for input arrays.numpy.array expected.Received %s" %(type(inArray))

	def immean(self, inArray, axis, verb=False):
		"""
		immean(self, inArray, axis, verb=False) -> numpy.ndarray
		Returns mean of some arrays.
		
		@param inArray: A list of arrays.
		@type inArray: numpy.ndarray
		@param axis: Getting mean using which axis. Can't be equal or larger than inArray's axises count.
		@type axis: integer
		@return: numpy.ndarray
		"""
		return self.imave(inArray, axis, verb=verb)

	def imsub(self, inArray, verb=False):
		"""
		imsub(self, inArray, verb=False) -> numpy.ndarray
		Returns subtract of two arrays.
		
		@param inArray: A list of arrays.
		@type inArray: numpy.ndarray
		@return: numpy.ndarray
		"""
		if type(inArray) == numpy.ndarray:
			if inArray.shape[0] == 2:
				if verb:
					print "'immed' done."
				return numpy.subtract(inArray[0], inArray[1])
			else:
				if verb:
					print "Subtract method can process just two arrays at once."
		else:
			if verb:
				print "Unexpected input type for input arrays.numpy.array expected.Received %s" %(type(inArray))

	def imcom(self, fileList, method, rejection, outFile, skp=True, verb=False):
		"""
		imcom(self, fileList, method, rejection, outFile, skp=True, verb=False) -> None
		Creates a combine of a list of images.

		@param fileList: A list of whole images wanted to combine.
		@type fileList: list
		@param method: Combine type. 'MEDIAN', 'AVERAGE', 'SUM', 'MEAN', 'EXTRACT'.
		@type method: string
		@param rejection: Rejection type. 'MINMAX' or 'NONE'.
		@type rejection: string
		@param outFile: Name of output file.
		@type outFile: string
		@param skp: Skip not existing input files (Optional, True by default).
		@type skp: boolean
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None	
		"""
		if type(fileList) == list:
			lst = []
			ilst = []
			shp = []
			err = ""
			u = 0
			for  i in fileList:
				if not self.envos.isFile(i):
					u = u + 1
			if u == 0:
				afo = True
			else:
				afo = False
				
			if u != len(fileList):
				if skp:
					if afo:
						con = True
						lst = fileList
					else:
						for i in fileList:
							if self.envos.isFile(i):
								lst.append(i)
						con = True
				else:
					if afo:
						con = True
						lst = fileList
					else:
						con = False
						if verb:
							print "Some files are missing."
				
				if con:
					h = hOP()
					headers = h.imhead(lst[0], "*")
					for i in lst:
						ilst.append(self.sopen(i, "readonly", verb=verb)[0].data)
					ilst = numpy.asarray(ilst)
					
					for i in ilst:
						shp.append(i.shape)
					if len(set(shp)) == 1:

						if "SUM".startswith(method.upper()):
							if "MINMAX".startswith(rejection.upper()):
								fl = self.minmaxrej(ilst, verb=verb)
								im = self.imsum(fl, 2, verb=verb)
							elif "NONE".startswith(rejection.upper()):
								im = self.imsum(ilst, 0, verb=verb)
							else:
								err = "RejectFalse"
								if verb:
									print "%s:Unknown rejection method." %(rejection)
						elif "MEDIAN".startswith(method.upper()):
							if "MINMAX".startswith(rejection.upper()):
								fl = self.minmaxrej(ilst, verb=verb)
								im = self.immed(fl, 2, verb=verb)
							elif "NONE".startswith(rejection.upper()):
								im = self.immed(ilst, 0, verb=verb)
							else:
								err = "RejectFalse"
								if verb:
									print "%s:Unknown rejection method." %(rejection)
						elif "AVERAGE".startswith(method.upper()):
							if "MINMAX".startswith(rejection.upper()):
								fl = self.minmaxrej(ilst, verb=verb)
								im = self.imave(fl, 2, verb=verb)
							elif "NONE".startswith(rejection.upper()):
								im =self.imave(ilst, 0, verb=verb)
							else:
								err = "RejectFalse"
								if verb:
									print "%s:Unknown rejection method." %(rejection)
						elif "MEAN".startswith(method.upper()):
							if "MINMAX".startswith(rejection.upper()):
								fl = self.minmaxrej(ilst, verb=verb)
								im = self.immean(fl, 2, verb=verb)
							elif "NONE".startswith(rejection.upper()):
								im =self.immean(ilst, 0, verb=verb)
							else:
								err = "RejectFalse"
								if verb:
									print "%s:Unknown rejection method." %(rejection)

						elif "EXTRACT".startswith(method.upper()):
							if "MINMAX".startswith(rejection.upper()):
								err = "exFalse"
								if verb:
									print "Rejection not allowed with EXTRACTION."
							elif "NONE".startswith(rejection.upper()):
								im =self.imsub(ilst, verb=verb)
							else:
								err = "RejectFalse"
								if verb:
									print "%s:Unknown rejection method." %(rejection)

						else:
							err = "CombFalse"
							if verb:
								print "%s:Unknown combine method." %(method)
						
					else:
						if verb:
							print "Matrix of all images have to be same. Check images."
					
					if err == "":
						if verb:
							print "'imcom' done."
						
						d = dOP()
						d.imcreate(im, headers, outFile, overWrite=True, verb=verb)
						
			else:
				if verb:
					print "All input data are not found in disk. Check all paths and retry."
		else:
			if verb:
				print "Unexpected input type for file List.\nArray expected.\nReceived %s" %(type(fileList))

class dOP():
	"""
	dOP stands for DATA OPERATIONS.
	This class contains functions to hanlde data of FIT/FITS files.
	"""
	__all__ = ["__init__", "dopen", "imcreate", "imget"]

	def __init__(self, verb=False):
		"""
		__init__(self, verb=False) -> None
		Initial function. Welcome the user.
		
		@param verb: Get information while operations (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		self.envos = myEnv.oOP()
		if verb:
			print "Welcome to data Operation class of myFit."

	def dopen(self, fileName, met, verb=False):
		"""
		dopen(self, fileName, met, verb=False) -> HDU
		Opens a FIT/FITS file.
		
		@param fileName: Input file path.
		@type fileName: string
		@param met: Mode for file to open. 'copyonwrite', 'readonly', 'update', 'append', or 'ostream'.
		@type met: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: HDU
		"""
		if self.envos.isFile(fileName, verb=verb):
			try:
				img = pyfits.open(fileName, mode=met)
				return img
			except:
				if verb:
					print "Can't hanlde this type of file."
		else:
			if verb:
				print "No such file."
		
	def imget(self, fileName, metod, verb=False):
		"""
		imget(self, fileName, metod, verb=False) -> numpy.ndarray
		Returns all data of an image.
		
		@param fileName: Input file path.
		@type fileName: string
		@param metod: Mode for file to open. 'copyonwrite', 'readonly', 'update', 'append', or 'ostream'.
		@type metod: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: numpy.ndarray
		"""
		img = self.dopen(fileName, metod, verb=verb)
		if type(img) == pyfits.hdu.hdulist.HDUList:
			data = img[0].data
			if verb:
				print "'imget' done."
			img.close()
			return numpy.asarray(data)
		else:
			if verb:
				print "Couldn't open %s as a FIT/FITS file" %(fileName)

	def imcreate(self, inArr, inHeader, oFile, overWrite=False, verb=False):
		"""
		imcreate(self, inArr, inHeader, oFile, overWrite=False, verb=False) -> None
		Creates an FIT/FITS file by given header and array.
		
		@param inArr: The numpy array that will fill the image data.
		@type inArr: numpy.ndarray
		@param inHeader: The list that will fill the header data.
		@type inHeader: list
		@param overWrite: Overwrite on file exist situation (Optional, False by default).
		@type overWrite: boolean
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None	
		"""
		if type(inArr) == numpy.ndarray:
			if type(inHeader) == list:
				hdu = pyfits.PrimaryHDU()
				for i in inHeader:
					hdu.header[i[0]] = i[1]
				if not "BZERO" in inHeader:
					hdu.header["BZERO"] = 0
				hdu.data = inArr
				

				if verb:
					"'Image created' done."
			else:
				if verb:
					print "Unexpected input type for Header.\nlist expected.\nReceived %s" %(type(inHeader))
		else:
			if verb:
				print "Unexpected input type for Image.\nnumpy.ndarray expected.\nReceived %s" %(type(inArr))
		
		if not self.envos.isFile(oFile):
			hdu.writeto(oFile)
		else:
			if overWrite:
				if verb:
					print "'%s' file does exist. Going to overwrite it." %(oFile)
				self.envos.rm(oFile, verb=verb)
				hdu.writeto(oFile)
			else:
				if verb:
					print "'%s' file does exist. Will not overwrite it." %(oFile)

