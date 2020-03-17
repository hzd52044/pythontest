import json 
import sys

filename = (r'D:\Python_test\pythontest\jsontest\cfg.json')

strData = {    
	'status':200,    
	'message':'获取信息成功!',    
	'data':{        
		'userInfo':{            
			'name':"麦嘟小布丁",            
			'sex':'女'        
		},        
		'meetInfo':[            
			{'id': 110,            
			'name': '人工智能技术会议',            
			'meet_date': '2019-01-08',            
			'meet_time': '16:30:00',            
			'meet_address': '会议室A'},            
			{'id': 221,            
			'name': '学习交流会',            
			'meet_date': '2018-12-19',            
			'meet_time': '14:30:00',            
			'meet_address': '会议室B'},            
			{'id': 226,            
			'name': '神经网络知识分享会',            
			'meet_date': '2018-12-19',            
			'meet_time': '09:00:00',            
			'meet_address': '会议室C'}            
			]   
	}
} 

#定义接口，用来获取json数据

def getMydata():    
	#return json.dumps(strData) 
	return json.dumps(open(filename)) 
if __name__ == "__main__":    
	# json.dumps()函数是将字典转化为字符串     
	jsonStr = json.dumps(strData)    
	#print(jsonStr)    
	# json.loads()函数是将字符串转化为字典    
	res = json.loads(jsonStr)    
	print(type(res),res)
