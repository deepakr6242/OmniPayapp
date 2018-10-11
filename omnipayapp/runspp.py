import os
import random

x= random.randint(6,9)
print x

with open('C:\\Python27\\Scripts\\omnipay\\log.txt','w+') as file:
	file.write("App  is running in 808"+str(x))
os.chdir('C:\\Python27\\Scripts\\omnipay')


try:
	os.system('python manage.py runserver 127.0.0.1:808'+str(x))
finally:
	print("The newly changed application   is running in  808 {}".format(x))
