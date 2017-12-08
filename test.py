import os
from os import listdir
from os.path import isfile, join
import subprocess
import time
import csv
import threading


def main():
	#change__config("cpu","./processor_speed_test")
	#change__config("control","./processor_speed_test")
	#change__config("cpu","./double_loop_test")
	#change__config("control","./double_loop_test")
	change_hb("./double_loop_test")
	#change_hb("./processor_speed_test")

def change_config(config,test):
	for id in range(0,10):
		for freq in range(1,10):
			for core in range(1,5):
				with open("/etc/poet/" + config + "_config",'r+') as f:
					lines = f.readlines()
					f.seek(0)
					f.truncate()
					f.write(lines[0])
					for it in range(0,10):
						f.write(str(id+it) + "\t" + str(freq+it*1.5) + '\t\t' + str(core*0.6))
						f.write('\n')
				sp = subprocess.Popen(test + " 10 10 2",shell=True, preexec_fn=os.setsid)
				sp.wait()
				data = []
				with open('poet.log') as f:
					data = [line.strip() for line in f]
				with open('compile_config.log','a') as f:
					for dt in data:
						f.write(str(dt))
						f.write('\n')
					f.write("id:  " + str(id) + "  speedup: " + str(freq) + "  powerup: " + str(core))
					f.write('\n')

def change_hb(test):
	for i in range(10,12):
		for j in range(10,20):
			for k in range(1,5):
				sp = subprocess.Popen(test + " " + str(2*i) + " " + str(j*2) + " " + str(2*k),shell=True, preexec_fn=os.setsid)
				sp.wait()
				data = []
				with open('poet.log') as f:
					data = [line.strip() for line in f]
				with open('compile.log','a') as f:
					for dt in data:
						f.write(str(dt))
						f.write('\n')
					f.write("num_beats: " + str(20*i) + "  target_rate: " + str(10*j) + "  window_size: " + str(2*k))
					f.write('\n')
			print(data)
			print("hello")

if __name__ == '__main__':
	main()
