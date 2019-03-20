from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def presenceID(context, id):
    return context.wait.until(EC.presence_of_element_located((By.ID, id)))

def presenceXP(context, xpath):
    return context.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

def visibilityID(context, id):
    return context.wait.until(EC.visibility_of_element_located((By.ID, id)))

def visibilityXP(context, xpath):
    return context.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
