import subprocess
from shutil import copy
import re

copy("chrome.ini", "behave.ini")
proc = subprocess.run("behave", stdout=subprocess.PIPE)

output = str(proc.stdout)
with open("proc_output.txt", "w") as otp:
	otp.write(output)
took = output[output.index("Took"):]
took = took[:-5]

with open('foldername.txt', 'r') as fn:
	path = fn.readline()

lines = ""

with open (f'{path}/index.html', 'r') as html:
	lines = html.readlines()
	with open (f'{path}/index.html', 'w') as html2:
		for i, line in enumerate(lines):
			if "<h1>Test run" in line:
				line = line + f"<h2>{took}</h2>"
				lines[i] = line
				break
		lines = "".join(lines)
		html2.write(lines)	
