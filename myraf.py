# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myraf.ui'
#
# Created: Mon Oct 22 03:15:34 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(756, 675)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(756, 675))
        Form.setMaximumSize(QtCore.QSize(756, 675))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/MYRaf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(True)
        self.gridLayout_16 = QtGui.QGridLayout(Form)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabCalibration = QtGui.QWidget()
        self.tabCalibration.setObjectName(_fromUtf8("tabCalibration"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabCalibration)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.checkBoxBias = QtGui.QCheckBox(self.tabCalibration)
        self.checkBoxBias.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBoxBias.setObjectName(_fromUtf8("checkBoxBias"))
        self.gridLayout_2.addWidget(self.checkBoxBias, 0, 0, 1, 1)
        self.checkBoxDark = QtGui.QCheckBox(self.tabCalibration)
        self.checkBoxDark.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBoxDark.setObjectName(_fromUtf8("checkBoxDark"))
        self.gridLayout_2.addWidget(self.checkBoxDark, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(517, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.checkBoxFlat = QtGui.QCheckBox(self.tabCalibration)
        self.checkBoxFlat.setMaximumSize(QtCore.QSize(60, 16777215))
        self.checkBoxFlat.setObjectName(_fromUtf8("checkBoxFlat"))
        self.gridLayout_2.addWidget(self.checkBoxFlat, 0, 2, 1, 1)
        self.tabWidgetCalibration = QtGui.QTabWidget(self.tabCalibration)
        self.tabWidgetCalibration.setObjectName(_fromUtf8("tabWidgetCalibration"))
        self.tabIMG = QtGui.QWidget()
        self.tabIMG.setObjectName(_fromUtf8("tabIMG"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tabIMG)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pushButtonIMGAdd = QtGui.QPushButton(self.tabIMG)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonIMGAdd.setIcon(icon1)
        self.pushButtonIMGAdd.setObjectName(_fromUtf8("pushButtonIMGAdd"))
        self.gridLayout_3.addWidget(self.pushButtonIMGAdd, 1, 3, 1, 1)
        self.pushButtonIMGRm = QtGui.QPushButton(self.tabIMG)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonIMGRm.setIcon(icon2)
        self.pushButtonIMGRm.setObjectName(_fromUtf8("pushButtonIMGRm"))
        self.gridLayout_3.addWidget(self.pushButtonIMGRm, 1, 2, 1, 1)
        self.listWidgetIMG = QtGui.QListWidget(self.tabIMG)
        self.listWidgetIMG.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetIMG.setObjectName(_fromUtf8("listWidgetIMG"))
        self.gridLayout_3.addWidget(self.listWidgetIMG, 0, 0, 1, 4)
        self.labelShowIMG = QtGui.QLabel(self.tabIMG)
        self.labelShowIMG.setObjectName(_fromUtf8("labelShowIMG"))
        self.gridLayout_3.addWidget(self.labelShowIMG, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(248, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.tabWidgetCalibration.addTab(self.tabIMG, _fromUtf8(""))
        self.tabBias = QtGui.QWidget()
        self.tabBias.setObjectName(_fromUtf8("tabBias"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tabBias)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.listWidgetIMGBias = QtGui.QListWidget(self.tabBias)
        self.listWidgetIMGBias.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetIMGBias.setObjectName(_fromUtf8("listWidgetIMGBias"))
        self.gridLayout_5.addWidget(self.listWidgetIMGBias, 0, 0, 1, 4)
        self.labelShowBias = QtGui.QLabel(self.tabBias)
        self.labelShowBias.setObjectName(_fromUtf8("labelShowBias"))
        self.gridLayout_5.addWidget(self.labelShowBias, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 1, 1, 1, 1)
        self.pushButtonBiasRm = QtGui.QPushButton(self.tabBias)
        self.pushButtonBiasRm.setIcon(icon2)
        self.pushButtonBiasRm.setObjectName(_fromUtf8("pushButtonBiasRm"))
        self.gridLayout_5.addWidget(self.pushButtonBiasRm, 1, 2, 1, 1)
        self.pushButtonBiasAdd = QtGui.QPushButton(self.tabBias)
        self.pushButtonBiasAdd.setIcon(icon1)
        self.pushButtonBiasAdd.setObjectName(_fromUtf8("pushButtonBiasAdd"))
        self.gridLayout_5.addWidget(self.pushButtonBiasAdd, 1, 3, 1, 1)
        self.tabWidgetCalibration.addTab(self.tabBias, _fromUtf8(""))
        self.tabDark = QtGui.QWidget()
        self.tabDark.setObjectName(_fromUtf8("tabDark"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tabDark)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.listWidgetDark = QtGui.QListWidget(self.tabDark)
        self.listWidgetDark.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetDark.setObjectName(_fromUtf8("listWidgetDark"))
        self.gridLayout_6.addWidget(self.listWidgetDark, 0, 0, 1, 4)
        self.labelShowDark = QtGui.QLabel(self.tabDark)
        self.labelShowDark.setObjectName(_fromUtf8("labelShowDark"))
        self.gridLayout_6.addWidget(self.labelShowDark, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 1, 1, 1, 1)
        self.pushButtonDarkRm = QtGui.QPushButton(self.tabDark)
        self.pushButtonDarkRm.setIcon(icon2)
        self.pushButtonDarkRm.setObjectName(_fromUtf8("pushButtonDarkRm"))
        self.gridLayout_6.addWidget(self.pushButtonDarkRm, 1, 2, 1, 1)
        self.pushButtonDarkAdd = QtGui.QPushButton(self.tabDark)
        self.pushButtonDarkAdd.setIcon(icon1)
        self.pushButtonDarkAdd.setObjectName(_fromUtf8("pushButtonDarkAdd"))
        self.gridLayout_6.addWidget(self.pushButtonDarkAdd, 1, 3, 1, 1)
        self.tabWidgetCalibration.addTab(self.tabDark, _fromUtf8(""))
        self.tabFlat = QtGui.QWidget()
        self.tabFlat.setObjectName(_fromUtf8("tabFlat"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tabFlat)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.listWidgetFlat = QtGui.QListWidget(self.tabFlat)
        self.listWidgetFlat.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetFlat.setObjectName(_fromUtf8("listWidgetFlat"))
        self.gridLayout_7.addWidget(self.listWidgetFlat, 0, 0, 1, 4)
        self.labelShowFlat = QtGui.QLabel(self.tabFlat)
        self.labelShowFlat.setObjectName(_fromUtf8("labelShowFlat"))
        self.gridLayout_7.addWidget(self.labelShowFlat, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 1, 1, 1, 1)
        self.pushButtonFlatRm = QtGui.QPushButton(self.tabFlat)
        self.pushButtonFlatRm.setIcon(icon2)
        self.pushButtonFlatRm.setObjectName(_fromUtf8("pushButtonFlatRm"))
        self.gridLayout_7.addWidget(self.pushButtonFlatRm, 1, 2, 1, 1)
        self.pushButtonFlatAdd = QtGui.QPushButton(self.tabFlat)
        self.pushButtonFlatAdd.setIcon(icon1)
        self.pushButtonFlatAdd.setObjectName(_fromUtf8("pushButtonFlatAdd"))
        self.gridLayout_7.addWidget(self.pushButtonFlatAdd, 1, 3, 1, 1)
        self.tabWidgetCalibration.addTab(self.tabFlat, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidgetCalibration, 1, 0, 1, 4)
        self.labelCalibPro = QtGui.QLabel(self.tabCalibration)
        self.labelCalibPro.setObjectName(_fromUtf8("labelCalibPro"))
        self.gridLayout_2.addWidget(self.labelCalibPro, 2, 0, 1, 4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBarCalib = QtGui.QProgressBar(self.tabCalibration)
        self.progressBarCalib.setProperty("value", 0)
        self.progressBarCalib.setObjectName(_fromUtf8("progressBarCalib"))
        self.horizontalLayout.addWidget(self.progressBarCalib)
        self.pushButtonGoCalib = QtGui.QPushButton(self.tabCalibration)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/go.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonGoCalib.setIcon(icon3)
        self.pushButtonGoCalib.setObjectName(_fromUtf8("pushButtonGoCalib"))
        self.horizontalLayout.addWidget(self.pushButtonGoCalib)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("img/cali.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabCalibration, icon4, _fromUtf8(""))
        self.tabPhotometry = QtGui.QWidget()
        self.tabPhotometry.setObjectName(_fromUtf8("tabPhotometry"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tabPhotometry)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.widget = QtGui.QWidget(self.tabPhotometry)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_14 = QtGui.QGridLayout(self.widget)
        self.gridLayout_14.setMargin(0)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        spacerItem5 = QtGui.QSpacerItem(73, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem5, 0, 0, 1, 3)
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setEnabled(False)
        self.checkBox.setMinimumSize(QtCore.QSize(21, 31))
        self.checkBox.setMaximumSize(QtCore.QSize(21, 31))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_14.addWidget(self.checkBox, 0, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("img/fh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_14.addWidget(self.pushButton, 0, 4, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.widget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setMinimumSize(QtCore.QSize(21, 31))
        self.checkBox_2.setMaximumSize(QtCore.QSize(21, 31))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_14.addWidget(self.checkBox_2, 0, 5, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_2.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_2.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("img/fv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_14.addWidget(self.pushButton_2, 0, 6, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_3.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_3.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("img/r.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_14.addWidget(self.pushButton_3, 0, 7, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QtCore.QSize(71, 31))
        self.lineEdit.setMaximumSize(QtCore.QSize(71, 31))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_14.addWidget(self.lineEdit, 0, 8, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(31, 31))
        self.pushButton_4.setMaximumSize(QtCore.QSize(31, 31))
        self.pushButton_4.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("img/rr.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_14.addWidget(self.pushButton_4, 0, 9, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(131, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem6, 0, 10, 1, 1)
        self.listWidget = QtGui.QListWidget(self.widget)
        self.listWidget.setEnabled(True)
        self.listWidget.setMinimumSize(QtCore.QSize(236, 454))
        self.listWidget.setMaximumSize(QtCore.QSize(236, 454))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_14.addWidget(self.listWidget, 0, 11, 2, 2)
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setMinimumSize(QtCore.QSize(450, 450))
        self.frame.setMaximumSize(QtCore.QSize(450, 450))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_13 = QtGui.QGridLayout(self.frame)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.label_30 = QtGui.QLabel(self.frame)
        self.label_30.setEnabled(False)
        self.label_30.setMinimumSize(QtCore.QSize(436, 436))
        self.label_30.setMaximumSize(QtCore.QSize(450, 450))
        self.label_30.setAutoFillBackground(True)
        self.label_30.setText(_fromUtf8(""))
        self.label_30.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_13.addWidget(self.label_30, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame, 1, 0, 2, 11)
        self.pushButtonAlignRm = QtGui.QPushButton(self.widget)
        self.pushButtonAlignRm.setMinimumSize(QtCore.QSize(91, 27))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("img/list-remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButtonAlignRm.setIcon(icon9)
        self.pushButtonAlignRm.setObjectName(_fromUtf8("pushButtonAlignRm"))
        self.gridLayout_14.addWidget(self.pushButtonAlignRm, 2, 11, 1, 1)
        self.pushButtonAlignAdd = QtGui.QPushButton(self.widget)
        self.pushButtonAlignAdd.setMinimumSize(QtCore.QSize(91, 27))
        self.pushButtonAlignAdd.setIcon(icon1)
        self.pushButtonAlignAdd.setObjectName(_fromUtf8("pushButtonAlignAdd"))
        self.gridLayout_14.addWidget(self.pushButtonAlignAdd, 2, 12, 1, 1)
        self.checkBoxAlign = QtGui.QCheckBox(self.widget)
        self.checkBoxAlign.setMaximumSize(QtCore.QSize(16777215, 22))
        self.checkBoxAlign.setChecked(False)
        self.checkBoxAlign.setObjectName(_fromUtf8("checkBoxAlign"))
        self.gridLayout_14.addWidget(self.checkBoxAlign, 3, 0, 1, 2)
        self.checkBox_3 = QtGui.QCheckBox(self.widget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_14.addWidget(self.checkBox_3, 3, 2, 1, 4)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_14.addWidget(self.label_3, 3, 11, 1, 1)
        self.comboBoxOBS_3 = QtGui.QComboBox(self.widget)
        self.comboBoxOBS_3.setMinimumSize(QtCore.QSize(80, 27))
        self.comboBoxOBS_3.setObjectName(_fromUtf8("comboBoxOBS_3"))
        self.gridLayout_14.addWidget(self.comboBoxOBS_3, 3, 12, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_14.addWidget(self.radioButton, 4, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_14.addWidget(self.lineEdit_2, 4, 1, 1, 5)
        self.radioButton_2 = QtGui.QRadioButton(self.widget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_14.addWidget(self.radioButton_2, 4, 6, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_14.addWidget(self.lineEdit_3, 4, 7, 1, 2)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_14.addWidget(self.label_2, 4, 11, 1, 1)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_14.addWidget(self.comboBox, 4, 12, 1, 1)
        self.labelPhotoPro = QtGui.QLabel(self.widget)
        self.labelPhotoPro.setMinimumSize(QtCore.QSize(0, 0))
        self.labelPhotoPro.setMaximumSize(QtCore.QSize(16777215, 33))
        self.labelPhotoPro.setObjectName(_fromUtf8("labelPhotoPro"))
        self.gridLayout_14.addWidget(self.labelPhotoPro, 5, 0, 1, 13)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.progressBarPhoto = QtGui.QProgressBar(self.widget)
        self.progressBarPhoto.setProperty("value", 0)
        self.progressBarPhoto.setObjectName(_fromUtf8("progressBarPhoto"))
        self.horizontalLayout_2.addWidget(self.progressBarPhoto)
        self.pushButtonGoPhoto = QtGui.QPushButton(self.widget)
        self.pushButtonGoPhoto.setIcon(icon3)
        self.pushButtonGoPhoto.setObjectName(_fromUtf8("pushButtonGoPhoto"))
        self.horizontalLayout_2.addWidget(self.pushButtonGoPhoto)
        self.gridLayout_14.addLayout(self.horizontalLayout_2, 6, 0, 1, 13)
        self.gridLayout_12.addWidget(self.widget, 0, 0, 1, 1)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("img/phot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabPhotometry, icon10, _fromUtf8(""))
        self.tabEditor = QtGui.QWidget()
        self.tabEditor.setObjectName(_fromUtf8("tabEditor"))
        self.gridLayout = QtGui.QGridLayout(self.tabEditor)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_28 = QtGui.QLabel(self.tabEditor)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout.addWidget(self.label_28, 0, 0, 1, 1)
        self.line_5 = QtGui.QFrame(self.tabEditor)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.gridLayout.addWidget(self.line_5, 0, 3, 2, 1)
        self.label_29 = QtGui.QLabel(self.tabEditor)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout.addWidget(self.label_29, 0, 4, 1, 1)
        self.listWidgetEditorHedit = QtGui.QListWidget(self.tabEditor)
        self.listWidgetEditorHedit.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetEditorHedit.setObjectName(_fromUtf8("listWidgetEditorHedit"))
        self.gridLayout.addWidget(self.listWidgetEditorHedit, 1, 0, 1, 3)
        self.listWidgetEditorHeditheader = QtGui.QListWidget(self.tabEditor)
        self.listWidgetEditorHeditheader.setObjectName(_fromUtf8("listWidgetEditorHeditheader"))
        self.gridLayout.addWidget(self.listWidgetEditorHeditheader, 1, 4, 1, 3)
        self.pushButtonEdiorHeditRemove = QtGui.QPushButton(self.tabEditor)
        self.pushButtonEdiorHeditRemove.setIcon(icon9)
        self.pushButtonEdiorHeditRemove.setObjectName(_fromUtf8("pushButtonEdiorHeditRemove"))
        self.gridLayout.addWidget(self.pushButtonEdiorHeditRemove, 2, 5, 1, 1)
        self.pushButtonEdiorHeditAdd = QtGui.QPushButton(self.tabEditor)
        self.pushButtonEdiorHeditAdd.setIcon(icon1)
        self.pushButtonEdiorHeditAdd.setObjectName(_fromUtf8("pushButtonEdiorHeditAdd"))
        self.gridLayout.addWidget(self.pushButtonEdiorHeditAdd, 2, 6, 1, 1)
        self.label = QtGui.QLabel(self.tabEditor)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.lineEditEdiorHeditFeild = QtGui.QLineEdit(self.tabEditor)
        self.lineEditEdiorHeditFeild.setMaxLength(8)
        self.lineEditEdiorHeditFeild.setObjectName(_fromUtf8("lineEditEdiorHeditFeild"))
        self.gridLayout.addWidget(self.lineEditEdiorHeditFeild, 3, 1, 1, 1)
        self.checkBoxEdiorHeditUseValueEx = QtGui.QCheckBox(self.tabEditor)
        self.checkBoxEdiorHeditUseValueEx.setObjectName(_fromUtf8("checkBoxEdiorHeditUseValueEx"))
        self.gridLayout.addWidget(self.checkBoxEdiorHeditUseValueEx, 3, 2, 1, 3)
        self.label_13 = QtGui.QLabel(self.tabEditor)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)
        self.lineEditEdiorHeditValue = QtGui.QLineEdit(self.tabEditor)
        self.lineEditEdiorHeditValue.setMaxLength(64)
        self.lineEditEdiorHeditValue.setObjectName(_fromUtf8("lineEditEdiorHeditValue"))
        self.gridLayout.addWidget(self.lineEditEdiorHeditValue, 4, 1, 1, 1)
        self.comboBoxEdiorHeditValueExist = QtGui.QComboBox(self.tabEditor)
        self.comboBoxEdiorHeditValueExist.setEnabled(False)
        self.comboBoxEdiorHeditValueExist.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxEdiorHeditValueExist.setObjectName(_fromUtf8("comboBoxEdiorHeditValueExist"))
        self.gridLayout.addWidget(self.comboBoxEdiorHeditValueExist, 4, 2, 1, 3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.progressBarEdiorHedit = QtGui.QProgressBar(self.tabEditor)
        self.progressBarEdiorHedit.setProperty("value", 0)
        self.progressBarEdiorHedit.setObjectName(_fromUtf8("progressBarEdiorHedit"))
        self.horizontalLayout_7.addWidget(self.progressBarEdiorHedit)
        self.pushButtonGoEdiorHedit = QtGui.QPushButton(self.tabEditor)
        self.pushButtonGoEdiorHedit.setIcon(icon3)
        self.pushButtonGoEdiorHedit.setObjectName(_fromUtf8("pushButtonGoEdiorHedit"))
        self.horizontalLayout_7.addWidget(self.pushButtonGoEdiorHedit)
        self.gridLayout.addLayout(self.horizontalLayout_7, 5, 0, 1, 7)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("img/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabEditor, icon11, _fromUtf8(""))
        self.tabHelp = QtGui.QWidget()
        self.tabHelp.setObjectName(_fromUtf8("tabHelp"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tabHelp)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_4 = QtGui.QLabel(self.tabHelp)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidgetHelp = QtGui.QTabWidget(self.tabHelp)
        self.tabWidgetHelp.setObjectName(_fromUtf8("tabWidgetHelp"))
        self.tabMYRafHelp = QtGui.QWidget()
        self.tabMYRafHelp.setObjectName(_fromUtf8("tabMYRafHelp"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tabMYRafHelp)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.checkBox_4 = QtGui.QCheckBox(self.tabMYRafHelp)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_8.addWidget(self.checkBox_4, 2, 0, 1, 1)
        self.textBrowserHelpMYRafHelp = QtGui.QTextBrowser(self.tabMYRafHelp)
        self.textBrowserHelpMYRafHelp.setObjectName(_fromUtf8("textBrowserHelpMYRafHelp"))
        self.gridLayout_8.addWidget(self.textBrowserHelpMYRafHelp, 1, 0, 1, 1)
        self.tabWidgetHelp.addTab(self.tabMYRafHelp, _fromUtf8(""))
        self.tabLogViewer = QtGui.QWidget()
        self.tabLogViewer.setObjectName(_fromUtf8("tabLogViewer"))
        self.gridLayout_10 = QtGui.QGridLayout(self.tabLogViewer)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.BrowserHelpLog = QtGui.QTextBrowser(self.tabLogViewer)
        self.BrowserHelpLog.setObjectName(_fromUtf8("BrowserHelpLog"))
        self.gridLayout_10.addWidget(self.BrowserHelpLog, 0, 0, 1, 3)
        spacerItem7 = QtGui.QSpacerItem(594, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 1, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.tabLogViewer)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_10.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButtonLogClear = QtGui.QPushButton(self.tabLogViewer)
        self.pushButtonLogClear.setObjectName(_fromUtf8("pushButtonLogClear"))
        self.gridLayout_10.addWidget(self.pushButtonLogClear, 1, 2, 1, 1)
        self.tabWidgetHelp.addTab(self.tabLogViewer, _fromUtf8(""))
        self.tabLicense = QtGui.QWidget()
        self.tabLicense.setObjectName(_fromUtf8("tabLicense"))
        self.gridLayout_11 = QtGui.QGridLayout(self.tabLicense)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.BrowserHelpLicense = QtGui.QTextBrowser(self.tabLicense)
        self.BrowserHelpLicense.setObjectName(_fromUtf8("BrowserHelpLicense"))
        self.gridLayout_11.addWidget(self.BrowserHelpLicense, 0, 0, 1, 1)
        self.tabWidgetHelp.addTab(self.tabLicense, _fromUtf8(""))
        self.tabDevelopers = QtGui.QWidget()
        self.tabDevelopers.setObjectName(_fromUtf8("tabDevelopers"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tabDevelopers)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.textBrowserHelpCredits = QtGui.QTextBrowser(self.tabDevelopers)
        self.textBrowserHelpCredits.setObjectName(_fromUtf8("textBrowserHelpCredits"))
        self.gridLayout_9.addWidget(self.textBrowserHelpCredits, 0, 0, 1, 1)
        self.tabWidgetHelp.addTab(self.tabDevelopers, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidgetHelp, 1, 0, 1, 1)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8("img/help-about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabHelp, icon12, _fromUtf8(""))
        self.gridLayout_16.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidgetCalibration.setCurrentIndex(0)
        self.tabWidgetHelp.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "MYRaf", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBias.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enable Zero correction</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxBias.setText(QtGui.QApplication.translate("Form", "Bias", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDark.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enable Dark correction</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxDark.setText(QtGui.QApplication.translate("Form", "Dark", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFlat.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enable Flat correction</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxFlat.setText(QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetCalibration.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonIMGAdd.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Add images for calibration</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonIMGAdd.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonIMGRm.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Remove selected image(s) from list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonIMGRm.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetIMG.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Images for calibration</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetIMG.setSortingEnabled(False)
        self.labelShowIMG.setText(QtGui.QApplication.translate("Form", "0 Files selected", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetCalibration.setTabText(self.tabWidgetCalibration.indexOf(self.tabIMG), QtGui.QApplication.translate("Form", "Images", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetIMGBias.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Bias images for calibration</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShowBias.setText(QtGui.QApplication.translate("Form", "0 Files selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBiasRm.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Remove selected image(s) from list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBiasRm.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBiasAdd.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Add bias/zero image(s)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonBiasAdd.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetCalibration.setTabText(self.tabWidgetCalibration.indexOf(self.tabBias), QtGui.QApplication.translate("Form", "Bias", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetDark.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Dark images for calibration</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShowDark.setText(QtGui.QApplication.translate("Form", "0 Files selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDarkRm.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Remove selected image(s) from list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDarkRm.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDarkAdd.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Add dark image(s)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDarkAdd.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetCalibration.setTabText(self.tabWidgetCalibration.indexOf(self.tabDark), QtGui.QApplication.translate("Form", "Dark", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetFlat.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Bias images for calibration</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShowFlat.setText(QtGui.QApplication.translate("Form", "0 Files selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFlatRm.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Remove selected image(s) from list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFlatRm.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFlatAdd.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Add flat image(s)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonFlatAdd.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetCalibration.setTabText(self.tabWidgetCalibration.indexOf(self.tabFlat), QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCalibPro.setText(QtGui.QApplication.translate("Form", "P Cal Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGoCalib.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Start Callibration  process</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGoCalib.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCalibration), QtGui.QApplication.translate("Form", "Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Flip Vectoral</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Flip Vectoral</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Flip Horizontal</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Flip Horizontal</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Rotate clockwise</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("Form", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Rotate Counterclockwise</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Images for alignment/photometry</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Display area for alignment/photometry</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAlignRm.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Remove selected image(s) from list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAlignRm.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAlignAdd.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Add images for alignment/photometry</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAlignAdd.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxAlign.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Enable alignment</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxAlign.setText(QtGui.QApplication.translate("Form", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Show alignment at last</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "Show me align", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Observatory selection</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Select Observatory:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxOBS_3.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Observatory selection</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Variable star\'s coordinates</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Form", "V:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Variable star\'s coordinates</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Check star\'s coordinates</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Form", "C:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Check star\'s coordinates</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Variant 1, using only scipy and the simple affine transorm.</p><p>Variant 2, using geomap/gregister, correcting also for distortions .</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Select Method", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Variant 1, using only scipy and the simple affine transorm.</p><p>Variant 2, using geomap/gregister, correcting also for distortions .</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Form", "Variant 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Form", "Variant 2", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPhotoPro.setText(QtGui.QApplication.translate("Form", "Po Pho Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGoPhoto.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Start alignment/photometry process</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGoPhoto.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPhotometry), QtGui.QApplication.translate("Form", "Photometry", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Form", "Image List:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Form", "Header:", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetEditorHedit.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Images for header editing</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidgetEditorHeditheader.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Header of selected file</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdiorHeditRemove.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Remove selected image(s) from list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdiorHeditRemove.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdiorHeditAdd.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Add image for header editing</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEdiorHeditAdd.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>The field will be added/updated for all list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Field", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEdiorHeditFeild.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>The field will be added/updated for all list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEdiorHeditUseValueEx.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Use this value for selected field</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxEdiorHeditUseValueEx.setText(QtGui.QApplication.translate("Form", "use value of an existing field.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>The value will added/updated for all list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditEdiorHeditValue.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>The value will added/updated for all list</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxEdiorHeditValueExist.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Use this value for selected field</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGoEdiorHedit.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Start header editin</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonGoEdiorHedit.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEditor), QtGui.QApplication.translate("Form", "Header Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Version 1.0-Beta", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Form", "Enable helping", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowserHelpMYRafHelp.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The MYRaf is a practicable astronomical image reduction and photometry software and interface for IRAF. For this purpose, MYRaf uses iraf, PyRAF and alipy via great programming language Python and Qt framework. Also MYRaf is a absolutely free software and distributed with GPLv3 license. You can use it without restrictive licenses, make copies for your friends, school or business.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">For more information and help:</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">    Myraf Project Home Page</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">        </span>http://myrafproject.org/</p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">    Myraf Project Wiki</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">        </span>http://wiki.myrafproject.org/</p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">    Myraf Project Blog</span></p>\n"
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\">        </span>http://myrafproject.org/blog/</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetHelp.setTabText(self.tabWidgetHelp.indexOf(self.tabMYRafHelp), QtGui.QApplication.translate("Form", "MYRaf Help", None, QtGui.QApplication.UnicodeUTF8))
        self.BrowserHelpLog.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Reload from Log file</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLogClear.setToolTip(QtGui.QApplication.translate("Form", "<html><head/><body><p>Clear the list below.</p><p><span style=\" font-weight:600;\">It will remove your log file.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLogClear.setText(QtGui.QApplication.translate("Form", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetHelp.setTabText(self.tabWidgetHelp.indexOf(self.tabLogViewer), QtGui.QApplication.translate("Form", "Log Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.BrowserHelpLicense.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                    GNU GENERAL PUBLIC LICENSE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                       Version 2, June 1991</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> Copyright (C) 1989, 1991 Free Software Foundation, Inc.,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> Everyone is permitted to copy and distribute verbatim copies</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> of this license document, but changing it is not allowed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                            Preamble</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  The licenses for most software are designed to take away your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">freedom to share and change it.  By contrast, the GNU General Public</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">License is intended to guarantee your freedom to share and change free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">software--to make sure the software is free for all its users.  This</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">General Public License applies to most of the Free Software</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Foundation\'s software and to any other program whose authors commit to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">using it.  (Some other Free Software Foundation software is covered by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the GNU Lesser General Public License instead.)  You can apply it to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">your programs, too.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  When we speak of free software, we are referring to freedom, not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">price.  Our General Public Licenses are designed to make sure that you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">have the freedom to distribute copies of free software (and charge for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">this service if you wish), that you receive source code or can get it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">if you want it, that you can change the software or use pieces of it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">in new free programs; and that you know you can do these things.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  To protect your rights, we need to make restrictions that forbid</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">anyone to deny you these rights or to ask you to surrender the rights.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">These restrictions translate to certain responsibilities for you if you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribute copies of the software, or if you modify it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  For example, if you distribute copies of such a program, whether</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">gratis or for a fee, you must give the recipients all the rights that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">you have.  You must make sure that they, too, receive or can get the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">source code.  And you must show them these terms so they know their</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">rights.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  We protect your rights with two steps: (1) copyright the software, and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">(2) offer you this license which gives you legal permission to copy,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribute and/or modify the software.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  Also, for each author\'s protection and ours, we want to make certain</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">that everyone understands that there is no warranty for this free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">software.  If the software is modified by someone else and passed on, we</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">want its recipients to know that what they have is not the original, so</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">that any problems introduced by others will not reflect on the original</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">authors\' reputations.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  Finally, any free program is threatened constantly by software</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">patents.  We wish to avoid the danger that redistributors of a free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">program will individually obtain patent licenses, in effect making the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">program proprietary.  To prevent this, we have made it clear that any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">patent must be licensed for everyone\'s free use or not licensed at all.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  The precise terms and conditions for copying, distribution and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">modification follow.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                    GNU GENERAL PUBLIC LICENSE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  0. This License applies to any program or other work which contains</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">a notice placed by the copyright holder saying it may be distributed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">under the terms of this General Public License.  The &quot;Program&quot;, below,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">refers to any such program or work, and a &quot;work based on the Program&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">means either the Program or any derivative work under copyright law:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">that is to say, a work containing the Program or a portion of it,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">either verbatim or with modifications and/or translated into another</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">language.  (Hereinafter, translation is included without limitation in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the term &quot;modification&quot;.)  Each licensee is addressed as &quot;you&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Activities other than copying, distribution and modification are not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">covered by this License; they are outside its scope.  The act of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">running the Program is not restricted, and the output from the Program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">is covered only if its contents constitute a work based on the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Program (independent of having been made by running the Program).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Whether that is true depends on what the Program does.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  1. You may copy and distribute verbatim copies of the Program\'s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">source code as you receive it, in any medium, provided that you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">conspicuously and appropriately publish on each copy an appropriate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">copyright notice and disclaimer of warranty; keep intact all the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">notices that refer to this License and to the absence of any warranty;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">and give any other recipients of the Program a copy of this License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">along with the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">You may charge a fee for the physical act of transferring a copy, and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">you may at your option offer warranty protection in exchange for a fee.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  2. You may modify your copy or copies of the Program or any portion</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">of it, thus forming a work based on the Program, and copy and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribute such modifications or work under the terms of Section 1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">above, provided that you also meet all of these conditions:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    a) You must cause the modified files to carry prominent notices</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    stating that you changed the files and the date of any change.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    b) You must cause any work that you distribute or publish, that in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    whole or in part contains or is derived from the Program or any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    part thereof, to be licensed as a whole at no charge to all third</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    parties under the terms of this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    c) If the modified program normally reads commands interactively</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    when run, you must cause it, when started running for such</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    interactive use in the most ordinary way, to print or display an</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    announcement including an appropriate copyright notice and a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    notice that there is no warranty (or else, saying that you provide</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    a warranty) and that users may redistribute the program under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    these conditions, and telling the user how to view a copy of this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    License.  (Exception: if the Program itself is interactive but</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    does not normally print such an announcement, your work based on</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    the Program is not required to print an announcement.)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">These requirements apply to the modified work as a whole.  If</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">identifiable sections of that work are not derived from the Program,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">and can be reasonably considered independent and separate works in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">themselves, then this License, and its terms, do not apply to those</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sections when you distribute them as separate works.  But when you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribute the same sections as part of a whole which is a work based</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">on the Program, the distribution of the whole must be on the terms of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">this License, whose permissions for other licensees extend to the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">entire whole, and thus to each and every part regardless of who wrote it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Thus, it is not the intent of this section to claim rights or contest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">your rights to work written entirely by you; rather, the intent is to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">exercise the right to control the distribution of derivative or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">collective works based on the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">In addition, mere aggregation of another work not based on the Program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">with the Program (or with a work based on the Program) on a volume of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">a storage or distribution medium does not bring the other work under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the scope of this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  3. You may copy and distribute the Program (or a work based on it,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">under Section 2) in object code or executable form under the terms of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sections 1 and 2 above provided that you also do one of the following:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    a) Accompany it with the complete corresponding machine-readable</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    source code, which must be distributed under the terms of Sections</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    1 and 2 above on a medium customarily used for software interchange; or,</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    b) Accompany it with a written offer, valid for at least three</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    years, to give any third party, for a charge no more than your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    cost of physically performing source distribution, a complete</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    machine-readable copy of the corresponding source code, to be</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    distributed under the terms of Sections 1 and 2 above on a medium</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    customarily used for software interchange; or,</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    c) Accompany it with the information you received as to the offer</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    to distribute corresponding source code.  (This alternative is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    allowed only for noncommercial distribution and only if you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    received the program in object code or executable form with such</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    an offer, in accord with Subsection b above.)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The source code for a work means the preferred form of the work for</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">making modifications to it.  For an executable work, complete source</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">code means all the source code for all modules it contains, plus any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">associated interface definition files, plus the scripts used to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">control compilation and installation of the executable.  However, as a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">special exception, the source code distributed need not include</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">anything that is normally distributed (in either source or binary</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">form) with the major components (compiler, kernel, and so on) of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">operating system on which the executable runs, unless that component</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">itself accompanies the executable.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If distribution of executable or object code is made by offering</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">access to copy from a designated place, then offering equivalent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">access to copy the source code from the same place counts as</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribution of the source code, even though third parties are not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">compelled to copy the source along with the object code.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  4. You may not copy, modify, sublicense, or distribute the Program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">except as expressly provided under this License.  Any attempt</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">otherwise to copy, modify, sublicense or distribute the Program is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">void, and will automatically terminate your rights under this License.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">However, parties who have received copies, or rights, from you under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">this License will not have their licenses terminated so long as such</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">parties remain in full compliance.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  5. You are not required to accept this License, since you have not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">signed it.  However, nothing else grants you permission to modify or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribute the Program or its derivative works.  These actions are</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">prohibited by law if you do not accept this License.  Therefore, by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">modifying or distributing the Program (or any work based on the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Program), you indicate your acceptance of this License to do so, and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">all its terms and conditions for copying, distributing or modifying</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the Program or works based on it.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  6. Each time you redistribute the Program (or any work based on the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Program), the recipient automatically receives a license from the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">original licensor to copy, distribute or modify the Program subject to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">these terms and conditions.  You may not impose any further</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">restrictions on the recipients\' exercise of the rights granted herein.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">You are not responsible for enforcing compliance by third parties to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  7. If, as a consequence of a court judgment or allegation of patent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">infringement or for any other reason (not limited to patent issues),</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">conditions are imposed on you (whether by court order, agreement or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">otherwise) that contradict the conditions of this License, they do not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">excuse you from the conditions of this License.  If you cannot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">distribute so as to satisfy simultaneously your obligations under this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">License and any other pertinent obligations, then as a consequence you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">may not distribute the Program at all.  For example, if a patent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">license would not permit royalty-free redistribution of the Program by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">all those who receive copies directly or indirectly through you, then</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the only way you could satisfy both it and this License would be to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">refrain entirely from distribution of the Program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If any portion of this section is held invalid or unenforceable under</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">any particular circumstance, the balance of the section is intended to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">apply and the section as a whole is intended to apply in other</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">circumstances.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">It is not the purpose of this section to induce you to infringe any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">patents or other property right claims or to contest validity of any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">such claims; this section has the sole purpose of protecting the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">integrity of the free software distribution system, which is</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">implemented by public license practices.  Many people have made</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">generous contributions to the wide range of software distributed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">through that system in reliance on consistent application of that</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">system; it is up to the author/donor to decide if he or she is willing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">to distribute software through any other system and a licensee cannot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">impose that choice.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This section is intended to make thoroughly clear what is believed to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">be a consequence of the rest of this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  8. If the distribution and/or use of the Program is restricted in</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">certain countries either by patents or by copyrighted interfaces, the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">original copyright holder who places the Program under this License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">may add an explicit geographical distribution limitation excluding</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">those countries, so that distribution is permitted only in or among</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">countries not thus excluded.  In such case, this License incorporates</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the limitation as if written in the body of this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  9. The Free Software Foundation may publish revised and/or new versions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">of the General Public License from time to time.  Such new versions will</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">be similar in spirit to the present version, but may differ in detail to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">address new problems or concerns.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Each version is given a distinguishing version number.  If the Program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">specifies a version number of this License which applies to it and &quot;any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">later version&quot;, you have the option of following the terms and conditions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">either of that version or of any later version published by the Free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Software Foundation.  If the Program does not specify a version number of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">this License, you may choose any version ever published by the Free Software</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Foundation.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  10. If you wish to incorporate parts of the Program into other free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">programs whose distribution conditions are different, write to the author</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">to ask for permission.  For software which is copyrighted by the Free</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Software Foundation, write to the Free Software Foundation; we sometimes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">make exceptions for this.  Our decision will be guided by the two goals</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">of preserving the free status of all derivatives of our free software and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">of promoting the sharing and reuse of software generally.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                            NO WARRANTY</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">PROVIDE THE PROGRAM &quot;AS IS&quot; WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">REPAIR OR CORRECTION.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">POSSIBILITY OF SUCH DAMAGES.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">                     END OF TERMS AND CONDITIONS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">            How to Apply These Terms to Your New Programs</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  If you develop a new program, and you want it to be of the greatest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">possible use to the public, the best way to achieve this is to make it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">free software which everyone can redistribute and change under these terms.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">  To do so, attach the following notices to the program.  It is safest</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">to attach them to the start of each source file to most effectively</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">convey the exclusion of warranty; and each file should have at least</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the &quot;copyright&quot; line and a pointer to where the full notice is found.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    &lt;one line to give the program\'s name and a brief idea of what it does.&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    This program is free software; you can redistribute it and/or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    it under the terms of the GNU General Public License as published by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    the Free Software Foundation; either version 2 of the License, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    (at your option) any later version.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    This program is distributed in the hope that it will be useful,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    GNU General Public License for more details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    You should have received a copy of the GNU General Public License along</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    with this program; if not, write to the Free Software Foundation, Inc.,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Also add information on how to contact you by electronic and paper mail.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">If the program is interactive, make it output a short notice like this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">when it starts in an interactive mode:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    Gnomovision version 69, Copyright (C) year name of author</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    This is free software, and you are welcome to redistribute it</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    under certain conditions; type `show c\' for details.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The hypothetical commands `show w\' and `show c\' should show the appropriate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">parts of the General Public License.  Of course, the commands you use may</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">be called something other than `show w\' and `show c\'; they could even be</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">mouse-clicks or menu items--whatever suits your program.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">You should also get your employer (if you work as a programmer) or your</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">school, if any, to sign a &quot;copyright disclaimer&quot; for the program, if</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">necessary.  Here is a sample; alter the names:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">The GNU General Public License does not permit incorporating your program</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">into proprietary programs.  If your program is a subroutine library, you</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">may consider it more useful to permit linking proprietary applications with</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">the library.  If this is what you want to do, use the GNU Lesser General</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Public License instead of this License.  But first, please read</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">http://www.gnu.org/philosophy/why-not-lgpl.html.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetHelp.setTabText(self.tabWidgetHelp.indexOf(self.tabLicense), QtGui.QApplication.translate("Form", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowserHelpCredits.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Created by:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Yücel KILIÇ: </span><span style=\" font-size:11pt; text-decoration: underline;\">yucelkilic@myrafproject.org</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Muhammed SHEMUNI: </span><span style=\" font-size:11pt; text-decoration: underline;\">m.shemuni@myrafproject.org</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidgetHelp.setTabText(self.tabWidgetHelp.indexOf(self.tabDevelopers), QtGui.QApplication.translate("Form", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHelp), QtGui.QApplication.translate("Form", "Help", None, QtGui.QApplication.UnicodeUTF8))

