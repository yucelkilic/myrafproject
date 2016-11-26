# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisw/graph.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindowGraph(object):
    def setupUi(self, MainWindowGraph):
        MainWindowGraph.setObjectName(_fromUtf8("MainWindowGraph"))
        MainWindowGraph.resize(650, 600)
        MainWindowGraph.setMinimumSize(QtCore.QSize(650, 600))
        self.centralwidget = QtGui.QWidget(MainWindowGraph)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindowGraph.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowGraph)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowGraph.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowGraph)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowGraph.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowGraph)
        QtCore.QMetaObject.connectSlotsByName(MainWindowGraph)

    def retranslateUi(self, MainWindowGraph):
        MainWindowGraph.setWindowTitle(_translate("MainWindowGraph", "MYRaf3 - Graph", None))

