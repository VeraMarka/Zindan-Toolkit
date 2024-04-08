import os
import colorama
import time

os.system("pkg install python")
os.system("pkg install figlet")
os.system("apt install git")
os.system("clear")

os.system("figlet Zindan Web")
print("\033[93mCreated By ZİNDAN WEB\033[0m")
print()
print("\033[91m\033[1m[1] Tiktok Hile\033[0m")
print("\033[93m\033[1m[2] Sms Bomb TR(bakımda)\033[0m")
print("\033[94m\033[1m[3] İnstagram TT hile\033[0m")
print("\033[92m\033[1m[4] İp Sorgu\033[0m")
print("\033[95m\033[1m[5] Web Site İnfo[0m")
print()
print("\033[1;31m~ Seçiminiz?;", end="")
print("\033[1;34m", end="")
seçim = int(input())
if seçim == 1:
  os.system("clear")
  os.system("git clone https://github.com/VeraMarka/Tiktok-Izlenme.git")
  os.system(cd Tiktok-Izlenme")
  os.system("python izlenme.py")

if seçim == 2:
  print("\033[93m\033[1mBu Araç Şuan bakımda.\033[0m")
  time.sleep("3)
  os.system("zindan-kit.py")

if seçim == 3:
  os.system("clear")
  os.system("git clone https://github.com/VeraMarka/IgTok.git")
  os.system("cd IgTok")
  os.system("python igtok.py")

if seçim == 4:
  os.system("clear")
  os.system("git clone https://github.com/VeraMarka/IpConfig.git")
  os.systen("cd IpConfig")
  os.system("python Zindan-Check.py")

if seçim == 5:
  os.system("clear")
  print("\033[95\033[1mBu Araç Şuan bakımda.\033[0m")
  time.sleep(3)
  os.system("zindan-kit.py")
  
  
  
  
