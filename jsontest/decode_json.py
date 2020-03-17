from meetInfo import getMydata
from Ui_meetList import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys
import json
from PyQt5.QtCore import *  

class MainWin(QMainWindow):

	def __init__(self):        
		super(MainWin, self).__init__()        
		print("mainwin is called!")        
		self.ui = Ui_MainWindow()        
		self.ui.setupUi(self)        
		self.ui.tableWidget.setColumnCount(5)  # 设置表格的列数        
		# self.ui.tableWidget.setRowCount(100)           #设置表格的行数        
		self.loadMeetInfo()        
		print(f"current rows:{self.ui.tableWidget.currentRow()}")     

	def loadMeetInfo(self):        
		data = getMydata()        # 获取信息列表        
		meetData = json.loads(data)['data']        # 获取用户信息        
		userInfo = meetData['userInfo']        
		userName = userInfo['name']        
		self.ui.userName.setText("当前用户为：" + userName)         

		# 获取会议详情        
		meetInfo = meetData['meetInfo']        
		# index=0        
		for i, item in enumerate(meetInfo):            
			# index+=1            
			# str(item['id'])将整型转换为字符串            
			self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)            
			print(self.ui.tableWidget.rowCount())            
			mId = QTableWidgetItem(str(item['id']))            
			mId.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中            
			mId.setFlags(Qt.ItemIsEnabled)  # 设置表格不可编辑模式            
			self.ui.tableWidget.setItem(                
				self.ui.tableWidget.rowCount() - 1, 0, mId)             

			mTitle = QTableWidgetItem(item['name'])            
			mTitle.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中            
			mTitle.setFlags(Qt.ItemIsEnabled)  # 设置表格不可编辑模式            
			self.ui.tableWidget.setItem(                
				self.ui.tableWidget.rowCount() - 1, 1, mTitle)             

			mTime = QTableWidgetItem(item['meet_time'])            
			mTime.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中            
			mTime.setFlags(Qt.ItemIsEnabled)  # 设置表格不可编辑模式            
			self.ui.tableWidget.setItem(                
				self.ui.tableWidget.rowCount() - 1, 2, mTime)             

			mAddress = QTableWidgetItem(item['meet_address'])            
			mAddress.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中            
			mAddress.setFlags(Qt.ItemIsEnabled)  # 设置表格不可编辑模式            
			self.ui.tableWidget.setItem(                
				self.ui.tableWidget.rowCount() - 1, 3, mAddress)        

		# return index     

	def addMeetBtn_clicked(self):        
		i = self.ui.tableWidget.rowCount()        
		i += 1        
		self.ui.tableWidget.setRowCount(i)        
		meetId = self.ui.meetId.text()        # print(type(meetId))        
		mId = QTableWidgetItem(meetId)        
		mId.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中        
		self.ui.tableWidget.setItem(i - 1, 0, mId)         
		meetTitle = self.ui.meetTitle.text()        
		mTitle = QTableWidgetItem(meetTitle)        
		mTitle.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中        
		self.ui.tableWidget.setItem(i - 1, 1, mTitle)         
		meetTime = self.ui.meetTime.text()        
		mTime = QTableWidgetItem(meetTime)        
		mTime.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中        
		self.ui.tableWidget.setItem(i - 1, 2, mTime)         
		meetAddress = self.ui.meetAddress.text()        
		mAddress = QTableWidgetItem(meetAddress)        
		mAddress.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中        
		self.ui.tableWidget.setItem(i - 1, 3, mAddress)         

		# LineEdit内容清除        
		self.ui.meetId.setText("")        
		self.ui.meetTitle.setText("")        
		self.ui.meetTime.setText("")        
		self.ui.meetAddress.setText("")  

if __name__ == "__main__":    
	app = QApplication(sys.argv)    
	main = MainWin()    # 显示主界面    
	main.show()     


	sys.exit(app.exec_())
