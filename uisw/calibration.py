# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisw/calibration.ui'
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

class Ui_MainWindowCali(object):
    def setupUi(self, MainWindowCali):
        MainWindowCali.setObjectName(_fromUtf8("MainWindowCali"))
        MainWindowCali.resize(650, 600)
        MainWindowCali.setMinimumSize(QtCore.QSize(650, 600))
        self.centralwidget = QtGui.QWidget(MainWindowCali)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.listWidget_5 = QtGui.QListWidget(self.tab_5)
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.gridLayout_7.addWidget(self.listWidget_5, 0, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.tab_5)
        self.pushButton_10.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_10.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_7.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.tab_5)
        self.pushButton_11.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_11.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_7.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.listWidget_6 = QtGui.QListWidget(self.tab_6)
        self.listWidget_6.setObjectName(_fromUtf8("listWidget_6"))
        self.gridLayout_8.addWidget(self.listWidget_6, 0, 0, 1, 3)
        self.label_7 = QtGui.QLabel(self.tab_6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.tab_6)
        self.pushButton_12.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_12.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_8.addWidget(self.pushButton_12, 1, 1, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.tab_6)
        self.pushButton_13.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_13.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout_8.addWidget(self.pushButton_13, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.listWidget_7 = QtGui.QListWidget(self.tab_7)
        self.listWidget_7.setObjectName(_fromUtf8("listWidget_7"))
        self.gridLayout_9.addWidget(self.listWidget_7, 0, 0, 1, 3)
        self.label_8 = QtGui.QLabel(self.tab_7)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_9.addWidget(self.label_8, 1, 0, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.tab_7)
        self.pushButton_14.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_14.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout_9.addWidget(self.pushButton_14, 1, 1, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.tab_7)
        self.pushButton_15.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_15.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_9.addWidget(self.pushButton_15, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_8)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.listWidget_8 = QtGui.QListWidget(self.tab_8)
        self.listWidget_8.setObjectName(_fromUtf8("listWidget_8"))
        self.gridLayout_10.addWidget(self.listWidget_8, 0, 0, 1, 3)
        self.label_9 = QtGui.QLabel(self.tab_8)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1)
        self.pushButton_16 = QtGui.QPushButton(self.tab_8)
        self.pushButton_16.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_16.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout_10.addWidget(self.pushButton_16, 1, 1, 1, 1)
        self.pushButton_17 = QtGui.QPushButton(self.tab_8)
        self.pushButton_17.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_17.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout_10.addWidget(self.pushButton_17, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_8, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 2, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindowCali.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowCali)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowCali.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowCali)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowCali.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowCali)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowCali)

    def retranslateUi(self, MainWindowCali):
        MainWindowCali.setWindowTitle(_translate("MainWindowCali", "MYRaf3 - Calibration", None))
        self.label_6.setText(_translate("MainWindowCali", "TextLabel", None))
        self.pushButton_10.setText(_translate("MainWindowCali", "Remove", None))
        self.pushButton_11.setText(_translate("MainWindowCali", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindowCali", "Data", None))
        self.label_7.setText(_translate("MainWindowCali", "TextLabel", None))
        self.pushButton_12.setText(_translate("MainWindowCali", "Remove", None))
        self.pushButton_13.setText(_translate("MainWindowCali", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindowCali", "Bias", None))
        self.label_8.setText(_translate("MainWindowCali", "TextLabel", None))
        self.pushButton_14.setText(_translate("MainWindowCali", "Remove", None))
        self.pushButton_15.setText(_translate("MainWindowCali", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindowCali", "Dark", None))
        self.label_9.setText(_translate("MainWindowCali", "TextLabel", None))
        self.pushButton_16.setText(_translate("MainWindowCali", "Remove", None))
        self.pushButton_17.setText(_translate("MainWindowCali", "Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindowCali", "Flat", None))
        self.label.setText(_translate("MainWindowCali", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindowCali", ":go", None))

