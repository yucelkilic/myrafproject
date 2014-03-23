#!/usr/bin/env python										
#-*- coding: utf-8 -*-										
 													
from setuptools import setup								
import glob											
setup(name = "myraf",									
	version = "2.0beta",									
	author = "Yücel Kılıç",							
	url = "http://myrafproject.org",					
	author_email ="yucelkilic[at]myrafproject.org",					
	description = "An easy GUI for IRAF Photometry",								
	long_description = "The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business.",						
	license = "GPLv3",									
	platforms = 'linux',									
	data_files = [ ("/usr/share/MYRaf2/img",glob.glob('./img/*')),    
                             ("/usr/share/MYRaf2/obsdat",glob.glob('./obsdat/*')),
							 ("/usr/share/MYRaf2/set",glob.glob('./set/*')),
                             ("/usr/share/MYRaf2",glob.glob('./fPlot.py')),
                             ("/usr/share/MYRaf2",glob.glob('./function.py')),
							 ("/usr/share/MYRaf2",glob.glob('./gui.py')),
							 ("/usr/share/MYRaf2",glob.glob('./main.py')),
                             ("/usr/share/MYRaf2",glob.glob('./function.py')),
							 ("/usr/share/MYRaf2",glob.glob('./matplotlibwidgetFile.py')),
							 ("/usr/share/MYRaf2",glob.glob('./myraf.py')),
							 ("/usr/share/MYRaf2",glob.glob('./myraf.ui')),
							 ("/usr/share/MYRaf2",glob.glob('./sexCat.py')),
 							 ("/usr/share/applications",glob.glob('./myraf2.desktop'))],
							 scripts = ['myraf2'])
