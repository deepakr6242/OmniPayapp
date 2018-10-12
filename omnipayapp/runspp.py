import os
import random


def deploy_run():
	port_end_digit= random.randint(6,9)
	app_version= random.randint(2,10)
	print port_end_digit
	print app_version
	os.system('mkdir C:\\Omnipay_production_'+str(app_version))

	os.chdir('C:\\Omnipay_production_'+str(app_version))
	new_app=os.system('git clone  https://github.com/deepakr6242/OmniPayapp.git')

	with open('C:\\portinfo\\log.txt','a+') as file:
		file.write("App  is running in 808"+str(port_end_digit)+'\n')
	os.chdir('C:\\Python27\\OmniPayapp')
	try:
		os.system('python manage.py runserver 127.0.0.1:808'+str(port_end_digit))

	except Exception as e:
		print"Exception is due to ",e

if __name__=="__main__":
	deploy_run()
