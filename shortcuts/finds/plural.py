from selenium import webdriver


def findIDs(context, id):
    return context.driver.find_elements_by_xpath(id)

def findXPs(context, xpath):
    return context.driver.find_elements_by_xpath(xpath)
