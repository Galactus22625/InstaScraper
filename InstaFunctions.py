from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import Accounts
import time
import logging

def loadfollowing(driver):
    followingbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]")))
    last_ht, ht = 0, 1
    while last_ht != ht:
        #exploit resize to reload people
        last_ht = ht
        time.sleep(4)
        
        #small window
        driver.set_window_size(600, 200)

        ht = driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight; """, followingbox)#inner box height

        #big window
        driver.set_window_size(800, 600)
        
    logging.info("Finished loading")

def loadfollowers(driver):
    box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))
    last_ht, ht = 0, 1
    while last_ht != ht:
        #exploit resize to reload people
        last_ht = ht
        time.sleep(4)
        
        #small window
        driver.set_window_size(600, 200)

        ht = driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
        return arguments[0].scrollHeight; """, box)#inner box height

        #big window
        driver.set_window_size(800, 600)
        
    logging.info("Finished loading")

def log_in(driver, login, password):
    usernamebox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
    usernamebox.send_keys(login)
    passwordbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
    passwordbox.send_keys(password)
    loginbutton = driver.find_element(By.XPATH, "//button[@class=' _acan _acap _acas _aj1- _ap30']")
    loginbutton.click()

def getaccounts(driver):
    accountselector = "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div > div._aano > div:nth-child(1) > div > div:nth-child(n) > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z.x78zum5.x1iyjqo2.xs83m0k.xeuugli.x1qughib.x6s0dn4.x1a02dak.x1q0g3np.xdl72j9 > div > div > div > div > div > a"
    people = driver.find_elements(By.CSS_SELECTOR, accountselector)
    names = [person.get_attribute('href').removeprefix('https://www.instagram.com/') for person in people]
    return names

def closefollowing(driver):
    closeButton = driver.find_element(By.XPATH, "//button[@class='_abl-']")
    closeButton.click()

def closefollowers(driver):
    closeButton = driver.find_element(By.XPATH, "//button[@class='_abl-']")
    closeButton.click()

#for testing functions
if __name__ == "__main__":
    pass