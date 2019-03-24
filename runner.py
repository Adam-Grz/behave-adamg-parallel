import subprocess
from shutil import (copy,
					move)
import re
import os
import glob
import sys
from time import sleep


# Read arguments from the command line
arg1 = ""
arg2 = ""

try:
	arg1 = sys.argv[1]
	arg2 = int(sys.argv[2])
except IndexError as e:
	print("""\n\t\tUsage: runner.py [browser] [number of parallel sessions]
			 \n\t\t[browser]:
			 \n\t\t\tchrome   --  start chromedriver
			 \n\t\t\tfirefox  --  start geckodriver
			 \n\t\t[number of parallel sessions]:
			 \n\t\t\t1 or higher""")
	sys.exit(1)

# Find and delete all files in /reports
files = glob.glob('reports/*')
for f in files:
    os.remove(f)

# Find and delete all files in /temp_output
files = glob.glob('temp_output/*')
for f in files:
    os.remove(f)

# Find and delete all files in /html_output
files = glob.glob('html_output/*')
for f in files:
    os.remove(f)

# Delete behave.ini if exists
try:
	os.remove("behave.ini")
except (FileNotFoundError) as e:
	pass

# Delete test_output.txt if exists
try:
	os.remove("test_output.txt")
except (FileNotFoundError) as e:
	pass

# Find all .feature files and store them in 2D lists
features = []

for dirpath, dirnames, filenames in os.walk("./features"):
	for filename in [f for f in filenames if f.endswith(".feature")]:
		features.append([[f"{dirpath}"],[f"{filename}"]])

# Copy the selected .ini as behave.ini so that behave has an .ini file to take parameters from
try:
	if 'chrome' in arg1:
		copy("chrome.ini", "behave.ini")
	elif 'firefox' in arg1:
		copy("firefox.ini", "behave.ini")
	elif not arg2.is_integer() or not arg2 or not 'chrome' or not 'firefox' in arg1:
		print("""\n\t\tUsage: runner.py [browser] [number of parallel sessions]
				 \n\t\t[browser]:
				 \n\t\t\tchrome   --  start chromedriver
				 \n\t\t\tfirefox  --  start geckodriver
				 \n\t\t[number of parallel sessions]:
				 \n\t\t\t1 or higher""")
		sys.exit(1)
except AttributeError as e:
	print("""\n\t\tUsage: runner.py [browser] [number of parallel sessions]
			 \n\t\t[browser]:
			 \n\t\t\tchrome   --  start chromedriver
			 \n\t\t\tfirefox  --  start geckodriver
			 \n\t\t[number of parallel sessions]:
			 \n\t\t\t1 or higher""")
	sys.exit(1)

# Fire up a number of behave processes equal to the number of features
def start_run(parallel):
	print()
	c = 0
	d = 0
	# while f_tracker <= len(features):
	# 	print(f_tracker, len(features))
	while not len(glob.glob("html_output/*.txt")) == len(features):
		d = c
		if parallel < len(features) - c:
			for a in range(0,parallel):
				output = f"temp_output/{features[c][1][0].split('.')[0]}.txt"
				os.system(f"start /b behave {features[c][0][0]}/{features[c][1][0]} > {output}")
				print(f"\t\tProcess {features[c][1][0].split('.')[0], c+1} started...")
				c += 1
		else:
			for a in range(c,len(features)):
				output = f"temp_output/{features[c][1][0].split('.')[0]}.txt"
				os.system(f"start /b behave {features[c][0][0]}/{features[c][1][0]} > {output}")
				print(f"\t\tProcess {features[c][1][0].split('.')[0], c+1} started...")
				c += 1
		for a in range(d,c):
			while True:
				f_open = open(f"temp_output/{features[a][1][0].split('.')[0]}.txt")
				f_read = f_open.read()
				f_open.close()
				sleep(2)
				if "Took" in f_read:
					move(f"temp_output/{features[a][1][0].split('.')[0]}.txt", f"html_output/{features[a][1][0].split('.')[0]}.txt")
					break

if arg2 < 1:
	print("\n\tERROR!")
	print(f"\n\t\tNumber of parallel sessions must be an integer 1 or higher! Is --> '{sys.argv[2]}', '{type(sys.argv[2])}'")
	sys.exit(1)

try:
	start_run(arg2)
except (TypeError, ValueError) as e:
	print("\n\tERROR!")
	print(f"\n\t\tNumber of parallel sessions must be an integer 1 or higher! Is --> '{arg2}', '{type(arg2)}'")
	sys.exit(1)