import subprocess
from shutil import copy

copy("chrome.ini", "behave.ini")
proc = subprocess.Popen("behave")
