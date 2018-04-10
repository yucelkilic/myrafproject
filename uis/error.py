# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
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

class Ui_MainWindowErr(object):
    def setupUi(self, MainWindowErr):
        MainWindowErr.setObjectName(_fromUtf8("MainWindowErr"))
        MainWindowErr.resize(400, 300)
        self.centralwidget = QtGui.QWidget(MainWindowErr)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Err_label = QtGui.QLabel(self.centralwidget)
        self.Err_label.setObjectName(_fromUtf8("Err_label"))
        self.gridLayout.addWidget(self.Err_label, 0, 0, 1, 1)
        self.Err_listWidget = QtGui.QListWidget(self.centralwidget)
        self.Err_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.Err_listWidget.setObjectName(_fromUtf8("Err_listWidget"))
        self.gridLayout.addWidget(self.Err_listWidget, 1, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(274, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.Err_pushButton = QtGui.QPushButton(self.centralwidget)
        self.Err_pushButton.setMinimumSize(QtCore.QSize(99, 27))
        self.Err_pushButton.setMaximumSize(QtCore.QSize(99, 27))
        self.Err_pushButton.setObjectName(_fromUtf8("Err_pushButton"))
        self.gridLayout.addWidget(self.Err_pushButton, 2, 1, 1, 1)
        self.Err_pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.Err_pushButton_2.setMinimumSize(QtCore.QSize(99, 27))
        self.Err_pushButton_2.setMaximumSize(QtCore.QSize(99, 27))
        self.Err_pushButton_2.setObjectName(_fromUtf8("Err_pushButton_2"))
        self.gridLayout.addWidget(self.Err_pushButton_2, 2, 2, 1, 1)
        MainWindowErr.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowErr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowErr.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowErr)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowErr.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowErr)
        QtCore.QMetaObject.connectSlotsByName(MainWindowErr)

    def retranslateUi(self, MainWindowErr):
        MainWindowErr.setWindowTitle(_translate("MainWindowErr", "MYRaf3 - Error", None))
        self.Err_label.setText(_translate("MainWindowErr", "TextLabel", None))
        self.Err_pushButton.setText(_translate("MainWindowErr", "Save", None))
        self.Err_pushButton_2.setText(_translate("MainWindowErr", "Ok", None))

