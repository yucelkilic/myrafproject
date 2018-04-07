# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 14:57:43 2018

@author: mshem
"""

from PyQt5 import QtWidgets

def add_files(self, flist):
    filename = QtWidgets.QFileDialog.getOpenFileNames(
            self ,"Images...","",("Fit or Fits (*.fits *.fit)"))[0]
    it = flist.count() - 1
    for x in filename:
        it = it+1
        item = QtWidgets.QListWidgetItem()
        flist.addItem(item)
        item = flist.item(it)
        item.setText(QtWidgets.QApplication.translate("Form", x, None))

def add(self, flist, the_list):
    it = flist.count() - 1
    for x in the_list:
        it = it+1
        item = QtWidgets.QListWidgetItem()
        flist.addItem(item)
        item = flist.item(it)
        item.setText(QtWidgets.QApplication.translate("Form", x, None))
        
def add_line_by_line(self, flist, file_name):
    the_f = open(file_name, "r")
    it = flist.count() - 1
    for x in the_f:
        ln = x.replace("\n", "")
        it = it+1
        item = QtWidgets.QListWidgetItem()
        flist.addItem(item)
        item = flist.item(it)
        item.setText(QtWidgets.QApplication.translate("Form", ln, None))

def question(self, question):
    answ = QtWidgets.QMessageBox.question(self, "MYRaf", question,
                                          QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.No)
    return(answ)

def rm(self, flist):
    for x in flist.selectedItems():
        flist.takeItem(flist.row(x))

def save_log_file(self):
    ofile = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save Log File', 'log.myl', 'myl (*.myl)')
    return(ofile[0])

def rm_all(self, flist):
    flist.clear()
        
def list_lenght(self, flist):
    return(flist.count())
    
def is_list_empty(self, flist):
    return(list_lenght(self, flist) == 0)