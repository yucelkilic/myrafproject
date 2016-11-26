# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisw/photometry.ui'
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

class Ui_MainWindowPhoto(object):
    def setupUi(self, MainWindowPhoto):
        MainWindowPhoto.setObjectName(_fromUtf8("MainWindowPhoto"))
        MainWindowPhoto.resize(650, 600)
        MainWindowPhoto.setMinimumSize(QtCore.QSize(650, 600))
        self.centralwidget = QtGui.QWidget(MainWindowPhoto)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.graphicsView = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 2, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.listView = QtGui.QListView(self.groupBox_2)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout_3.addWidget(self.listView, 0, 0, 1, 2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.listView_2 = QtGui.QListView(self.groupBox_3)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.gridLayout_4.addWidget(self.listView_2, 0, 0, 1, 2)
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_4.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 2, 1)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindowPhoto.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowPhoto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowPhoto.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowPhoto)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowPhoto.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowPhoto)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowPhoto)

    def retranslateUi(self, MainWindowPhoto):
        MainWindowPhoto.setWindowTitle(_translate("MainWindowPhoto", "MYRaf3 - Photometry", None))
        self.groupBox.setTitle(_translate("MainWindowPhoto", "Display", None))
        self.groupBox_2.setTitle(_translate("MainWindowPhoto", "Files", None))
        self.pushButton_3.setText(_translate("MainWindowPhoto", "Remove", None))
        self.pushButton_2.setText(_translate("MainWindowPhoto", "Add", None))
        self.groupBox_3.setTitle(_translate("MainWindowPhoto", "Sources", None))
        self.pushButton_4.setText(_translate("MainWindowPhoto", "Remove", None))
        self.pushButton_5.setText(_translate("MainWindowPhoto", "Display", None))
        self.label.setText(_translate("MainWindowPhoto", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindowPhoto", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindowPhoto", "Apperture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowPhoto", "Ensemble", None))

