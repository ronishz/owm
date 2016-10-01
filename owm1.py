import os,sys,time
d=time.strftime("%Y-%m-%d")
t=time.strftime("%H:%M:%S")	
os.system("python owm.py | grep "+d+" -A 2 -B 14 > output.txt")
os.system("sed -i 's/u//g' output.txt")
os.system("sed -i 's/poplation/population/g' output.txt")
os.system("sed -i 's/hmidity/humidity/g' output.txt")
os.system("sed -i 's/clods/clouds/g' output.txt")
os.system("sed -i 's/grnd/ground/g' output.txt")
os.system("sed -i 's/contry/country/g' output.txt")
f=open("output.txt","r")
f1=f.read()
print f1
