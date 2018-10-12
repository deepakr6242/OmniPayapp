import os
import random
import datetime

def foo():


	port_end_digit= random.randint(1,9)
	print port_end_digit

	with open('C:\\Python27\\Scripts\\omnipay\\log.txt','a+') as file:
		file.write("App  is running in 808"+str(port_end_digit)+str(datetime.datetime.now())+'\n')
	print"logged"
	os.chdir('C:\\Python27\\Scripts\\omnipay')


	try:
		os.system('python manage.py runserver 127.0.0.1:808'+str(port_end_digit))

	except Exceptio as e:
		print"Exception is due to ",e
foo()
