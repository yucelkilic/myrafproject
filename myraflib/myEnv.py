# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:31:52 2018

@author: mshem
"""
#Importing needed functions
from os.path import expanduser
from os.path import exists
from os.path import isfile
from os.path import dirname
from os.path import basename
from os.path import realpath
from os.path import splitext
from os.path import abspath

from os import name as osname
from os import remove

from glob import glob

from shutil import copy2
from shutil import move

from datetime import datetime

from getpass import getuser

from platform import uname
from platform import system

from inspect import currentframe
from inspect import getouterframes

from  numpy import genfromtxt
from  numpy import savetxt


class etc():
    def __init__(self, verb=True):
        self.verb = verb
        self.log_file = abspath("{}/log.my".format(expanduser("~")))
        self.mini_log_file = abspath("{}/mlog.my".format(expanduser("~")))
        
    def time_stamp(self):
        return(str(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")))
    
    def user_name(self):
        return(str(getuser()))
    
    def system_info(self):
        si = uname()
        return("{}, {}, {}, {}".format(si[0], si[2], si[5], self.user_name()))

    def caller_function(self, pri=False):
        curframe = currentframe()
        calframe = getouterframes(curframe, 2)
        caller = calframe
        self.system_info()
        if pri:
            return("{}>{}>{}".format(caller[0][3], caller[1][3], caller[2][3]))
        else:
            return(caller)
            
    def print_if(self, text):
        if self.verb:
            print("[{}|{}]{}".format(self.time_stamp(), self.system_info(),
                   text))
            
    def log(self, text):
        log_file = open(self.log_file, "a")
        log_file.write("Time: {}\n".format(self.time_stamp()))
        log_file.write("System Info: {}\n".format(self.system_info()))
        log_file.write("Log: {}\n".format(text))
        log_file.write("Function: {}\n\n\n".format((self.caller_function())))
        log_file.close()
        
        self.mini_log(text)
        self.print_if(text)
        
    def mini_log(self, text):
        mini_log_file = open(self.mini_log_file, "a")
        mini_log_file.write("[{}|{}] --> {}\n".format(self.time_stamp(),
                            self.system_info(), text))
        mini_log_file.close()
        
    def dump_mlog(self):
        mini_log_file = open(self.mini_log_file, "w")
        mini_log_file.close()
        
    def dump_log(self):
        log_file = open(self.log_file, "w")
        log_file.close()
        
    def is_it_windows(self):
        return(system() == 'Windows')
        
    def is_it_linux(self):
        return(system() == 'Linux')
        
    def is_it_other(self):
        return(not (self.is_it_linux() or self.is_it_windows()))
        
    def beep(self):
        print("\a")
    
class file_op():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = etc(verb=verb)
            
    def abs_path(self, path):
        try:
            return(abspath(path))
        except Exception as e:
            self.etc.log(e)
            

    def list_of_fiels(self, path, ext="*"):
        try:
            if self.is_dir(path):
                pt = self.abs_path("{}/{}".format(path, ext))
                return(sorted(glob(pt)))
        except Exception as e:
            self.etc.log(e)  
            
    def is_file(self, src):
        try:
            self.etc.print_if("Checking if file {0} exist".format(src))
            return(isfile(src))
        except Exception as e:
            self.etc.log(e)
            return(False)
        
    def is_dir(self, src):
        try:
            self.etc.print_if("Checking if directory {0} exist".format(src))
            return((not self.is_file(src)) and exists(src))
        except Exception as e:
            self.etc.log(e)
            return(False)
    
    def get_home_dir(self):
        try:
            self.etc.print_if("Getting Home dir path")
            return(expanduser("~"))
        except Exception as e:
            self.etc.log(e)
    
    def get_base_name(self, src):
        try:
            self.etc.print_if("Finding path and file name for {0}".format(src))
            pn = dirname(realpath(src))
            fn = basename(realpath(src))
            return(pn, fn)
        except Exception as e:
            self.etc.log(e)
    
    def get_extension(self, src):
        try:
            self.etc.print_if("Finding extension for {0}".format(src))
            return(splitext(src)[1])
        except Exception as e:
            self.etc.log(e)
            
    def split_file_name(self, src):
        try:
            self.etc.print_if("Chopping path {0}".format(src))
            path, name = self.get_base_name(src)
            name , extension = self.get_extension(name)
            return(path, name, extension)
        except Exception as e:
            self.etc.log(e)
            
    def cp(self, src, dst):
        try:
            self.etc.print_if("Copying file {0} to {1}".format(src, dst))
            copy2(src, dst)
        except Exception as e:
            self.etc.log(e)
            
    def rm(self, src):
        try:
            self.etc.print_if("Removing file {0}".format(src))
            remove(src)
        except Exception as e:
            self.etc.log(e)
            
    def mv(self, src, dst):
        try:
            self.etc.print_if("Moving file {0} to {1}".format(src, dst))
            move(src, dst)
        except Exception as e:
            self.etc.log(e)
            
    def read_array(self, src, dm=" ", dtype=float):
        try:
            self.etc.print_if("Reading {0}".format(src))
            return(genfromtxt(src, comments='#', delimiter=dm, dtype=dtype))
        except Exception as e:
            self.etc.log(e)
            
    def write_array(self, src, arr, dm=" ", h=""):
        try:
            self.etc.print_if("Writing to {0}".format(src))
            savetxt(src, arr, delimiter=dm, newline='\n', header=h)
        except Exception as e:
            self.etc.log(e)
