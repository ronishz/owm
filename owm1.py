import os,sys,time
d=time.strftime("%Y-%m-%d")
def getWeather():	
	os.system("python owm.py | grep "+d+" -A 14 -B 2 > output.txt")
	os.system("sed -i 's/u//g' output.txt")
	os.system("sed -i 's/poplation/population/g' output.txt")
	os.system("sed -i 's/hmidity/humidity/g' output.txt")
	os.system("sed -i 's/clods/clouds/g' output.txt")
	os.system("sed -i 's/grnd/ground/g' output.txt")
	os.system("sed -i 's/contry/country/g' output.txt")
	
getWeather()	
n=input("For what time do you want to see today's weather?\n1. 12pm\n2. 3pm\n3. 6pm\n4. 10pm\n")	
if(n==1):	
	os.system("cat output.txt | grep 12:00:00 -A 14 -B 2")
elif(n==2):
	os.system("cat output.txt | grep 15:00:00 -A 14 -B 2")
elif(n==3):
	os.system("cat output.txt | grep 18:00:00 -A 14 -B 2")
elif(n==4):
	os.system("cat output.txt | grep 21:00:00 -A 14 -B 2")
		
