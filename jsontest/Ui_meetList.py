# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_meetList.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addMeetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addMeetBtn.setGeometry(QtCore.QRect(390, 380, 93, 28))
        self.addMeetBtn.setObjectName("addMeetBtn")
        self.userName = QtWidgets.QLabel(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(380, 50, 151, 16))
        self.userName.setObjectName("userName")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 390, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 460, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 460, 72, 15))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 510, 72, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 510, 72, 15))
        self.label_7.setObjectName("label_7")
        self.meetAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.meetAddress.setGeometry(QtCore.QRect(370, 510, 151, 21))
        self.meetAddress.setObjectName("meetAddress")
        self.meetId = QtWidgets.QLineEdit(self.centralwidget)
        self.meetId.setGeometry(QtCore.QRect(130, 460, 141, 21))
        self.meetId.setObjectName("meetId")
        self.meetTime = QtWidgets.QLineEdit(self.centralwidget)
        self.meetTime.setGeometry(QtCore.QRect(130, 510, 141, 21))
        self.meetTime.setObjectName("meetTime")
        self.meetTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.meetTitle.setGeometry(QtCore.QRect(370, 460, 151, 21))
        self.meetTitle.setObjectName("meetTitle")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 561, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.addMeetBtn.clicked.connect(MainWindow.addMeetBtn_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addMeetBtn.setText(_translate("MainWindow", "添加"))
        self.userName.setText(_translate("MainWindow", "当前用户为：张三"))
        self.label_2.setText(_translate("MainWindow", "会议列表信息"))
        self.label_3.setText(_translate("MainWindow", "新增会议信息"))
        self.label_4.setText(_translate("MainWindow", "会议ID:"))
        self.label_5.setText(_translate("MainWindow", "会议名称："))
        self.label_6.setText(_translate("MainWindow", "会议时间："))
        self.label_7.setText(_translate("MainWindow", "会议地点："))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "会议ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "会议名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "会议时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "会议地点"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "备注"))