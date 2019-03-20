import subprocess
from shutil import copy

copy("firefox.ini", "behave.ini")
proc = subprocess.Popen("behave")
