#!/usr/bin/env python
#author: HB
import os
print("\033[95m")
os.system("clear")

print('''

 _   _ ____ _____ ___   ___  _
| | | | __ )_   _/ _ \ / _ \| |
| |_| |  _ \ | || | | | | | | |
|  _  | |_) || || |_| | |_| | |___
|_| |_|____/ |_| \___/ \___/|_____|


	1-) Tool'u Başlat 

	2-) İletişim

	3-) Bu dizine Toolu yükle

	4-) Bu dizinden Toolu sil

	5-) Tam kurulum (bazı durumlarda kök kullanıcı gerektirir)
			    
	6-) Tool Güncelle

	''')



HBT00L = input("Hangisini seçiyorsunuz? ")

if(HBT00L=="1"):
		os.system("python3 sys/main.py")
elif(HBT00L=="2"):
	print('''


		''')

elif(HBT00L=="3"):
	os.system("cd ..")
	os.system("git clone https://github.com/H4CK3RBRO/HBTOOL.git")
elif(HBT00L=="4"):
	print("\033[91mBu dizindeki Tool ve ilgili herşey kaldırılacak")
	sec = input("Kaldırmak istediğinize emin misiniz? y/n ")
	if(sec=="y"):
		os.system("cd ..")
		os.system("rm -rf HBTOOL")
	elif(sec=="n"):
		os.system("python3 main.py")
elif(HBT00L=="5"):
	os.system("apt install chkrootkit figlet python python2 python3 crunch git hydra mpv php")
	os.system("pip install -r sys/requirements.txt")
	os.system("apt update")
	print("Kurulum Tamamlandı 👍:)")
elif(HBT00L=="6"):
	os.system("rm -rf ../HBTOOL")
	os.system("git clone https://github.com/H4CK3RBRO/HBTOOL.git")
	os.system("pip install -r HBTOOL/requirements.txt")
	print("Tool Güncellendi :)")
else:
		os.system("python3 hbtool.py")