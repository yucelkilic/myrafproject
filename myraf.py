# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myraf.ui'
#
# Created: Fri Dec 13 13:42:52 2013
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
        Form.resize(750, 653)
        Form.setMinimumSize(QtCore.QSize(750, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/MYRaf.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setMinimumSize(QtCore.QSize(60, 20))
        self.checkBox.setMaximumSize(QtCore.QSize(60, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_3.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setMinimumSize(QtCore.QSize(60, 20))
        self.checkBox_2.setMaximumSize(QtCore.QSize(60, 20))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.tab)
        self.checkBox_3.setMinimumSize(QtCore.QSize(60, 20))
        self.checkBox_3.setMaximumSize(QtCore.QSize(60, 20))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(self.tab)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_5.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab_6)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/rem.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_5.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_6)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.tab_6)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 3)
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.tab_8 = QtGui.QWidget()
        self.tab_8.setObjectName(_fromUtf8("tab_8"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_8)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_4 = QtGui.QLabel(self.tab_8)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.tab_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 25))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("img/sav.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout_6.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.tab_8)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_6.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.tab_8)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_6.addWidget(self.pushButton_5, 1, 3, 1, 1)
        self.listWidget_2 = QtGui.QListWidget(self.tab_8)
        self.listWidget_2.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.gridLayout_6.addWidget(self.listWidget_2, 0, 0, 1, 4)
        self.tabWidget_2.addTab(self.tab_8, _fromUtf8(""))
        self.tab_9 = QtGui.QWidget()
        self.tab_9.setObjectName(_fromUtf8("tab_9"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_9)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_5 = QtGui.QLabel(self.tab_9)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_8.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.tab_9)
        self.pushButton_9.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_9.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_8.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.tab_9)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout_8.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.tab_9)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_10.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_8.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.listWidget_3 = QtGui.QListWidget(self.tab_9)
        self.listWidget_3.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_3.setObjectName(_fromUtf8("listWidget_3"))
        self.gridLayout_8.addWidget(self.listWidget_3, 0, 0, 1, 4)
        self.tabWidget_2.addTab(self.tab_9, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_6 = QtGui.QLabel(self.tab_7)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.tab_7)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.gridLayout_7.addWidget(self.pushButton_12, 1, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.tab_7)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_11.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_7.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.pushButton_13 = QtGui.QPushButton(self.tab_7)
        self.pushButton_13.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_13.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.gridLayout_7.addWidget(self.pushButton_13, 1, 3, 1, 1)
        self.listWidget_4 = QtGui.QListWidget(self.tab_7)
        self.listWidget_4.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_4.setObjectName(_fromUtf8("listWidget_4"))
        self.gridLayout_7.addWidget(self.listWidget_4, 0, 0, 1, 4)
        self.tabWidget_2.addTab(self.tab_7, _fromUtf8(""))
        self.gridLayout_4.addWidget(self.tabWidget_2, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("img/run.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 2, 1)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.tabWidget_3 = QtGui.QTabWidget(self.tab_2)
        self.tabWidget_3.setObjectName(_fromUtf8("tabWidget_3"))
        self.tab_10 = QtGui.QWidget()
        self.tab_10.setObjectName(_fromUtf8("tab_10"))
        self.gridLayout_13 = QtGui.QGridLayout(self.tab_10)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_10)
        self.groupBox_2.setMinimumSize(QtCore.QSize(227, 481))
        self.groupBox_2.setMaximumSize(QtCore.QSize(227, 16777215))
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.pushButton_16 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_16.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_16.setIcon(icon2)
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.gridLayout_11.addWidget(self.pushButton_16, 1, 0, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_15.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout_11.addWidget(self.pushButton_15, 1, 1, 1, 1)
        self.listWidget_5 = QtGui.QListWidget(self.groupBox_2)
        self.listWidget_5.setMinimumSize(QtCore.QSize(211, 411))
        self.listWidget_5.setMaximumSize(QtCore.QSize(211, 16777215))
        self.listWidget_5.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.gridLayout_11.addWidget(self.listWidget_5, 0, 0, 1, 2)
        self.gridLayout_12.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab_10)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_14 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.graphicsView = QtGui.QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout_14.addWidget(self.graphicsView, 0, 0, 1, 5)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_14.addWidget(self.label_8, 1, 0, 1, 1)
        self.pushButton_17 = QtGui.QPushButton(self.groupBox)
        self.pushButton_17.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_17.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_17.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("img/rac.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.gridLayout_14.addWidget(self.pushButton_17, 1, 1, 1, 1)
        self.pushButton_18 = QtGui.QPushButton(self.groupBox)
        self.pushButton_18.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_18.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_18.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("img/flv.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon6)
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.gridLayout_14.addWidget(self.pushButton_18, 1, 2, 1, 1)
        self.pushButton_19 = QtGui.QPushButton(self.groupBox)
        self.pushButton_19.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_19.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_19.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("img/flh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_19.setIcon(icon7)
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.gridLayout_14.addWidget(self.pushButton_19, 1, 3, 1, 1)
        self.pushButton_20 = QtGui.QPushButton(self.groupBox)
        self.pushButton_20.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_20.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_20.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8("img/rcw.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon8)
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.gridLayout_14.addWidget(self.pushButton_20, 1, 4, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_7 = QtGui.QLabel(self.tab_10)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.tab_10)
        self.pushButton_14.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_14.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_14.setIcon(icon4)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.gridLayout_10.addWidget(self.pushButton_14, 0, 1, 2, 1)
        self.progressBar_2 = QtGui.QProgressBar(self.tab_10)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.gridLayout_10.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_10, _fromUtf8(""))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.gridLayout_19 = QtGui.QGridLayout(self.tab_11)
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.gridLayout_15 = QtGui.QGridLayout()
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.label_10 = QtGui.QLabel(self.tab_11)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_15.addWidget(self.label_10, 0, 0, 1, 1)
        self.pushButton_27 = QtGui.QPushButton(self.tab_11)
        self.pushButton_27.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_27.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_27.setIcon(icon4)
        self.pushButton_27.setObjectName(_fromUtf8("pushButton_27"))
        self.gridLayout_15.addWidget(self.pushButton_27, 0, 1, 2, 1)
        self.progressBar_3 = QtGui.QProgressBar(self.tab_11)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.gridLayout_15.addWidget(self.progressBar_3, 1, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_15, 1, 0, 1, 1)
        self.gridLayout_18 = QtGui.QGridLayout()
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_11)
        self.groupBox_3.setMinimumSize(QtCore.QSize(227, 481))
        self.groupBox_3.setMaximumSize(QtCore.QSize(227, 16777215))
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_16 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_11.setFrameShadow(QtGui.QFrame.Plain)
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_16.addWidget(self.label_11, 2, 0, 1, 2)
        self.pushButton_22 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_22.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_22.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_22.setIcon(icon1)
        self.pushButton_22.setObjectName(_fromUtf8("pushButton_22"))
        self.gridLayout_16.addWidget(self.pushButton_22, 1, 1, 1, 1)
        self.pushButton_21 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_21.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_21.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_21.setIcon(icon2)
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.gridLayout_16.addWidget(self.pushButton_21, 1, 0, 1, 1)
        self.listWidget_6 = QtGui.QListWidget(self.groupBox_3)
        self.listWidget_6.setMinimumSize(QtCore.QSize(211, 401))
        self.listWidget_6.setMaximumSize(QtCore.QSize(211, 16777215))
        self.listWidget_6.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_6.setObjectName(_fromUtf8("listWidget_6"))
        self.gridLayout_16.addWidget(self.listWidget_6, 0, 0, 1, 2)
        self.gridLayout_18.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_11)
        self.groupBox_4.setFlat(True)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_17 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.groupBox_4)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.gridLayout_17.addWidget(self.graphicsView_2, 0, 0, 1, 5)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_17.addWidget(self.label_9, 1, 0, 1, 1)
        self.pushButton_23 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_23.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_23.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_23.setText(_fromUtf8(""))
        self.pushButton_23.setIcon(icon5)
        self.pushButton_23.setObjectName(_fromUtf8("pushButton_23"))
        self.gridLayout_17.addWidget(self.pushButton_23, 1, 1, 1, 1)
        self.pushButton_24 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_24.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_24.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_24.setText(_fromUtf8(""))
        self.pushButton_24.setIcon(icon6)
        self.pushButton_24.setObjectName(_fromUtf8("pushButton_24"))
        self.gridLayout_17.addWidget(self.pushButton_24, 1, 2, 1, 1)
        self.pushButton_25 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_25.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_25.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_25.setText(_fromUtf8(""))
        self.pushButton_25.setIcon(icon7)
        self.pushButton_25.setObjectName(_fromUtf8("pushButton_25"))
        self.gridLayout_17.addWidget(self.pushButton_25, 1, 3, 1, 1)
        self.pushButton_26 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_26.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_26.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_26.setText(_fromUtf8(""))
        self.pushButton_26.setIcon(icon8)
        self.pushButton_26.setObjectName(_fromUtf8("pushButton_26"))
        self.gridLayout_17.addWidget(self.pushButton_26, 1, 4, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_11, _fromUtf8(""))
        self.gridLayout_9.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_25 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_20 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_20.addWidget(self.label_12, 1, 0, 1, 1)
        self.pushButton_30 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_30.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_30.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_30.setText(_fromUtf8(""))
        self.pushButton_30.setIcon(icon7)
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.gridLayout_20.addWidget(self.pushButton_30, 1, 3, 1, 1)
        self.graphicsView_3 = QtGui.QGraphicsView(self.groupBox_5)
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.gridLayout_20.addWidget(self.graphicsView_3, 0, 0, 1, 5)
        self.pushButton_29 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_29.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_29.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_29.setText(_fromUtf8(""))
        self.pushButton_29.setIcon(icon6)
        self.pushButton_29.setObjectName(_fromUtf8("pushButton_29"))
        self.gridLayout_20.addWidget(self.pushButton_29, 1, 2, 1, 1)
        self.pushButton_28 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_28.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_28.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_28.setText(_fromUtf8(""))
        self.pushButton_28.setIcon(icon5)
        self.pushButton_28.setObjectName(_fromUtf8("pushButton_28"))
        self.gridLayout_20.addWidget(self.pushButton_28, 1, 1, 1, 1)
        self.pushButton_31 = QtGui.QPushButton(self.groupBox_5)
        self.pushButton_31.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_31.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_31.setText(_fromUtf8(""))
        self.pushButton_31.setIcon(icon8)
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.gridLayout_20.addWidget(self.pushButton_31, 1, 4, 1, 1)
        self.gridLayout_25.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_22 = QtGui.QGridLayout()
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setMinimumSize(QtCore.QSize(222, 221))
        self.groupBox_6.setMaximumSize(QtCore.QSize(227, 16777215))
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_21 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.pushButton_32 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_32.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_32.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_32.setIcon(icon2)
        self.pushButton_32.setObjectName(_fromUtf8("pushButton_32"))
        self.gridLayout_21.addWidget(self.pushButton_32, 1, 0, 1, 1)
        self.pushButton_33 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_33.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_33.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_33.setIcon(icon1)
        self.pushButton_33.setObjectName(_fromUtf8("pushButton_33"))
        self.gridLayout_21.addWidget(self.pushButton_33, 1, 1, 1, 1)
        self.listWidget_7 = QtGui.QListWidget(self.groupBox_6)
        self.listWidget_7.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_7.setObjectName(_fromUtf8("listWidget_7"))
        self.gridLayout_21.addWidget(self.listWidget_7, 0, 0, 1, 2)
        self.gridLayout_22.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_7.setMinimumSize(QtCore.QSize(219, 261))
        self.groupBox_7.setMaximumSize(QtCore.QSize(227, 16777215))
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_23 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_7)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout_23.addWidget(self.checkBox_4, 0, 0, 1, 1)
        self.listWidget_8 = QtGui.QListWidget(self.groupBox_7)
        self.listWidget_8.setEnabled(False)
        self.listWidget_8.setMinimumSize(QtCore.QSize(211, 175))
        self.listWidget_8.setMaximumSize(QtCore.QSize(211, 16777215))
        self.listWidget_8.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_8.setObjectName(_fromUtf8("listWidget_8"))
        self.gridLayout_23.addWidget(self.listWidget_8, 1, 0, 1, 2)
        self.pushButton_45 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_45.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_45.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_45.setIcon(icon2)
        self.pushButton_45.setObjectName(_fromUtf8("pushButton_45"))
        self.gridLayout_23.addWidget(self.pushButton_45, 2, 1, 1, 1)
        self.gridLayout_22.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_22, 0, 1, 1, 1)
        self.gridLayout_24 = QtGui.QGridLayout()
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_24.addWidget(self.label_14, 0, 0, 1, 1)
        self.pushButton_35 = QtGui.QPushButton(self.tab_3)
        self.pushButton_35.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_35.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_35.setIcon(icon4)
        self.pushButton_35.setObjectName(_fromUtf8("pushButton_35"))
        self.gridLayout_24.addWidget(self.pushButton_35, 0, 1, 2, 1)
        self.progressBar_5 = QtGui.QProgressBar(self.tab_3)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName(_fromUtf8("progressBar_5"))
        self.gridLayout_24.addWidget(self.progressBar_5, 1, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_24, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_24 = QtGui.QWidget()
        self.tab_24.setObjectName(_fromUtf8("tab_24"))
        self.gridLayout_70 = QtGui.QGridLayout(self.tab_24)
        self.gridLayout_70.setObjectName(_fromUtf8("gridLayout_70"))
        self.groupBox_16 = QtGui.QGroupBox(self.tab_24)
        self.groupBox_16.setObjectName(_fromUtf8("groupBox_16"))
        self.gridLayout_70.addWidget(self.groupBox_16, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(507, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_70.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_42 = QtGui.QPushButton(self.tab_24)
        self.pushButton_42.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_42.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_42.setIcon(icon3)
        self.pushButton_42.setObjectName(_fromUtf8("pushButton_42"))
        self.gridLayout_70.addWidget(self.pushButton_42, 1, 1, 1, 1)
        self.pushButton_44 = QtGui.QPushButton(self.tab_24)
        self.pushButton_44.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_44.setMaximumSize(QtCore.QSize(100, 25))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8("img/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_44.setIcon(icon9)
        self.pushButton_44.setObjectName(_fromUtf8("pushButton_44"))
        self.gridLayout_70.addWidget(self.pushButton_44, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_24, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_26 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.tabWidget_4 = QtGui.QTabWidget(self.tab_4)
        self.tabWidget_4.setObjectName(_fromUtf8("tabWidget_4"))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        self.gridLayout_72 = QtGui.QGridLayout(self.tab_12)
        self.gridLayout_72.setObjectName(_fromUtf8("gridLayout_72"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_12)
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_28 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.listWidget_11 = QtGui.QListWidget(self.groupBox_8)
        self.listWidget_11.setObjectName(_fromUtf8("listWidget_11"))
        self.gridLayout_28.addWidget(self.listWidget_11, 0, 0, 1, 1)
        self.gridLayout_72.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.tab_12)
        self.groupBox_9.setMinimumSize(QtCore.QSize(227, 481))
        self.groupBox_9.setMaximumSize(QtCore.QSize(227, 16777215))
        self.groupBox_9.setFlat(True)
        self.groupBox_9.setCheckable(False)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_27 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.pushButton_36 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_36.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_36.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_36.setIcon(icon1)
        self.pushButton_36.setObjectName(_fromUtf8("pushButton_36"))
        self.gridLayout_27.addWidget(self.pushButton_36, 1, 1, 1, 1)
        self.pushButton_37 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_37.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_37.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_37.setIcon(icon2)
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.gridLayout_27.addWidget(self.pushButton_37, 1, 0, 1, 1)
        self.listWidget_9 = QtGui.QListWidget(self.groupBox_9)
        self.listWidget_9.setMinimumSize(QtCore.QSize(211, 401))
        self.listWidget_9.setMaximumSize(QtCore.QSize(211, 16777215))
        self.listWidget_9.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_9.setObjectName(_fromUtf8("listWidget_9"))
        self.gridLayout_27.addWidget(self.listWidget_9, 0, 0, 1, 2)
        self.gridLayout_72.addWidget(self.groupBox_9, 0, 1, 2, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.tab_12)
        self.groupBox_10.setFlat(True)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_30 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        self.gridLayout_29 = QtGui.QGridLayout()
        self.gridLayout_29.setObjectName(_fromUtf8("gridLayout_29"))
        self.label_15 = QtGui.QLabel(self.groupBox_10)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_29.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit.setMaxLength(8)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_29.addWidget(self.lineEdit, 0, 1, 2, 1)
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_10)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.gridLayout_29.addWidget(self.checkBox_5, 0, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox_10)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_29.addWidget(self.comboBox, 1, 2, 2, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_10)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_29.addWidget(self.label_16, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_29.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.gridLayout_30.addLayout(self.gridLayout_29, 0, 0, 1, 3)
        self.label_17 = QtGui.QLabel(self.groupBox_10)
        self.label_17.setText(_fromUtf8(""))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_30.addWidget(self.label_17, 1, 0, 1, 1)
        self.pushButton_38 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_38.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_38.setMaximumSize(QtCore.QSize(100, 25))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/img/rem.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_38.setIcon(icon10)
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.gridLayout_30.addWidget(self.pushButton_38, 1, 1, 1, 1)
        self.pushButton_39 = QtGui.QPushButton(self.groupBox_10)
        self.pushButton_39.setMinimumSize(QtCore.QSize(130, 25))
        self.pushButton_39.setMaximumSize(QtCore.QSize(130, 25))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8("../../.designer/backup/img/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_39.setIcon(icon11)
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.gridLayout_30.addWidget(self.pushButton_39, 1, 2, 1, 1)
        self.gridLayout_72.addWidget(self.groupBox_10, 1, 0, 1, 1)
        self.gridLayout_35 = QtGui.QGridLayout()
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.progressBar_4 = QtGui.QProgressBar(self.tab_12)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar_4.setObjectName(_fromUtf8("progressBar_4"))
        self.gridLayout_35.addWidget(self.progressBar_4, 1, 0, 1, 1)
        self.label_41 = QtGui.QLabel(self.tab_12)
        self.label_41.setText(_fromUtf8(""))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_35.addWidget(self.label_41, 0, 0, 1, 1)
        self.gridLayout_72.addLayout(self.gridLayout_35, 2, 0, 1, 2)
        self.tabWidget_4.addTab(self.tab_12, _fromUtf8(""))
        self.tab_14 = QtGui.QWidget()
        self.tab_14.setObjectName(_fromUtf8("tab_14"))
        self.gridLayout_33 = QtGui.QGridLayout(self.tab_14)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_32 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_32.setObjectName(_fromUtf8("gridLayout_32"))
        self.pushButton_41 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_41.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_41.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_41.setIcon(icon10)
        self.pushButton_41.setObjectName(_fromUtf8("pushButton_41"))
        self.gridLayout_32.addWidget(self.pushButton_41, 1, 1, 1, 1)
        self.pushButton_40 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_40.setMinimumSize(QtCore.QSize(130, 25))
        self.pushButton_40.setMaximumSize(QtCore.QSize(130, 25))
        self.pushButton_40.setIcon(icon11)
        self.pushButton_40.setObjectName(_fromUtf8("pushButton_40"))
        self.gridLayout_32.addWidget(self.pushButton_40, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_32.addItem(spacerItem1, 1, 0, 1, 1)
        self.listWidget_12 = QtGui.QListWidget(self.groupBox_12)
        self.listWidget_12.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listWidget_12.setObjectName(_fromUtf8("listWidget_12"))
        self.gridLayout_32.addWidget(self.listWidget_12, 0, 0, 1, 3)
        self.gridLayout_33.addWidget(self.groupBox_12, 0, 0, 1, 1)
        self.groupBox_11 = QtGui.QGroupBox(self.tab_14)
        self.groupBox_11.setMaximumSize(QtCore.QSize(227, 16777215))
        self.groupBox_11.setFlat(True)
        self.groupBox_11.setCheckable(False)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_31 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.gridLayout_34 = QtGui.QGridLayout()
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.label_21 = QtGui.QLabel(self.groupBox_11)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_34.addWidget(self.label_21, 2, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_34.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_34.addWidget(self.lineEdit_6, 7, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_34.addWidget(self.lineEdit_7, 9, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_11)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_34.addWidget(self.label_23, 4, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_11)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_34.addWidget(self.plainTextEdit, 13, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_11)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_34.addWidget(self.label_22, 6, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_34.addWidget(self.lineEdit_5, 5, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_11)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_34.addWidget(self.label_25, 8, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_11)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_34.addWidget(self.label_24, 12, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_8.setText(_fromUtf8(""))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_34.addWidget(self.lineEdit_8, 11, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_11)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_34.addWidget(self.label_26, 10, 0, 1, 1)
        self.label_20 = QtGui.QLabel(self.groupBox_11)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_34.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_11)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_34.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.gridLayout_31.addLayout(self.gridLayout_34, 0, 0, 1, 1)
        self.gridLayout_33.addWidget(self.groupBox_11, 0, 1, 1, 1)
        self.tabWidget_4.addTab(self.tab_14, _fromUtf8(""))
        self.gridLayout_26.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_20 = QtGui.QWidget()
        self.tab_20.setObjectName(_fromUtf8("tab_20"))
        self.gridLayout_36 = QtGui.QGridLayout(self.tab_20)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.tabWidget_6 = QtGui.QTabWidget(self.tab_20)
        self.tabWidget_6.setObjectName(_fromUtf8("tabWidget_6"))
        self.tab_21 = QtGui.QWidget()
        self.tab_21.setObjectName(_fromUtf8("tab_21"))
        self.gridLayout_37 = QtGui.QGridLayout(self.tab_21)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.toolBox_2 = QtGui.QToolBox(self.tab_21)
        self.toolBox_2.setObjectName(_fromUtf8("toolBox_2"))
        self.page_6 = QtGui.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 706, 406))
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.gridLayout_38 = QtGui.QGridLayout(self.page_6)
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.scrollArea_6 = QtGui.QScrollArea(self.page_6)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName(_fromUtf8("scrollArea_6"))
        self.scrollAreaWidgetContents_6 = QtGui.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 690, 390))
        self.scrollAreaWidgetContents_6.setObjectName(_fromUtf8("scrollAreaWidgetContents_6"))
        self.gridLayout_55 = QtGui.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_55.setObjectName(_fromUtf8("gridLayout_55"))
        self.gridLayout_54 = QtGui.QGridLayout()
        self.gridLayout_54.setObjectName(_fromUtf8("gridLayout_54"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents_6)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_54.addWidget(self.label_13, 0, 0, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_54.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents_6)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_54.addWidget(self.label_18, 1, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.gridLayout_54.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.scrollAreaWidgetContents_6)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_54.addWidget(self.label_19, 2, 0, 1, 1)
        self.lineEdit_9 = QtGui.QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.gridLayout_54.addWidget(self.lineEdit_9, 2, 1, 1, 1)
        self.gridLayout_55.addLayout(self.gridLayout_54, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_55.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 251, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_55.addItem(spacerItem3, 1, 0, 1, 1)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_38.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_6, _fromUtf8(""))
        self.page_7 = QtGui.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 96, 95))
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.gridLayout_50 = QtGui.QGridLayout(self.page_7)
        self.gridLayout_50.setObjectName(_fromUtf8("gridLayout_50"))
        self.scrollArea_7 = QtGui.QScrollArea(self.page_7)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName(_fromUtf8("scrollArea_7"))
        self.scrollAreaWidgetContents_7 = QtGui.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 191, 136))
        self.scrollAreaWidgetContents_7.setObjectName(_fromUtf8("scrollAreaWidgetContents_7"))
        self.gridLayout_61 = QtGui.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_61.setObjectName(_fromUtf8("gridLayout_61"))
        self.gridLayout_56 = QtGui.QGridLayout()
        self.gridLayout_56.setObjectName(_fromUtf8("gridLayout_56"))
        self.label_29 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_56.addWidget(self.label_29, 0, 0, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.gridLayout_56.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.label_30 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_56.addWidget(self.label_30, 1, 0, 1, 1)
        self.comboBox_5 = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout_56.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.label_35 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.gridLayout_56.addWidget(self.label_35, 2, 0, 1, 1)
        self.comboBox_8 = QtGui.QComboBox(self.scrollAreaWidgetContents_7)
        self.comboBox_8.setObjectName(_fromUtf8("comboBox_8"))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.comboBox_8.addItem(_fromUtf8(""))
        self.gridLayout_56.addWidget(self.comboBox_8, 2, 1, 1, 1)
        self.label_28 = QtGui.QLabel(self.scrollAreaWidgetContents_7)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_56.addWidget(self.label_28, 3, 0, 1, 1)
        self.lineEdit_10 = QtGui.QLineEdit(self.scrollAreaWidgetContents_7)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.gridLayout_56.addWidget(self.lineEdit_10, 3, 1, 1, 1)
        self.gridLayout_61.addLayout(self.gridLayout_56, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_61.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 220, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_61.addItem(spacerItem5, 1, 0, 1, 1)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_50.addWidget(self.scrollArea_7, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_7, _fromUtf8(""))
        self.page_8 = QtGui.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 96, 95))
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.gridLayout_51 = QtGui.QGridLayout(self.page_8)
        self.gridLayout_51.setObjectName(_fromUtf8("gridLayout_51"))
        self.scrollArea_8 = QtGui.QScrollArea(self.page_8)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName(_fromUtf8("scrollArea_8"))
        self.scrollAreaWidgetContents_8 = QtGui.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 185, 136))
        self.scrollAreaWidgetContents_8.setObjectName(_fromUtf8("scrollAreaWidgetContents_8"))
        self.gridLayout_62 = QtGui.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_62.setObjectName(_fromUtf8("gridLayout_62"))
        self.gridLayout_57 = QtGui.QGridLayout()
        self.gridLayout_57.setObjectName(_fromUtf8("gridLayout_57"))
        self.label_32 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_57.addWidget(self.label_32, 0, 0, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.gridLayout_57.addWidget(self.comboBox_6, 0, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.gridLayout_57.addWidget(self.label_33, 1, 0, 1, 1)
        self.comboBox_7 = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.comboBox_7.setObjectName(_fromUtf8("comboBox_7"))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.comboBox_7.addItem(_fromUtf8(""))
        self.gridLayout_57.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.label_36 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_57.addWidget(self.label_36, 2, 0, 1, 1)
        self.comboBox_9 = QtGui.QComboBox(self.scrollAreaWidgetContents_8)
        self.comboBox_9.setObjectName(_fromUtf8("comboBox_9"))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.comboBox_9.addItem(_fromUtf8(""))
        self.gridLayout_57.addWidget(self.comboBox_9, 2, 1, 1, 1)
        self.label_31 = QtGui.QLabel(self.scrollAreaWidgetContents_8)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_57.addWidget(self.label_31, 3, 0, 1, 1)
        self.lineEdit_11 = QtGui.QLineEdit(self.scrollAreaWidgetContents_8)
        self.lineEdit_11.setText(_fromUtf8(""))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.gridLayout_57.addWidget(self.lineEdit_11, 3, 1, 1, 1)
        self.gridLayout_62.addLayout(self.gridLayout_57, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_62.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 220, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_62.addItem(spacerItem7, 1, 0, 1, 1)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_51.addWidget(self.scrollArea_8, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_8, _fromUtf8(""))
        self.page_9 = QtGui.QWidget()
        self.page_9.setGeometry(QtCore.QRect(0, 0, 96, 95))
        self.page_9.setObjectName(_fromUtf8("page_9"))
        self.gridLayout_52 = QtGui.QGridLayout(self.page_9)
        self.gridLayout_52.setObjectName(_fromUtf8("gridLayout_52"))
        self.scrollArea_9 = QtGui.QScrollArea(self.page_9)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName(_fromUtf8("scrollArea_9"))
        self.scrollAreaWidgetContents_9 = QtGui.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_9.setObjectName(_fromUtf8("scrollAreaWidgetContents_9"))
        self.label_34 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_34.setGeometry(QtCore.QRect(20, 50, 61, 23))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lineEdit_12 = QtGui.QLineEdit(self.scrollAreaWidgetContents_9)
        self.lineEdit_12.setGeometry(QtCore.QRect(87, 50, 264, 23))
        self.lineEdit_12.setText(_fromUtf8(""))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.comboBox_10 = QtGui.QComboBox(self.scrollAreaWidgetContents_9)
        self.comboBox_10.setGeometry(QtCore.QRect(87, 20, 262, 25))
        self.comboBox_10.setObjectName(_fromUtf8("comboBox_10"))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.comboBox_10.addItem(_fromUtf8(""))
        self.label_37 = QtGui.QLabel(self.scrollAreaWidgetContents_9)
        self.label_37.setGeometry(QtCore.QRect(20, 20, 61, 25))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_52.addWidget(self.scrollArea_9, 0, 0, 1, 1)
        self.toolBox_2.addItem(self.page_9, _fromUtf8(""))
        self.gridLayout_37.addWidget(self.toolBox_2, 0, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_21, _fromUtf8(""))
        self.tab_23 = QtGui.QWidget()
        self.tab_23.setObjectName(_fromUtf8("tab_23"))
        self.gridLayout_63 = QtGui.QGridLayout(self.tab_23)
        self.gridLayout_63.setObjectName(_fromUtf8("gridLayout_63"))
        self.scrollArea_10 = QtGui.QScrollArea(self.tab_23)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName(_fromUtf8("scrollArea_10"))
        self.scrollAreaWidgetContents_10 = QtGui.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 328, 124))
        self.scrollAreaWidgetContents_10.setObjectName(_fromUtf8("scrollAreaWidgetContents_10"))
        self.gridLayout_60 = QtGui.QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_60.setObjectName(_fromUtf8("gridLayout_60"))
        self.gridLayout_58 = QtGui.QGridLayout()
        self.gridLayout_58.setObjectName(_fromUtf8("gridLayout_58"))
        self.radioButton = QtGui.QRadioButton(self.scrollAreaWidgetContents_10)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout_58.addWidget(self.radioButton, 0, 0, 1, 1)
        self.scrollArea_11 = QtGui.QScrollArea(self.scrollAreaWidgetContents_10)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName(_fromUtf8("scrollArea_11"))
        self.scrollAreaWidgetContents_11 = QtGui.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 213, 393))
        self.scrollAreaWidgetContents_11.setObjectName(_fromUtf8("scrollAreaWidgetContents_11"))
        self.gridLayout_71 = QtGui.QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_71.setObjectName(_fromUtf8("gridLayout_71"))
        self.groupBox_13 = QtGui.QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.gridLayout_53 = QtGui.QGridLayout(self.groupBox_13)
        self.gridLayout_53.setObjectName(_fromUtf8("gridLayout_53"))
        self.label_38 = QtGui.QLabel(self.groupBox_13)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_53.addWidget(self.label_38, 0, 0, 1, 1)
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.gridLayout_53.addWidget(self.lineEdit_13, 0, 1, 1, 1)
        self.label_39 = QtGui.QLabel(self.groupBox_13)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_53.addWidget(self.label_39, 1, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_13)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_53.addWidget(self.lineEdit_14, 1, 1, 1, 1)
        self.gridLayout_71.addWidget(self.groupBox_13, 0, 0, 1, 1)
        self.groupBox_14 = QtGui.QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.gridLayout_68 = QtGui.QGridLayout(self.groupBox_14)
        self.gridLayout_68.setObjectName(_fromUtf8("gridLayout_68"))
        self.gridLayout_64 = QtGui.QGridLayout()
        self.gridLayout_64.setObjectName(_fromUtf8("gridLayout_64"))
        self.label_40 = QtGui.QLabel(self.groupBox_14)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_64.addWidget(self.label_40, 0, 0, 1, 1)
        self.dial = QtGui.QDial(self.groupBox_14)
        self.dial.setMinimum(5)
        self.dial.setMaximum(120)
        self.dial.setPageStep(1)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(False)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.gridLayout_64.addWidget(self.dial, 1, 0, 1, 1)
        self.gridLayout_68.addLayout(self.gridLayout_64, 0, 0, 1, 1)
        self.gridLayout_65 = QtGui.QGridLayout()
        self.gridLayout_65.setObjectName(_fromUtf8("gridLayout_65"))
        self.dial_2 = QtGui.QDial(self.groupBox_14)
        self.dial_2.setMinimum(5)
        self.dial_2.setMaximum(120)
        self.dial_2.setPageStep(1)
        self.dial_2.setProperty("value", 25)
        self.dial_2.setWrapping(False)
        self.dial_2.setNotchesVisible(False)
        self.dial_2.setObjectName(_fromUtf8("dial_2"))
        self.gridLayout_65.addWidget(self.dial_2, 1, 0, 1, 1)
        self.label_42 = QtGui.QLabel(self.groupBox_14)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_65.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_68.addLayout(self.gridLayout_65, 0, 1, 1, 1)
        self.gridLayout_66 = QtGui.QGridLayout()
        self.gridLayout_66.setObjectName(_fromUtf8("gridLayout_66"))
        self.label_46 = QtGui.QLabel(self.groupBox_14)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.gridLayout_66.addWidget(self.label_46, 0, 0, 1, 1)
        self.dial_3 = QtGui.QDial(self.groupBox_14)
        self.dial_3.setMinimum(5)
        self.dial_3.setMaximum(120)
        self.dial_3.setPageStep(1)
        self.dial_3.setProperty("value", 10)
        self.dial_3.setWrapping(False)
        self.dial_3.setNotchesVisible(False)
        self.dial_3.setObjectName(_fromUtf8("dial_3"))
        self.gridLayout_66.addWidget(self.dial_3, 1, 0, 1, 1)
        self.gridLayout_68.addLayout(self.gridLayout_66, 0, 2, 1, 1)
        self.gridLayout_71.addWidget(self.groupBox_14, 1, 0, 1, 1)
        self.groupBox_15 = QtGui.QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.gridLayout_67 = QtGui.QGridLayout(self.groupBox_15)
        self.gridLayout_67.setObjectName(_fromUtf8("gridLayout_67"))
        self.label_44 = QtGui.QLabel(self.groupBox_15)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_67.addWidget(self.label_44, 0, 0, 1, 1)
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_15)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_67.addWidget(self.lineEdit_15, 0, 1, 1, 1)
        self.label_45 = QtGui.QLabel(self.groupBox_15)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_67.addWidget(self.label_45, 1, 0, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_15)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.gridLayout_67.addWidget(self.lineEdit_16, 1, 1, 1, 1)
        self.gridLayout_71.addWidget(self.groupBox_15, 2, 0, 1, 1)
        self.groupBox_17 = QtGui.QGroupBox(self.scrollAreaWidgetContents_11)
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.gridLayout_69 = QtGui.QGridLayout(self.groupBox_17)
        self.gridLayout_69.setObjectName(_fromUtf8("gridLayout_69"))
        self.label_47 = QtGui.QLabel(self.groupBox_17)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.gridLayout_69.addWidget(self.label_47, 0, 0, 1, 1)
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox_17)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.gridLayout_69.addWidget(self.lineEdit_18, 0, 1, 1, 1)
        self.label_48 = QtGui.QLabel(self.groupBox_17)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.gridLayout_69.addWidget(self.label_48, 1, 0, 1, 1)
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_17)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.gridLayout_69.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.gridLayout_71.addWidget(self.groupBox_17, 3, 0, 1, 1)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.gridLayout_58.addWidget(self.scrollArea_11, 1, 0, 1, 1)
        self.gridLayout_60.addLayout(self.gridLayout_58, 0, 0, 1, 1)
        self.gridLayout_59 = QtGui.QGridLayout()
        self.gridLayout_59.setObjectName(_fromUtf8("gridLayout_59"))
        self.radioButton_2 = QtGui.QRadioButton(self.scrollAreaWidgetContents_10)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout_59.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.scrollArea_12 = QtGui.QScrollArea(self.scrollAreaWidgetContents_10)
        self.scrollArea_12.setEnabled(False)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollArea_12.setObjectName(_fromUtf8("scrollArea_12"))
        self.scrollAreaWidgetContents_12 = QtGui.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_12.setObjectName(_fromUtf8("scrollAreaWidgetContents_12"))
        self.pushButton_43 = QtGui.QPushButton(self.scrollAreaWidgetContents_12)
        self.pushButton_43.setGeometry(QtCore.QRect(100, 150, 99, 25))
        self.pushButton_43.setObjectName(_fromUtf8("pushButton_43"))
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)
        self.gridLayout_59.addWidget(self.scrollArea_12, 1, 0, 1, 1)
        self.gridLayout_60.addLayout(self.gridLayout_59, 0, 1, 1, 1)
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.gridLayout_63.addWidget(self.scrollArea_10, 0, 0, 1, 1)
        self.tabWidget_6.addTab(self.tab_23, _fromUtf8(""))
        self.gridLayout_36.addWidget(self.tabWidget_6, 0, 0, 1, 2)
        self.label_27 = QtGui.QLabel(self.tab_20)
        self.label_27.setText(_fromUtf8(""))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_36.addWidget(self.label_27, 1, 0, 1, 1)
        self.pushButton_34 = QtGui.QPushButton(self.tab_20)
        self.pushButton_34.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_34.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_34.setIcon(icon3)
        self.pushButton_34.setObjectName(_fromUtf8("pushButton_34"))
        self.gridLayout_36.addWidget(self.pushButton_34, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_20, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_39 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        self.tabWidget_5 = QtGui.QTabWidget(self.tab_5)
        self.tabWidget_5.setObjectName(_fromUtf8("tabWidget_5"))
        self.tab_15 = QtGui.QWidget()
        self.tab_15.setObjectName(_fromUtf8("tab_15"))
        self.gridLayout_40 = QtGui.QGridLayout(self.tab_15)
        self.gridLayout_40.setObjectName(_fromUtf8("gridLayout_40"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_15)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_40.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_15, _fromUtf8(""))
        self.tab_17 = QtGui.QWidget()
        self.tab_17.setObjectName(_fromUtf8("tab_17"))
        self.gridLayout_41 = QtGui.QGridLayout(self.tab_17)
        self.gridLayout_41.setObjectName(_fromUtf8("gridLayout_41"))
        self.toolBox = QtGui.QToolBox(self.tab_17)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 706, 406))
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_49 = QtGui.QGridLayout(self.page)
        self.gridLayout_49.setObjectName(_fromUtf8("gridLayout_49"))
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 706, 406))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_48 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_48.setObjectName(_fromUtf8("gridLayout_48"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 96, 95))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_47 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_47.setObjectName(_fromUtf8("gridLayout_47"))
        self.scrollArea_3 = QtGui.QScrollArea(self.page_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.scrollAreaWidgetContents_3.setObjectName(_fromUtf8("scrollAreaWidgetContents_3"))
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_47.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 706, 406))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.gridLayout_46 = QtGui.QGridLayout(self.page_4)
        self.gridLayout_46.setObjectName(_fromUtf8("gridLayout_46"))
        self.toolBox.addItem(self.page_4, _fromUtf8(""))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 706, 406))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.gridLayout_45 = QtGui.QGridLayout(self.page_5)
        self.gridLayout_45.setObjectName(_fromUtf8("gridLayout_45"))
        self.toolBox.addItem(self.page_5, _fromUtf8(""))
        self.gridLayout_41.addWidget(self.toolBox, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_17, _fromUtf8(""))
        self.tab_16 = QtGui.QWidget()
        self.tab_16.setObjectName(_fromUtf8("tab_16"))
        self.gridLayout_42 = QtGui.QGridLayout(self.tab_16)
        self.gridLayout_42.setObjectName(_fromUtf8("gridLayout_42"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab_16)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_42.addWidget(self.textBrowser_3, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_16, _fromUtf8(""))
        self.tab_18 = QtGui.QWidget()
        self.tab_18.setObjectName(_fromUtf8("tab_18"))
        self.gridLayout_43 = QtGui.QGridLayout(self.tab_18)
        self.gridLayout_43.setObjectName(_fromUtf8("gridLayout_43"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_18)
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.gridLayout_43.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_18, _fromUtf8(""))
        self.tab_19 = QtGui.QWidget()
        self.tab_19.setObjectName(_fromUtf8("tab_19"))
        self.gridLayout_44 = QtGui.QGridLayout(self.tab_19)
        self.gridLayout_44.setObjectName(_fromUtf8("gridLayout_44"))
        self.listWidget_10 = QtGui.QListWidget(self.tab_19)
        self.listWidget_10.setObjectName(_fromUtf8("listWidget_10"))
        self.gridLayout_44.addWidget(self.listWidget_10, 0, 0, 1, 1)
        self.tabWidget_5.addTab(self.tab_19, _fromUtf8(""))
        self.gridLayout_39.addWidget(self.tabWidget_5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "MYRaf V2.0", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Form", "Bias", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Form", "Dark", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QtGui.QApplication.translate("Form", "Images", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QtGui.QApplication.translate("Form", "Bias", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QtGui.QApplication.translate("Form", "Dark", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_16.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Display:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), QtGui.QApplication.translate("Form", "Auto Align", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_27.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_22.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_21.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Display:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QtGui.QApplication.translate("Form", "Manual Align", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Display:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_32.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_33.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("Form", "Photometry Method:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setText(QtGui.QApplication.translate("Form", "All Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_45.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_35.setText(QtGui.QApplication.translate("Form", ":go", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "Photometry", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_16.setTitle(QtGui.QApplication.translate("Form", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_42.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_44.setText(QtGui.QApplication.translate("Form", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_24), QtGui.QApplication.translate("Form", "Graph", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("Form", "Header:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("Form", "Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_36.setText(QtGui.QApplication.translate("Form", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_37.setText(QtGui.QApplication.translate("Form", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setTitle(QtGui.QApplication.translate("Form", "Operations:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "Field:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setText(QtGui.QApplication.translate("Form", "Use value from an existing field", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Form", "Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_38.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_39.setText(QtGui.QApplication.translate("Form", "Insert/Update", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), QtGui.QApplication.translate("Form", "Header Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_12.setTitle(QtGui.QApplication.translate("Form", "Observatories List:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_41.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_40.setText(QtGui.QApplication.translate("Form", "Insert/Update", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setTitle(QtGui.QApplication.translate("Form", "Observatory:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Form", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Form", "Longitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Form", "Latitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Form", "Altitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Form", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("Form", "Time Zone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Form", "Observatory", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_14), QtGui.QApplication.translate("Form", "Observatory Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Combine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Form", "average", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Form", "Reject", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("Form", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("Form", "minmax", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("Form", "ccdclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(3, QtGui.QApplication.translate("Form", "crreject", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(4, QtGui.QApplication.translate("Form", "sigclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(5, QtGui.QApplication.translate("Form", "avsigclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(6, QtGui.QApplication.translate("Form", "pclip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "ccdtype", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_6), QtGui.QApplication.translate("Form", "Zero Combine Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Form", "Combine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(1, QtGui.QApplication.translate("Form", "average", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("Form", "Reject", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(0, QtGui.QApplication.translate("Form", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(1, QtGui.QApplication.translate("Form", "minmax", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(2, QtGui.QApplication.translate("Form", "ccdclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(3, QtGui.QApplication.translate("Form", "crreject", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(4, QtGui.QApplication.translate("Form", "sigclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(5, QtGui.QApplication.translate("Form", "avsigclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_5.setItemText(6, QtGui.QApplication.translate("Form", "pclip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("Form", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(0, QtGui.QApplication.translate("Form", "exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(1, QtGui.QApplication.translate("Form", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(2, QtGui.QApplication.translate("Form", "mode", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(3, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_8.setItemText(4, QtGui.QApplication.translate("Form", "mean", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Form", "ccdtype", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_7), QtGui.QApplication.translate("Form", "Dark Combine Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("Form", "Combine", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(0, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_6.setItemText(1, QtGui.QApplication.translate("Form", "average", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("Form", "Reject", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(0, QtGui.QApplication.translate("Form", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(1, QtGui.QApplication.translate("Form", "minmax", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(2, QtGui.QApplication.translate("Form", "ccdclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(3, QtGui.QApplication.translate("Form", "crreject", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(4, QtGui.QApplication.translate("Form", "sigclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(5, QtGui.QApplication.translate("Form", "avsigclip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_7.setItemText(6, QtGui.QApplication.translate("Form", "pclip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("Form", "Subset", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(0, QtGui.QApplication.translate("Form", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_9.setItemText(1, QtGui.QApplication.translate("Form", "no", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("Form", "ccdtype", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_8), QtGui.QApplication.translate("Form", "Flat Combine Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("Form", "ccdtype", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(0, QtGui.QApplication.translate("Form", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_10.setItemText(1, QtGui.QApplication.translate("Form", "no", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("Form", "Subset", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_9), QtGui.QApplication.translate("Form", "Calibration Setting", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_21), QtGui.QApplication.translate("Form", "Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("Form", "iraf Photometry", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_13.setTitle(QtGui.QApplication.translate("Form", "DataPars", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("Form", "Exposur", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_13.setText(QtGui.QApplication.translate("Form", "exptime", None, QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(QtGui.QApplication.translate("Form", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_14.setText(QtGui.QApplication.translate("Form", "subset", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_14.setTitle(QtGui.QApplication.translate("Form", "FitSkyPars", None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(QtGui.QApplication.translate("Form", "Annulus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Form", "Dannulus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("Form", "CBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_15.setTitle(QtGui.QApplication.translate("Form", "PhotPars", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("Form", "Apertur", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_15.setText(QtGui.QApplication.translate("Form", "10,15,20,25,30", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("Form", "ZMag", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_16.setText(QtGui.QApplication.translate("Form", "25", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_17.setTitle(QtGui.QApplication.translate("Form", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47.setText(QtGui.QApplication.translate("Form", "Observatory", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_18.setText(QtGui.QApplication.translate("Form", "observat", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48.setText(QtGui.QApplication.translate("Form", "ObsTime", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_17.setText(QtGui.QApplication.translate("Form", "time-obs", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("Form", "Ensemble Photometry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_43.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_23), QtGui.QApplication.translate("Form", "Photometry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_34.setText(QtGui.QApplication.translate("Form", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_20), QtGui.QApplication.translate("Form", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
"<p align=\"justify\" style=\" margin-top:5px; margin-bottom:5px; margin-left:5px; margin-right:5px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">        </span><span style=\" font-weight:600; font-style:italic;\">http://myrafproject.org/blog/</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_15), QtGui.QApplication.translate("Form", "MYRaf", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Form", "Starting With MYRaf", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Form", "Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("Form", "Align", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("Form", "Photometry", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QtGui.QApplication.translate("Form", "Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_17), QtGui.QApplication.translate("Form", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_3.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">&lt;http://www.gnu.org/philosophy/why-not-lgpl.html&gt;.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_16), QtGui.QApplication.translate("Form", "License", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Created by:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Yücel KILIÇ: </span><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">yucelkilic@myrafproject.org</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic;\">Muhammed SHEMUNI: </span><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">m.shemuni@myrafproject.org</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), QtGui.QApplication.translate("Form", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_19), QtGui.QApplication.translate("Form", "Log Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("Form", "Help", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

