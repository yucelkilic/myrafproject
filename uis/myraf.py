# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/myraf.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(548, 390)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(548, 390))
        MainWindow.setMaximumSize(QtCore.QSize(548, 390))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 3, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setText(_fromUtf8(""))
        self.pushButton_4.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_5.setMouseTracking(True)
        self.pushButton_5.setAutoFillBackground(True)
        self.pushButton_5.setText(_fromUtf8(""))
        self.pushButton_5.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 3, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_6.setMouseTracking(True)
        self.pushButton_6.setAutoFillBackground(True)
        self.pushButton_6.setText(_fromUtf8(""))
        self.pushButton_6.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_7.setMouseTracking(True)
        self.pushButton_7.setAutoFillBackground(True)
        self.pushButton_7.setText(_fromUtf8(""))
        self.pushButton_7.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 3, 2, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_8.setMouseTracking(True)
        self.pushButton_8.setAutoFillBackground(True)
        self.pushButton_8.setText(_fromUtf8(""))
        self.pushButton_8.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 3, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(128, 128))
        self.pushButton_3.setMouseTracking(True)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setText(_fromUtf8(""))
        self.pushButton_3.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionCalibration = QtGui.QAction(MainWindow)
        self.actionCalibration.setObjectName(_fromUtf8("actionCalibration"))
        self.actionAlign = QtGui.QAction(MainWindow)
        self.actionAlign.setObjectName(_fromUtf8("actionAlign"))
        self.actionPhotometry = QtGui.QAction(MainWindow)
        self.actionPhotometry.setObjectName(_fromUtf8("actionPhotometry"))
        self.actionGraph = QtGui.QAction(MainWindow)
        self.actionGraph.setObjectName(_fromUtf8("actionGraph"))
        self.actionEditor = QtGui.QAction(MainWindow)
        self.actionEditor.setObjectName(_fromUtf8("actionEditor"))
        self.actionScheduler = QtGui.QAction(MainWindow)
        self.actionScheduler.setObjectName(_fromUtf8("actionScheduler"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.menuFile.addAction(self.actionQuit)
        self.menuWindow.addAction(self.actionCalibration)
        self.menuWindow.addAction(self.actionAlign)
        self.menuWindow.addAction(self.actionPhotometry)
        self.menuWindow.addAction(self.actionGraph)
        self.menuWindow.addAction(self.actionEditor)
        self.menuWindow.addAction(self.actionScheduler)
        self.menuWindow.addAction(self.actionSettings)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MYRaf3 Beta", None))
        self.label_7.setText(_translate("MainWindow", "Settings", None))
        self.label_8.setText(_translate("MainWindow", "Help", None))
        self.label_3.setText(_translate("MainWindow", "Photometry", None))
        self.label_4.setText(_translate("MainWindow", "Graph", None))
        self.label_6.setText(_translate("MainWindow", "Scheduler", None))
        self.label_2.setText(_translate("MainWindow", "Align", None))
        self.label_5.setText(_translate("MainWindow", "Editor", None))
        self.label.setText(_translate("MainWindow", "Calibration", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Window", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionCalibration.setText(_translate("MainWindow", "Calibration", None))
        self.actionAlign.setText(_translate("MainWindow", "Align", None))
        self.actionPhotometry.setText(_translate("MainWindow", "Photometry", None))
        self.actionGraph.setText(_translate("MainWindow", "Graph", None))
        self.actionEditor.setText(_translate("MainWindow", "Editor", None))
        self.actionScheduler.setText(_translate("MainWindow", "Scheduler", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))

