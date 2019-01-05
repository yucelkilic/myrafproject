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
from os.path import getsize

from os import remove
from os import mkdir

from glob import glob

from shutil import copy2
from shutil import move

from datetime import datetime

from getpass import getuser

from platform import uname
from platform import system

from inspect import currentframe
from inspect import getouterframes

import webbrowser

try:
    from numpy import genfromtxt
    from numpy import savetxt
    from numpy import asarray
    from numpy import zeros
except Exception as e:
    print("{}. Numpy is not installed?".format(e))
    exit(0)


class etc():
    def __init__(self, verb=True):
        self.verb = verb
        self.log_dir = abspath("{}/mylog/".format(expanduser("~")))
        self.log_file = abspath("{}/log.my".format(self.log_dir))
        self.mini_log_file = abspath("{}/mlog.my".format(self.log_dir))
        
        self.setting_file = abspath("{}/.myset.set".format(expanduser("~")))
        self.def_setting_file = abspath("./def_myset.set")
        
        
        self.observat_dir = abspath("./observat/")
        
        if not((not isfile(self.log_dir)) and exists(self.log_dir)):
            mkdir(self.log_dir)
        
    def zeros(self, x, y):
        try:
            return(zeros((x, y)))
        except Exception as e:
            self.log(e)
        
    def user_is_a_monkey(self):
        try:
            a_website = "https://www.youtube.com/watch?v=hTWKbfoikeg"
            webbrowser.open_new(a_website)
        except:
            self.log("DEVELOPER IS A MONKEY")
        
    def time_stamp(self):
        return(str(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")))
        
    def time_stamp_(self):
        return(str(datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")))
    
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
            return("{}>{}>{}".format(
                    caller[0][3], caller[1][3], caller[2][3]))
        else:
            return(caller)
            
    def print_if(self, text):
        if self.verb:
            print("[{}|{}] --> {}".format(self.time_stamp(),
                  self.system_info(), text))
            
    def log(self, text):
        try:
            log_file = open(self.log_file, "a")
            log_file.write("Time: {}\n".format(self.time_stamp()))
            log_file.write("System Info: {}\n".format(self.system_info()))
            log_file.write("Log: {}\n".format(text))
            log_file.write("Function: {}\n\n\n".format(self.caller_function()))
            log_file.close()
            
            self.mini_log(text)
            self.print_if(text)
        except Exception as e:
            print(e)
        
    def mini_log(self, text):
        mini_log_file = open(self.mini_log_file, "a")
        mini_log_file.write("[{}|{}] --> {}\n".format(self.time_stamp(),
                            self.system_info(), text))
        mini_log_file.close()
        
    def dump_mlog(self):
        try:
            self.log("Deleting the Mini Log file.")
            mini_log_file = open(self.mini_log_file, "w")
            mini_log_file.close()
        except Exception as e:
            print(e)
        
    def dump_log(self):
        try:
            self.log("Deleting the Log file.")
            log_file = open(self.log_file, "w")
            log_file.close()
        except Exception as e:
            print(e)
        
    def is_it_windows(self):
        self.log("Checking if the OS is Windows")
        return(system() == 'Windows')
        
    def is_it_linux(self):
        self.log("Checking if the OS is Linux")
        return(system() == 'Linux')
        
    def is_it_other(self):
        self.log("Checking if the OS is Other")
        return(not (self.is_it_linux() or self.is_it_windows()))
        
    def beep(self):
        print("\a")
    
class file_op():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = etc(verb=verb)
            
    def get_size(self, path):
        try:
            if self.is_file(path):
                return(getsize(path))
        except Exception as e:
            self.etc.log(e)
        
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
        self.etc.log("Checking if file {0} exist".format(src))
        try:
            return(isfile(src))
        except Exception as e:
            self.etc.log(e)
            return(False)
        
    def is_dir(self, src):
        self.etc.log("Checking if directory {0} exist".format(src))
        try:
            return((not self.is_file(src)) and exists(src))
        except Exception as e:
            self.etc.log(e)
            return(False)
    
    def get_home_dir(self):
        self.etc.log("Getting Home dir path")
        try:
            return(expanduser("~"))
        except Exception as e:
            self.etc.log(e)
    
    def get_base_name(self, src):
        self.etc.log("Finding path and file name for {0}".format(src))
        try:
            pn = dirname(realpath(src))
            fn = basename(realpath(src))
            return(pn, fn)
        except Exception as e:
            self.etc.log(e)
    
    def get_extension(self, src):
        self.etc.log("Finding extension for {0}".format(src))
        try:
            return(splitext(src))
        except Exception as e:
            self.etc.log(e)
            
    def split_file_name(self, src):
        self.etc.log("Chopping path {0}".format(src))
        try:
            path, name = self.get_base_name(src)
            name, extension = self.get_extension(name)
            return(path, name, extension)
        except Exception as e:
            self.etc.log(e)
            
    def cp(self, src, dst):
        self.etc.log("Copying file {0} to {1}".format(src, dst))
        try:
            copy2(src, dst)
        except Exception as e:
            self.etc.log(e)
            
    def rm(self, src):
        self.etc.log("Removing file {0}".format(src))
        try:
            remove(src)
        except Exception as e:
            self.etc.log(e)
            
    def mv(self, src, dst):
        self.etc.log("Moving file {0} to {1}".format(src, dst))
        try:
            move(src, dst)
        except Exception as e:
            self.etc.log(e)
            
    def mkdir(self, path):
        try:
            if not self.is_dir:
                mkdir(path)
        except Exception as e:
            self.etc.log(e)
            
    def read_array(self, src, dm=" ", dtype=float):
        self.etc.log("Reading {0}".format(src))
        try:
            return(genfromtxt(src, comments='#', delimiter=dm, dtype=dtype))
        except Exception as e:
            self.etc.log(e)
            
    def write_array(self, src, arr, dm=" ", h=""):
        self.etc.log("Writing to {0}".format(src))
        try:
            arr = asarray(arr)
            savetxt(src, arr, delimiter=dm, newline='\n', header=h)
        except Exception as e:
            self.etc.log(e)
    def write_list(self, dest, the_list):
        f = open(dest, "w")
        for i in the_list:
            f.write("{}\n".format(i))
        
        f.close()
            

class converter():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = etc(verb=self.verb)
        
    def list2npar(self, lst):
        self.etc.log("Converting List to Numpy Array")
        try:
            return(asarray(lst))
        except Exception as e:
            self.etc.log(e)