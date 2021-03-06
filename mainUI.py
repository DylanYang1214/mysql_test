# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1018, 860)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btnLoadDb = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadDb.setObjectName("btnLoadDb")
        self.horizontalLayout_5.addWidget(self.btnLoadDb)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)
        self.horizontalLayout_5.setStretch(2, 10)
        self.horizontalLayout_5.setStretch(3, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.queryTabWidget = QtWidgets.QWidget()
        self.queryTabWidget.setObjectName("queryTabWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.queryTabWidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.groupBox = QtWidgets.QGroupBox(self.queryTabWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.textDataId = QtWidgets.QLineEdit(self.groupBox)
        self.textDataId.setObjectName("textDataId")
        self.horizontalLayout.addWidget(self.textDataId)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.textDataFileName = QtWidgets.QLineEdit(self.groupBox)
        self.textDataFileName.setObjectName("textDataFileName")
        self.horizontalLayout.addWidget(self.textDataFileName)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.dateDataDate1 = QtWidgets.QDateEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateDataDate1.sizePolicy().hasHeightForWidth())
        self.dateDataDate1.setSizePolicy(sizePolicy)
        self.dateDataDate1.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateDataDate1.setObjectName("dateDataDate1")
        self.horizontalLayout_2.addWidget(self.dateDataDate1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.dateDataDate2 = QtWidgets.QDateEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateDataDate2.sizePolicy().hasHeightForWidth())
        self.dateDataDate2.setSizePolicy(sizePolicy)
        self.dateDataDate2.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateDataDate2.setObjectName("dateDataDate2")
        self.horizontalLayout_2.addWidget(self.dateDataDate2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.cmbDataLocation = QtWidgets.QComboBox(self.groupBox)
        self.cmbDataLocation.setObjectName("cmbDataLocation")
        self.cmbDataLocation.addItem("")
        self.cmbDataLocation.addItem("")
        self.cmbDataLocation.addItem("")
        self.cmbDataLocation.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbDataLocation)
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_3.addWidget(self.label_32)
        self.cmbDataModel = QtWidgets.QComboBox(self.groupBox)
        self.cmbDataModel.setObjectName("cmbDataModel")
        self.cmbDataModel.addItem("")
        self.cmbDataModel.addItem("")
        self.cmbDataModel.addItem("")
        self.cmbDataModel.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbDataModel)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.cmbDataMode = QtWidgets.QComboBox(self.groupBox)
        self.cmbDataMode.setObjectName("cmbDataMode")
        self.cmbDataMode.addItem("")
        self.cmbDataMode.addItem("")
        self.cmbDataMode.addItem("")
        self.cmbDataMode.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbDataMode)
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_3.addWidget(self.label_31)
        self.cmbDataEnv = QtWidgets.QComboBox(self.groupBox)
        self.cmbDataEnv.setObjectName("cmbDataEnv")
        self.cmbDataEnv.addItem("")
        self.cmbDataEnv.addItem("")
        self.cmbDataEnv.addItem("")
        self.cmbDataEnv.addItem("")
        self.cmbDataEnv.addItem("")
        self.cmbDataEnv.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbDataEnv)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.textDataRemarks = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textDataRemarks.sizePolicy().hasHeightForWidth())
        self.textDataRemarks.setSizePolicy(sizePolicy)
        self.textDataRemarks.setMaximumSize(QtCore.QSize(16777215, 45))
        self.textDataRemarks.setObjectName("textDataRemarks")
        self.horizontalLayout_4.addWidget(self.textDataRemarks)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.barQuery = QtWidgets.QProgressBar(self.groupBox)
        self.barQuery.setProperty("value", 24)
        self.barQuery.setObjectName("barQuery")
        self.horizontalLayout_9.addWidget(self.barQuery)
        self.btnQuery = QtWidgets.QPushButton(self.groupBox)
        self.btnQuery.setObjectName("btnQuery")
        self.horizontalLayout_9.addWidget(self.btnQuery)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.textHistory = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textHistory.sizePolicy().hasHeightForWidth())
        self.textHistory.setSizePolicy(sizePolicy)
        self.textHistory.setMaximumSize(QtCore.QSize(16777215, 45))
        self.textHistory.setObjectName("textHistory")
        self.verticalLayout.addWidget(self.textHistory)
        self.horizontalLayout_11.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.queryTabWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.historyTextBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.historyTextBrowser.setObjectName("historyTextBrowser")
        self.horizontalLayout_10.addWidget(self.historyTextBrowser)
        self.horizontalLayout_11.addWidget(self.groupBox_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.groupBox_2 = QtWidgets.QGroupBox(self.queryTabWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.btnQueryModify = QtWidgets.QPushButton(self.groupBox_2)
        self.btnQueryModify.setObjectName("btnQueryModify")
        self.horizontalLayout_16.addWidget(self.btnQueryModify)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_16.addWidget(self.pushButton_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem3)
        self.btnQueryDelete = QtWidgets.QPushButton(self.groupBox_2)
        self.btnQueryDelete.setObjectName("btnQueryDelete")
        self.horizontalLayout_16.addWidget(self.btnQueryDelete)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.tableView1 = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableView1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView1.setObjectName("tableView1")
        self.tableView1.setColumnCount(9)
        self.tableView1.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        item.setFont(font)
        self.tableView1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView1.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView1.setItem(1, 0, item)
        self.tableView1.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_2.addWidget(self.tableView1)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_11.addWidget(self.groupBox_2)
        self.verticalLayout_11.setStretch(1, 3)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.queryTabWidget, "")
        self.addTabWidget = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.addTabWidget.setFont(font)
        self.addTabWidget.setObjectName("addTabWidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.addTabWidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.groupBox_5 = QtWidgets.QGroupBox(self.addTabWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.btnSelectFile = QtWidgets.QPushButton(self.groupBox_5)
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.horizontalLayout_13.addWidget(self.btnSelectFile)
        self.btnViewFile = QtWidgets.QPushButton(self.groupBox_5)
        self.btnViewFile.setObjectName("btnViewFile")
        self.horizontalLayout_13.addWidget(self.btnViewFile)
        self.btnAddtoDb = QtWidgets.QPushButton(self.groupBox_5)
        self.btnAddtoDb.setObjectName("btnAddtoDb")
        self.horizontalLayout_13.addWidget(self.btnAddtoDb)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_40 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_14.addWidget(self.label_40)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_14.addWidget(self.lineEdit)
        self.verticalLayout_6.addLayout(self.horizontalLayout_14)
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout_6.addWidget(self.progressBar_3)
        self.textAddinfo = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textAddinfo.setObjectName("textAddinfo")
        self.verticalLayout_6.addWidget(self.textAddinfo)
        self.horizontalLayout_12.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.addTabWidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_7.addWidget(self.textBrowser_2)
        self.horizontalLayout_12.addWidget(self.groupBox_6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.groupBox_4 = QtWidgets.QGroupBox(self.addTabWidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btnAddModify = QtWidgets.QPushButton(self.groupBox_4)
        self.btnAddModify.setObjectName("btnAddModify")
        self.horizontalLayout_15.addWidget(self.btnAddModify)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_15.addWidget(self.pushButton_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem5)
        self.btnAddDelete = QtWidgets.QPushButton(self.groupBox_4)
        self.btnAddDelete.setObjectName("btnAddDelete")
        self.horizontalLayout_15.addWidget(self.btnAddDelete)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.tableView2 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableView2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView2.setObjectName("tableView2")
        self.tableView2.setColumnCount(9)
        self.tableView2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        item.setFont(font)
        self.tableView2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableView2.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableView2.setItem(0, 8, item)
        self.tableView2.verticalHeader().setDefaultSectionSize(25)
        self.verticalLayout_8.addWidget(self.tableView2)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_10.addWidget(self.groupBox_4)
        self.verticalLayout_10.setStretch(0, 2)
        self.verticalLayout_10.setStretch(1, 3)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.tabWidget.addTab(self.addTabWidget, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1018, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_2.setBuddy(self.textDataId)
        self.label_4.setBuddy(self.textDataFileName)
        self.label_3.setBuddy(self.dateDataDate1)
        self.label_7.setBuddy(self.dateDataDate2)
        self.label_8.setBuddy(self.cmbDataLocation)
        self.label_32.setBuddy(self.cmbDataModel)
        self.label_9.setBuddy(self.cmbDataMode)
        self.label_31.setBuddy(self.cmbDataEnv)
        self.label_16.setBuddy(self.textDataRemarks)
        self.label_40.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据管理系统"))
        self.btnLoadDb.setText(_translate("MainWindow", "加载库"))
        self.label.setText(_translate("MainWindow", "数据管理系统"))
        self.groupBox.setTitle(_translate("MainWindow", "输入检索条件："))
        self.label_2.setText(_translate("MainWindow", "数据ID："))
        self.textDataId.setPlaceholderText(_translate("MainWindow", "检索数据ID"))
        self.label_4.setText(_translate("MainWindow", "文件名："))
        self.textDataFileName.setPlaceholderText(_translate("MainWindow", "文件名"))
        self.label_3.setText(_translate("MainWindow", "时间从："))
        self.label_7.setText(_translate("MainWindow", "至："))
        self.label_8.setText(_translate("MainWindow", "地点   ："))
        self.cmbDataLocation.setItemText(0, _translate("MainWindow", "不限"))
        self.cmbDataLocation.setItemText(1, _translate("MainWindow", "火星"))
        self.cmbDataLocation.setItemText(2, _translate("MainWindow", "月球"))
        self.cmbDataLocation.setItemText(3, _translate("MainWindow", "木星"))
        self.label_32.setText(_translate("MainWindow", "型号："))
        self.cmbDataModel.setItemText(0, _translate("MainWindow", "不限"))
        self.cmbDataModel.setItemText(1, _translate("MainWindow", "终结者"))
        self.cmbDataModel.setItemText(2, _translate("MainWindow", "超人"))
        self.cmbDataModel.setItemText(3, _translate("MainWindow", "钢铁侠"))
        self.label_9.setText(_translate("MainWindow", "重频："))
        self.cmbDataMode.setItemText(0, _translate("MainWindow", "不限"))
        self.cmbDataMode.setItemText(1, _translate("MainWindow", "HPRF"))
        self.cmbDataMode.setItemText(2, _translate("MainWindow", "MFPR"))
        self.cmbDataMode.setItemText(3, _translate("MainWindow", "LPRF"))
        self.label_31.setText(_translate("MainWindow", "环境："))
        self.cmbDataEnv.setItemText(0, _translate("MainWindow", "不限"))
        self.cmbDataEnv.setItemText(1, _translate("MainWindow", "沙地"))
        self.cmbDataEnv.setItemText(2, _translate("MainWindow", "森林"))
        self.cmbDataEnv.setItemText(3, _translate("MainWindow", "城市"))
        self.cmbDataEnv.setItemText(4, _translate("MainWindow", "海洋"))
        self.cmbDataEnv.setItemText(5, _translate("MainWindow", "戈壁"))
        self.label_16.setText(_translate("MainWindow", "备注  ："))
        self.textDataRemarks.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textDataRemarks.setPlaceholderText(_translate("MainWindow", "检索备注信息"))
        self.btnQuery.setText(_translate("MainWindow", "查询"))
        self.textHistory.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textHistory.setPlaceholderText(_translate("MainWindow", "查询结果"))
        self.groupBox_3.setTitle(_translate("MainWindow", "数据预览："))
        self.historyTextBrowser.setPlaceholderText(_translate("MainWindow", "预览选择的数据信息"))
        self.groupBox_2.setTitle(_translate("MainWindow", "查询结果"))
        self.btnQueryModify.setText(_translate("MainWindow", "更改"))
        self.pushButton_4.setText(_translate("MainWindow", "重置"))
        self.btnQueryDelete.setText(_translate("MainWindow", "删除"))
        item = self.tableView1.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "例如："))
        item = self.tableView1.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableView1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "数据ID"))
        item = self.tableView1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableView1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableView1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "地点"))
        item = self.tableView1.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "型号"))
        item = self.tableView1.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "重频"))
        item = self.tableView1.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "环境"))
        item = self.tableView1.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "备注"))
        item = self.tableView1.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "数据地址"))
        __sortingEnabled = self.tableView1.isSortingEnabled()
        self.tableView1.setSortingEnabled(False)
        item = self.tableView1.item(0, 0)
        item.setText(_translate("MainWindow", "10000001"))
        item = self.tableView1.item(0, 1)
        item.setText(_translate("MainWindow", "7s2019010101"))
        item = self.tableView1.item(0, 2)
        item.setText(_translate("MainWindow", "2019-05-22"))
        item = self.tableView1.item(0, 3)
        item.setText(_translate("MainWindow", "火星"))
        item = self.tableView1.item(0, 4)
        item.setText(_translate("MainWindow", "钢铁侠"))
        item = self.tableView1.item(0, 5)
        item.setText(_translate("MainWindow", "HPRF"))
        item = self.tableView1.item(0, 6)
        item.setText(_translate("MainWindow", "城市"))
        item = self.tableView1.item(0, 7)
        item.setText(_translate("MainWindow", "C:\\Users\\Yx\\Downloads"))
        item = self.tableView1.item(0, 8)
        item.setText(_translate("MainWindow", "数据有瑕疵"))
        item = self.tableView1.item(1, 0)
        item.setText(_translate("MainWindow", "202003060209"))
        self.tableView1.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.queryTabWidget), _translate("MainWindow", "数据查询"))
        self.groupBox_5.setTitle(_translate("MainWindow", "新增数据"))
        self.btnSelectFile.setText(_translate("MainWindow", "设置文件路径"))
        self.btnViewFile.setText(_translate("MainWindow", "获取数据条目"))
        self.btnAddtoDb.setText(_translate("MainWindow", "添加至数据库"))
        self.label_40.setText(_translate("MainWindow", "文件路径："))
        self.textAddinfo.setPlaceholderText(_translate("MainWindow", "新增条目信息......"))
        self.groupBox_6.setTitle(_translate("MainWindow", "数据预览："))
        self.textBrowser_2.setPlaceholderText(_translate("MainWindow", "预览选择的数据信息"))
        self.groupBox_4.setTitle(_translate("MainWindow", "新增数据条目预览"))
        self.btnAddModify.setText(_translate("MainWindow", "更改"))
        self.pushButton_5.setText(_translate("MainWindow", "重置"))
        self.btnAddDelete.setText(_translate("MainWindow", "删除"))
        item = self.tableView2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "例如："))
        item = self.tableView2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "数据ID"))
        item = self.tableView2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "文件名"))
        item = self.tableView2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时间"))
        item = self.tableView2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "地点"))
        item = self.tableView2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "型号"))
        item = self.tableView2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "重频"))
        item = self.tableView2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "环境"))
        item = self.tableView2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "备注"))
        item = self.tableView2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "数据地址"))
        __sortingEnabled = self.tableView2.isSortingEnabled()
        self.tableView2.setSortingEnabled(False)
        item = self.tableView2.item(0, 0)
        item.setText(_translate("MainWindow", " 100000001"))
        item = self.tableView2.item(0, 1)
        item.setText(_translate("MainWindow", "7s2019010101"))
        item = self.tableView2.item(0, 2)
        item.setText(_translate("MainWindow", "2019-05-22"))
        item = self.tableView2.item(0, 3)
        item.setText(_translate("MainWindow", "火星"))
        item = self.tableView2.item(0, 4)
        item.setText(_translate("MainWindow", "钢铁侠"))
        item = self.tableView2.item(0, 5)
        item.setText(_translate("MainWindow", "HPRF"))
        item = self.tableView2.item(0, 6)
        item.setText(_translate("MainWindow", "城市"))
        item = self.tableView2.item(0, 7)
        item.setText(_translate("MainWindow", "C:\\Users\\Yx\\Downloads"))
        item = self.tableView2.item(0, 8)
        item.setText(_translate("MainWindow", "数据有瑕疵"))
        self.tableView2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addTabWidget), _translate("MainWindow", "添加"))
