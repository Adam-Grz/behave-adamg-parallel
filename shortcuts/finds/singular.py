from selenium import webdriver


def findID(context, id):
    return context.driver.find_element_by_xpath(id)

def findXP(context, xpath):
    return context.driver.find_element_by_xpath(xpath)
