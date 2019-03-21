import subprocess
from shutil import copy
import re
import os
import glob
import sys


# Read arguments from the command line
argument = ""

try:
	argument = sys.argv[1]
except IndexError as e:
	print("""\n\t\tUse one of the following arguments:
			 \n\t\t\tchrome   --  start chromedriver
			 \n\t\t\tfirefox  --  start geckodriver""")

# Find and delete xml files in /reports
files = glob.glob('/reports/*')
for f in files:
    os.remove(f)

# Delete behave.ini if exists
try:
	os.remove("behave.ini")
except (FileNotFoundError) as e:
	pass

# Copy the selected .ini as behave.ini so that behave has an .ini file to take parameters from
if 'chrome' in argument:
	print("\n\tStarting chromedriver...\n")
	copy("chrome.ini", "behave.ini")

if 'firefox' in argument:
	print("\n\tStarting geckodriver...\n")
	copy("firefox.ini", "behave.ini")

# Find all .feature files and store them in features dictionary
features = {}

for dirpath, dirnames, filenames in os.walk("."):
	for filename in [f for f in filenames if f.endswith(".feature")]:
		features[f"{dirpath}"] = f"{filename}"

# Fire up a number of behave processes equal to the number of features
for index, (key, value) in enumerate(features.items()):
	proc1 = os.system(f"start /b behave {key} > {value.split('.')[0]}.txt")
	print(f"Process {index+1} started...")

