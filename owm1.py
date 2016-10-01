import os,sys,time
t=time.strftime("%Y-%m-%d")
os.system("python owm.py | grep "+t+" -A 2 -B 14")
