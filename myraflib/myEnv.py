# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
MYRaf Environment Module.
Note that all modules with name started by 'my' such as myFit, myEnv are MYRaf's third party modules.
For further information:

	From myraflib import myEnv
	help(myEnv)
"""

import os
import shutil
__all__ = ["oOP"]
class oOP():
	"""
	oOP stands for OS OPERATIONS. Such as, removing, renaming, path checking etc... 
	"""
	__all__ = ["__init__", "isFile", "isPath", "rm"]

	def __init__(self, verb=False):
		"""
		__init__(self, verb=False) -> None
		Initial function. Welcome the user.
		
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		if verb:
			print "Welcome to OS Operation class of myEnv."
			
	def isFile(self, fileName, verb=False):
		"""
		isFile(self, fileName, verb=False) -> Boolean
		Checks if file exist or not.
		
		@param fileName: Input file path.
		@type fileName: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: boolean
		"""
		if os.path.isfile(fileName):
			if verb:
				print "'%s' file does exist." %(fileName)
		else:
			if verb:
				print "'%s' file does not exist." %(fileName)
		
		return  os.path.isfile(fileName)


	def isPath(self, path, verb=False):
		"""
		isPath(self, path, verb=False) -> Boolean
		Checks if path exist or not.
		
		@param path: Input path.
		@type path: string
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: boolean
		"""
		if os.path.isfile(path) == False and os.path.exists(path) == True:
			if verb:
				print "'%s' path does exist." %(path)
			return True
		else:
			if verb:
				print "'%s' path does not exist." %(path)
			return False

	def rm(self, path, force=False, recu=False, verb=False):
		"""
		rm(self, path, force=False, recu=False, verb=False) -> None
		Deletes file or directories
		
		@param path: Input path.
		@type path: string
		@param force: Force operation (Optional, False by default).
		@type force: boolean
		@param recu: Delete all contents if directory is not empty (Optional, False by default).
		@type recu: boolean
		@param verb: Get information while operation (Optional, False by default).
		@type verb: boolean
		@return: None
		"""
		if force:
			if self.isFile(path, verb=verb):
				if verb:
					print "File deleted."
				os.remove(path)
			elif self.isPath(path, verb=verb):
				if os.listdir(path) == []:
					os.rmdir(path)
					if verb:
						print "'%s' Direectory edeleted." %(path)
				else:
					shutil.rmtree(path)
					if verb:
						print "'%s' Directory deleted with it's contents." %(path)
			else:
				if verb:
					print "%s no such file or directory" %(path)
		else:
			if self.isFile(path, verb=verb):
				if verb:
					print "'%s' File deleted." %(path)
				os.remove(path)
			elif self.isPath(path, verb=verb):
				if os.listdir(path) == []:
					os.rmdir(path)
					if verb:
						print "'%s' Direectory edeleted." %(path)
				else:
					if recu:
						shutil.rmtree(path)
						if verb:
							print "'%s' Directory deleted with it's contents." %(path)
					else:
						if verb:
							print "'%s' Directory is not emptry. Skipping..." %(path)		
			else:
				if verb:
					print "%s no such file or directory" %(path)
