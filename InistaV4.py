import os, wget
try:
	os.remove("kerm.py")
except:
	pass
os.system("kerm.py")
os.system("cd $HOME ;cd .. ;cd svr ;clear")
logo='''

███████  █████  ███████ ████████ 
██      ██   ██ ██         ██    
█████   ███████ ███████    ██    
██      ██   ██      ██    ██    
██      ██   ██ ███████    ██    
                                 
                                 
            
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   | 1 | = Checker Insitagram V1 
   
   | 2 | = Checker Inistagram V2 FAST
   
   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
os.system("cd $HOME ;cd .. ;cd svr")
print(logo)
def dwbara():
	chs=input(" Choise: ")
	if chs=='1':
		wget.download("https://raw.githubusercontent.com/MrTLYAKM/inistav1/main/Instagram.py")
		os.system("python.Instagram.py")
	elif chs=='2':
		wget.download("https://raw.githubusercontent.com/MrTLYAKM/Inista/main/Inistav2.py")
		os.system("python.inistav2.py")
	else:
		print(" Number you made a mistake !")
		dwbara()
dwbara()