# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\myraf.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(801, 800)
        Form.setMinimumSize(QtCore.QSize(800, 800))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.listWidget_6 = QtWidgets.QListWidget(self.tab_7)
        self.listWidget_6.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_6.setObjectName("listWidget_6")
        self.gridLayout_7.addWidget(self.listWidget_6, 0, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.tab_7)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_5.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_7.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_6.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_7.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.listWidget_7 = QtWidgets.QListWidget(self.tab_8)
        self.listWidget_7.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_7.setObjectName("listWidget_7")
        self.gridLayout_8.addWidget(self.listWidget_7, 0, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.tab_8)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_37.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_37.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_8.addWidget(self.pushButton_37, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_8.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_8.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_8.addWidget(self.pushButton_8, 1, 3, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.listWidget_8 = QtWidgets.QListWidget(self.tab_9)
        self.listWidget_8.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_8.setObjectName("listWidget_8")
        self.gridLayout_9.addWidget(self.listWidget_8, 0, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.tab_9)
        self.label_5.setObjectName("label_5")
        self.gridLayout_9.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_40.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_40.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_9.addWidget(self.pushButton_40, 1, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_9.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_9.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_9.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_10.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_10.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_9.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.listWidget_9 = QtWidgets.QListWidget(self.tab_10)
        self.listWidget_9.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_9.setObjectName("listWidget_9")
        self.gridLayout_10.addWidget(self.listWidget_9, 0, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.tab_10)
        self.label_6.setObjectName("label_6")
        self.gridLayout_10.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_41.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_41.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_10.addWidget(self.pushButton_41, 1, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_11.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_11.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_10)
        self.pushButton_12.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_12.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_10.addWidget(self.pushButton_12, 1, 3, 1, 1)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 2, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.disp_align = gingaWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_align.sizePolicy().hasHeightForWidth())
        self.disp_align.setSizePolicy(sizePolicy)
        self.disp_align.setObjectName("disp_align")
        self.gridLayout_39.addWidget(self.disp_align, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(170, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 2, 0, 1, 2)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 0, 1, 2, 1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.gridLayout_5.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.gridLayout_60 = QtWidgets.QGridLayout(self.tab_25)
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_25)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.disp_photometry = gingaWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_photometry.sizePolicy().hasHeightForWidth())
        self.disp_photometry.setSizePolicy(sizePolicy)
        self.disp_photometry.setObjectName("disp_photometry")
        self.gridLayout_44.addWidget(self.disp_photometry, 0, 0, 1, 1)
        self.gridLayout_60.addWidget(self.groupBox_3, 0, 0, 2, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_25)
        self.groupBox_4.setMinimumSize(QtCore.QSize(170, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_2.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout_12.addWidget(self.listWidget_2, 0, 0, 1, 2)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_14.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_14.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_12.addWidget(self.pushButton_14, 1, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_15.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_15.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_12.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.gridLayout_60.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_25 = QtWidgets.QGroupBox(self.tab_25)
        self.groupBox_25.setObjectName("groupBox_25")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.groupBox_25)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_25)
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_48.addWidget(self.pushButton_34, 0, 0, 1, 2)
        self.listWidget_14 = QtWidgets.QListWidget(self.groupBox_25)
        self.listWidget_14.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_14.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_14.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_14.setObjectName("listWidget_14")
        self.gridLayout_48.addWidget(self.listWidget_14, 1, 0, 1, 2)
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_25)
        self.pushButton_36.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_36.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_48.addWidget(self.pushButton_36, 2, 0, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_25)
        self.pushButton_35.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_35.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_48.addWidget(self.pushButton_35, 2, 1, 1, 1)
        self.gridLayout_60.addWidget(self.groupBox_25, 1, 1, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_8 = QtWidgets.QLabel(self.tab_25)
        self.label_8.setObjectName("label_8")
        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_25)
        self.pushButton_16.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_16.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_13.addWidget(self.pushButton_16, 0, 1, 2, 1)
        self.progressBar_4 = QtWidgets.QProgressBar(self.tab_25)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.gridLayout_13.addWidget(self.progressBar_4, 1, 0, 1, 1)
        self.gridLayout_60.addLayout(self.gridLayout_13, 2, 0, 1, 2)
        self.tabWidget_6.addTab(self.tab_25, "")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.gridLayout_63 = QtWidgets.QGridLayout(self.tab_26)
        self.gridLayout_63.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_63.setObjectName("gridLayout_63")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_26)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.disp_atrack = gingaWidget(self.groupBox_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_atrack.sizePolicy().hasHeightForWidth())
        self.disp_atrack.setSizePolicy(sizePolicy)
        self.disp_atrack.setObjectName("disp_atrack")
        self.gridLayout_49.addWidget(self.disp_atrack, 0, 0, 1, 1)
        self.gridLayout_63.addWidget(self.groupBox_16, 0, 0, 2, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.tab_26)
        self.groupBox_18.setMinimumSize(QtCore.QSize(170, 0))
        self.groupBox_18.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.listWidget_13 = QtWidgets.QListWidget(self.groupBox_18)
        self.listWidget_13.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_13.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_13.setObjectName("listWidget_13")
        self.gridLayout_55.addWidget(self.listWidget_13, 0, 0, 1, 2)
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_18)
        self.pushButton_32.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_32.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_55.addWidget(self.pushButton_32, 1, 0, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_18)
        self.pushButton_33.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_33.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_55.addWidget(self.pushButton_33, 1, 1, 1, 1)
        self.gridLayout_63.addWidget(self.groupBox_18, 0, 1, 1, 1)
        self.groupBox_26 = QtWidgets.QGroupBox(self.tab_26)
        self.groupBox_26.setObjectName("groupBox_26")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.groupBox_26)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.listWidget_15 = QtWidgets.QListWidget(self.groupBox_26)
        self.listWidget_15.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_15.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_15.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_15.setObjectName("listWidget_15")
        self.gridLayout_58.addWidget(self.listWidget_15, 1, 0, 1, 2)
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_26)
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_58.addWidget(self.pushButton_42, 0, 0, 1, 2)
        self.pushButton_43 = QtWidgets.QPushButton(self.groupBox_26)
        self.pushButton_43.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_43.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_58.addWidget(self.pushButton_43, 3, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_26)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_58.addWidget(self.checkBox_6, 3, 0, 1, 1)
        self.gridLayout_63.addWidget(self.groupBox_26, 1, 1, 1, 1)
        self.gridLayout_52 = QtWidgets.QGridLayout()
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.label_27 = QtWidgets.QLabel(self.tab_26)
        self.label_27.setObjectName("label_27")
        self.gridLayout_52.addWidget(self.label_27, 0, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.tab_26)
        self.pushButton_31.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_31.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_52.addWidget(self.pushButton_31, 0, 1, 2, 1)
        self.progressBar_7 = QtWidgets.QProgressBar(self.tab_26)
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setObjectName("progressBar_7")
        self.gridLayout_52.addWidget(self.progressBar_7, 1, 0, 1, 1)
        self.gridLayout_63.addLayout(self.gridLayout_52, 2, 0, 1, 2)
        self.tabWidget_6.addTab(self.tab_26, "")
        self.gridLayout_14.addWidget(self.tabWidget_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_8)
        self.listWidget_4.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget_4.setObjectName("listWidget_4")
        self.gridLayout_28.addWidget(self.listWidget_4, 0, 0, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_7.setMinimumSize(QtCore.QSize(170, 0))
        self.groupBox_7.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_7)
        self.listWidget_3.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_26.addWidget(self.listWidget_3, 0, 0, 1, 2)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_19.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_19.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_26.addWidget(self.pushButton_19, 1, 0, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_20.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_20.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_26.addWidget(self.pushButton_20, 1, 1, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_7, 0, 1, 2, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_11)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_15 = QtWidgets.QLabel(self.groupBox_9)
        self.label_15.setObjectName("label_15")
        self.gridLayout_29.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_29.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_9)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_29.addWidget(self.checkBox_5, 0, 2, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.groupBox_9)
        self.label_16.setObjectName("label_16")
        self.gridLayout_29.addWidget(self.label_16, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_29.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_12.setEnabled(False)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout_29.addWidget(self.comboBox_12, 1, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(293, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem, 2, 0, 1, 2)
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_38.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_38.setMaximumSize(QtCore.QSize(100, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../.designer/.designer/backup/img/rem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_38.setIcon(icon)
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_29.addWidget(self.pushButton_38, 2, 2, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_39.setMinimumSize(QtCore.QSize(130, 25))
        self.pushButton_39.setMaximumSize(QtCore.QSize(130, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../.designer/.designer/backup/img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_39.setIcon(icon1)
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_29.addWidget(self.pushButton_39, 2, 3, 1, 1)
        self.gridLayout_30.addWidget(self.groupBox_9, 1, 0, 1, 1)
        self.gridLayout_27 = QtWidgets.QGridLayout()
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_11)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.gridLayout_27.addWidget(self.progressBar_3, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_11)
        self.label_10.setObjectName("label_10")
        self.gridLayout_27.addWidget(self.label_10, 0, 0, 1, 1)
        self.gridLayout_30.addLayout(self.gridLayout_27, 2, 0, 1, 2)
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.label_20 = QtWidgets.QLabel(self.groupBox_12)
        self.label_20.setObjectName("label_20")
        self.gridLayout_46.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_46.addWidget(self.lineEdit_3, 0, 1, 1, 3)
        self.label_21 = QtWidgets.QLabel(self.groupBox_12)
        self.label_21.setObjectName("label_21")
        self.gridLayout_46.addWidget(self.label_21, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_46.addWidget(self.lineEdit_4, 1, 1, 1, 3)
        self.label_22 = QtWidgets.QLabel(self.groupBox_12)
        self.label_22.setObjectName("label_22")
        self.gridLayout_46.addWidget(self.label_22, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_46.addWidget(self.lineEdit_5, 2, 1, 1, 3)
        self.label_23 = QtWidgets.QLabel(self.groupBox_12)
        self.label_23.setObjectName("label_23")
        self.gridLayout_46.addWidget(self.label_23, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_46.addWidget(self.lineEdit_6, 3, 1, 1, 3)
        self.label_24 = QtWidgets.QLabel(self.groupBox_12)
        self.label_24.setObjectName("label_24")
        self.gridLayout_46.addWidget(self.label_24, 4, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_46.addWidget(self.lineEdit_7, 4, 1, 1, 3)
        self.label_26 = QtWidgets.QLabel(self.groupBox_12)
        self.label_26.setObjectName("label_26")
        self.gridLayout_46.addWidget(self.label_26, 5, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_12)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_46.addWidget(self.lineEdit_8, 5, 1, 1, 3)
        self.label_25 = QtWidgets.QLabel(self.groupBox_12)
        self.label_25.setObjectName("label_25")
        self.gridLayout_46.addWidget(self.label_25, 6, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_12)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_46.addWidget(self.plainTextEdit, 7, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(377, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_46.addItem(spacerItem1, 8, 0, 1, 2)
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_29.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_29.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_46.addWidget(self.pushButton_29, 8, 2, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_12)
        self.pushButton_30.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_30.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_46.addWidget(self.pushButton_30, 8, 3, 1, 1)
        self.gridLayout_47.addWidget(self.groupBox_12, 0, 0, 1, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_12)
        self.groupBox_11.setMinimumSize(QtCore.QSize(170, 0))
        self.groupBox_11.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.listWidget_12 = QtWidgets.QListWidget(self.groupBox_11)
        self.listWidget_12.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_12.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_12.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_12.setObjectName("listWidget_12")
        self.gridLayout_36.addWidget(self.listWidget_12, 0, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_36.addWidget(self.pushButton_13, 1, 0, 1, 1)
        self.gridLayout_47.addWidget(self.groupBox_11, 0, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.groupBox_32 = QtWidgets.QGroupBox(self.tab_13)
        self.groupBox_32.setObjectName("groupBox_32")
        self.gridLayout_61 = QtWidgets.QGridLayout(self.groupBox_32)
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.disp_cosmicC = gingaWidget(self.groupBox_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_cosmicC.sizePolicy().hasHeightForWidth())
        self.disp_cosmicC.setSizePolicy(sizePolicy)
        self.disp_cosmicC.setObjectName("disp_cosmicC")
        self.gridLayout_61.addWidget(self.disp_cosmicC, 0, 0, 1, 1)
        self.gridLayout_33.addWidget(self.groupBox_32, 0, 0, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_13)
        self.groupBox_10.setMinimumSize(QtCore.QSize(170, 0))
        self.groupBox_10.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.listWidget_5 = QtWidgets.QListWidget(self.groupBox_10)
        self.listWidget_5.setMinimumSize(QtCore.QSize(150, 0))
        self.listWidget_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_5.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_5.setObjectName("listWidget_5")
        self.gridLayout_31.addWidget(self.listWidget_5, 0, 0, 1, 2)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_21.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_21.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_31.addWidget(self.pushButton_21, 1, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_22.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_22.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_31.addWidget(self.pushButton_22, 1, 1, 1, 1)
        self.gridLayout_33.addWidget(self.groupBox_10, 0, 1, 1, 1)
        self.gridLayout_32 = QtWidgets.QGridLayout()
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.label_11 = QtWidgets.QLabel(self.tab_13)
        self.label_11.setObjectName("label_11")
        self.gridLayout_32.addWidget(self.label_11, 0, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_23.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_23.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_32.addWidget(self.pushButton_23, 0, 1, 2, 1)
        self.progressBar_5 = QtWidgets.QProgressBar(self.tab_13)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.gridLayout_32.addWidget(self.progressBar_5, 1, 0, 1, 1)
        self.gridLayout_33.addLayout(self.gridLayout_32, 1, 0, 1, 2)
        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.tab_14)
        self.gridLayout_34.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.listWidget_11 = QtWidgets.QListWidget(self.tab_14)
        self.listWidget_11.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_11.setObjectName("listWidget_11")
        self.gridLayout_34.addWidget(self.listWidget_11, 0, 0, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.tab_14)
        self.label_17.setObjectName("label_17")
        self.gridLayout_34.addWidget(self.label_17, 1, 0, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_25.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_25.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_34.addWidget(self.pushButton_25, 1, 1, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_24.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_24.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_34.addWidget(self.pushButton_24, 1, 2, 1, 1)
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.label_14 = QtWidgets.QLabel(self.tab_14)
        self.label_14.setObjectName("label_14")
        self.gridLayout_35.addWidget(self.label_14, 0, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.tab_14)
        self.pushButton_26.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_26.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_35.addWidget(self.pushButton_26, 0, 1, 2, 1)
        self.progressBar_6 = QtWidgets.QProgressBar(self.tab_14)
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.gridLayout_35.addWidget(self.progressBar_6, 1, 0, 1, 1)
        self.gridLayout_34.addLayout(self.gridLayout_35, 2, 0, 1, 3)
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.gridLayout_15.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem2 = QtWidgets.QSpacerItem(677, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem2, 2, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_17.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_17.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_16.addWidget(self.pushButton_17, 2, 1, 1, 1)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.gridLayout_62 = QtWidgets.QGridLayout(self.tab_17)
        self.gridLayout_62.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.groupBox_21 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.groupBox_21)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.gridLayout_54 = QtWidgets.QGridLayout()
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_21)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_54.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_21)
        self.label_18.setObjectName("label_18")
        self.gridLayout_54.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_21)
        self.label_13.setObjectName("label_13")
        self.gridLayout_54.addWidget(self.label_13, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_21)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_54.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.gridLayout_37.addLayout(self.gridLayout_54, 0, 0, 1, 1)
        self.gridLayout_62.addWidget(self.groupBox_21, 0, 0, 1, 1)
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_22.setObjectName("groupBox_22")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.groupBox_22)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.gridLayout_56 = QtWidgets.QGridLayout()
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.label_35 = QtWidgets.QLabel(self.groupBox_22)
        self.label_35.setObjectName("label_35")
        self.gridLayout_56.addWidget(self.label_35, 2, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_22)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_56.addWidget(self.comboBox_8, 2, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_22)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_56.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_22)
        self.label_29.setObjectName("label_29")
        self.gridLayout_56.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_22)
        self.label_30.setObjectName("label_30")
        self.gridLayout_56.addWidget(self.label_30, 1, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_22)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_56.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.gridLayout_38.addLayout(self.gridLayout_56, 0, 0, 1, 1)
        self.gridLayout_62.addWidget(self.groupBox_22, 0, 1, 2, 1)
        self.groupBox_23 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_23.setObjectName("groupBox_23")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.groupBox_23)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.label_36 = QtWidgets.QLabel(self.groupBox_23)
        self.label_36.setObjectName("label_36")
        self.gridLayout_57.addWidget(self.label_36, 2, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_23)
        self.label_32.setObjectName("label_32")
        self.gridLayout_57.addWidget(self.label_32, 0, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_23)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_57.addWidget(self.comboBox_6, 0, 1, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_23)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_57.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_23)
        self.label_33.setObjectName("label_33")
        self.gridLayout_57.addWidget(self.label_33, 1, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_23)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_57.addWidget(self.comboBox_9, 2, 1, 1, 1)
        self.gridLayout_50.addLayout(self.gridLayout_57, 0, 0, 1, 1)
        self.gridLayout_62.addWidget(self.groupBox_23, 1, 0, 2, 1)
        self.groupBox_24 = QtWidgets.QGroupBox(self.tab_17)
        self.groupBox_24.setObjectName("groupBox_24")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.groupBox_24)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_37 = QtWidgets.QLabel(self.groupBox_24)
        self.label_37.setObjectName("label_37")
        self.gridLayout_18.addWidget(self.label_37, 0, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_24)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.gridLayout_18.addWidget(self.comboBox_10, 0, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_24)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout_18.addWidget(self.label_28, 1, 0, 1, 2)
        self.gridLayout_51.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.gridLayout_62.addWidget(self.groupBox_24, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 184, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_62.addItem(spacerItem3, 3, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_17, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_11.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_11.addWidget(self.label_9, 1, 0, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.gridLayout_11.addWidget(self.comboBox_11, 1, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_71 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_71.setObjectName("gridLayout_71")
        self.label_65 = QtWidgets.QLabel(self.groupBox_20)
        self.label_65.setObjectName("label_65")
        self.gridLayout_71.addWidget(self.label_65, 0, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_71.addWidget(self.lineEdit_22, 0, 1, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.groupBox_20)
        self.label_66.setObjectName("label_66")
        self.gridLayout_71.addWidget(self.label_66, 1, 0, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_71.addWidget(self.lineEdit_23, 1, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_20, 0, 1, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_14.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_59 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.label_40 = QtWidgets.QLabel(self.groupBox_14)
        self.label_40.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_40.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_59.addWidget(self.label_40, 0, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_14)
        self.doubleSpinBox_2.setDecimals(2)
        self.doubleSpinBox_2.setMinimum(2.0)
        self.doubleSpinBox_2.setMaximum(100.0)
        self.doubleSpinBox_2.setProperty("value", 12.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_59.addWidget(self.doubleSpinBox_2, 0, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox_14)
        self.label_42.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_59.addWidget(self.label_42, 1, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_14)
        self.doubleSpinBox.setDecimals(2)
        self.doubleSpinBox.setMaximum(100.0)
        self.doubleSpinBox.setProperty("value", 5.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_59.addWidget(self.doubleSpinBox, 1, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.groupBox_14)
        self.label_46.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_59.addWidget(self.label_46, 2, 0, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox_14)
        self.doubleSpinBox_3.setDecimals(2)
        self.doubleSpinBox_3.setMaximum(100.0)
        self.doubleSpinBox_3.setProperty("value", 5.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_59.addWidget(self.doubleSpinBox_3, 2, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_14, 1, 0, 1, 1)
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_69 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_69.setObjectName("gridLayout_69")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_17)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_69.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_17)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_69.addWidget(self.lineEdit_25, 4, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.groupBox_17)
        self.label_47.setObjectName("label_47")
        self.gridLayout_69.addWidget(self.label_47, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_17)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_69.addWidget(self.checkBox_4, 4, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.groupBox_17)
        self.label_48.setObjectName("label_48")
        self.gridLayout_69.addWidget(self.label_48, 1, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_17)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_69.addWidget(self.lineEdit_18, 0, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_17, 1, 1, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.label_39 = QtWidgets.QLabel(self.groupBox_13)
        self.label_39.setObjectName("label_39")
        self.gridLayout_53.addWidget(self.label_39, 1, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_53.addWidget(self.lineEdit_13, 0, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_13)
        self.label_38.setObjectName("label_38")
        self.gridLayout_53.addWidget(self.label_38, 0, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_14.setMaxLength(8)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_53.addWidget(self.lineEdit_14, 1, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_13, 2, 0, 1, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_19)
        self.doubleSpinBox_4.setDecimals(0)
        self.doubleSpinBox_4.setMinimum(2.0)
        self.doubleSpinBox_4.setMaximum(100.0)
        self.doubleSpinBox_4.setProperty("value", 2.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_41.addWidget(self.doubleSpinBox_4, 0, 1, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.groupBox_19)
        self.label_64.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_64.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_41.addWidget(self.label_64, 0, 0, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.groupBox_19)
        self.label_70.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_70.setObjectName("label_70")
        self.gridLayout_41.addWidget(self.label_70, 2, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_19)
        self.spinBox.setMaximum(20000)
        self.spinBox.setProperty("value", 500)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_41.addWidget(self.spinBox, 2, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_19, 2, 1, 1, 1)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_44 = QtWidgets.QLabel(self.groupBox_15)
        self.label_44.setObjectName("label_44")
        self.gridLayout_20.addWidget(self.label_44, 0, 0, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox_5.setMinimum(1.0)
        self.doubleSpinBox_5.setMaximum(100.0)
        self.doubleSpinBox_5.setProperty("value", 10.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_20.addWidget(self.doubleSpinBox_5, 0, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.groupBox_15)
        self.label_45.setObjectName("label_45")
        self.gridLayout_20.addWidget(self.label_45, 1, 0, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox_15)
        self.doubleSpinBox_8.setMaximum(200.0)
        self.doubleSpinBox_8.setProperty("value", 25.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_20.addWidget(self.doubleSpinBox_8, 1, 1, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.groupBox_15)
        self.label_57.setObjectName("label_57")
        self.gridLayout_20.addWidget(self.label_57, 2, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_15)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_20.addWidget(self.lineEdit_26, 2, 1, 1, 1)
        self.gridLayout_17.addWidget(self.groupBox_15, 3, 0, 1, 1)
        self.groupBox_31 = QtWidgets.QGroupBox(self.tab_16)
        self.groupBox_31.setObjectName("groupBox_31")
        self.gridLayout_68 = QtWidgets.QGridLayout(self.groupBox_31)
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.pushButton_50 = QtWidgets.QPushButton(self.groupBox_31)
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_68.addWidget(self.pushButton_50, 1, 1, 1, 1)
        self.listWidget_20 = QtWidgets.QListWidget(self.groupBox_31)
        self.listWidget_20.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_20.setObjectName("listWidget_20")
        self.gridLayout_68.addWidget(self.listWidget_20, 0, 2, 3, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.groupBox_31)
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_68.addWidget(self.pushButton_49, 0, 1, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.groupBox_31)
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_68.addWidget(self.pushButton_51, 2, 1, 1, 1)
        self.listWidget_19 = QtWidgets.QListWidget(self.groupBox_31)
        self.listWidget_19.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_19.setObjectName("listWidget_19")
        self.gridLayout_68.addWidget(self.listWidget_19, 0, 0, 3, 1)
        self.gridLayout_17.addWidget(self.groupBox_31, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 247, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 241, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_17.addItem(spacerItem5, 4, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_16, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_18)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_84 = QtWidgets.QLabel(self.tab_18)
        self.label_84.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_84.setObjectName("label_84")
        self.gridLayout_19.addWidget(self.label_84, 0, 0, 1, 1)
        self.doubleSpinBox_20 = QtWidgets.QDoubleSpinBox(self.tab_18)
        self.doubleSpinBox_20.setDecimals(7)
        self.doubleSpinBox_20.setMaximum(100000000.0)
        self.doubleSpinBox_20.setSingleStep(0.1)
        self.doubleSpinBox_20.setProperty("value", 2.2)
        self.doubleSpinBox_20.setObjectName("doubleSpinBox_20")
        self.gridLayout_19.addWidget(self.doubleSpinBox_20, 0, 1, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.tab_18)
        self.label_85.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_85.setObjectName("label_85")
        self.gridLayout_19.addWidget(self.label_85, 1, 0, 1, 1)
        self.doubleSpinBox_21 = QtWidgets.QDoubleSpinBox(self.tab_18)
        self.doubleSpinBox_21.setDecimals(7)
        self.doubleSpinBox_21.setMaximum(100000000.0)
        self.doubleSpinBox_21.setSingleStep(0.1)
        self.doubleSpinBox_21.setProperty("value", 10.0)
        self.doubleSpinBox_21.setObjectName("doubleSpinBox_21")
        self.gridLayout_19.addWidget(self.doubleSpinBox_21, 1, 1, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.tab_18)
        self.label_86.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_86.setObjectName("label_86")
        self.gridLayout_19.addWidget(self.label_86, 2, 0, 1, 1)
        self.doubleSpinBox_22 = QtWidgets.QDoubleSpinBox(self.tab_18)
        self.doubleSpinBox_22.setDecimals(7)
        self.doubleSpinBox_22.setMaximum(100000000.0)
        self.doubleSpinBox_22.setSingleStep(0.1)
        self.doubleSpinBox_22.setProperty("value", 5.0)
        self.doubleSpinBox_22.setObjectName("doubleSpinBox_22")
        self.gridLayout_19.addWidget(self.doubleSpinBox_22, 2, 1, 1, 1)
        self.label_87 = QtWidgets.QLabel(self.tab_18)
        self.label_87.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_87.setObjectName("label_87")
        self.gridLayout_19.addWidget(self.label_87, 3, 0, 1, 1)
        self.doubleSpinBox_23 = QtWidgets.QDoubleSpinBox(self.tab_18)
        self.doubleSpinBox_23.setDecimals(7)
        self.doubleSpinBox_23.setMaximum(100000000.0)
        self.doubleSpinBox_23.setSingleStep(0.1)
        self.doubleSpinBox_23.setProperty("value", 0.3)
        self.doubleSpinBox_23.setObjectName("doubleSpinBox_23")
        self.gridLayout_19.addWidget(self.doubleSpinBox_23, 3, 1, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.tab_18)
        self.label_88.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_88.setObjectName("label_88")
        self.gridLayout_19.addWidget(self.label_88, 4, 0, 1, 1)
        self.doubleSpinBox_24 = QtWidgets.QDoubleSpinBox(self.tab_18)
        self.doubleSpinBox_24.setDecimals(7)
        self.doubleSpinBox_24.setMaximum(100000000.0)
        self.doubleSpinBox_24.setSingleStep(0.1)
        self.doubleSpinBox_24.setProperty("value", 5.0)
        self.doubleSpinBox_24.setObjectName("doubleSpinBox_24")
        self.gridLayout_19.addWidget(self.doubleSpinBox_24, 4, 1, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.tab_18)
        self.label_89.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_89.setObjectName("label_89")
        self.gridLayout_19.addWidget(self.label_89, 5, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_18)
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setProperty("value", 4)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_19.addWidget(self.spinBox_2, 5, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_18)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_19.addWidget(self.checkBox_3, 6, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 530, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem6, 7, 0, 1, 2)
        self.tabWidget_4.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_19)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_19)
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_73 = QtWidgets.QLabel(self.groupBox_5)
        self.label_73.setObjectName("label_73")
        self.gridLayout_21.addWidget(self.label_73, 1, 0, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_21.addWidget(self.lineEdit_27, 0, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.groupBox_5)
        self.label_72.setObjectName("label_72")
        self.gridLayout_21.addWidget(self.label_72, 0, 0, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_21.addWidget(self.lineEdit_28, 1, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_21.addWidget(self.checkBox_2, 2, 0, 1, 2)
        self.gridLayout_22.addWidget(self.groupBox_5, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 452, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem7, 1, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_19, "")
        self.gridLayout_16.addWidget(self.tabWidget_4, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.tab_20)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_20)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_40.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_21)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        spacerItem8 = QtWidgets.QSpacerItem(20, 481, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem8, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_21)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_23.addWidget(self.label_12, 1, 0, 1, 2)
        self.progressBar_8 = QtWidgets.QProgressBar(self.tab_21)
        self.progressBar_8.setProperty("value", 0)
        self.progressBar_8.setObjectName("progressBar_8")
        self.gridLayout_23.addWidget(self.progressBar_8, 2, 0, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_23.addWidget(self.pushButton_52, 2, 1, 1, 1)
        self.tabWidget_5.addTab(self.tab_21, "")
        self.tab_32 = QtWidgets.QWidget()
        self.tab_32.setObjectName("tab_32")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.tab_32)
        self.gridLayout_45.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_32)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout_45.addWidget(self.textBrowser_4, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_32, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.tab_22)
        self.gridLayout_42.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_22)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout_42.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_22, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.tab_23)
        self.gridLayout_43.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_23)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_43.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_23, "")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.tab_24)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.listWidget_10 = QtWidgets.QListWidget(self.tab_24)
        self.listWidget_10.setObjectName("listWidget_10")
        self.gridLayout_25.addWidget(self.listWidget_10, 0, 0, 1, 4)
        self.label_19 = QtWidgets.QLabel(self.tab_24)
        self.label_19.setObjectName("label_19")
        self.gridLayout_25.addWidget(self.label_19, 1, 0, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_28.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_28.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_25.addWidget(self.pushButton_28, 1, 1, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_27.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_27.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_25.addWidget(self.pushButton_27, 1, 2, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_24)
        self.pushButton_18.setMinimumSize(QtCore.QSize(72, 0))
        self.pushButton_18.setMaximumSize(QtCore.QSize(72, 16777215))
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_25.addWidget(self.pushButton_18, 1, 3, 1, 1)
        self.tabWidget_5.addTab(self.tab_24, "")
        self.gridLayout_24.addWidget(self.tabWidget_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MYRaf V3"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton_5.setText(_translate("Form", "Remove"))
        self.pushButton_6.setText(_translate("Form", "Add"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "Images"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.pushButton_37.setText(_translate("Form", "Save"))
        self.pushButton_7.setText(_translate("Form", "Remove"))
        self.pushButton_8.setText(_translate("Form", "Add"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "Bias"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.pushButton_40.setText(_translate("Form", "Save"))
        self.pushButton_9.setText(_translate("Form", "Remove"))
        self.pushButton_10.setText(_translate("Form", "Add"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Form", "Dark"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.pushButton_41.setText(_translate("Form", "Save"))
        self.pushButton_11.setText(_translate("Form", "Remove"))
        self.pushButton_12.setText(_translate("Form", "Add"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("Form", "Flat"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", ":go"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Calibration"))
        self.groupBox.setTitle(_translate("Form", "Image"))
        self.groupBox_2.setTitle(_translate("Form", "File List"))
        self.pushButton_4.setText(_translate("Form", "Remove"))
        self.pushButton_3.setText(_translate("Form", "Add"))
        self.checkBox.setText(_translate("Form", "Auto Align"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", ":go"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Align"))
        self.groupBox_3.setTitle(_translate("Form", "Image"))
        self.groupBox_4.setTitle(_translate("Form", "File List"))
        self.pushButton_14.setText(_translate("Form", "Remove"))
        self.pushButton_15.setText(_translate("Form", "Add"))
        self.groupBox_25.setTitle(_translate("Form", "Coordinates"))
        self.pushButton_34.setText(_translate("Form", "Run Sex!"))
        self.pushButton_36.setText(_translate("Form", "Remove"))
        self.pushButton_35.setText(_translate("Form", "Display"))
        self.label_8.setText(_translate("Form", "TextLabel"))
        self.pushButton_16.setText(_translate("Form", ":go"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_25), _translate("Form", "Classic"))
        self.groupBox_16.setTitle(_translate("Form", "Image"))
        self.groupBox_18.setTitle(_translate("Form", "File List"))
        self.pushButton_32.setText(_translate("Form", "Remove"))
        self.pushButton_33.setText(_translate("Form", "Add"))
        self.groupBox_26.setTitle(_translate("Form", "Objects"))
        self.pushButton_42.setText(_translate("Form", "Run A-Track!"))
        self.pushButton_43.setText(_translate("Form", "Remove"))
        self.checkBox_6.setText(_translate("Form", "Display"))
        self.label_27.setText(_translate("Form", "TextLabel"))
        self.pushButton_31.setText(_translate("Form", ":go"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_26), _translate("Form", "A-Track"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Photometry"))
        self.groupBox_8.setTitle(_translate("Form", "Header"))
        self.groupBox_7.setTitle(_translate("Form", "File List"))
        self.pushButton_19.setText(_translate("Form", "Remove"))
        self.pushButton_20.setText(_translate("Form", "Add"))
        self.groupBox_9.setTitle(_translate("Form", "Operations:"))
        self.label_15.setText(_translate("Form", "Field:"))
        self.checkBox_5.setText(_translate("Form", "Use value from an existing field"))
        self.label_16.setText(_translate("Form", "Value:"))
        self.pushButton_38.setText(_translate("Form", "Delete"))
        self.pushButton_39.setText(_translate("Form", "Insert/Update"))
        self.label_10.setText(_translate("Form", "TextLabel"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("Form", "Header"))
        self.groupBox_12.setTitle(_translate("Form", "Properties"))
        self.label_20.setText(_translate("Form", "Observatory"))
        self.label_21.setText(_translate("Form", "Name"))
        self.label_22.setText(_translate("Form", "Longitude"))
        self.label_23.setText(_translate("Form", "Latitude"))
        self.label_24.setText(_translate("Form", "Altitude"))
        self.label_26.setText(_translate("Form", "Time Zone"))
        self.label_25.setText(_translate("Form", "Commendation"))
        self.pushButton_29.setText(_translate("Form", "Remove"))
        self.pushButton_30.setText(_translate("Form", "Add"))
        self.groupBox_11.setTitle(_translate("Form", "File List"))
        self.pushButton_13.setText(_translate("Form", "Reload"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("Form", "Observatory"))
        self.groupBox_32.setTitle(_translate("Form", "Display:"))
        self.groupBox_10.setTitle(_translate("Form", "File List"))
        self.pushButton_21.setText(_translate("Form", "Remove"))
        self.pushButton_22.setText(_translate("Form", "Add"))
        self.label_11.setText(_translate("Form", "TextLabel"))
        self.pushButton_23.setText(_translate("Form", ":go"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("Form", "Cosmic"))
        self.label_17.setText(_translate("Form", "TextLabel"))
        self.pushButton_25.setText(_translate("Form", "Remove"))
        self.pushButton_24.setText(_translate("Form", "Add"))
        self.label_14.setText(_translate("Form", "TextLabel"))
        self.pushButton_26.setText(_translate("Form", ":go"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("Form", "WCS"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("Form", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Editor"))
        self.pushButton_17.setText(_translate("Form", "Save"))
        self.groupBox_21.setTitle(_translate("Form", "Zero Combine Setting"))
        self.comboBox_2.setItemText(0, _translate("Form", "median"))
        self.comboBox_2.setItemText(1, _translate("Form", "average"))
        self.label_18.setText(_translate("Form", "Reject"))
        self.label_13.setText(_translate("Form", "Combine"))
        self.comboBox_3.setItemText(0, _translate("Form", "none"))
        self.comboBox_3.setItemText(1, _translate("Form", "minmax"))
        self.comboBox_3.setItemText(2, _translate("Form", "ccdclip"))
        self.comboBox_3.setItemText(3, _translate("Form", "crreject"))
        self.comboBox_3.setItemText(4, _translate("Form", "sigclip"))
        self.comboBox_3.setItemText(5, _translate("Form", "avsigclip"))
        self.comboBox_3.setItemText(6, _translate("Form", "pclip"))
        self.groupBox_22.setTitle(_translate("Form", "Dark Combine Setting"))
        self.label_35.setText(_translate("Form", "Scale"))
        self.comboBox_8.setItemText(0, _translate("Form", "exposure"))
        self.comboBox_8.setItemText(1, _translate("Form", "none"))
        self.comboBox_8.setItemText(2, _translate("Form", "mode"))
        self.comboBox_8.setItemText(3, _translate("Form", "median"))
        self.comboBox_8.setItemText(4, _translate("Form", "mean"))
        self.comboBox_4.setItemText(0, _translate("Form", "median"))
        self.comboBox_4.setItemText(1, _translate("Form", "average"))
        self.label_29.setText(_translate("Form", "Combine"))
        self.label_30.setText(_translate("Form", "Reject"))
        self.comboBox_5.setItemText(0, _translate("Form", "none"))
        self.comboBox_5.setItemText(1, _translate("Form", "minmax"))
        self.comboBox_5.setItemText(2, _translate("Form", "ccdclip"))
        self.comboBox_5.setItemText(3, _translate("Form", "crreject"))
        self.comboBox_5.setItemText(4, _translate("Form", "sigclip"))
        self.comboBox_5.setItemText(5, _translate("Form", "avsigclip"))
        self.comboBox_5.setItemText(6, _translate("Form", "pclip"))
        self.groupBox_23.setTitle(_translate("Form", "Flat Combine Setting"))
        self.label_36.setText(_translate("Form", "Subset"))
        self.label_32.setText(_translate("Form", "Combine"))
        self.comboBox_6.setItemText(0, _translate("Form", "median"))
        self.comboBox_6.setItemText(1, _translate("Form", "average"))
        self.comboBox_7.setItemText(0, _translate("Form", "none"))
        self.comboBox_7.setItemText(1, _translate("Form", "minmax"))
        self.comboBox_7.setItemText(2, _translate("Form", "ccdclip"))
        self.comboBox_7.setItemText(3, _translate("Form", "crreject"))
        self.comboBox_7.setItemText(4, _translate("Form", "sigclip"))
        self.comboBox_7.setItemText(5, _translate("Form", "avsigclip"))
        self.comboBox_7.setItemText(6, _translate("Form", "pclip"))
        self.label_33.setText(_translate("Form", "Reject"))
        self.comboBox_9.setItemText(0, _translate("Form", "yes"))
        self.comboBox_9.setItemText(1, _translate("Form", "no"))
        self.groupBox_24.setTitle(_translate("Form", "Calibration Ssetting"))
        self.label_37.setText(_translate("Form", "Subset"))
        self.comboBox_10.setItemText(0, _translate("Form", "yes"))
        self.comboBox_10.setItemText(1, _translate("Form", "no"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_17), _translate("Form", "Calibration"))
        self.groupBox_6.setTitle(_translate("Form", "Ensemble Photometry"))
        self.label_7.setText(_translate("Form", "Catalog"))
        self.comboBox.setItemText(0, _translate("Form", "NOMAD"))
        self.comboBox.setItemText(1, _translate("Form", "USNO"))
        self.comboBox.setItemText(2, _translate("Form", "Gaia"))
        self.label_9.setText(_translate("Form", "Filter"))
        self.comboBox_11.setItemText(0, _translate("Form", "R"))
        self.comboBox_11.setItemText(1, _translate("Form", "B"))
        self.comboBox_11.setItemText(2, _translate("Form", "V"))
        self.groupBox_20.setTitle(_translate("Form", "WCS"))
        self.label_65.setText(_translate("Form", "Right ascension"))
        self.lineEdit_22.setText(_translate("Form", "ra"))
        self.label_66.setText(_translate("Form", "Declination"))
        self.lineEdit_23.setText(_translate("Form", "dec"))
        self.groupBox_14.setTitle(_translate("Form", "FitSkyPars"))
        self.label_40.setText(_translate("Form", "Annulus"))
        self.label_42.setText(_translate("Form", "Dannulus"))
        self.label_46.setText(_translate("Form", "CBox"))
        self.groupBox_17.setTitle(_translate("Form", "Location and Time"))
        self.lineEdit_17.setText(_translate("Form", "time-obs"))
        self.label_47.setText(_translate("Form", "Observatory"))
        self.checkBox_4.setText(_translate("Form", "Epoch"))
        self.label_48.setToolTip(_translate("Form", "If not give DATE-OBS"))
        self.label_48.setText(_translate("Form", "TIME-OBS"))
        self.lineEdit_18.setText(_translate("Form", "observat"))
        self.groupBox_13.setTitle(_translate("Form", "DataPars"))
        self.label_39.setText(_translate("Form", "Filter"))
        self.lineEdit_13.setText(_translate("Form", "exptime"))
        self.label_38.setText(_translate("Form", "Exposur"))
        self.lineEdit_14.setText(_translate("Form", "subset"))
        self.groupBox_19.setTitle(_translate("Form", "Star finder"))
        self.label_64.setText(_translate("Form", "Threshold"))
        self.label_70.setText(_translate("Form", "Maximum Stars To find"))
        self.groupBox_15.setTitle(_translate("Form", "PhotPars"))
        self.label_44.setText(_translate("Form", "Apertur"))
        self.label_45.setText(_translate("Form", "ZMag"))
        self.label_57.setText(_translate("Form", "Gain"))
        self.lineEdit_26.setText(_translate("Form", "gain"))
        self.groupBox_31.setTitle(_translate("Form", "Extract From Header"))
        self.pushButton_50.setText(_translate("Form", "<<"))
        self.pushButton_49.setText(_translate("Form", ">>"))
        self.pushButton_51.setText(_translate("Form", "Update List"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), _translate("Form", "Photometry"))
        self.label_84.setText(_translate("Form", "Gain"))
        self.label_85.setText(_translate("Form", "Read Noise"))
        self.label_86.setText(_translate("Form", "Sigma Clip"))
        self.label_87.setText(_translate("Form", "Sigma Frac."))
        self.label_88.setText(_translate("Form", "Object Lim."))
        self.label_89.setText(_translate("Form", "Max Iteration"))
        self.checkBox_3.setText(_translate("Form", "Save Mask files"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_18), _translate("Form", "Cosmic Cleaner"))
        self.groupBox_5.setTitle(_translate("Form", "Go Online"))
        self.label_73.setText(_translate("Form", "Api Key"))
        self.lineEdit_27.setText(_translate("Form", "http://nova.astrometry.net/api/"))
        self.label_72.setText(_translate("Form", "Server"))
        self.checkBox_2.setText(_translate("Form", "Compress before upload"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_19), _translate("Form", "WCS(astrometry.net)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Settings"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic;\">The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic;\">For more information and help:</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">    Myraf Project Home Page</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600; font-style:italic;\">http://myrafproject.org/</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">    Myraf Project Wiki</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:600; font-style:italic;\">http://wiki.myrafproject.org/</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">    Myraf Project Blog</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic;\">http://myrafproject.org/blog/</span></p></body></html>"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_20), _translate("Form", "MYRaf"))
        self.pushButton_52.setText(_translate("Form", "Update MYRaf"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_21), _translate("Form", "Help"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040; background-color:#fcfcfc;\">Ginga Quick Reference</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"main-image-window\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">M</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">ain image window</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040;\">These keyboard and mouse operations are available when the main image window has the focus.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"panning-and-zooming-commands\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">P</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">anning and Zooming commands</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"><br /></span></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Scroll wheel turned</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Zoom in or out</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Digit (1234567890)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Zoom image to zoom steps 1, 2, ..., 9, 10</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Shift + Digit</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Zoom image to zoom steps -1, -2, ..., -9, -10</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Backquote (`)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Zoom image to fit window and center it</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#404040;\">Minus, Underscore</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040;\">(-, _)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Zoom out</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\">Equals, Plus</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff;\">(=, +)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Zoom in</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Middle (scroll) button drag</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Pan image freely (when zoomed in)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">p</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Set pan position for zooming</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Shift + Left click</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Set pan position for zooming</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">c</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Set pan position to the center of the image</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">q</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Pan image freely (when zoomed in); Left drag</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Ctrl + Left drag</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\">Proportional pan (press and drag left mouse</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff;\">button</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">apostrophe (‘)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Set autozoom for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-style:italic; color:#404040;\">override</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">doublequote (”)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Set autozoom for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-style:italic; color:#ffffff;\">on</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#404040;\">Ctrl + Scroll wheel</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040;\">turned</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Adjust zoom by intermediate coarse steps</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\">Shift + Scroll wheel</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff;\">turned</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Adjust zoom by intermediate fine steps</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"cut-levels-and-colormap-commands\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">C</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">ut levels and colormap commands</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"><br /></span></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">a</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Auto cut levels</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">s</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Cycle color distribution algorithm</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">S</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Reset color distribution algorithm to “linear”</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">period (.)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\">Interactive cut </span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; font-style:italic; color:#ffffff;\">both</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#ffffff;\"> low and high (with left</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff;\">mouse button)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">slash (/)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-weight:600; color:#404040;\">Interactive warp colormap (with left mouse</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040;\">button)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">semicolon (;)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Set autocuts for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-style:italic; color:#ffffff;\">override</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">colon (:)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Set autocuts for new images to</span><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; font-style:italic; color:#404040;\">on</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">question (?)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Restore the color map to its original state</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"transform-commands\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">T</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">ransform commands</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"><br /></span></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Left bracket ([)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Toggle flip image in X</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Left brace ({)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Reset to no flip of image in X</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Right bracket (])</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Toggle flip image in Y</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Right brace (})</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Reset to no flip image in Y</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Backslash (\\)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Swap X and Y axes</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Vertical bar (|)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Reset to no swap of X and Y axes</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">r</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Interactive rotate (with left mouse button)</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">R</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Restore rotation to 0 degrees</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">e</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Increment current rotation by 90 degrees</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">E</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Increment current rotation by -90 degrees</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">o</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Orient image by WCS so North=Up and East=Left</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">O</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Orient image by WCS so North=Up and East=Right</span></p></td></tr></table>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"reference-viewer-only\"></a><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">R</span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:11pt; font-weight:696; color:#404040;\">eference Viewer Only</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"><br /></span></p>\n"
"<table border=\"1\" style=\" margin-top:0px; margin-bottom:24px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">I</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Raise Info tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">H</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Raise Header tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Z</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Raise Zoom tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">D</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Raise Dialogs tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">T</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Raise Thumbs tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">C</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Raise Contents tab</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">left angle (&lt;)</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Toggle collapse left pane</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">right angle (&gt;)</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Toggle collapse right pane</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">f</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Toggle full screen</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">F</span></p></td>\n"
"<td bgcolor=\"#000000\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#ffffff; background-color:#000000;\">Panoramic full screen</span></p></td></tr>\n"
"<tr>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">m</span></p></td>\n"
"<td bgcolor=\"#f3f6f6\" style=\" vertical-align:middle; padding-left:16; padding-right:16; padding-top:8; padding-bottom:8;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040; background-color:#f3f6f6;\">Maximize window</span></p></td></tr></table>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600;\">Note:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040;\">If there are one or more plugins active, additional mouse or keyboard bindings may be present. In general, the left mouse button is used to select, pick or move, and the right mouse button is used to draw a shape for the operation.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Lato,proxima-nova,Helvetica Neue,Arial,sans-serif\'; font-size:11pt; color:#404040;\">On the Mac, control + mouse button can also be used to draw or right click. You can also press and release the space bar to make the next drag operation a drawing operation.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt;\">Ref = http://ginga.readthedocs.org/en/latest/quickref.html</span></p></body></html>"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_32), _translate("Form", "Ginga (Display)"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">GNU GENERAL PUBLIC LICENSE</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Version 3, 29 June 2007</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Copyright © 2007 Free Software Foundation, Inc. &lt;</span><span style=\" font-size:12pt;\">https://fsf.org/</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">&gt;</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"preamble\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">P</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">reamble</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The GNU General Public License is a free, copyleft license for software and other kinds of works.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">For the developers\' and authors\' protection, the GPL clearly explains that there is no warranty for this free software. For both users\' and authors\' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users\' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The precise terms and conditions for copying, distribution and modification follow.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"terms\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">T</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">ERMS AND CONDITIONS</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section0\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">0</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Definitions.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">“This License” refers to version 3 of the GNU General Public License.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">“Copyright” also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">“The Program” refers to any copyrightable work licensed under this License. Each licensee is addressed as “you”. “Licensees” and “recipients” may be individuals or organizations.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">To “modify” a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a “modified version” of the earlier work or a work “based on” the earlier work.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A “covered work” means either the unmodified Program or a work based on the Program.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">To “propagate” a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">To “convey” a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">An interactive user interface displays “Appropriate Legal Notices” to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section1\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Source Code.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The “source code” for a work means the preferred form of the work for making modifications to it. “Object code” means any non-source form of a work.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A “Standard Interface” means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The “System Libraries” of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A “Major Component”, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The “Corresponding Source” for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work\'s System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The Corresponding Source for a work in source code form is that same work.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section2\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">2</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Basic Permissions.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section3\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">3</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Protecting Users\' Legal Rights From Anti-Circumvention Law.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work\'s users, your or third parties\' legal rights to forbid circumvention of technological measures.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section4\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">4</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Conveying Verbatim Copies.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may convey verbatim copies of the Program\'s source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section5\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">5</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Conveying Modified Source Versions.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">a) The work must carry prominent notices stating that you modified it, and giving a relevant date.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to “keep intact all notices”.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an “aggregate” if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation\'s users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section6\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">6</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Conveying Non-Source Forms.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A “User Product” is either (1) a “consumer product”, which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, “normally used” refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">“Installation Information” for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section7\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">7</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Additional Terms.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">“Additional permissions” are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">d) Limiting the use for publicity purposes of names of licensors or authors of the material; or</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or</span></li>\n"
"<li style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:medium;\">f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">All other non-permissive additional terms are considered “further restrictions” within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section8\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">8</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Termination.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section9\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">9</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">. Acceptance Not Required for Having Copies.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a covered work, you indicate your acceptance of this License to do so.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section10\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">0. Automatic Licensing of Downstream Recipients.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">An “entity transaction” is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party\'s predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section11\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1. Patents.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A “contributor” is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor\'s “contributor version”.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A contributor\'s “essential patent claims” are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, “control” includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor\'s essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">In the following three paragraphs, a “patent license” is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To “grant” such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. “Knowingly relying” means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient\'s use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">A patent license is “discriminatory” if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section12\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">2. No Surrender of Others\' Freedom.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section13\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">3. Use with the GNU Affero General Public License.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Notwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section14\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">4. Revised Versions of this License.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy\'s public statement of acceptance of a version permanently authorizes you to choose that version for the Program.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section15\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">5. Disclaimer of Warranty.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section16\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">6. Limitation of Liability.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"section17\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">1</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">7. Interpretation of Sections 15 and 16.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If the disclaimer of warranty and limitation of liability provided above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">END OF TERMS AND CONDITIONS</span></p>\n"
"<p align=\"justify\" style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"howto\"></a><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">H</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:600; color:#000000;\">ow to Apply These Terms to Your New Programs</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the “copyright” line and a pointer to where the full notice is found.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    &lt;one line to give the program\'s name and a brief idea of what it does.&gt;</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    This program is free software: you can redistribute it and/or modify</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    the Free Software Foundation, either version 3 of the License, or</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    (at your option) any later version.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    GNU General Public License for more details.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    You should have received a copy of the GNU General Public License</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    along with this program.  If not, see &lt;https://www.gnu.org/licenses/&gt;.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">Also add information on how to contact you by electronic and paper mail.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    This is free software, and you are welcome to redistribute it</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt; color:#000000;\">    under certain conditions; type `show c\' for details.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The hypothetical commands `show w\' and `show c\' should show the appropriate parts of the General Public License. Of course, your program\'s commands might be different; for a GUI interface, you would use an “about box”.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">You should also get your employer (if you work as a programmer) or school, if any, to sign a “copyright disclaimer” for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see &lt;</span><span style=\" font-size:12pt;\">https://www.gnu.org/licenses/</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">&gt;.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with the library. If this is what you want to do, use the GNU Lesser General Public License instead of this License. But first, please read &lt;</span><span style=\" font-size:12pt;\">https://www.gnu.org/licenses/why-not-lgpl.html</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt; color:#000000;\">&gt;.</span></p></body></html>"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_22), _translate("Form", "License"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic;\">Created by:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic;\">Yücel KILIÇ: </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic; text-decoration: underline;\">yucelkilic@myrafproject.org</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic;\">Muhammed SHEMUNI: </span><span style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:600; font-style:italic; text-decoration: underline;\">m.shemuni@myrafproject.org</span></p></body></html>"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_23), _translate("Form", "Credits"))
        self.label_19.setText(_translate("Form", "TextLabel"))
        self.pushButton_28.setText(_translate("Form", "Reload"))
        self.pushButton_27.setText(_translate("Form", "Clear"))
        self.pushButton_18.setText(_translate("Form", "Save"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_24), _translate("Form", "Log Viewer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Help"))

from gingawidgetFile import gingaWidget
