import subprocess
from shutil import copy
import re
import os
import glob

files = glob.glob('/reports/*')
for f in files:
    os.remove(f)

try:
	os.remove("behave.ini")
except (FileNotFoundError) as e:
	pass


copy("firefox.ini", "behave.ini")

features = {}

for dirpath, dirnames, filenames in os.walk("."):
	for filename in [f for f in filenames if f.endswith(".feature")]:
		features[f"{dirpath}"] = f"{filename}"

for index, (key, value) in enumerate(features.items()):
	proc1 = os.system(f"start /b behave {key} > {value.split('.')[0]}.txt")
	print(f"Process {index+1} started...")

