# -*- coding: utf-8 -*-
#
# gingawidgetFile.py -- Plotting function for embedded matplotlib widget with Ginga.
#
# Thanks for Eric Jeschke (eric@naoj.org), https://github.com/ejeschke/ginga
# and
# https://gist.github.com/Maduranga/ for embedding matplotlibWidget into PyQt4

# Copyleft, Yücel Kılıç (yucelkilic@myrafproject.org) and Mohammad Niaei Shameoni (mshemuni@myrafproject.org).
# This is open-source software licensed under a GPLv3 license.

from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

import sys, os
import platform
# just in case you want to use qt
os.environ['QT_API'] = 'pyqt'

import matplotlib
options = ['Qt4Agg', 'GTK', 'GTKAgg', 'MacOSX', 'GTKCairo', 'WXAgg',
           'TkAgg', 'QtAgg', 'FltkAgg', 'WX']
# Force a specific toolkit on mac
macos_ver = platform.mac_ver()[0]
if len(macos_ver) > 0:
    # change this to "pass" if you want to force a different backend
    # On Mac OS X I found the default choice for matplotlib is not stable
    # with ginga
    matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt
 
class MplCanvas(FigureCanvas):
 
    def __init__(self):
        # create a regular matplotlib figure
        self.fig = plt.figure()
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
 
 
class gingaWidget(QtGui.QWidget):
 
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.toolbar)
        self.setLayout(self.vbl)
        self.parent = parent
