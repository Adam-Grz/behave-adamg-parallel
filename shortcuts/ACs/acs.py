from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC


def hover(context, element):
	AC(context.driver).move_to_element(element).perform()