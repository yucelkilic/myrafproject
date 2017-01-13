# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat Jan 14 00:11:21 2017
#      by: PyQt4 UI code generator 4.10.4
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
        MainWindow.resize(730, 710)
        MainWindow.setMinimumSize(QtCore.QSize(730, 710))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tab_9)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.listWidget_9 = QtGui.QListWidget(self.tab_9)
        self.listWidget_9.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_9.setObjectName(_fromUtf8("listWidget_9"))
        self.gridLayout_11.addWidget(self.listWidget_9, 0, 0, 1, 3)
        self.label_10 = QtGui.QLabel(self.tab_9)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_11.addWidget(self.label_10, 1, 0, 1, 1)
        self.pushButton_21 = QtGui.QPushButton(self.tab_9)
        self.pushButton_21.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_21.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.gridLayout_11.addWidget(self.pushButton_21, 1, 1, 1, 1)
        self.pushButton_22 = QtGui.QPushButton(self.tab_9)
        self.pushButton_22.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_22.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.gridLayout_11.addWidget(self.pushButton_22, 1, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_9, _fromUtf8(""))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_10)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.pushButton_23 = QtGui.QPushButton(self.tab_10)
        self.pushButton_23.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_23.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.gridLayout_12.addWidget(self.pushButton_23, 1, 3, 1, 1)
        self.listWidget_10 = QtGui.QListWidget(self.tab_10)
        self.listWidget_10.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_10.setObjectName(_fromUtf8("listWidget_10"))
        self.gridLayout_12.addWidget(self.listWidget_10, 0, 0, 1, 4)
        self.label_11 = QtGui.QLabel(self.tab_10)
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_12.addWidget(self.label_11, 1, 0, 1, 1)
        self.pushButton_24 = QtGui.QPushButton(self.tab_10)
        self.pushButton_24.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_24.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.gridLayout_12.addWidget(self.pushButton_24, 1, 2, 1, 1)
        self.pushButton_25 = QtGui.QPushButton(self.tab_10)
        self.pushButton_25.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_25.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.gridLayout_12.addWidget(self.pushButton_25, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_10, _fromUtf8(""))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_11)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.listWidget_11 = QtGui.QListWidget(self.tab_11)
        self.listWidget_11.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_11.setObjectName(_fromUtf8("listWidget_11"))
        self.gridLayout_13.addWidget(self.listWidget_11, 0, 0, 1, 4)
        self.label_12 = QtGui.QLabel(self.tab_11)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_13.addWidget(self.label_12, 1, 0, 1, 1)
        self.pushButton_26 = QtGui.QPushButton(self.tab_11)
        self.pushButton_26.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_26.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.gridLayout_13.addWidget(self.pushButton_26, 1, 2, 1, 1)
        self.pushButton_27 = QtGui.QPushButton(self.tab_11)
        self.pushButton_27.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_27.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.gridLayout_13.addWidget(self.pushButton_27, 1, 3, 1, 1)
        self.pushButton_28 = QtGui.QPushButton(self.tab_11)
        self.pushButton_28.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_28.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.gridLayout_13.addWidget(self.pushButton_28, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_11, _fromUtf8(""))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tab_12)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.label_13 = QtGui.QLabel(self.tab_12)
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_14.addWidget(self.label_13, 1, 0, 1, 1)
        self.pushButton_29 = QtGui.QPushButton(self.tab_12)
        self.pushButton_29.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_29.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.gridLayout_14.addWidget(self.pushButton_29, 1, 2, 1, 1)
        self.pushButton_30 = QtGui.QPushButton(self.tab_12)
        self.pushButton_30.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_30.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.gridLayout_14.addWidget(self.pushButton_30, 1, 3, 1, 1)
        self.listWidget_12 = QtGui.QListWidget(self.tab_12)
        self.listWidget_12.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_12.setObjectName(_fromUtf8("listWidget_12"))
        self.gridLayout_14.addWidget(self.listWidget_12, 0, 0, 1, 4)
        self.pushButton_31 = QtGui.QPushButton(self.tab_12)
        self.pushButton_31.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_31.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.gridLayout_14.addWidget(self.pushButton_31, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_12, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setText(_fromUtf8(""))
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
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_20 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.disp_aut_align = gingaWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_aut_align.sizePolicy().hasHeightForWidth())
        self.disp_aut_align.setSizePolicy(sizePolicy)
        self.disp_aut_align.setObjectName(_fromUtf8("disp_aut_align"))
        self.gridLayout_5.addWidget(self.disp_aut_align, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_6.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_6.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_6.addWidget(self.listWidget, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_15.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_15.addWidget(self.pushButton_4, 0, 1, 2, 1)
        self.progressBar_2 = QtGui.QProgressBar(self.tab_3)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.gridLayout_15.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_15, 1, 0, 1, 2)
        self.tabWidget_3.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_16 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.disp_man_align = gingaWidget(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_man_align.sizePolicy().hasHeightForWidth())
        self.disp_man_align.setSizePolicy(sizePolicy)
        self.disp_man_align.setObjectName(_fromUtf8("disp_man_align"))
        self.gridLayout_8.addWidget(self.disp_man_align, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_8.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_18 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_18.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_18.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.groupBox_3)
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout_18.addWidget(self.listWidget_2, 0, 0, 1, 2)
        self.gridLayout_16.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_19.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_19.addWidget(self.pushButton_7, 0, 1, 2, 1)
        self.progressBar_3 = QtGui.QProgressBar(self.tab_4)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.gridLayout_19.addWidget(self.progressBar_3, 1, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_19, 1, 0, 1, 2)
        self.tabWidget_3.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout_20.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_13 = QtGui.QWidget()
        self.tab_13.setObjectName(_fromUtf8("tab_13"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tab_13)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.tabWidget_4 = QtGui.QTabWidget(self.tab_13)
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.gridLayout_21 = QtGui.QGridLayout(self.tab_14)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.disp_phot = gingaWidget(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_phot.sizePolicy().hasHeightForWidth())
        self.disp_phot.setSizePolicy(sizePolicy)
        self.disp_phot.setObjectName(_fromUtf8("disp_phot"))
        self.gridLayout_9.addWidget(self.disp_phot, 0, 0, 1, 1)
        self.gridLayout_21.addWidget(self.groupBox_5, 0, 0, 2, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_6.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_23 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_8.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_23.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_9.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_9.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_23.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.listWidget_3 = QtGui.QListWidget(self.groupBox_6)
        self.listWidget_3.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.gridLayout_23.addWidget(self.listWidget_3, 0, 0, 1, 2)
        self.gridLayout_21.addWidget(self.groupBox_6, 0, 1, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_7.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_7.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_24 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.pushButton_32 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_32.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_32.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.gridLayout_24.addWidget(self.pushButton_32, 1, 0, 1, 1)
        self.pushButton_33 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_33.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_33.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.gridLayout_24.addWidget(self.pushButton_33, 1, 1, 1, 1)
        self.listWidget_4 = QtGui.QListWidget(self.groupBox_7)
        self.listWidget_4.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.gridLayout_24.addWidget(self.listWidget_4, 0, 0, 1, 2)
        self.gridLayout_21.addWidget(self.groupBox_7, 1, 1, 1, 1)
        self.gridLayout_25 = QtGui.QGridLayout()
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.label_5 = QtGui.QLabel(self.tab_14)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_25.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton_34 = QtGui.QPushButton(self.tab_14)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_34.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_34.setObjectName(_fromUtf8("pushButton_34"))
        self.gridLayout_25.addWidget(self.pushButton_34, 0, 1, 2, 1)
        self.progressBar_4 = QtGui.QProgressBar(self.tab_14)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName(_fromUtf8("progressBar_4"))
        self.gridLayout_25.addWidget(self.progressBar_4, 1, 0, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_25, 2, 0, 1, 2)
        self.tabWidget_4.addTab(self.tab_14, _fromUtf8(""))
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName(_fromUtf8("tab_15"))
        self.tabWidget_4.addTab(self.tab_15, _fromUtf8(""))
        self.gridLayout_10.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_13, _fromUtf8(""))
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName(_fromUtf8("tab_16"))
        self.gridLayout_26 = QtGui.QGridLayout(self.tab_16)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.tabWidget_11 = QtGui.QTabWidget(self.tab_16)
        self.tabWidget_11.setObjectName(_fromUtf8("tabWidget_11"))
        self.tab_30 = QtGui.QWidget()
        self.tab_30.setObjectName(_fromUtf8("tab_30"))
        self.gridLayout_56 = QtGui.QGridLayout(self.tab_30)
        self.gridLayout_56.setObjectName(_fromUtf8("gridLayout_56"))
        self.tableWidget = QtGui.QTableWidget(self.tab_30)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_56.addWidget(self.tableWidget, 0, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.tab_30)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_56.addWidget(self.label_7, 1, 0, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.tab_30)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_56.addWidget(self.pushButton_12, 1, 1, 1, 1)
        self.tabWidget_11.addTab(self.tab_30, _fromUtf8(""))
        self.tab_25 = QtGui.QWidget()
        self.tab_25.setObjectName(_fromUtf8("tab_25"))
        self.gridLayout_61 = QtGui.QGridLayout(self.tab_25)
        self.gridLayout_61.setObjectName(_fromUtf8("gridLayout_61"))
        self.groupBox_16 = QtGui.QGroupBox(self.tab_25)
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.gridLayout_61.addWidget(self.groupBox_16, 0, 0, 1, 1)
        self.tabWidget_11.addTab(self.tab_25, _fromUtf8(""))
        self.gridLayout_26.addWidget(self.tabWidget_11, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_16, _fromUtf8(""))
        self.tab_17 = QtGui.QWidget()
        self.tab_17.setObjectName(_fromUtf8("tab_17"))
        self.gridLayout_43 = QtGui.QGridLayout(self.tab_17)
        self.gridLayout_43.setObjectName(_fromUtf8("gridLayout_43"))
        self.tabWidget_5 = QtGui.QTabWidget(self.tab_17)
        self.tabWidget_5.setObjectName(_fromUtf8("tabWidget_5"))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        self.gridLayout_27 = QtGui.QGridLayout(self.tab_18)
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.gridLayout_28 = QtGui.QGridLayout()
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_18)
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_29 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.listWidget_13 = QtGui.QListWidget(self.groupBox_8)
        self.listWidget_13.setObjectName(_fromUtf8("listWidget_13"))
        self.gridLayout_29.addWidget(self.listWidget_13, 0, 0, 1, 1)
        self.gridLayout_28.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.tab_18)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 110))
        self.groupBox_9.setMaximumSize(QtCore.QSize(16777215, 110))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_30 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        self.gridLayout_31 = QtGui.QGridLayout()
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.label_14 = QtGui.QLabel(self.groupBox_9)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_31.addWidget(self.label_14, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_31.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox_9)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_31.addWidget(self.checkBox, 0, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox_9)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_31.addWidget(self.label_15, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_31.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox_9)
        self.comboBox.setEnabled(False)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_31.addWidget(self.comboBox, 1, 2, 1, 1)
        self.gridLayout_30.addLayout(self.gridLayout_31, 0, 0, 1, 1)
        self.gridLayout_28.addWidget(self.groupBox_9, 1, 0, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_28, 0, 0, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.tab_18)
        self.groupBox_10.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_10.setFlat(True)
        self.groupBox_10.setCheckable(False)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_32 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.listWidget_14 = QtGui.QListWidget(self.groupBox_10)
        self.listWidget_14.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_14.setObjectName(_fromUtf8("listWidget_14"))
        self.gridLayout_32.addWidget(self.listWidget_14, 0, 0, 1, 2)
        self.pushButton_37 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_37.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_37.setMaximumSize(QtCore.QSize(70, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/.designer/.designer/backup/img/rem.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_37.setIcon(icon)
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.gridLayout_32.addWidget(self.pushButton_37, 1, 0, 1, 1)
        self.pushButton_36 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_36.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_36.setMaximumSize(QtCore.QSize(70, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/.designer/.designer/backup/img/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_36.setIcon(icon1)
        self.pushButton_36.setObjectName(_fromUtf8("pushButton_36"))
        self.gridLayout_32.addWidget(self.pushButton_36, 1, 1, 1, 1)
        self.gridLayout_27.addWidget(self.groupBox_10, 0, 1, 1, 1)
        self.gridLayout_33 = QtGui.QGridLayout()
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.label_16 = QtGui.QLabel(self.tab_18)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_33.addWidget(self.label_16, 0, 0, 1, 1)
        self.pushButton_35 = QtGui.QPushButton(self.tab_18)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy)
        self.pushButton_35.setMinimumSize(QtCore.QSize(125, 25))
        self.pushButton_35.setMaximumSize(QtCore.QSize(125, 25))
        self.pushButton_35.setObjectName(_fromUtf8("pushButton_35"))
        self.gridLayout_33.addWidget(self.pushButton_35, 0, 1, 1, 1)
        self.progressBar_5 = QtGui.QProgressBar(self.tab_18)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName(_fromUtf8("progressBar_5"))
        self.gridLayout_33.addWidget(self.progressBar_5, 1, 0, 1, 1)
        self.pushButton_38 = QtGui.QPushButton(self.tab_18)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setMinimumSize(QtCore.QSize(125, 25))
        self.pushButton_38.setMaximumSize(QtCore.QSize(125, 25))
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.gridLayout_33.addWidget(self.pushButton_38, 1, 1, 1, 1)
        self.gridLayout_27.addLayout(self.gridLayout_33, 1, 0, 1, 2)
        self.tabWidget_5.addTab(self.tab_18, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        self.gridLayout_34 = QtGui.QGridLayout(self.tab_19)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_19)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_35 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.listWidget_15 = QtGui.QListWidget(self.groupBox_11)
        self.listWidget_15.setObjectName(_fromUtf8("listWidget_15"))
        self.gridLayout_35.addWidget(self.listWidget_15, 0, 0, 1, 1)
        self.gridLayout_34.addWidget(self.groupBox_11, 0, 0, 1, 1)
        self.groupBox_12 = QtGui.QGroupBox(self.tab_19)
        self.groupBox_12.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_12.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_12.setFlat(True)
        self.groupBox_12.setCheckable(False)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_36 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.label_20 = QtGui.QLabel(self.groupBox_12)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_36.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_36.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_12)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_36.addWidget(self.label_21, 2, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_36.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_12)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_36.addWidget(self.label_23, 4, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_36.addWidget(self.lineEdit_5, 5, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_12)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_36.addWidget(self.label_22, 6, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_36.addWidget(self.lineEdit_6, 7, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_12)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_36.addWidget(self.label_25, 8, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_36.addWidget(self.lineEdit_7, 9, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_12)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_36.addWidget(self.label_26, 10, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_12)
        self.lineEdit_8.setText(_fromUtf8(""))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_36.addWidget(self.lineEdit_8, 11, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_12)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_36.addWidget(self.label_24, 12, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_12)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_36.addWidget(self.plainTextEdit, 13, 0, 1, 1)
        self.gridLayout_34.addWidget(self.groupBox_12, 0, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(375, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_39 = QtGui.QPushButton(self.tab_19)
        self.pushButton_39.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton_39.setMaximumSize(QtCore.QSize(110, 16777215))
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.gridLayout_34.addWidget(self.pushButton_39, 1, 1, 1, 1)
        self.pushButton_40 = QtGui.QPushButton(self.tab_19)
        self.pushButton_40.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton_40.setMaximumSize(QtCore.QSize(110, 16777215))
        self.pushButton_40.setObjectName(_fromUtf8("pushButton_40"))
        self.gridLayout_34.addWidget(self.pushButton_40, 1, 2, 1, 1)
        self.tabWidget_5.addTab(self.tab_19, _fromUtf8(""))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        self.gridLayout_37 = QtGui.QGridLayout(self.tab_20)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.groupBox_13 = QtGui.QGroupBox(self.tab_20)
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.gridLayout_38 = QtGui.QGridLayout(self.groupBox_13)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.disp_cosmic_clean = gingaWidget(self.groupBox_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_cosmic_clean.sizePolicy().hasHeightForWidth())
        self.disp_cosmic_clean.setSizePolicy(sizePolicy)
        self.disp_cosmic_clean.setObjectName(_fromUtf8("disp_cosmic_clean"))
        self.gridLayout_38.addWidget(self.disp_cosmic_clean, 0, 0, 1, 1)
        self.gridLayout_37.addWidget(self.groupBox_13, 0, 0, 1, 1)
        self.groupBox_14 = QtGui.QGroupBox(self.tab_20)
        self.groupBox_14.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_14.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_14.setFlat(True)
        self.groupBox_14.setCheckable(False)
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.gridLayout_39 = QtGui.QGridLayout(self.groupBox_14)
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        self.listWidget_16 = QtGui.QListWidget(self.groupBox_14)
        self.listWidget_16.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_16.setObjectName(_fromUtf8("listWidget_16"))
        self.gridLayout_39.addWidget(self.listWidget_16, 0, 0, 1, 2)
        self.pushButton_41 = QtGui.QPushButton(self.groupBox_14)
        self.pushButton_41.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_41.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_41.setIcon(icon)
        self.pushButton_41.setObjectName(_fromUtf8("pushButton_41"))
        self.gridLayout_39.addWidget(self.pushButton_41, 1, 0, 1, 1)
        self.pushButton_42 = QtGui.QPushButton(self.groupBox_14)
        self.pushButton_42.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_42.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_42.setIcon(icon1)
        self.pushButton_42.setObjectName(_fromUtf8("pushButton_42"))
        self.gridLayout_39.addWidget(self.pushButton_42, 1, 1, 1, 1)
        self.gridLayout_37.addWidget(self.groupBox_14, 0, 1, 1, 1)
        self.gridLayout_40 = QtGui.QGridLayout()
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.label_17 = QtGui.QLabel(self.tab_20)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_40.addWidget(self.label_17, 0, 0, 1, 1)
        self.pushButton_43 = QtGui.QPushButton(self.tab_20)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_43.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_43.setObjectName(_fromUtf8("pushButton_43"))
        self.gridLayout_40.addWidget(self.pushButton_43, 0, 1, 2, 1)
        self.progressBar_6 = QtGui.QProgressBar(self.tab_20)
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName(_fromUtf8("progressBar_6"))
        self.gridLayout_40.addWidget(self.progressBar_6, 1, 0, 1, 1)
        self.gridLayout_37.addLayout(self.gridLayout_40, 1, 0, 1, 2)
        self.tabWidget_5.addTab(self.tab_20, _fromUtf8(""))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        self.gridLayout_41 = QtGui.QGridLayout(self.tab_21)
        self.gridLayout_41.setObjectName(_fromUtf8("gridLayout_41"))
        self.listWidget_17 = QtGui.QListWidget(self.tab_21)
        self.listWidget_17.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_17.setObjectName(_fromUtf8("listWidget_17"))
        self.gridLayout_41.addWidget(self.listWidget_17, 0, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(397, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_41.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_44 = QtGui.QPushButton(self.tab_21)
        self.pushButton_44.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_44.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_44.setObjectName(_fromUtf8("pushButton_44"))
        self.gridLayout_41.addWidget(self.pushButton_44, 1, 1, 1, 1)
        self.pushButton_45 = QtGui.QPushButton(self.tab_21)
        self.pushButton_45.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_45.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_45.setObjectName(_fromUtf8("pushButton_45"))
        self.gridLayout_41.addWidget(self.pushButton_45, 1, 2, 1, 2)
        self.label_18 = QtGui.QLabel(self.tab_21)
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_41.addWidget(self.label_18, 2, 0, 1, 3)
        self.pushButton_46 = QtGui.QPushButton(self.tab_21)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)
        self.pushButton_46.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_46.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_46.setObjectName(_fromUtf8("pushButton_46"))
        self.gridLayout_41.addWidget(self.pushButton_46, 2, 3, 2, 1)
        self.progressBar_7 = QtGui.QProgressBar(self.tab_21)
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setObjectName(_fromUtf8("progressBar_7"))
        self.gridLayout_41.addWidget(self.progressBar_7, 3, 0, 1, 3)
        self.tabWidget_5.addTab(self.tab_21, _fromUtf8(""))
        self.tab_22 = QtGui.QWidget()
        self.tab_22.setObjectName(_fromUtf8("tab_22"))
        self.gridLayout_42 = QtGui.QGridLayout(self.tab_22)
        self.gridLayout_42.setObjectName(_fromUtf8("gridLayout_42"))
        self.label_19 = QtGui.QLabel(self.tab_22)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_42.addWidget(self.label_19, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_22, _fromUtf8(""))
        self.gridLayout_43.addWidget(self.tabWidget_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_17, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        self.gridLayout_55 = QtGui.QGridLayout(self.tab_23)
        self.gridLayout_55.setObjectName(_fromUtf8("gridLayout_55"))
        self.gridLayout_45 = QtGui.QGridLayout()
        self.gridLayout_45.setObjectName(_fromUtf8("gridLayout_45"))
        self.groupBox_30 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_30.setObjectName(_fromUtf8("groupBox_30"))
        self.gridLayout_104 = QtGui.QGridLayout(self.groupBox_30)
        self.gridLayout_104.setObjectName(_fromUtf8("gridLayout_104"))
        self.graphicsView_4 = QtGui.QGraphicsView(self.groupBox_30)
        self.graphicsView_4.setObjectName(_fromUtf8("graphicsView_4"))
        self.gridLayout_104.addWidget(self.graphicsView_4, 0, 0, 1, 1)
        self.gridLayout_45.addWidget(self.groupBox_30, 0, 0, 1, 1)
        self.groupBox_15 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_15.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_15.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.gridLayout_46 = QtGui.QGridLayout(self.groupBox_15)
        self.gridLayout_46.setObjectName(_fromUtf8("gridLayout_46"))
        spacerItem2 = QtGui.QSpacerItem(55, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_46.addItem(spacerItem2, 1, 0, 1, 1)
        self.pushButton_48 = QtGui.QPushButton(self.groupBox_15)
        self.pushButton_48.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_48.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_48.setIcon(icon)
        self.pushButton_48.setObjectName(_fromUtf8("pushButton_48"))
        self.gridLayout_46.addWidget(self.pushButton_48, 1, 1, 1, 1)
        self.pushButton_49 = QtGui.QPushButton(self.groupBox_15)
        self.pushButton_49.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_49.setObjectName(_fromUtf8("pushButton_49"))
        self.gridLayout_46.addWidget(self.pushButton_49, 1, 2, 1, 1)
        self.pushButton_50 = QtGui.QPushButton(self.groupBox_15)
        self.pushButton_50.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_50.setIcon(icon1)
        self.pushButton_50.setObjectName(_fromUtf8("pushButton_50"))
        self.gridLayout_46.addWidget(self.pushButton_50, 1, 3, 1, 1)
        self.listWidget_18 = QtGui.QListWidget(self.groupBox_15)
        self.listWidget_18.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_18.setObjectName(_fromUtf8("listWidget_18"))
        self.gridLayout_46.addWidget(self.listWidget_18, 0, 0, 1, 4)
        self.gridLayout_45.addWidget(self.groupBox_15, 1, 0, 1, 1)
        self.gridLayout_55.addLayout(self.gridLayout_45, 0, 0, 1, 1)
        self.gridLayout_47 = QtGui.QGridLayout()
        self.gridLayout_47.setObjectName(_fromUtf8("gridLayout_47"))
        self.label_27 = QtGui.QLabel(self.tab_23)
        self.label_27.setMinimumSize(QtCore.QSize(50, 0))
        self.label_27.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_47.addWidget(self.label_27, 0, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.tab_23)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(180, 0))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout_47.addWidget(self.lineEdit_9, 0, 1, 1, 1)
        self.groupBox_25 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_25.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox_25.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_25.setObjectName(_fromUtf8("groupBox_25"))
        self.gridLayout_48 = QtGui.QGridLayout(self.groupBox_25)
        self.gridLayout_48.setObjectName(_fromUtf8("gridLayout_48"))
        self.tabWidget_8 = QtGui.QTabWidget(self.groupBox_25)
        self.tabWidget_8.setEnabled(True)
        self.tabWidget_8.setDocumentMode(False)
        self.tabWidget_8.setTabsClosable(False)
        self.tabWidget_8.setMovable(False)
        self.tabWidget_8.setObjectName(_fromUtf8("tabWidget_8"))
        self.tab_26 = QtGui.QWidget()
        self.tab_26.setObjectName(_fromUtf8("tab_26"))
        self.gridLayout_49 = QtGui.QGridLayout(self.tab_26)
        self.gridLayout_49.setObjectName(_fromUtf8("gridLayout_49"))
        self.listWidget_19 = QtGui.QListWidget(self.tab_26)
        self.listWidget_19.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_19.setObjectName(_fromUtf8("listWidget_19"))
        self.gridLayout_49.addWidget(self.listWidget_19, 0, 0, 1, 2)
        self.pushButton_51 = QtGui.QPushButton(self.tab_26)
        self.pushButton_51.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_51.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_51.setIcon(icon)
        self.pushButton_51.setObjectName(_fromUtf8("pushButton_51"))
        self.gridLayout_49.addWidget(self.pushButton_51, 1, 0, 1, 1)
        self.pushButton_52 = QtGui.QPushButton(self.tab_26)
        self.pushButton_52.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_52.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_52.setIcon(icon1)
        self.pushButton_52.setObjectName(_fromUtf8("pushButton_52"))
        self.gridLayout_49.addWidget(self.pushButton_52, 1, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_26, _fromUtf8(""))
        self.tab_27 = QtGui.QWidget()
        self.tab_27.setObjectName(_fromUtf8("tab_27"))
        self.gridLayout_50 = QtGui.QGridLayout(self.tab_27)
        self.gridLayout_50.setObjectName(_fromUtf8("gridLayout_50"))
        self.listWidget_20 = QtGui.QListWidget(self.tab_27)
        self.listWidget_20.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_20.setObjectName(_fromUtf8("listWidget_20"))
        self.gridLayout_50.addWidget(self.listWidget_20, 0, 0, 1, 2)
        self.pushButton_53 = QtGui.QPushButton(self.tab_27)
        self.pushButton_53.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_53.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_53.setIcon(icon)
        self.pushButton_53.setObjectName(_fromUtf8("pushButton_53"))
        self.gridLayout_50.addWidget(self.pushButton_53, 1, 0, 1, 1)
        self.pushButton_54 = QtGui.QPushButton(self.tab_27)
        self.pushButton_54.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_54.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_54.setIcon(icon1)
        self.pushButton_54.setObjectName(_fromUtf8("pushButton_54"))
        self.gridLayout_50.addWidget(self.pushButton_54, 1, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_27, _fromUtf8(""))
        self.tab_28 = QtGui.QWidget()
        self.tab_28.setObjectName(_fromUtf8("tab_28"))
        self.gridLayout_51 = QtGui.QGridLayout(self.tab_28)
        self.gridLayout_51.setObjectName(_fromUtf8("gridLayout_51"))
        self.listWidget_21 = QtGui.QListWidget(self.tab_28)
        self.listWidget_21.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_21.setObjectName(_fromUtf8("listWidget_21"))
        self.gridLayout_51.addWidget(self.listWidget_21, 0, 0, 1, 2)
        self.pushButton_55 = QtGui.QPushButton(self.tab_28)
        self.pushButton_55.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_55.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_55.setIcon(icon)
        self.pushButton_55.setObjectName(_fromUtf8("pushButton_55"))
        self.gridLayout_51.addWidget(self.pushButton_55, 1, 0, 1, 1)
        self.pushButton_56 = QtGui.QPushButton(self.tab_28)
        self.pushButton_56.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_56.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_56.setIcon(icon1)
        self.pushButton_56.setObjectName(_fromUtf8("pushButton_56"))
        self.gridLayout_51.addWidget(self.pushButton_56, 1, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_28, _fromUtf8(""))
        self.tab_29 = QtGui.QWidget()
        self.tab_29.setObjectName(_fromUtf8("tab_29"))
        self.gridLayout_52 = QtGui.QGridLayout(self.tab_29)
        self.gridLayout_52.setObjectName(_fromUtf8("gridLayout_52"))
        self.listWidget_22 = QtGui.QListWidget(self.tab_29)
        self.listWidget_22.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_22.setObjectName(_fromUtf8("listWidget_22"))
        self.gridLayout_52.addWidget(self.listWidget_22, 0, 0, 1, 2)
        self.pushButton_57 = QtGui.QPushButton(self.tab_29)
        self.pushButton_57.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_57.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_57.setIcon(icon)
        self.pushButton_57.setObjectName(_fromUtf8("pushButton_57"))
        self.gridLayout_52.addWidget(self.pushButton_57, 1, 0, 1, 1)
        self.pushButton_58 = QtGui.QPushButton(self.tab_29)
        self.pushButton_58.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_58.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_58.setIcon(icon1)
        self.pushButton_58.setObjectName(_fromUtf8("pushButton_58"))
        self.gridLayout_52.addWidget(self.pushButton_58, 1, 1, 1, 1)
        self.tabWidget_8.addTab(self.tab_29, _fromUtf8(""))
        self.gridLayout_48.addWidget(self.tabWidget_8, 0, 0, 1, 1)
        self.gridLayout_47.addWidget(self.groupBox_25, 1, 0, 1, 2)
        self.groupBox_27 = QtGui.QGroupBox(self.tab_23)
        self.groupBox_27.setMinimumSize(QtCore.QSize(250, 0))
        self.groupBox_27.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_27.setObjectName(_fromUtf8("groupBox_27"))
        self.gridLayout_53 = QtGui.QGridLayout(self.groupBox_27)
        self.gridLayout_53.setObjectName(_fromUtf8("gridLayout_53"))
        self.checkBox_11 = QtGui.QCheckBox(self.groupBox_27)
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.gridLayout_53.addWidget(self.checkBox_11, 0, 0, 1, 1)
        self.groupBox_29 = QtGui.QGroupBox(self.groupBox_27)
        self.groupBox_29.setEnabled(True)
        self.groupBox_29.setCheckable(False)
        self.groupBox_29.setChecked(False)
        self.groupBox_29.setObjectName(_fromUtf8("groupBox_29"))
        self.gridLayout_54 = QtGui.QGridLayout(self.groupBox_29)
        self.gridLayout_54.setObjectName(_fromUtf8("gridLayout_54"))
        self.listWidget_23 = QtGui.QListWidget(self.groupBox_29)
        self.listWidget_23.setEnabled(True)
        self.listWidget_23.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_23.setObjectName(_fromUtf8("listWidget_23"))
        self.gridLayout_54.addWidget(self.listWidget_23, 2, 0, 1, 2)
        self.pushButton_59 = QtGui.QPushButton(self.groupBox_29)
        self.pushButton_59.setEnabled(True)
        self.pushButton_59.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_59.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_59.setIcon(icon)
        self.pushButton_59.setObjectName(_fromUtf8("pushButton_59"))
        self.gridLayout_54.addWidget(self.pushButton_59, 3, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(89, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem3, 3, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_29)
        self.checkBox_2.setEnabled(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_54.addWidget(self.checkBox_2, 1, 0, 1, 2)
        self.gridLayout_53.addWidget(self.groupBox_29, 1, 0, 1, 1)
        self.gridLayout_47.addWidget(self.groupBox_27, 2, 0, 1, 2)
        self.gridLayout_55.addLayout(self.gridLayout_47, 0, 1, 1, 1)
        self.gridLayout_44 = QtGui.QGridLayout()
        self.gridLayout_44.setObjectName(_fromUtf8("gridLayout_44"))
        self.progressBar_8 = QtGui.QProgressBar(self.tab_23)
        self.progressBar_8.setProperty("value", 0)
        self.progressBar_8.setObjectName(_fromUtf8("progressBar_8"))
        self.gridLayout_44.addWidget(self.progressBar_8, 0, 0, 1, 1)
        self.pushButton_47 = QtGui.QPushButton(self.tab_23)
        self.pushButton_47.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_47.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_47.setObjectName(_fromUtf8("pushButton_47"))
        self.gridLayout_44.addWidget(self.pushButton_47, 0, 1, 2, 1)
        self.progressBar_9 = QtGui.QProgressBar(self.tab_23)
        self.progressBar_9.setProperty("value", 0)
        self.progressBar_9.setObjectName(_fromUtf8("progressBar_9"))
        self.gridLayout_44.addWidget(self.progressBar_9, 1, 0, 1, 1)
        self.gridLayout_55.addLayout(self.gridLayout_44, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_23, _fromUtf8(""))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        self.gridLayout_113 = QtGui.QGridLayout(self.tab_24)
        self.gridLayout_113.setObjectName(_fromUtf8("gridLayout_113"))
        self.tabWidget_6 = QtGui.QTabWidget(self.tab_24)
        self.tabWidget_6.setObjectName(_fromUtf8("tabWidget_6"))
        self.tab_35 = QtGui.QWidget()
        self.tab_35.setObjectName(_fromUtf8("tab_35"))
        self.gridLayout_82 = QtGui.QGridLayout(self.tab_35)
        self.gridLayout_82.setObjectName(_fromUtf8("gridLayout_82"))
        self.groupBox_34 = QtGui.QGroupBox(self.tab_35)
        self.groupBox_34.setObjectName(_fromUtf8("groupBox_34"))
        self.gridLayout_83 = QtGui.QGridLayout(self.groupBox_34)
        self.gridLayout_83.setObjectName(_fromUtf8("gridLayout_83"))
        self.label_55 = QtGui.QLabel(self.groupBox_34)
        self.label_55.setMinimumSize(QtCore.QSize(20, 0))
        self.label_55.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.gridLayout_83.addWidget(self.label_55, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(529, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_83.addItem(spacerItem4, 0, 3, 1, 1)
        self.label_56 = QtGui.QLabel(self.groupBox_34)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.gridLayout_83.addWidget(self.label_56, 1, 2, 1, 1)
        self.dial_2 = QtGui.QDial(self.groupBox_34)
        self.dial_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dial_2.setMouseTracking(True)
        self.dial_2.setMinimum(1)
        self.dial_2.setMaximum(8)
        self.dial_2.setPageStep(1)
        self.dial_2.setSliderPosition(1)
        self.dial_2.setOrientation(QtCore.Qt.Horizontal)
        self.dial_2.setInvertedAppearance(False)
        self.dial_2.setInvertedControls(False)
        self.dial_2.setWrapping(False)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName(_fromUtf8("dial_2"))
        self.gridLayout_83.addWidget(self.dial_2, 0, 0, 1, 3)
        self.label_58 = QtGui.QLabel(self.groupBox_34)
        self.label_58.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_58.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.gridLayout_83.addWidget(self.label_58, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_83.addItem(spacerItem5, 2, 1, 1, 1)
        self.gridLayout_82.addWidget(self.groupBox_34, 0, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_35, _fromUtf8(""))
        self.tab_36 = QtGui.QWidget()
        self.tab_36.setObjectName(_fromUtf8("tab_36"))
        self.gridLayout_85 = QtGui.QGridLayout(self.tab_36)
        self.gridLayout_85.setObjectName(_fromUtf8("gridLayout_85"))
        self.groupBox_35 = QtGui.QGroupBox(self.tab_36)
        self.groupBox_35.setFlat(True)
        self.groupBox_35.setObjectName(_fromUtf8("groupBox_35"))
        self.gridLayout_86 = QtGui.QGridLayout(self.groupBox_35)
        self.gridLayout_86.setObjectName(_fromUtf8("gridLayout_86"))
        self.gridLayout_87 = QtGui.QGridLayout()
        self.gridLayout_87.setObjectName(_fromUtf8("gridLayout_87"))
        self.label_59 = QtGui.QLabel(self.groupBox_35)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_87.addWidget(self.label_59, 0, 0, 1, 1)
        self.comboBox_12 = QtGui.QComboBox(self.groupBox_35)
        self.comboBox_12.setObjectName(_fromUtf8("comboBox_12"))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.comboBox_12.addItem(_fromUtf8(""))
        self.gridLayout_87.addWidget(self.comboBox_12, 0, 1, 1, 1)
        self.label_60 = QtGui.QLabel(self.groupBox_35)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_87.addWidget(self.label_60, 1, 0, 1, 1)
        self.comboBox_13 = QtGui.QComboBox(self.groupBox_35)
        self.comboBox_13.setObjectName(_fromUtf8("comboBox_13"))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.comboBox_13.addItem(_fromUtf8(""))
        self.gridLayout_87.addWidget(self.comboBox_13, 1, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.groupBox_35)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_87.addWidget(self.label_61, 2, 0, 1, 1)
        self.lineEdit_21 = QtGui.QLineEdit(self.groupBox_35)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.gridLayout_87.addWidget(self.lineEdit_21, 2, 1, 1, 1)
        self.gridLayout_86.addLayout(self.gridLayout_87, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(20, 142, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_86.addItem(spacerItem6, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.groupBox_35, 0, 0, 1, 1)
        self.groupBox_37 = QtGui.QGroupBox(self.tab_36)
        self.groupBox_37.setObjectName(_fromUtf8("groupBox_37"))
        self.gridLayout_88 = QtGui.QGridLayout(self.groupBox_37)
        self.gridLayout_88.setObjectName(_fromUtf8("gridLayout_88"))
        self.gridLayout_89 = QtGui.QGridLayout()
        self.gridLayout_89.setObjectName(_fromUtf8("gridLayout_89"))
        self.label_62 = QtGui.QLabel(self.groupBox_37)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_89.addWidget(self.label_62, 0, 0, 1, 1)
        self.comboBox_14 = QtGui.QComboBox(self.groupBox_37)
        self.comboBox_14.setObjectName(_fromUtf8("comboBox_14"))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.comboBox_14.addItem(_fromUtf8(""))
        self.gridLayout_89.addWidget(self.comboBox_14, 0, 1, 1, 1)
        self.label_63 = QtGui.QLabel(self.groupBox_37)
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.gridLayout_89.addWidget(self.label_63, 1, 0, 1, 1)
        self.comboBox_15 = QtGui.QComboBox(self.groupBox_37)
        self.comboBox_15.setObjectName(_fromUtf8("comboBox_15"))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.comboBox_15.addItem(_fromUtf8(""))
        self.gridLayout_89.addWidget(self.comboBox_15, 1, 1, 1, 1)
        self.label_71 = QtGui.QLabel(self.groupBox_37)
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.gridLayout_89.addWidget(self.label_71, 2, 0, 1, 1)
        self.comboBox_16 = QtGui.QComboBox(self.groupBox_37)
        self.comboBox_16.setObjectName(_fromUtf8("comboBox_16"))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.comboBox_16.addItem(_fromUtf8(""))
        self.gridLayout_89.addWidget(self.comboBox_16, 2, 1, 1, 1)
        self.label_80 = QtGui.QLabel(self.groupBox_37)
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.gridLayout_89.addWidget(self.label_80, 3, 0, 1, 1)
        self.lineEdit_30 = QtGui.QLineEdit(self.groupBox_37)
        self.lineEdit_30.setObjectName(_fromUtf8("lineEdit_30"))
        self.gridLayout_89.addWidget(self.lineEdit_30, 3, 1, 1, 1)
        self.gridLayout_88.addLayout(self.gridLayout_89, 0, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 113, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_88.addItem(spacerItem7, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.groupBox_37, 0, 1, 1, 1)
        self.groupBox_38 = QtGui.QGroupBox(self.tab_36)
        self.groupBox_38.setObjectName(_fromUtf8("groupBox_38"))
        self.gridLayout_90 = QtGui.QGridLayout(self.groupBox_38)
        self.gridLayout_90.setObjectName(_fromUtf8("gridLayout_90"))
        self.gridLayout_92 = QtGui.QGridLayout()
        self.gridLayout_92.setObjectName(_fromUtf8("gridLayout_92"))
        self.label_81 = QtGui.QLabel(self.groupBox_38)
        self.label_81.setObjectName(_fromUtf8("label_81"))
        self.gridLayout_92.addWidget(self.label_81, 0, 0, 1, 1)
        self.comboBox_17 = QtGui.QComboBox(self.groupBox_38)
        self.comboBox_17.setObjectName(_fromUtf8("comboBox_17"))
        self.comboBox_17.addItem(_fromUtf8(""))
        self.comboBox_17.addItem(_fromUtf8(""))
        self.gridLayout_92.addWidget(self.comboBox_17, 0, 1, 1, 1)
        self.label_82 = QtGui.QLabel(self.groupBox_38)
        self.label_82.setObjectName(_fromUtf8("label_82"))
        self.gridLayout_92.addWidget(self.label_82, 1, 0, 1, 1)
        self.comboBox_18 = QtGui.QComboBox(self.groupBox_38)
        self.comboBox_18.setObjectName(_fromUtf8("comboBox_18"))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.comboBox_18.addItem(_fromUtf8(""))
        self.gridLayout_92.addWidget(self.comboBox_18, 1, 1, 1, 1)
        self.label_83 = QtGui.QLabel(self.groupBox_38)
        self.label_83.setObjectName(_fromUtf8("label_83"))
        self.gridLayout_92.addWidget(self.label_83, 2, 0, 1, 1)
        self.comboBox_19 = QtGui.QComboBox(self.groupBox_38)
        self.comboBox_19.setObjectName(_fromUtf8("comboBox_19"))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.comboBox_19.addItem(_fromUtf8(""))
        self.gridLayout_92.addWidget(self.comboBox_19, 2, 1, 1, 1)
        self.label_84 = QtGui.QLabel(self.groupBox_38)
        self.label_84.setObjectName(_fromUtf8("label_84"))
        self.gridLayout_92.addWidget(self.label_84, 3, 0, 1, 1)
        self.lineEdit_31 = QtGui.QLineEdit(self.groupBox_38)
        self.lineEdit_31.setText(_fromUtf8(""))
        self.lineEdit_31.setObjectName(_fromUtf8("lineEdit_31"))
        self.gridLayout_92.addWidget(self.lineEdit_31, 3, 1, 1, 1)
        self.gridLayout_90.addLayout(self.gridLayout_92, 0, 0, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 113, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_90.addItem(spacerItem8, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.groupBox_38, 1, 0, 1, 1)
        self.groupBox_39 = QtGui.QGroupBox(self.tab_36)
        self.groupBox_39.setObjectName(_fromUtf8("groupBox_39"))
        self.gridLayout_93 = QtGui.QGridLayout(self.groupBox_39)
        self.gridLayout_93.setObjectName(_fromUtf8("gridLayout_93"))
        self.gridLayout_94 = QtGui.QGridLayout()
        self.gridLayout_94.setObjectName(_fromUtf8("gridLayout_94"))
        self.label_85 = QtGui.QLabel(self.groupBox_39)
        self.label_85.setObjectName(_fromUtf8("label_85"))
        self.gridLayout_94.addWidget(self.label_85, 0, 0, 1, 1)
        self.comboBox_20 = QtGui.QComboBox(self.groupBox_39)
        self.comboBox_20.setObjectName(_fromUtf8("comboBox_20"))
        self.comboBox_20.addItem(_fromUtf8(""))
        self.comboBox_20.addItem(_fromUtf8(""))
        self.gridLayout_94.addWidget(self.comboBox_20, 0, 1, 1, 1)
        self.label_86 = QtGui.QLabel(self.groupBox_39)
        self.label_86.setObjectName(_fromUtf8("label_86"))
        self.gridLayout_94.addWidget(self.label_86, 1, 0, 1, 1)
        self.lineEdit_32 = QtGui.QLineEdit(self.groupBox_39)
        self.lineEdit_32.setText(_fromUtf8(""))
        self.lineEdit_32.setObjectName(_fromUtf8("lineEdit_32"))
        self.gridLayout_94.addWidget(self.lineEdit_32, 1, 1, 1, 1)
        self.gridLayout_93.addLayout(self.gridLayout_94, 0, 0, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 171, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_93.addItem(spacerItem9, 1, 0, 1, 1)
        self.gridLayout_85.addWidget(self.groupBox_39, 1, 1, 1, 1)
        self.tabWidget_6.addTab(self.tab_36, _fromUtf8(""))
        self.tab_37 = QtGui.QWidget()
        self.tab_37.setObjectName(_fromUtf8("tab_37"))
        self.gridLayout_95 = QtGui.QGridLayout(self.tab_37)
        self.gridLayout_95.setObjectName(_fromUtf8("gridLayout_95"))
        self.gridLayout_96 = QtGui.QGridLayout()
        self.gridLayout_96.setObjectName(_fromUtf8("gridLayout_96"))
        self.groupBox_40 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_40.setObjectName(_fromUtf8("groupBox_40"))
        self.gridLayout_97 = QtGui.QGridLayout(self.groupBox_40)
        self.gridLayout_97.setObjectName(_fromUtf8("gridLayout_97"))
        self.label_87 = QtGui.QLabel(self.groupBox_40)
        self.label_87.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_87.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_87.setObjectName(_fromUtf8("label_87"))
        self.gridLayout_97.addWidget(self.label_87, 0, 0, 1, 1)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.groupBox_40)
        self.doubleSpinBox_8.setDecimals(0)
        self.doubleSpinBox_8.setMaximum(1000.0)
        self.doubleSpinBox_8.setProperty("value", 25.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.gridLayout_97.addWidget(self.doubleSpinBox_8, 0, 1, 1, 1)
        self.label_88 = QtGui.QLabel(self.groupBox_40)
        self.label_88.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_88.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_88.setObjectName(_fromUtf8("label_88"))
        self.gridLayout_97.addWidget(self.label_88, 1, 0, 1, 1)
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(self.groupBox_40)
        self.doubleSpinBox_9.setDecimals(0)
        self.doubleSpinBox_9.setMaximum(1000.0)
        self.doubleSpinBox_9.setProperty("value", 5.0)
        self.doubleSpinBox_9.setObjectName(_fromUtf8("doubleSpinBox_9"))
        self.gridLayout_97.addWidget(self.doubleSpinBox_9, 1, 1, 1, 1)
        self.label_89 = QtGui.QLabel(self.groupBox_40)
        self.label_89.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_89.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_89.setObjectName(_fromUtf8("label_89"))
        self.gridLayout_97.addWidget(self.label_89, 2, 0, 1, 1)
        self.doubleSpinBox_15 = QtGui.QDoubleSpinBox(self.groupBox_40)
        self.doubleSpinBox_15.setDecimals(0)
        self.doubleSpinBox_15.setMaximum(1000.0)
        self.doubleSpinBox_15.setProperty("value", 10.0)
        self.doubleSpinBox_15.setObjectName(_fromUtf8("doubleSpinBox_15"))
        self.gridLayout_97.addWidget(self.doubleSpinBox_15, 2, 1, 1, 1)
        self.gridLayout_96.addWidget(self.groupBox_40, 0, 0, 1, 1)
        self.groupBox_41 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_41.setObjectName(_fromUtf8("groupBox_41"))
        self.gridLayout_98 = QtGui.QGridLayout(self.groupBox_41)
        self.gridLayout_98.setObjectName(_fromUtf8("gridLayout_98"))
        self.label_90 = QtGui.QLabel(self.groupBox_41)
        self.label_90.setObjectName(_fromUtf8("label_90"))
        self.gridLayout_98.addWidget(self.label_90, 1, 0, 1, 1)
        self.lineEdit_33 = QtGui.QLineEdit(self.groupBox_41)
        self.lineEdit_33.setObjectName(_fromUtf8("lineEdit_33"))
        self.gridLayout_98.addWidget(self.lineEdit_33, 0, 1, 1, 1)
        self.label_91 = QtGui.QLabel(self.groupBox_41)
        self.label_91.setObjectName(_fromUtf8("label_91"))
        self.gridLayout_98.addWidget(self.label_91, 0, 0, 1, 1)
        self.lineEdit_34 = QtGui.QLineEdit(self.groupBox_41)
        self.lineEdit_34.setMaxLength(8)
        self.lineEdit_34.setObjectName(_fromUtf8("lineEdit_34"))
        self.gridLayout_98.addWidget(self.lineEdit_34, 1, 1, 1, 1)
        self.gridLayout_96.addWidget(self.groupBox_41, 1, 0, 1, 1)
        self.groupBox_42 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_42.setObjectName(_fromUtf8("groupBox_42"))
        self.gridLayout_99 = QtGui.QGridLayout(self.groupBox_42)
        self.gridLayout_99.setObjectName(_fromUtf8("gridLayout_99"))
        self.label_92 = QtGui.QLabel(self.groupBox_42)
        self.label_92.setObjectName(_fromUtf8("label_92"))
        self.gridLayout_99.addWidget(self.label_92, 0, 0, 1, 1)
        self.lineEdit_35 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_35.setObjectName(_fromUtf8("lineEdit_35"))
        self.gridLayout_99.addWidget(self.lineEdit_35, 0, 1, 1, 1)
        self.label_93 = QtGui.QLabel(self.groupBox_42)
        self.label_93.setObjectName(_fromUtf8("label_93"))
        self.gridLayout_99.addWidget(self.label_93, 1, 0, 1, 1)
        self.lineEdit_36 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_36.setObjectName(_fromUtf8("lineEdit_36"))
        self.gridLayout_99.addWidget(self.lineEdit_36, 1, 1, 1, 1)
        self.label_94 = QtGui.QLabel(self.groupBox_42)
        self.label_94.setObjectName(_fromUtf8("label_94"))
        self.gridLayout_99.addWidget(self.label_94, 2, 0, 1, 1)
        self.lineEdit_37 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_37.setObjectName(_fromUtf8("lineEdit_37"))
        self.gridLayout_99.addWidget(self.lineEdit_37, 2, 1, 1, 1)
        self.label_95 = QtGui.QLabel(self.groupBox_42)
        self.label_95.setObjectName(_fromUtf8("label_95"))
        self.gridLayout_99.addWidget(self.label_95, 3, 0, 1, 1)
        self.lineEdit_38 = QtGui.QLineEdit(self.groupBox_42)
        self.lineEdit_38.setText(_fromUtf8(""))
        self.lineEdit_38.setObjectName(_fromUtf8("lineEdit_38"))
        self.gridLayout_99.addWidget(self.lineEdit_38, 3, 1, 1, 1)
        self.gridLayout_96.addWidget(self.groupBox_42, 2, 0, 1, 1)
        self.groupBox_43 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_43.setObjectName(_fromUtf8("groupBox_43"))
        self.gridLayout_100 = QtGui.QGridLayout(self.groupBox_43)
        self.gridLayout_100.setObjectName(_fromUtf8("gridLayout_100"))
        self.label_96 = QtGui.QLabel(self.groupBox_43)
        self.label_96.setObjectName(_fromUtf8("label_96"))
        self.gridLayout_100.addWidget(self.label_96, 0, 0, 1, 1)
        self.lineEdit_39 = QtGui.QLineEdit(self.groupBox_43)
        self.lineEdit_39.setObjectName(_fromUtf8("lineEdit_39"))
        self.gridLayout_100.addWidget(self.lineEdit_39, 0, 1, 1, 1)
        self.label_97 = QtGui.QLabel(self.groupBox_43)
        self.label_97.setObjectName(_fromUtf8("label_97"))
        self.gridLayout_100.addWidget(self.label_97, 1, 0, 1, 1)
        self.lineEdit_40 = QtGui.QLineEdit(self.groupBox_43)
        self.lineEdit_40.setObjectName(_fromUtf8("lineEdit_40"))
        self.gridLayout_100.addWidget(self.lineEdit_40, 1, 1, 1, 1)
        self.gridLayout_96.addWidget(self.groupBox_43, 3, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_96, 0, 0, 1, 1)
        self.gridLayout_101 = QtGui.QGridLayout()
        self.gridLayout_101.setObjectName(_fromUtf8("gridLayout_101"))
        self.groupBox_44 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_44.setMinimumSize(QtCore.QSize(250, 160))
        self.groupBox_44.setObjectName(_fromUtf8("groupBox_44"))
        self.gridLayout_102 = QtGui.QGridLayout(self.groupBox_44)
        self.gridLayout_102.setObjectName(_fromUtf8("gridLayout_102"))
        self.label_98 = QtGui.QLabel(self.groupBox_44)
        self.label_98.setObjectName(_fromUtf8("label_98"))
        self.gridLayout_102.addWidget(self.label_98, 2, 0, 1, 1)
        self.lineEdit_41 = QtGui.QLineEdit(self.groupBox_44)
        self.lineEdit_41.setObjectName(_fromUtf8("lineEdit_41"))
        self.gridLayout_102.addWidget(self.lineEdit_41, 6, 2, 1, 1)
        self.label_99 = QtGui.QLabel(self.groupBox_44)
        self.label_99.setObjectName(_fromUtf8("label_99"))
        self.gridLayout_102.addWidget(self.label_99, 0, 0, 1, 1)
        self.lineEdit_42 = QtGui.QLineEdit(self.groupBox_44)
        self.lineEdit_42.setObjectName(_fromUtf8("lineEdit_42"))
        self.gridLayout_102.addWidget(self.lineEdit_42, 0, 2, 1, 1)
        self.lineEdit_43 = QtGui.QLineEdit(self.groupBox_44)
        self.lineEdit_43.setObjectName(_fromUtf8("lineEdit_43"))
        self.gridLayout_102.addWidget(self.lineEdit_43, 2, 2, 1, 1)
        self.label_100 = QtGui.QLabel(self.groupBox_44)
        self.label_100.setObjectName(_fromUtf8("label_100"))
        self.gridLayout_102.addWidget(self.label_100, 5, 0, 1, 1)
        self.lineEdit_44 = QtGui.QLineEdit(self.groupBox_44)
        self.lineEdit_44.setObjectName(_fromUtf8("lineEdit_44"))
        self.gridLayout_102.addWidget(self.lineEdit_44, 5, 2, 1, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_44)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_102.addWidget(self.checkBox_5, 6, 0, 1, 1)
        self.checkBox_13 = QtGui.QCheckBox(self.groupBox_44)
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.gridLayout_102.addWidget(self.checkBox_13, 1, 0, 1, 3)
        self.gridLayout_101.addWidget(self.groupBox_44, 0, 0, 1, 1)
        self.groupBox_45 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_45.setObjectName(_fromUtf8("groupBox_45"))
        self.gridLayout_103 = QtGui.QGridLayout(self.groupBox_45)
        self.gridLayout_103.setObjectName(_fromUtf8("gridLayout_103"))
        self.label_101 = QtGui.QLabel(self.groupBox_45)
        self.label_101.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_101.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_101.setObjectName(_fromUtf8("label_101"))
        self.gridLayout_103.addWidget(self.label_101, 0, 0, 1, 1)
        self.doubleSpinBox_16 = QtGui.QDoubleSpinBox(self.groupBox_45)
        self.doubleSpinBox_16.setEnabled(False)
        self.doubleSpinBox_16.setDecimals(0)
        self.doubleSpinBox_16.setMinimum(2.0)
        self.doubleSpinBox_16.setMaximum(100.0)
        self.doubleSpinBox_16.setProperty("value", 2.0)
        self.doubleSpinBox_16.setObjectName(_fromUtf8("doubleSpinBox_16"))
        self.gridLayout_103.addWidget(self.doubleSpinBox_16, 0, 1, 1, 1)
        self.label_102 = QtGui.QLabel(self.groupBox_45)
        self.label_102.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_102.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_102.setObjectName(_fromUtf8("label_102"))
        self.gridLayout_103.addWidget(self.label_102, 1, 0, 1, 1)
        self.doubleSpinBox_17 = QtGui.QDoubleSpinBox(self.groupBox_45)
        self.doubleSpinBox_17.setEnabled(False)
        self.doubleSpinBox_17.setDecimals(0)
        self.doubleSpinBox_17.setMinimum(1.0)
        self.doubleSpinBox_17.setMaximum(100.0)
        self.doubleSpinBox_17.setProperty("value", 4.0)
        self.doubleSpinBox_17.setObjectName(_fromUtf8("doubleSpinBox_17"))
        self.gridLayout_103.addWidget(self.doubleSpinBox_17, 1, 1, 1, 1)
        self.label_103 = QtGui.QLabel(self.groupBox_45)
        self.label_103.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_103.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_103.setObjectName(_fromUtf8("label_103"))
        self.gridLayout_103.addWidget(self.label_103, 2, 0, 1, 1)
        self.doubleSpinBox_18 = QtGui.QDoubleSpinBox(self.groupBox_45)
        self.doubleSpinBox_18.setEnabled(False)
        self.doubleSpinBox_18.setDecimals(0)
        self.doubleSpinBox_18.setMinimum(1.0)
        self.doubleSpinBox_18.setMaximum(100.0)
        self.doubleSpinBox_18.setProperty("value", 9.0)
        self.doubleSpinBox_18.setObjectName(_fromUtf8("doubleSpinBox_18"))
        self.gridLayout_103.addWidget(self.doubleSpinBox_18, 2, 1, 1, 1)
        self.doubleSpinBox_19 = QtGui.QDoubleSpinBox(self.groupBox_45)
        self.doubleSpinBox_19.setDecimals(0)
        self.doubleSpinBox_19.setMinimum(1.0)
        self.doubleSpinBox_19.setMaximum(10000.0)
        self.doubleSpinBox_19.setProperty("value", 25.0)
        self.doubleSpinBox_19.setObjectName(_fromUtf8("doubleSpinBox_19"))
        self.gridLayout_103.addWidget(self.doubleSpinBox_19, 4, 1, 1, 1)
        self.label_104 = QtGui.QLabel(self.groupBox_45)
        self.label_104.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_104.setObjectName(_fromUtf8("label_104"))
        self.gridLayout_103.addWidget(self.label_104, 4, 0, 1, 1)
        self.gridLayout_101.addWidget(self.groupBox_45, 1, 0, 1, 1)
        self.groupBox_46 = QtGui.QGroupBox(self.tab_37)
        self.groupBox_46.setObjectName(_fromUtf8("groupBox_46"))
        self.gridLayout_105 = QtGui.QGridLayout(self.groupBox_46)
        self.gridLayout_105.setObjectName(_fromUtf8("gridLayout_105"))
        self.pushButton_66 = QtGui.QPushButton(self.groupBox_46)
        self.pushButton_66.setObjectName(_fromUtf8("pushButton_66"))
        self.gridLayout_105.addWidget(self.pushButton_66, 1, 1, 1, 1)
        self.listWidget_26 = QtGui.QListWidget(self.groupBox_46)
        self.listWidget_26.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_26.setObjectName(_fromUtf8("listWidget_26"))
        self.gridLayout_105.addWidget(self.listWidget_26, 0, 2, 3, 1)
        self.pushButton_67 = QtGui.QPushButton(self.groupBox_46)
        self.pushButton_67.setObjectName(_fromUtf8("pushButton_67"))
        self.gridLayout_105.addWidget(self.pushButton_67, 0, 1, 1, 1)
        self.pushButton_68 = QtGui.QPushButton(self.groupBox_46)
        self.pushButton_68.setObjectName(_fromUtf8("pushButton_68"))
        self.gridLayout_105.addWidget(self.pushButton_68, 2, 1, 1, 1)
        self.listWidget_27 = QtGui.QListWidget(self.groupBox_46)
        self.listWidget_27.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_27.setObjectName(_fromUtf8("listWidget_27"))
        self.gridLayout_105.addWidget(self.listWidget_27, 0, 0, 3, 1)
        self.gridLayout_101.addWidget(self.groupBox_46, 2, 0, 1, 1)
        self.gridLayout_95.addLayout(self.gridLayout_101, 0, 1, 1, 1)
        self.tabWidget_6.addTab(self.tab_37, _fromUtf8(""))
        self.tab_38 = QtGui.QWidget()
        self.tab_38.setObjectName(_fromUtf8("tab_38"))
        self.gridLayout_106 = QtGui.QGridLayout(self.tab_38)
        self.gridLayout_106.setObjectName(_fromUtf8("gridLayout_106"))
        self.gridLayout_107 = QtGui.QGridLayout()
        self.gridLayout_107.setObjectName(_fromUtf8("gridLayout_107"))
        self.checkBox_17 = QtGui.QCheckBox(self.tab_38)
        self.checkBox_17.setChecked(True)
        self.checkBox_17.setObjectName(_fromUtf8("checkBox_17"))
        self.gridLayout_107.addWidget(self.checkBox_17, 0, 0, 1, 2)
        self.label_105 = QtGui.QLabel(self.tab_38)
        self.label_105.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_105.setObjectName(_fromUtf8("label_105"))
        self.gridLayout_107.addWidget(self.label_105, 1, 0, 1, 1)
        self.doubleSpinBox_20 = QtGui.QDoubleSpinBox(self.tab_38)
        self.doubleSpinBox_20.setDecimals(7)
        self.doubleSpinBox_20.setMaximum(100000000.0)
        self.doubleSpinBox_20.setSingleStep(0.1)
        self.doubleSpinBox_20.setProperty("value", 2.2)
        self.doubleSpinBox_20.setObjectName(_fromUtf8("doubleSpinBox_20"))
        self.gridLayout_107.addWidget(self.doubleSpinBox_20, 1, 1, 1, 1)
        self.label_106 = QtGui.QLabel(self.tab_38)
        self.label_106.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_106.setObjectName(_fromUtf8("label_106"))
        self.gridLayout_107.addWidget(self.label_106, 2, 0, 1, 1)
        self.doubleSpinBox_21 = QtGui.QDoubleSpinBox(self.tab_38)
        self.doubleSpinBox_21.setDecimals(7)
        self.doubleSpinBox_21.setMaximum(100000000.0)
        self.doubleSpinBox_21.setSingleStep(0.1)
        self.doubleSpinBox_21.setProperty("value", 10.0)
        self.doubleSpinBox_21.setObjectName(_fromUtf8("doubleSpinBox_21"))
        self.gridLayout_107.addWidget(self.doubleSpinBox_21, 2, 1, 1, 1)
        self.label_107 = QtGui.QLabel(self.tab_38)
        self.label_107.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_107.setObjectName(_fromUtf8("label_107"))
        self.gridLayout_107.addWidget(self.label_107, 3, 0, 1, 1)
        self.doubleSpinBox_22 = QtGui.QDoubleSpinBox(self.tab_38)
        self.doubleSpinBox_22.setDecimals(7)
        self.doubleSpinBox_22.setMaximum(100000000.0)
        self.doubleSpinBox_22.setSingleStep(0.1)
        self.doubleSpinBox_22.setProperty("value", 5.0)
        self.doubleSpinBox_22.setObjectName(_fromUtf8("doubleSpinBox_22"))
        self.gridLayout_107.addWidget(self.doubleSpinBox_22, 3, 1, 1, 1)
        self.label_108 = QtGui.QLabel(self.tab_38)
        self.label_108.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_108.setObjectName(_fromUtf8("label_108"))
        self.gridLayout_107.addWidget(self.label_108, 4, 0, 1, 1)
        self.doubleSpinBox_23 = QtGui.QDoubleSpinBox(self.tab_38)
        self.doubleSpinBox_23.setDecimals(7)
        self.doubleSpinBox_23.setMaximum(100000000.0)
        self.doubleSpinBox_23.setSingleStep(0.1)
        self.doubleSpinBox_23.setProperty("value", 0.3)
        self.doubleSpinBox_23.setObjectName(_fromUtf8("doubleSpinBox_23"))
        self.gridLayout_107.addWidget(self.doubleSpinBox_23, 4, 1, 1, 1)
        self.label_109 = QtGui.QLabel(self.tab_38)
        self.label_109.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_109.setObjectName(_fromUtf8("label_109"))
        self.gridLayout_107.addWidget(self.label_109, 5, 0, 1, 1)
        self.doubleSpinBox_24 = QtGui.QDoubleSpinBox(self.tab_38)
        self.doubleSpinBox_24.setDecimals(7)
        self.doubleSpinBox_24.setMaximum(100000000.0)
        self.doubleSpinBox_24.setSingleStep(0.1)
        self.doubleSpinBox_24.setProperty("value", 5.0)
        self.doubleSpinBox_24.setObjectName(_fromUtf8("doubleSpinBox_24"))
        self.gridLayout_107.addWidget(self.doubleSpinBox_24, 5, 1, 1, 1)
        self.gridLayout_106.addLayout(self.gridLayout_107, 0, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 300, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_106.addItem(spacerItem10, 1, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_38, _fromUtf8(""))
        self.tab_39 = QtGui.QWidget()
        self.tab_39.setObjectName(_fromUtf8("tab_39"))
        self.gridLayout_108 = QtGui.QGridLayout(self.tab_39)
        self.gridLayout_108.setObjectName(_fromUtf8("gridLayout_108"))
        self.label_110 = QtGui.QLabel(self.tab_39)
        self.label_110.setObjectName(_fromUtf8("label_110"))
        self.gridLayout_108.addWidget(self.label_110, 0, 0, 1, 1)
        self.lineEdit_45 = QtGui.QLineEdit(self.tab_39)
        self.lineEdit_45.setObjectName(_fromUtf8("lineEdit_45"))
        self.gridLayout_108.addWidget(self.lineEdit_45, 0, 1, 1, 1)
        self.label_111 = QtGui.QLabel(self.tab_39)
        self.label_111.setObjectName(_fromUtf8("label_111"))
        self.gridLayout_108.addWidget(self.label_111, 1, 0, 1, 1)
        self.lineEdit_46 = QtGui.QLineEdit(self.tab_39)
        self.lineEdit_46.setObjectName(_fromUtf8("lineEdit_46"))
        self.gridLayout_108.addWidget(self.lineEdit_46, 1, 1, 1, 1)
        self.groupBox_47 = QtGui.QGroupBox(self.tab_39)
        self.groupBox_47.setObjectName(_fromUtf8("groupBox_47"))
        self.gridLayout_109 = QtGui.QGridLayout(self.groupBox_47)
        self.gridLayout_109.setObjectName(_fromUtf8("gridLayout_109"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_47)
        self.radioButton_4.setChecked(False)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout_109.addWidget(self.radioButton_4, 0, 0, 1, 1)
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_47)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.gridLayout_109.addWidget(self.radioButton_5, 1, 0, 1, 1)
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_47)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.gridLayout_109.addWidget(self.radioButton_6, 2, 0, 1, 1)
        self.gridLayout_108.addWidget(self.groupBox_47, 2, 0, 1, 2)
        self.checkBox_20 = QtGui.QCheckBox(self.tab_39)
        self.checkBox_20.setChecked(True)
        self.checkBox_20.setObjectName(_fromUtf8("checkBox_20"))
        self.gridLayout_108.addWidget(self.checkBox_20, 3, 0, 1, 2)
        self.checkBox_21 = QtGui.QCheckBox(self.tab_39)
        self.checkBox_21.setObjectName(_fromUtf8("checkBox_21"))
        self.gridLayout_108.addWidget(self.checkBox_21, 4, 0, 1, 2)
        spacerItem11 = QtGui.QSpacerItem(20, 253, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_108.addItem(spacerItem11, 5, 0, 1, 2)
        self.tabWidget_6.addTab(self.tab_39, _fromUtf8(""))
        self.tab_40 = QtGui.QWidget()
        self.tab_40.setObjectName(_fromUtf8("tab_40"))
        self.gridLayout_110 = QtGui.QGridLayout(self.tab_40)
        self.gridLayout_110.setObjectName(_fromUtf8("gridLayout_110"))
        self.groupBox_48 = QtGui.QGroupBox(self.tab_40)
        self.groupBox_48.setObjectName(_fromUtf8("groupBox_48"))
        self.gridLayout_111 = QtGui.QGridLayout(self.groupBox_48)
        self.gridLayout_111.setObjectName(_fromUtf8("gridLayout_111"))
        self.label_112 = QtGui.QLabel(self.groupBox_48)
        self.label_112.setObjectName(_fromUtf8("label_112"))
        self.gridLayout_111.addWidget(self.label_112, 0, 0, 1, 1)
        self.lineEdit_47 = QtGui.QLineEdit(self.groupBox_48)
        self.lineEdit_47.setObjectName(_fromUtf8("lineEdit_47"))
        self.gridLayout_111.addWidget(self.lineEdit_47, 0, 1, 1, 2)
        spacerItem12 = QtGui.QSpacerItem(197, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_111.addItem(spacerItem12, 1, 0, 1, 2)
        self.pushButton_69 = QtGui.QPushButton(self.groupBox_48)
        self.pushButton_69.setObjectName(_fromUtf8("pushButton_69"))
        self.gridLayout_111.addWidget(self.pushButton_69, 1, 2, 1, 1)
        self.gridLayout_110.addWidget(self.groupBox_48, 0, 0, 1, 1)
        self.groupBox_49 = QtGui.QGroupBox(self.tab_40)
        self.groupBox_49.setObjectName(_fromUtf8("groupBox_49"))
        self.gridLayout_112 = QtGui.QGridLayout(self.groupBox_49)
        self.gridLayout_112.setObjectName(_fromUtf8("gridLayout_112"))
        self.label_113 = QtGui.QLabel(self.groupBox_49)
        self.label_113.setObjectName(_fromUtf8("label_113"))
        self.gridLayout_112.addWidget(self.label_113, 0, 0, 1, 1)
        self.comboBox_21 = QtGui.QComboBox(self.groupBox_49)
        self.comboBox_21.setObjectName(_fromUtf8("comboBox_21"))
        self.gridLayout_112.addWidget(self.comboBox_21, 0, 1, 1, 2)
        spacerItem13 = QtGui.QSpacerItem(197, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_112.addItem(spacerItem13, 1, 0, 1, 2)
        self.pushButton_70 = QtGui.QPushButton(self.groupBox_49)
        self.pushButton_70.setObjectName(_fromUtf8("pushButton_70"))
        self.gridLayout_112.addWidget(self.pushButton_70, 1, 2, 1, 1)
        self.gridLayout_110.addWidget(self.groupBox_49, 0, 1, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(20, 366, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_110.addItem(spacerItem14, 1, 0, 1, 2)
        self.tabWidget_6.addTab(self.tab_40, _fromUtf8(""))
        self.gridLayout_113.addWidget(self.tabWidget_6, 0, 0, 1, 2)
        spacerItem15 = QtGui.QSpacerItem(734, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_113.addItem(spacerItem15, 1, 0, 1, 1)
        self.pushButton_60 = QtGui.QPushButton(self.tab_24)
        self.pushButton_60.setObjectName(_fromUtf8("pushButton_60"))
        self.gridLayout_113.addWidget(self.pushButton_60, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_24, _fromUtf8(""))
        self.tab_41 = QtGui.QWidget()
        self.tab_41.setObjectName(_fromUtf8("tab_41"))
        self.gridLayout_121 = QtGui.QGridLayout(self.tab_41)
        self.gridLayout_121.setObjectName(_fromUtf8("gridLayout_121"))
        self.tabWidget_7 = QtGui.QTabWidget(self.tab_41)
        self.tabWidget_7.setObjectName(_fromUtf8("tabWidget_7"))
        self.tab_42 = QtGui.QWidget()
        self.tab_42.setObjectName(_fromUtf8("tab_42"))
        self.gridLayout_114 = QtGui.QGridLayout(self.tab_42)
        self.gridLayout_114.setObjectName(_fromUtf8("gridLayout_114"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_42)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_114.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_42, _fromUtf8(""))
        self.tab_43 = QtGui.QWidget()
        self.tab_43.setObjectName(_fromUtf8("tab_43"))
        self.gridLayout_115 = QtGui.QGridLayout(self.tab_43)
        self.gridLayout_115.setObjectName(_fromUtf8("gridLayout_115"))
        self.label_114 = QtGui.QLabel(self.tab_43)
        self.label_114.setText(_fromUtf8(""))
        self.label_114.setObjectName(_fromUtf8("label_114"))
        self.gridLayout_115.addWidget(self.label_114, 0, 0, 1, 2)
        self.tabWidget_7.addTab(self.tab_43, _fromUtf8(""))
        self.tab_44 = QtGui.QWidget()
        self.tab_44.setObjectName(_fromUtf8("tab_44"))
        self.gridLayout_116 = QtGui.QGridLayout(self.tab_44)
        self.gridLayout_116.setObjectName(_fromUtf8("gridLayout_116"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.tab_44)
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.gridLayout_116.addWidget(self.textBrowser_5, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_44, _fromUtf8(""))
        self.tab_45 = QtGui.QWidget()
        self.tab_45.setObjectName(_fromUtf8("tab_45"))
        self.gridLayout_117 = QtGui.QGridLayout(self.tab_45)
        self.gridLayout_117.setObjectName(_fromUtf8("gridLayout_117"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.tab_45)
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.gridLayout_117.addWidget(self.textBrowser_4, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_45, _fromUtf8(""))
        self.tab_31 = QtGui.QWidget()
        self.tab_31.setObjectName(_fromUtf8("tab_31"))
        self.gridLayout_63 = QtGui.QGridLayout(self.tab_31)
        self.gridLayout_63.setObjectName(_fromUtf8("gridLayout_63"))
        self.textBrowser_6 = QtGui.QTextBrowser(self.tab_31)
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.gridLayout_63.addWidget(self.textBrowser_6, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_31, _fromUtf8(""))
        self.tab_46 = QtGui.QWidget()
        self.tab_46.setObjectName(_fromUtf8("tab_46"))
        self.gridLayout_118 = QtGui.QGridLayout(self.tab_46)
        self.gridLayout_118.setObjectName(_fromUtf8("gridLayout_118"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab_46)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_118.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_46, _fromUtf8(""))
        self.tab_47 = QtGui.QWidget()
        self.tab_47.setObjectName(_fromUtf8("tab_47"))
        self.gridLayout_119 = QtGui.QGridLayout(self.tab_47)
        self.gridLayout_119.setObjectName(_fromUtf8("gridLayout_119"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_47)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.gridLayout_119.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.tabWidget_7.addTab(self.tab_47, _fromUtf8(""))
        self.tab_48 = QtGui.QWidget()
        self.tab_48.setObjectName(_fromUtf8("tab_48"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_48)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.listWidget_28 = QtGui.QListWidget(self.tab_48)
        self.listWidget_28.setObjectName(_fromUtf8("listWidget_28"))
        self.gridLayout_7.addWidget(self.listWidget_28, 0, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.tab_48)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.tab_48)
        self.pushButton_11.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_11.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_7.addWidget(self.pushButton_11, 1, 1, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.tab_48)
        self.pushButton_10.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_10.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_7.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.tabWidget_7.addTab(self.tab_48, _fromUtf8(""))
        self.gridLayout_121.addWidget(self.tabWidget_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_41, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(1)
        self.tabWidget_7.setCurrentIndex(0)
        QtCore.QObject.connect(self.dial_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_58.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MYRaf 3", None))
        self.pushButton_21.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_22.setText(_translate("MainWindow", "Add", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Data", None))
        self.pushButton_23.setText(_translate("MainWindow", "Add", None))
        self.pushButton_24.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_25.setText(_translate("MainWindow", "Save", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Bias", None))
        self.pushButton_26.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_27.setText(_translate("MainWindow", "Add", None))
        self.pushButton_28.setText(_translate("MainWindow", "Save", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Dark", None))
        self.pushButton_29.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_30.setText(_translate("MainWindow", "Add", None))
        self.pushButton_31.setText(_translate("MainWindow", "Save", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Flat", None))
        self.pushButton.setText(_translate("MainWindow", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Calibration", None))
        self.groupBox.setTitle(_translate("MainWindow", "Display", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Files", None))
        self.pushButton_2.setText(_translate("MainWindow", "Add", None))
        self.pushButton_3.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_4.setText(_translate("MainWindow", ":go", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Auto", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Display", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Files", None))
        self.pushButton_6.setText(_translate("MainWindow", "Add", None))
        self.pushButton_5.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_7.setText(_translate("MainWindow", ":go", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Manual", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Align", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Display", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Files", None))
        self.pushButton_8.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_9.setText(_translate("MainWindow", "Add", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Sources", None))
        self.pushButton_32.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_33.setText(_translate("MainWindow", "Display", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_34.setText(_translate("MainWindow", ":go", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), _translate("MainWindow", "Aperture", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), _translate("MainWindow", "Ensemble", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Photometry", None))
        self.label_7.setText(_translate("MainWindow", "File_name", None))
        self.pushButton_12.setText(_translate("MainWindow", "Import", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_30), _translate("MainWindow", "Data Extractor", None))
        self.groupBox_16.setTitle(_translate("MainWindow", "Display", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_25), _translate("MainWindow", "Graph", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_16), _translate("MainWindow", "Extract/Graph", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Header:", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Operation", None))
        self.label_14.setText(_translate("MainWindow", "Field", None))
        self.checkBox.setText(_translate("MainWindow", "Existing", None))
        self.label_15.setText(_translate("MainWindow", "Value", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Files:", None))
        self.pushButton_37.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_36.setText(_translate("MainWindow", "Add", None))
        self.label_16.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_35.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_38.setText(_translate("MainWindow", "Insert/Update", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("MainWindow", "Header", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Observatory List", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Files", None))
        self.label_20.setText(_translate("MainWindow", "Observatory", None))
        self.label_21.setText(_translate("MainWindow", "Name", None))
        self.label_23.setText(_translate("MainWindow", "Longitude", None))
        self.label_22.setText(_translate("MainWindow", "Latitude", None))
        self.label_25.setText(_translate("MainWindow", "Altitude", None))
        self.label_26.setText(_translate("MainWindow", "Time Zone", None))
        self.label_24.setText(_translate("MainWindow", "Other", None))
        self.pushButton_39.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_40.setText(_translate("MainWindow", "Insert/Update", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_19), _translate("MainWindow", "Observatory", None))
        self.groupBox_13.setTitle(_translate("MainWindow", "Display", None))
        self.groupBox_14.setTitle(_translate("MainWindow", "Files:", None))
        self.pushButton_41.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_42.setText(_translate("MainWindow", "Add", None))
        self.label_17.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_43.setText(_translate("MainWindow", ":go", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_20), _translate("MainWindow", "Cosmic Cleaner", None))
        self.pushButton_44.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_45.setText(_translate("MainWindow", "Add", None))
        self.pushButton_46.setText(_translate("MainWindow", ":go", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_21), _translate("MainWindow", "Convert to Fits", None))
        self.label_19.setText(_translate("MainWindow", "Wait for it", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_22), _translate("MainWindow", "WCS (Online)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_17), _translate("MainWindow", "Editor", None))
        self.groupBox_30.setTitle(_translate("MainWindow", "Display:", None))
        self.groupBox_15.setTitle(_translate("MainWindow", "Scheduler List", None))
        self.pushButton_48.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_49.setText(_translate("MainWindow", "Update", None))
        self.pushButton_50.setText(_translate("MainWindow", "Add", None))
        self.label_27.setText(_translate("MainWindow", "Session", None))
        self.groupBox_25.setTitle(_translate("MainWindow", "Images:", None))
        self.pushButton_51.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_52.setText(_translate("MainWindow", "Add", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_26), _translate("MainWindow", "Data", None))
        self.pushButton_53.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_54.setText(_translate("MainWindow", "Add", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_27), _translate("MainWindow", "Bias", None))
        self.pushButton_55.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_56.setText(_translate("MainWindow", "Add", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_28), _translate("MainWindow", "Dark", None))
        self.pushButton_57.setText(_translate("MainWindow", "Remove", None))
        self.pushButton_58.setText(_translate("MainWindow", "Add", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_29), _translate("MainWindow", "Flat", None))
        self.groupBox_27.setTitle(_translate("MainWindow", "Processes:", None))
        self.checkBox_11.setText(_translate("MainWindow", "Align", None))
        self.groupBox_29.setTitle(_translate("MainWindow", "Photometry", None))
        self.pushButton_59.setText(_translate("MainWindow", "Remove", None))
        self.checkBox_2.setText(_translate("MainWindow", "Ensemble", None))
        self.pushButton_47.setText(_translate("MainWindow", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_23), _translate("MainWindow", "Scheduler", None))
        self.groupBox_34.setTitle(_translate("MainWindow", "CPU(s) to Use", None))
        self.label_55.setText(_translate("MainWindow", "of", None))
        self.label_56.setText(_translate("MainWindow", "8", None))
        self.label_58.setText(_translate("MainWindow", "1", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_35), _translate("MainWindow", "General", None))
        self.groupBox_35.setTitle(_translate("MainWindow", "Zero Combine Setting", None))
        self.label_59.setText(_translate("MainWindow", "Combine", None))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "median", None))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "average", None))
        self.label_60.setText(_translate("MainWindow", "Reject", None))
        self.comboBox_13.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox_13.setItemText(1, _translate("MainWindow", "minmax", None))
        self.comboBox_13.setItemText(2, _translate("MainWindow", "ccdclip", None))
        self.comboBox_13.setItemText(3, _translate("MainWindow", "crreject", None))
        self.comboBox_13.setItemText(4, _translate("MainWindow", "sigclip", None))
        self.comboBox_13.setItemText(5, _translate("MainWindow", "avsigclip", None))
        self.comboBox_13.setItemText(6, _translate("MainWindow", "pclip", None))
        self.label_61.setText(_translate("MainWindow", "ccdtype", None))
        self.groupBox_37.setTitle(_translate("MainWindow", "Dark Combine Setting", None))
        self.label_62.setText(_translate("MainWindow", "Combine", None))
        self.comboBox_14.setItemText(0, _translate("MainWindow", "median", None))
        self.comboBox_14.setItemText(1, _translate("MainWindow", "average", None))
        self.label_63.setText(_translate("MainWindow", "Reject", None))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "minmax", None))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "ccdclip", None))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "crreject", None))
        self.comboBox_15.setItemText(4, _translate("MainWindow", "sigclip", None))
        self.comboBox_15.setItemText(5, _translate("MainWindow", "avsigclip", None))
        self.comboBox_15.setItemText(6, _translate("MainWindow", "pclip", None))
        self.label_71.setText(_translate("MainWindow", "Scale", None))
        self.comboBox_16.setItemText(0, _translate("MainWindow", "exposure", None))
        self.comboBox_16.setItemText(1, _translate("MainWindow", "none", None))
        self.comboBox_16.setItemText(2, _translate("MainWindow", "mode", None))
        self.comboBox_16.setItemText(3, _translate("MainWindow", "median", None))
        self.comboBox_16.setItemText(4, _translate("MainWindow", "mean", None))
        self.label_80.setText(_translate("MainWindow", "ccdtype", None))
        self.groupBox_38.setTitle(_translate("MainWindow", "Flat Combine Setting", None))
        self.label_81.setText(_translate("MainWindow", "Combine", None))
        self.comboBox_17.setItemText(0, _translate("MainWindow", "median", None))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "average", None))
        self.label_82.setText(_translate("MainWindow", "Reject", None))
        self.comboBox_18.setItemText(0, _translate("MainWindow", "none", None))
        self.comboBox_18.setItemText(1, _translate("MainWindow", "minmax", None))
        self.comboBox_18.setItemText(2, _translate("MainWindow", "ccdclip", None))
        self.comboBox_18.setItemText(3, _translate("MainWindow", "crreject", None))
        self.comboBox_18.setItemText(4, _translate("MainWindow", "sigclip", None))
        self.comboBox_18.setItemText(5, _translate("MainWindow", "avsigclip", None))
        self.comboBox_18.setItemText(6, _translate("MainWindow", "pclip", None))
        self.label_83.setText(_translate("MainWindow", "Subset", None))
        self.comboBox_19.setItemText(0, _translate("MainWindow", "yes", None))
        self.comboBox_19.setItemText(1, _translate("MainWindow", "no", None))
        self.label_84.setText(_translate("MainWindow", "ccdtype", None))
        self.groupBox_39.setTitle(_translate("MainWindow", "Calibration Ssetting", None))
        self.label_85.setText(_translate("MainWindow", "Subset", None))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "yes", None))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "no", None))
        self.label_86.setText(_translate("MainWindow", "ccdtype", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_36), _translate("MainWindow", "Calibration", None))
        self.groupBox_40.setTitle(_translate("MainWindow", "FitSkyPars", None))
        self.label_87.setText(_translate("MainWindow", "Annulus", None))
        self.label_88.setText(_translate("MainWindow", "Dannulus", None))
        self.label_89.setText(_translate("MainWindow", "CBox", None))
        self.groupBox_41.setTitle(_translate("MainWindow", "DataPars", None))
        self.label_90.setText(_translate("MainWindow", "Filter", None))
        self.lineEdit_33.setText(_translate("MainWindow", "exptime", None))
        self.label_91.setText(_translate("MainWindow", "Exposur", None))
        self.lineEdit_34.setText(_translate("MainWindow", "subset", None))
        self.groupBox_42.setTitle(_translate("MainWindow", "PhotPars", None))
        self.label_92.setText(_translate("MainWindow", "Apertur", None))
        self.lineEdit_35.setText(_translate("MainWindow", "10,15,20,25,30", None))
        self.label_93.setText(_translate("MainWindow", "ZMag", None))
        self.lineEdit_36.setText(_translate("MainWindow", "25", None))
        self.label_94.setText(_translate("MainWindow", "Gain", None))
        self.lineEdit_37.setText(_translate("MainWindow", "gain", None))
        self.label_95.setText(_translate("MainWindow", "FixPix", None))
        self.groupBox_43.setTitle(_translate("MainWindow", "WCS", None))
        self.label_96.setText(_translate("MainWindow", "Right ascension", None))
        self.lineEdit_39.setText(_translate("MainWindow", "ra", None))
        self.label_97.setText(_translate("MainWindow", "Declination", None))
        self.lineEdit_40.setText(_translate("MainWindow", "dec", None))
        self.groupBox_44.setTitle(_translate("MainWindow", "Location and Time", None))
        self.label_98.setText(_translate("MainWindow", "Time OBS", None))
        self.label_99.setText(_translate("MainWindow", "Observatory", None))
        self.lineEdit_42.setText(_translate("MainWindow", "observat", None))
        self.lineEdit_43.setText(_translate("MainWindow", "time-obs", None))
        self.label_100.setText(_translate("MainWindow", "Date OBS", None))
        self.lineEdit_44.setText(_translate("MainWindow", "date-obs", None))
        self.checkBox_5.setText(_translate("MainWindow", "Epoch", None))
        self.checkBox_13.setText(_translate("MainWindow", "Time Stamp", None))
        self.groupBox_45.setTitle(_translate("MainWindow", "Star finder", None))
        self.label_101.setText(_translate("MainWindow", "Flux Radius", None))
        self.label_102.setText(_translate("MainWindow", "Min FWHM", None))
        self.label_103.setText(_translate("MainWindow", "Max FWHM", None))
        self.label_104.setText(_translate("MainWindow", "Maximum Stars To find", None))
        self.groupBox_46.setTitle(_translate("MainWindow", "Extract From Header", None))
        self.pushButton_66.setText(_translate("MainWindow", "<<", None))
        self.pushButton_67.setText(_translate("MainWindow", ">>", None))
        self.pushButton_68.setText(_translate("MainWindow", "Update List", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_37), _translate("MainWindow", "Photometry", None))
        self.checkBox_17.setText(_translate("MainWindow", "Additionally Create Mask Files", None))
        self.label_105.setText(_translate("MainWindow", "Gain", None))
        self.label_106.setText(_translate("MainWindow", "Read Noise", None))
        self.label_107.setText(_translate("MainWindow", "Sigma Clip", None))
        self.label_108.setText(_translate("MainWindow", "Sigma Frac.", None))
        self.label_109.setText(_translate("MainWindow", "Object Lim.", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_38), _translate("MainWindow", "Cosmic Cleaner", None))
        self.label_110.setText(_translate("MainWindow", "Server", None))
        self.lineEdit_45.setText(_translate("MainWindow", "http://nova.astrometry.net/api/", None))
        self.label_111.setText(_translate("MainWindow", "Api Key", None))
        self.groupBox_47.setTitle(_translate("MainWindow", "Before Upload:", None))
        self.radioButton_4.setText(_translate("MainWindow", "Do Nothing", None))
        self.radioButton_5.setText(_translate("MainWindow", "Compress (For Low Band Widths)", None))
        self.radioButton_6.setText(_translate("MainWindow", "Convert to Binary File (For Very Low Band Widths)", None))
        self.checkBox_20.setText(_translate("MainWindow", "Align Befor Application", None))
        self.checkBox_21.setText(_translate("MainWindow", "Create WCS Headers Separately", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_39), _translate("MainWindow", "WCS", None))
        self.groupBox_48.setTitle(_translate("MainWindow", "Save", None))
        self.label_112.setText(_translate("MainWindow", "Session Name", None))
        self.pushButton_69.setText(_translate("MainWindow", "Save", None))
        self.groupBox_49.setTitle(_translate("MainWindow", "Load", None))
        self.label_113.setText(_translate("MainWindow", "Session Name", None))
        self.pushButton_70.setText(_translate("MainWindow", "Load", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_40), _translate("MainWindow", "Sessions", None))
        self.pushButton_60.setText(_translate("MainWindow", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_24), _translate("MainWindow", "Settings", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">For more information and help:</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">    Myraf Project Home Page</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">http://myrafproject.org/</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">    Myraf Project Wiki</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">http://wiki.myrafproject.org/</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">    Myraf Project Blog</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-weight:600; font-style:italic;\">http://myrafproject.org/blog/</span></p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_42), _translate("MainWindow", "MYRaf", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_43), _translate("MainWindow", "Help", None))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_44), _translate("MainWindow", "Features", None))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040; background-color:#fcfcfc;\">Ginga Quick Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"main-image-window\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">M</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">ain image window</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040;\">These keyboard and mouse operations are available when the main image window has the focus.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"panning-and-zooming-commands\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">P</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">anning and Zooming commands</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Scroll wheel turned</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Zoom in or out</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Digit (1234567890)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Zoom image to zoom steps 1, 2, ..., 9, 10</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Shift + Digit</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Zoom image to zoom steps -1, -2, ..., -9, -10</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Backquote (`)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Zoom image to fit window and center it</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#404040;\">Minus, Underscore</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040;\">(-, _)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Zoom out</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#ffffff;\">Equals, Plus</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff;\">(=, +)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Zoom in</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Middle (scroll) button drag</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Pan image freely (when zoomed in)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">p</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Set pan position for zooming</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Shift + Left click</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Set pan position for zooming</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">c</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Set pan position to the center of the image</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">q</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Pan image freely (when zoomed in); Left drag</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Ctrl + Left drag</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#ffffff;\">Proportional pan (press and drag left mouse</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff;\">button</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">apostrophe (‘)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Set autozoom for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-style:italic; color:#404040;\">override</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">doublequote (”)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Set autozoom for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-style:italic; color:#ffffff;\">on</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#404040;\">Ctrl + Scroll wheel</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040;\">turned</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Adjust zoom by intermediate coarse steps</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#ffffff;\">Shift + Scroll wheel</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff;\">turned</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Adjust zoom by intermediate fine steps</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cut-levels-and-colormap-commands\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">C</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">ut levels and colormap commands</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">a</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Auto cut levels</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">s</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Cycle color distribution algorithm</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">S</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Reset color distribution algorithm to “linear”</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">period (.)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#ffffff;\">Interactive cut </span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; font-style:italic; color:#ffffff;\">both</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#ffffff;\"> low and high (with left</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff;\">mouse button)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">slash (/)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-weight:600; color:#404040;\">Interactive warp colormap (with left mouse</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040;\">button)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">semicolon (;)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Set autocuts for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-style:italic; color:#ffffff;\">override</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">colon (:)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Set autocuts for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-style:italic; color:#404040;\">on</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">question (?)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Restore the color map to its original state</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"transform-commands\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">T</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">ransform commands</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Left bracket ([)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Toggle flip image in X</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Left brace ({)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Reset to no flip of image in X</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Right bracket (])</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Toggle flip image in Y</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Right brace (})</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Reset to no flip image in Y</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Backslash (\\)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Swap X and Y axes</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Vertical bar (|)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Reset to no swap of X and Y axes</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">r</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Interactive rotate (with left mouse button)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">R</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Restore rotation to 0 degrees</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">e</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Increment current rotation by 90 degrees</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">E</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Increment current rotation by -90 degrees</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">o</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Orient image by WCS so North=Up and East=Left</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">O</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Orient image by WCS so North=Up and East=Right</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"reference-viewer-only\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">R</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-weight:696; color:#404040;\">eference Viewer Only</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">I</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Raise Info tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">H</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Raise Header tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Z</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Raise Zoom tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">D</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Raise Dialogs tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">T</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Raise Thumbs tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">C</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Raise Contents tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">left angle (&lt;)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Toggle collapse left pane</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">right angle (&gt;)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Toggle collapse right pane</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">f</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Toggle full screen</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">F</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#ffffff; background-color:#000000;\">Panoramic full screen</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">m</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040; background-color:#f3f6f6;\">Maximize window</span></p></td></tr></table>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Note:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040;\">If there are one or more plugins active, additional mouse or keyboard bindings may be present. In general, the left mouse button is used to select, pick or move, and the right mouse button is used to draw a shape for the operation.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; color:#404040;\">On the Mac, control + mouse button can also be used to draw or right click. You can also press and release the space bar to make the next drag operation a drawing operation.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ref = http://ginga.readthedocs.org/en/latest/quickref.html</p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_45), _translate("MainWindow", "Ginga (Display)", None))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks to <span style=\" font-weight:600;\">A-Track</span> Team, MYRaf can track moving object(NEOs, Asteroids, etc) in file series.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ref: https://github.com/yucelkilic/A-Track</p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_31), _translate("MainWindow", "A-Track", None))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">                    GNU GENERAL PUBLIC LICENSE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">                       Version 3, 29 June 2007</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\"> Copyright (C) 2007 Free Software Foundation, Inc. &lt;http://fsf.org/&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\"> Everyone is permitted to copy and distribute verbatim copies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\"> of this license document, but changing it is not allowed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">                            Preamble</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The GNU General Public License is a free, copyleft license for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">software and other kinds of works.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The licenses for most software and other practical works are designed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to take away your freedom to share and change the works.  By contrast,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the GNU General Public License is intended to guarantee your freedom to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">share and change all versions of a program--to make sure it remains free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">software for all its users.  We, the Free Software Foundation, use the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">GNU General Public License for most of our software; it applies also to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">any other work released this way by its authors.  You can apply it to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">your programs, too.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  When we speak of free software, we are referring to freedom, not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">price.  Our General Public Licenses are designed to make sure that you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">have the freedom to distribute copies of free software (and charge for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">them if you wish), that you receive source code or can get it if you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">want it, that you can change the software or use pieces of it in new</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">free programs, and that you know you can do these things.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  To protect your rights, we need to prevent others from denying you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">these rights or asking you to surrender the rights.  Therefore, you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">certain responsibilities if you distribute copies of the software, or if</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">you modify it: responsibilities to respect the freedom of others.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  For example, if you distribute copies of such a program, whether</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">gratis or for a fee, you must pass on to the recipients the same</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">freedoms that you received.  You must make sure that they, too, receive</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">or can get the source code.  And you must show them these terms so they</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">know their rights.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Developers that use the GNU GPL protect your rights with two steps:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">(1) assert copyright on the software, and (2) offer you this License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">giving you legal permission to copy, distribute and/or modify it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  For the developers\' and authors\' protection, the GPL clearly explains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">that there is no warranty for this free software.  For both users\' and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">authors\' sake, the GPL requires that modified versions be marked as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">changed, so that their problems will not be attributed erroneously to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">authors of previous versions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Some devices are designed to deny users access to install or run</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modified versions of the software inside them, although the manufacturer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">can do so.  This is fundamentally incompatible with the aim of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">protecting users\' freedom to change the software.  The systematic</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">pattern of such abuse occurs in the area of products for individuals to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">use, which is precisely where it is most unacceptable.  Therefore, we</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">have designed this version of the GPL to prohibit the practice for those</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">products.  If such problems arise substantially in other domains, we</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">stand ready to extend this provision to those domains in future versions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">of the GPL, as needed to protect the freedom of users.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Finally, every program is threatened constantly by software patents.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">States should not allow patents to restrict development and use of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">software on general-purpose computers, but in those that do, we wish to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">avoid the special danger that patents applied to a free program could</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">make it effectively proprietary.  To prevent this, the GPL assures that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">patents cannot be used to render the program non-free.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The precise terms and conditions for copying, distribution and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modification follow.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">                       TERMS AND CONDITIONS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  0. Definitions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  &quot;This License&quot; refers to version 3 of the GNU General Public License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  &quot;Copyright&quot; also means copyright-like laws that apply to other kinds of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">works, such as semiconductor masks.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  &quot;The Program&quot; refers to any copyrightable work licensed under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License.  Each licensee is addressed as &quot;you&quot;.  &quot;Licensees&quot; and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">&quot;recipients&quot; may be individuals or organizations.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  To &quot;modify&quot; a work means to copy from or adapt all or part of the work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in a fashion requiring copyright permission, other than the making of an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">exact copy.  The resulting work is called a &quot;modified version&quot; of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">earlier work or a work &quot;based on&quot; the earlier work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A &quot;covered work&quot; means either the unmodified Program or a work based</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">on the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  To &quot;propagate&quot; a work means to do anything with it that, without</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">permission, would make you directly or secondarily liable for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">infringement under applicable copyright law, except executing it on a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">computer or modifying a private copy.  Propagation includes copying,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">distribution (with or without modification), making available to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">public, and in some countries other activities as well.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  To &quot;convey&quot; a work means any kind of propagation that enables other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">parties to make or receive copies.  Mere interaction with a user through</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">a computer network, with no transfer of a copy, is not conveying.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  An interactive user interface displays &quot;Appropriate Legal Notices&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to the extent that it includes a convenient and prominently visible</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">feature that (1) displays an appropriate copyright notice, and (2)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">tells the user that there is no warranty for the work (except to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">extent that warranties are provided), that licensees may convey the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">work under this License, and how to view a copy of this License.  If</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the interface presents a list of user commands or options, such as a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">menu, a prominent item in the list meets this criterion.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  1. Source Code.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The &quot;source code&quot; for a work means the preferred form of the work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">for making modifications to it.  &quot;Object code&quot; means any non-source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">form of a work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A &quot;Standard Interface&quot; means an interface that either is an official</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">standard defined by a recognized standards body, or, in the case of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">interfaces specified for a particular programming language, one that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">is widely used among developers working in that language.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The &quot;System Libraries&quot; of an executable work include anything, other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">than the work as a whole, that (a) is included in the normal form of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">packaging a Major Component, but which is not part of that Major</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Component, and (b) serves only to enable use of the work with that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Major Component, or to implement a Standard Interface for which an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">implementation is available to the public in source code form.  A</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">&quot;Major Component&quot;, in this context, means a major essential component</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">(kernel, window system, and so on) of the specific operating system</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">(if any) on which the executable work runs, or a compiler used to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">produce the work, or an object code interpreter used to run it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The &quot;Corresponding Source&quot; for a work in object code form means all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the source code needed to generate, install, and (for an executable</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">work) run the object code and to modify the work, including scripts to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">control those activities.  However, it does not include the work\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">System Libraries, or general-purpose tools or generally available free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">programs which are used unmodified in performing those activities but</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">which are not part of the work.  For example, Corresponding Source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">includes interface definition files associated with source files for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the work, and the source code for shared libraries and dynamically</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">linked subprograms that the work is specifically designed to require,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">such as by intimate data communication or control flow between those</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">subprograms and other parts of the work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The Corresponding Source need not include anything that users</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">can regenerate automatically from other parts of the Corresponding</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Source.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The Corresponding Source for a work in source code form is that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">same work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  2. Basic Permissions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  All rights granted under this License are granted for the term of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">copyright on the Program, and are irrevocable provided the stated</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">conditions are met.  This License explicitly affirms your unlimited</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">permission to run the unmodified Program.  The output from running a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">covered work is covered by this License only if the output, given its</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">content, constitutes a covered work.  This License acknowledges your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">rights of fair use or other equivalent, as provided by copyright law.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may make, run and propagate covered works that you do not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">convey, without conditions so long as your license otherwise remains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in force.  You may convey covered works to others for the sole purpose</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">of having them make modifications exclusively for you, or provide you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">with facilities for running those works, provided that you comply with</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the terms of this License in conveying all material for which you do</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">not control copyright.  Those thus making or running the covered works</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">for you must do so exclusively on your behalf, under your direction</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">and control, on terms that prohibit them from making any copies of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">your copyrighted material outside their relationship with you.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Conveying under any other circumstances is permitted solely under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the conditions stated below.  Sublicensing is not allowed; section 10</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">makes it unnecessary.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  3. Protecting Users\' Legal Rights From Anti-Circumvention Law.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  No covered work shall be deemed part of an effective technological</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">measure under any applicable law fulfilling obligations under article</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">11 of the WIPO copyright treaty adopted on 20 December 1996, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">similar laws prohibiting or restricting circumvention of such</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">measures.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  When you convey a covered work, you waive any legal power to forbid</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">circumvention of technological measures to the extent such circumvention</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">is effected by exercising rights under this License with respect to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the covered work, and you disclaim any intention to limit operation or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modification of the work as a means of enforcing, against the work\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">users, your or third parties\' legal rights to forbid circumvention of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">technological measures.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  4. Conveying Verbatim Copies.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may convey verbatim copies of the Program\'s source code as you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">receive it, in any medium, provided that you conspicuously and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">appropriately publish on each copy an appropriate copyright notice;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">keep intact all notices stating that this License and any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">non-permissive terms added in accord with section 7 apply to the code;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">keep intact all notices of the absence of any warranty; and give all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">recipients a copy of this License along with the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may charge any price or no price for each copy that you convey,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">and you may offer support or warranty protection for a fee.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  5. Conveying Modified Source Versions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may convey a work based on the Program, or the modifications to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">produce it from the Program, in the form of source code under the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">terms of section 4, provided that you also meet all of these conditions:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    a) The work must carry prominent notices stating that you modified</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    it, and giving a relevant date.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    b) The work must carry prominent notices stating that it is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    released under this License and any conditions added under section</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    7.  This requirement modifies the requirement in section 4 to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    &quot;keep intact all notices&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    c) You must license the entire work, as a whole, under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    License to anyone who comes into possession of a copy.  This</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    License will therefore apply, along with any applicable section 7</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    additional terms, to the whole of the work, and all its parts,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    regardless of how they are packaged.  This License gives no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    permission to license the work in any other way, but it does not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    invalidate such permission if you have separately received it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    d) If the work has interactive user interfaces, each must display</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Appropriate Legal Notices; however, if the Program has interactive</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    interfaces that do not display Appropriate Legal Notices, your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    work need not make them do so.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A compilation of a covered work with other separate and independent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">works, which are not by their nature extensions of the covered work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">and which are not combined with it such as to form a larger program,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in or on a volume of a storage or distribution medium, is called an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">&quot;aggregate&quot; if the compilation and its resulting copyright are not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">used to limit the access or legal rights of the compilation\'s users</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">beyond what the individual works permit.  Inclusion of a covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in an aggregate does not cause this License to apply to the other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">parts of the aggregate.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  6. Conveying Non-Source Forms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may convey a covered work in object code form under the terms</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">of sections 4 and 5, provided that you also convey the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">machine-readable Corresponding Source under the terms of this License,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in one of these ways:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    a) Convey the object code in, or embodied in, a physical product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    (including a physical distribution medium), accompanied by the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Corresponding Source fixed on a durable physical medium</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    customarily used for software interchange.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    b) Convey the object code in, or embodied in, a physical product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    (including a physical distribution medium), accompanied by a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    written offer, valid for at least three years and valid for as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    long as you offer spare parts or customer support for that product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    model, to give anyone who possesses the object code either (1) a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    copy of the Corresponding Source for all the software in the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    product that is covered by this License, on a durable physical</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    medium customarily used for software interchange, for a price no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    more than your reasonable cost of physically performing this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    conveying of source, or (2) access to copy the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Corresponding Source from a network server at no charge.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    c) Convey individual copies of the object code with a copy of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    written offer to provide the Corresponding Source.  This</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    alternative is allowed only occasionally and noncommercially, and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    only if you received the object code with such an offer, in accord</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    with subsection 6b.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    d) Convey the object code by offering access from a designated</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    place (gratis or for a charge), and offer equivalent access to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Corresponding Source in the same way through the same place at no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    further charge.  You need not require recipients to copy the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Corresponding Source along with the object code.  If the place to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    copy the object code is a network server, the Corresponding Source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    may be on a different server (operated by you or a third party)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    that supports equivalent copying facilities, provided you maintain</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    clear directions next to the object code saying where to find the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Corresponding Source.  Regardless of what server hosts the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Corresponding Source, you remain obligated to ensure that it is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    available for as long as needed to satisfy these requirements.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    e) Convey the object code using peer-to-peer transmission, provided</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    you inform other peers where the object code and Corresponding</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Source of the work are being offered to the general public at no</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    charge under subsection 6d.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A separable portion of the object code, whose source code is excluded</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">from the Corresponding Source as a System Library, need not be</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">included in conveying the object code work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A &quot;User Product&quot; is either (1) a &quot;consumer product&quot;, which means any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">tangible personal property which is normally used for personal, family,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">or household purposes, or (2) anything designed or sold for incorporation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">into a dwelling.  In determining whether a product is a consumer product,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">doubtful cases shall be resolved in favor of coverage.  For a particular</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">product received by a particular user, &quot;normally used&quot; refers to a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">typical or common use of that class of product, regardless of the status</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">of the particular user or of the way in which the particular user</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">actually uses, or expects or is expected to use, the product.  A product</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">is a consumer product regardless of whether the product has substantial</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">commercial, industrial or non-consumer uses, unless such uses represent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the only significant mode of use of the product.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  &quot;Installation Information&quot; for a User Product means any methods,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">procedures, authorization keys, or other information required to install</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">and execute modified versions of a covered work in that User Product from</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">a modified version of its Corresponding Source.  The information must</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">suffice to ensure that the continued functioning of the modified object</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">code is in no case prevented or interfered with solely because</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modification has been made.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If you convey an object code work under this section in, or with, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">specifically for use in, a User Product, and the conveying occurs as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">part of a transaction in which the right of possession and use of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">User Product is transferred to the recipient in perpetuity or for a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">fixed term (regardless of how the transaction is characterized), the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Corresponding Source conveyed under this section must be accompanied</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">by the Installation Information.  But this requirement does not apply</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">if neither you nor any third party retains the ability to install</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modified object code on the User Product (for example, the work has</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">been installed in ROM).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The requirement to provide Installation Information does not include a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">requirement to continue to provide support service, warranty, or updates</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">for a work that has been modified or installed by the recipient, or for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the User Product in which it has been modified or installed.  Access to a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">network may be denied when the modification itself materially and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">adversely affects the operation of the network or violates the rules and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">protocols for communication across the network.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Corresponding Source conveyed, and Installation Information provided,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in accord with this section must be in a format that is publicly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">documented (and with an implementation available to the public in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">source code form), and must require no special password or key for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">unpacking, reading or copying.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  7. Additional Terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  &quot;Additional permissions&quot; are terms that supplement the terms of this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License by making exceptions from one or more of its conditions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Additional permissions that are applicable to the entire Program shall</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">be treated as though they were included in this License, to the extent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">that they are valid under applicable law.  If additional permissions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">apply only to part of the Program, that part may be used separately</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">under those permissions, but the entire Program remains governed by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">this License without regard to the additional permissions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  When you convey a copy of a covered work, you may at your option</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">remove any additional permissions from that copy, or from any part of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">it.  (Additional permissions may be written to require their own</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">removal in certain cases when you modify the work.)  You may place</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">additional permissions on material, added by you to a covered work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">for which you have or can give appropriate copyright permission.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Notwithstanding any other provision of this License, for material you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">add to a covered work, you may (if authorized by the copyright holders of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">that material) supplement the terms of this License with terms:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    a) Disclaiming warranty or limiting liability differently from the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    terms of sections 15 and 16 of this License; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    b) Requiring preservation of specified reasonable legal notices or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    author attributions in that material or in the Appropriate Legal</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Notices displayed by works containing it; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    c) Prohibiting misrepresentation of the origin of that material, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    requiring that modified versions of such material be marked in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    reasonable ways as different from the original version; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    d) Limiting the use for publicity purposes of names of licensors or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    authors of the material; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    e) Declining to grant rights under trademark law for use of some</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    trade names, trademarks, or service marks; or</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    f) Requiring indemnification of licensors and authors of that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    material by anyone who conveys the material (or modified versions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    it) with contractual assumptions of liability to the recipient, for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    any liability that these contractual assumptions directly impose on</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    those licensors and authors.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  All other non-permissive additional terms are considered &quot;further</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">restrictions&quot; within the meaning of section 10.  If the Program as you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">received it, or any part of it, contains a notice stating that it is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">governed by this License along with a term that is a further</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">restriction, you may remove that term.  If a license document contains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">a further restriction but permits relicensing or conveying under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License, you may add to a covered work material governed by the terms</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">of that license document, provided that the further restriction does</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">not survive such relicensing or conveying.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If you add terms to a covered work in accord with this section, you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">must place, in the relevant source files, a statement of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">additional terms that apply to those files, or a notice indicating</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">where to find the applicable terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Additional terms, permissive or non-permissive, may be stated in the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">form of a separately written license, or stated as exceptions;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the above requirements apply either way.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  8. Termination.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may not propagate or modify a covered work except as expressly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">provided under this License.  Any attempt otherwise to propagate or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modify it is void, and will automatically terminate your rights under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">this License (including any patent licenses granted under the third</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">paragraph of section 11).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  However, if you cease all violation of this License, then your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">license from a particular copyright holder is reinstated (a)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">provisionally, unless and until the copyright holder explicitly and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">finally terminates your license, and (b) permanently, if the copyright</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">holder fails to notify you of the violation by some reasonable means</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">prior to 60 days after the cessation.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Moreover, your license from a particular copyright holder is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">reinstated permanently if the copyright holder notifies you of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">violation by some reasonable means, this is the first time you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">received notice of violation of this License (for any work) from that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">copyright holder, and you cure the violation prior to 30 days after</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">your receipt of the notice.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Termination of your rights under this section does not terminate the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">licenses of parties who have received copies or rights from you under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">this License.  If your rights have been terminated and not permanently</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">reinstated, you do not qualify to receive new licenses for the same</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">material under section 10.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  9. Acceptance Not Required for Having Copies.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You are not required to accept this License in order to receive or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">run a copy of the Program.  Ancillary propagation of a covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">occurring solely as a consequence of using peer-to-peer transmission</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to receive a copy likewise does not require acceptance.  However,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">nothing other than this License grants you permission to propagate or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">modify any covered work.  These actions infringe copyright if you do</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">not accept this License.  Therefore, by modifying or propagating a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">covered work, you indicate your acceptance of this License to do so.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  10. Automatic Licensing of Downstream Recipients.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Each time you convey a covered work, the recipient automatically</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">receives a license from the original licensors, to run, modify and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">propagate that work, subject to this License.  You are not responsible</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">for enforcing compliance by third parties with this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  An &quot;entity transaction&quot; is a transaction transferring control of an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">organization, or substantially all assets of one, or subdividing an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">organization, or merging organizations.  If propagation of a covered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">work results from an entity transaction, each party to that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">transaction who receives a copy of the work also receives whatever</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">licenses to the work the party\'s predecessor in interest had or could</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">give under the previous paragraph, plus a right to possession of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Corresponding Source of the work from the predecessor in interest, if</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the predecessor has it or can get it with reasonable efforts.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You may not impose any further restrictions on the exercise of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">rights granted or affirmed under this License.  For example, you may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">not impose a license fee, royalty, or other charge for exercise of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">rights granted under this License, and you may not initiate litigation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">(including a cross-claim or counterclaim in a lawsuit) alleging that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">any patent claim is infringed by making, using, selling, offering for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">sale, or importing the Program or any portion of it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  11. Patents.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A &quot;contributor&quot; is a copyright holder who authorizes use under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License of the Program or a work on which the Program is based.  The</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">work thus licensed is called the contributor\'s &quot;contributor version&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A contributor\'s &quot;essential patent claims&quot; are all patent claims</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">owned or controlled by the contributor, whether already acquired or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">hereafter acquired, that would be infringed by some manner, permitted</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">by this License, of making, using, or selling its contributor version,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">but do not include claims that would be infringed only as a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">consequence of further modification of the contributor version.  For</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">purposes of this definition, &quot;control&quot; includes the right to grant</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">patent sublicenses in a manner consistent with the requirements of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Each contributor grants you a non-exclusive, worldwide, royalty-free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">patent license under the contributor\'s essential patent claims, to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">make, use, sell, offer for sale, import and otherwise run, modify and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">propagate the contents of its contributor version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  In the following three paragraphs, a &quot;patent license&quot; is any express</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">agreement or commitment, however denominated, not to enforce a patent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">(such as an express permission to practice a patent or covenant not to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">sue for patent infringement).  To &quot;grant&quot; such a patent license to a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">party means to make such an agreement or commitment not to enforce a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">patent against the party.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If you convey a covered work, knowingly relying on a patent license,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">and the Corresponding Source of the work is not available for anyone</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to copy, free of charge and under the terms of this License, through a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">publicly available network server or other readily accessible means,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">then you must either (1) cause the Corresponding Source to be so</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">available, or (2) arrange to deprive yourself of the benefit of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">patent license for this particular work, or (3) arrange, in a manner</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">consistent with the requirements of this License, to extend the patent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">license to downstream recipients.  &quot;Knowingly relying&quot; means you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">actual knowledge that, but for the patent license, your conveying the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">covered work in a country, or your recipient\'s use of the covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in a country, would infringe one or more identifiable patents in that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">country that you have reason to believe are valid.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If, pursuant to or in connection with a single transaction or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">arrangement, you convey, or propagate by procuring conveyance of, a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">covered work, and grant a patent license to some of the parties</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">receiving the covered work authorizing them to use, propagate, modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">or convey a specific copy of the covered work, then the patent license</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">you grant is automatically extended to all recipients of the covered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">work and works based on it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  A patent license is &quot;discriminatory&quot; if it does not include within</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the scope of its coverage, prohibits the exercise of, or is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">conditioned on the non-exercise of one or more of the rights that are</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">specifically granted under this License.  You may not convey a covered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">work if you are a party to an arrangement with a third party that is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">in the business of distributing software, under which you make payment</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to the third party based on the extent of your activity of conveying</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the work, and under which the third party grants, to any of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">parties who would receive the covered work from you, a discriminatory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">patent license (a) in connection with copies of the covered work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">conveyed by you (or copies made from those copies), or (b) primarily</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">for and in connection with specific products or compilations that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">contain the covered work, unless you entered into that arrangement,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">or that patent license was granted, prior to 28 March 2007.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Nothing in this License shall be construed as excluding or limiting</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">any implied license or other defenses to infringement that may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">otherwise be available to you under applicable patent law.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  12. No Surrender of Others\' Freedom.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If conditions are imposed on you (whether by court order, agreement or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">otherwise) that contradict the conditions of this License, they do not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">excuse you from the conditions of this License.  If you cannot convey a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">covered work so as to satisfy simultaneously your obligations under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License and any other pertinent obligations, then as a consequence you may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">not convey it at all.  For example, if you agree to terms that obligate you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to collect a royalty for further conveying from those to whom you convey</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the Program, the only way you could satisfy both those terms and this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License would be to refrain entirely from conveying the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  13. Use with the GNU Affero General Public License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Notwithstanding any other provision of this License, you have</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">permission to link or combine any covered work with a work licensed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">under version 3 of the GNU Affero General Public License into a single</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">combined work, and to convey the resulting work.  The terms of this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">License will continue to apply to the part which is the covered work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">but the special requirements of the GNU Affero General Public License,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">section 13, concerning interaction through a network will apply to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">combination as such.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  14. Revised Versions of this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The Free Software Foundation may publish revised and/or new versions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the GNU General Public License from time to time.  Such new versions will</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">be similar in spirit to the present version, but may differ in detail to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">address new problems or concerns.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Each version is given a distinguishing version number.  If the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Program specifies that a certain numbered version of the GNU General</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Public License &quot;or any later version&quot; applies to it, you have the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">option of following the terms and conditions either of that numbered</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">version or of any later version published by the Free Software</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Foundation.  If the Program does not specify a version number of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">GNU General Public License, you may choose any version ever published</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">by the Free Software Foundation.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If the Program specifies that a proxy can decide which future</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">versions of the GNU General Public License can be used, that proxy\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">public statement of acceptance of a version permanently authorizes you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to choose that version for the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  Later license versions may give you additional or different</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">permissions.  However, no additional obligations are imposed on any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">author or copyright holder as a result of your choosing to follow a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  15. Disclaimer of Warranty.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM &quot;AS IS&quot; WITHOUT WARRANTY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">ALL NECESSARY SERVICING, REPAIR OR CORRECTION.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  16. Limitation of Liability.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">SUCH DAMAGES.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  17. Interpretation of Sections 15 and 16.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If the disclaimer of warranty and limitation of liability provided</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">above cannot be given local legal effect according to their terms,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">reviewing courts shall apply local law that most closely approximates</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">an absolute waiver of all civil liability in connection with the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Program, unless a warranty or assumption of liability accompanies a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">copy of the Program in return for a fee.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">                     END OF TERMS AND CONDITIONS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">            How to Apply These Terms to Your New Programs</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If you develop a new program, and you want it to be of the greatest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">possible use to the public, the best way to achieve this is to make it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">free software which everyone can redistribute and change under these terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  To do so, attach the following notices to the program.  It is safest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">to attach them to the start of each source file to most effectively</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">state the exclusion of warranty; and each file should have at least</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the &quot;copyright&quot; line and a pointer to where the full notice is found.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    &lt;one line to give the program\'s name and a brief idea of what it does.&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    This program is free software: you can redistribute it and/or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    the Free Software Foundation, either version 3 of the License, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    (at your option) any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    You should have received a copy of the GNU General Public License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Also add information on how to contact you by electronic and paper mail.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  If the program does terminal interaction, make it output a short</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">notice like this when it starts in an interactive mode:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    This is free software, and you are welcome to redistribute it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">    under certain conditions; type `show c\' for details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">The hypothetical commands `show w\' and `show c\' should show the appropriate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">parts of the General Public License.  Of course, your program\'s commands</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">might be different; for a GUI interface, you would use an &quot;about box&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  You should also get your employer (if you work as a programmer) or school,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">if any, to sign a &quot;copyright disclaimer&quot; for the program, if necessary.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">For more information on this, and how to apply and follow the GNU GPL, see</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">&lt;http://www.gnu.org/licenses/&gt;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">  The GNU General Public License does not permit incorporating your program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">into proprietary programs.  If your program is a subroutine library, you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">may consider it more useful to permit linking proprietary applications with</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">the library.  If this is what you want to do, use the GNU Lesser General</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Public License instead of this License.  But first, please read</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">&lt;http://www.gnu.org/philosophy/why-not-lgpl.html&gt;.</span></p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_46), _translate("MainWindow", "License", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Created by:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Yücel KILIÇ: </span><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">yucelkilic@myrafproject.org</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Muhammed SHEMUNI: </span><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">m.shemuni@myrafproject.org</span></p></body></html>", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_47), _translate("MainWindow", "Credits", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_11.setText(_translate("MainWindow", "Delete", None))
        self.pushButton_10.setText(_translate("MainWindow", "Save", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_48), _translate("MainWindow", "Log Viewer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_41), _translate("MainWindow", "Help", None))

from gingawidgetFile import gingaWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

