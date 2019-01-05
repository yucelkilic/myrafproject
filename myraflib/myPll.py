# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 00:49:07 2018

@author: msh
"""

from math import ceil
import threading

try:
    from . import myEnv
except Exception as e:
    print("{}. Cannot find myEnv.py".format(e))
    exit(0)


class proc():
    def __init__(self, verb=True):
        self.verb = verb
        self.etc = myEnv.etc(verb=self.verb)
        
    def job_devider(self, args, pieces=2):
        try:
            n = ceil(float(len(args))/float(pieces))
            for i in range(0, len(args), n):
                yield args[i:i + n]
        except Exception as e:
            self.etc.print_if(e)
            
    def do(self, funck, args, pieces=2):
        try:
            splited_args = self.job_devider(args, pieces=pieces)
            lst = []
            for i in splited_args:
                lst.append(threading.Thread(target=funck, args=(i,)))
                
            for u in lst:
                u.start()
                
            for z in lst:
                z.join()
        except Exception as e:
            self.etc.print_if(e)