# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uis/editor.ui'
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

class Ui_MainWindowEdit(object):
    def setupUi(self, MainWindowEdit):
        MainWindowEdit.setObjectName(_fromUtf8("MainWindowEdit"))
        MainWindowEdit.resize(650, 623)
        MainWindowEdit.setMinimumSize(QtCore.QSize(650, 600))
        self.centralwidget = QtGui.QWidget(MainWindowEdit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_16 = QtGui.QGridLayout(self.tab)
        self.gridLayout_16.setObjectName(_fromUtf8("gridLayout_16"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab)
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_28 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.listWidget_11 = QtGui.QListWidget(self.groupBox_8)
        self.listWidget_11.setObjectName(_fromUtf8("listWidget_11"))
        self.gridLayout_28.addWidget(self.listWidget_11, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_8, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 110))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 110))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_4.addWidget(self.checkBox, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setEnabled(False)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_4.addWidget(self.comboBox, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_9.setFlat(True)
        self.groupBox_9.setCheckable(False)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.listWidget_9 = QtGui.QListWidget(self.groupBox_9)
        self.listWidget_9.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_9.setObjectName(_fromUtf8("listWidget_9"))
        self.gridLayout_2.addWidget(self.listWidget_9, 0, 0, 1, 2)
        self.pushButton_37 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_37.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_37.setMaximumSize(QtCore.QSize(70, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/.designer/.designer/backup/img/rem.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_37.setIcon(icon)
        self.pushButton_37.setObjectName(_fromUtf8("pushButton_37"))
        self.gridLayout_2.addWidget(self.pushButton_37, 1, 0, 1, 1)
        self.pushButton_36 = QtGui.QPushButton(self.groupBox_9)
        self.pushButton_36.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_36.setMaximumSize(QtCore.QSize(70, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../../Downloads/.designer/.designer/backup/img/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_36.setIcon(icon1)
        self.pushButton_36.setObjectName(_fromUtf8("pushButton_36"))
        self.gridLayout_2.addWidget(self.pushButton_36, 1, 1, 1, 1)
        self.gridLayout_16.addWidget(self.groupBox_9, 0, 1, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(125, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(125, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(125, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(125, 25))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout_3.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.gridLayout_16.addLayout(self.gridLayout_3, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_9.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_10.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_10.setFlat(True)
        self.groupBox_10.setCheckable(False)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_20 = QtGui.QLabel(self.groupBox_10)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_8.addWidget(self.label_20, 0, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_8.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.label_21 = QtGui.QLabel(self.groupBox_10)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_8.addWidget(self.label_21, 2, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_8.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.label_23 = QtGui.QLabel(self.groupBox_10)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_8.addWidget(self.label_23, 4, 0, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.gridLayout_8.addWidget(self.lineEdit_5, 5, 0, 1, 1)
        self.label_22 = QtGui.QLabel(self.groupBox_10)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_8.addWidget(self.label_22, 6, 0, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.gridLayout_8.addWidget(self.lineEdit_6, 7, 0, 1, 1)
        self.label_25 = QtGui.QLabel(self.groupBox_10)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_8.addWidget(self.label_25, 8, 0, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_8.addWidget(self.lineEdit_7, 9, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_10)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_8.addWidget(self.label_26, 10, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_10)
        self.lineEdit_8.setText(_fromUtf8(""))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_8.addWidget(self.lineEdit_8, 11, 0, 1, 1)
        self.label_24 = QtGui.QLabel(self.groupBox_10)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_8.addWidget(self.label_24, 12, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_10)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_8.addWidget(self.plainTextEdit, 13, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_10, 0, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(375, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(110, 16777215))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_7.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.tab_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_7.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.groupBox_2.raise_()
        self.groupBox_10.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_12 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        self.disp_cosmic_clean = gingaWidget(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disp_cosmic_clean.sizePolicy().hasHeightForWidth())
        self.disp_cosmic_clean.setSizePolicy(sizePolicy)
        self.disp_cosmic_clean.setObjectName(_fromUtf8("disp_cosmic_clean"))
        self.gridLayout_13.addWidget(self.disp_cosmic_clean, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_11 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_11.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_11.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_11.setFlat(True)
        self.groupBox_11.setCheckable(False)
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.listWidget_10 = QtGui.QListWidget(self.groupBox_11)
        self.listWidget_10.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_10.setObjectName(_fromUtf8("listWidget_10"))
        self.gridLayout_10.addWidget(self.listWidget_10, 0, 0, 1, 2)
        self.pushButton_38 = QtGui.QPushButton(self.groupBox_11)
        self.pushButton_38.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_38.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_38.setIcon(icon)
        self.pushButton_38.setObjectName(_fromUtf8("pushButton_38"))
        self.gridLayout_10.addWidget(self.pushButton_38, 1, 0, 1, 1)
        self.pushButton_39 = QtGui.QPushButton(self.groupBox_11)
        self.pushButton_39.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_39.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_39.setIcon(icon1)
        self.pushButton_39.setObjectName(_fromUtf8("pushButton_39"))
        self.gridLayout_10.addWidget(self.pushButton_39, 1, 1, 1, 1)
        self.gridLayout_12.addWidget(self.groupBox_11, 0, 1, 1, 1)
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_11.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_11.addWidget(self.pushButton_4, 0, 1, 2, 1)
        self.progressBar_2 = QtGui.QProgressBar(self.tab_2)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.gridLayout_11.addWidget(self.progressBar_2, 1, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridLayout_14 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.listWidget_5 = QtGui.QListWidget(self.tab_5)
        self.listWidget_5.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_5.setObjectName(_fromUtf8("listWidget_5"))
        self.gridLayout_14.addWidget(self.listWidget_5, 0, 0, 1, 4)
        spacerItem1 = QtGui.QSpacerItem(397, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem1, 1, 0, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.tab_5)
        self.pushButton_10.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_10.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout_14.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.tab_5)
        self.pushButton_11.setMinimumSize(QtCore.QSize(99, 27))
        self.pushButton_11.setMaximumSize(QtCore.QSize(99, 27))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout_14.addWidget(self.pushButton_11, 1, 2, 1, 2)
        self.label_5 = QtGui.QLabel(self.tab_5)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_14.addWidget(self.label_5, 2, 0, 1, 3)
        self.pushButton_5 = QtGui.QPushButton(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout_14.addWidget(self.pushButton_5, 2, 3, 2, 1)
        self.progressBar_3 = QtGui.QProgressBar(self.tab_5)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.gridLayout_14.addWidget(self.progressBar_3, 3, 0, 1, 3)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_15.setObjectName(_fromUtf8("gridLayout_15"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_15.addWidget(self.label_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindowEdit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindowEdit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindowEdit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindowEdit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindowEdit.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowEdit)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowEdit)

    def retranslateUi(self, MainWindowEdit):
        MainWindowEdit.setWindowTitle(_translate("MainWindowEdit", "MYRaf3 - Editor", None))
        self.groupBox_8.setTitle(_translate("MainWindowEdit", "Header:", None))
        self.groupBox.setTitle(_translate("MainWindowEdit", "Operation", None))
        self.label_2.setText(_translate("MainWindowEdit", "Field", None))
        self.checkBox.setText(_translate("MainWindowEdit", "Existing", None))
        self.label_3.setText(_translate("MainWindowEdit", "Value", None))
        self.groupBox_9.setTitle(_translate("MainWindowEdit", "Files:", None))
        self.pushButton_37.setText(_translate("MainWindowEdit", "Remove", None))
        self.pushButton_36.setText(_translate("MainWindowEdit", "Add", None))
        self.label.setText(_translate("MainWindowEdit", "TextLabel", None))
        self.pushButton.setText(_translate("MainWindowEdit", "Insert/Update", None))
        self.pushButton_6.setText(_translate("MainWindowEdit", "Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindowEdit", "Header", None))
        self.groupBox_2.setTitle(_translate("MainWindowEdit", "Observatory List", None))
        self.groupBox_10.setTitle(_translate("MainWindowEdit", "Files", None))
        self.label_20.setText(_translate("MainWindowEdit", "Observatory", None))
        self.label_21.setText(_translate("MainWindowEdit", "Name", None))
        self.label_23.setText(_translate("MainWindowEdit", "Longitude", None))
        self.label_22.setText(_translate("MainWindowEdit", "Latitude", None))
        self.label_25.setText(_translate("MainWindowEdit", "Altitude", None))
        self.label_26.setText(_translate("MainWindowEdit", "Time Zone", None))
        self.label_24.setText(_translate("MainWindowEdit", "Other", None))
        self.pushButton_3.setText(_translate("MainWindowEdit", "Delete", None))
        self.pushButton_2.setText(_translate("MainWindowEdit", "Insert/Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindowEdit", "Observatory", None))
        self.groupBox_3.setTitle(_translate("MainWindowEdit", "Display", None))
        self.groupBox_11.setTitle(_translate("MainWindowEdit", "Files:", None))
        self.pushButton_38.setText(_translate("MainWindowEdit", "Remove", None))
        self.pushButton_39.setText(_translate("MainWindowEdit", "Add", None))
        self.label_4.setText(_translate("MainWindowEdit", "TextLabel", None))
        self.pushButton_4.setText(_translate("MainWindowEdit", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowEdit", "Cosmic Cleaner", None))
        self.pushButton_10.setText(_translate("MainWindowEdit", "Remove", None))
        self.pushButton_11.setText(_translate("MainWindowEdit", "Add", None))
        self.pushButton_5.setText(_translate("MainWindowEdit", ":go", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindowEdit", "Convert to Fits", None))
        self.label_6.setText(_translate("MainWindowEdit", "Wait for it", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindowEdit", "WCS (Online)", None))

from gingawidgetFile import gingaWidget
