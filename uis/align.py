# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisw/align.ui'
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

class Ui_MainWindowAlign(object):
    def setupUi(self, MainWindowAlign):
        MainWindowAlign.setObjectName(_fromUtf8("MainWindowAlign"))
        MainWindowAlign.resize(650, 600)
        MainWindowAlign.setMinimumSize(QtCore.QSize(650, 600))
        self.centralwidget = QtGui.QWidget(MainWindowAlign)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.graphicsView = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 1, 2, 1)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.groupBox_4)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.gridLayout_8.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_7.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_7.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_3)
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout_7.addWidget(self.listWidget_2, 0, 0, 1, 2)
        self.gridLayout_9.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_6.addWidget(self.pushButton_4, 0, 1, 2, 1)
        self.progressBar_2 = QtGui.QProgressBar(self.tab_2)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.gridLayout_6.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_6, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindowAlign.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowAlign)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowAlign.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowAlign)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowAlign.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowAlign)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAlign)

    def retranslateUi(self, MainWindowAlign):
        MainWindowAlign.setWindowTitle(_translate("MainWindowAlign", "MYRaf3 - Align", None))
        self.groupBox.setTitle(_translate("MainWindowAlign", "Display", None))
        self.groupBox_2.setTitle(_translate("MainWindowAlign", "Files", None))
        self.pushButton_2.setText(_translate("MainWindowAlign", "Add", None))
        self.pushButton_3.setText(_translate("MainWindowAlign", "Remove", None))
        self.label.setText(_translate("MainWindowAlign", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindowAlign", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindowAlign", "Auto", None))
        self.groupBox_4.setTitle(_translate("MainWindowAlign", "Display", None))
        self.label_3.setText(_translate("MainWindowAlign", "TextLabel", None))
        self.groupBox_3.setTitle(_translate("MainWindowAlign", "Files", None))
        self.pushButton_6.setText(_translate("MainWindowAlign", "Add", None))
        self.pushButton_5.setText(_translate("MainWindowAlign", "Remove", None))
        self.label_2.setText(_translate("MainWindowAlign", "TextLabel", None))
        self.pushButton_4.setText(_translate("MainWindowAlign", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowAlign", "Manual", None))
