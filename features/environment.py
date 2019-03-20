from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
from html_behave import reporter
from shutil import rmtree

__TIMEOUT = 5

def before_all(context):
	try:
		os.remove("behave.ini")
		rmtree('/reports')
	except (FileNotFoundError) as e:
		pass

def before_scenario(context, scenario):
	browser = context.config.userdata.get("browser")
	if "chrome" in browser:
	    context.driver = webdriver.Chrome()
	elif "firefox" in browser:
		context.driver = webdriver.Firefox()
	context.driver.maximize_window()
	context.wait = WebDriverWait(context.driver, __TIMEOUT)

def after_scenario(context, scenario):
	context.driver.quit()

def after_all(context):
	try:
		os.remove("behave.ini")
	except (FileNotFoundError) as e:
		pass

	reporter()

