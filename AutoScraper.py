from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import Accounts
from InstaFunctions import *
from FollowBack import FollowBack

loginstring = Accounts.test.login
passwordstring = Accounts.test.password

if __name__ == "__main__":

	driver = webdriver.Chrome()
	driver.get("https://www.instagram.com")

	log_in(driver, loginstring, passwordstring)
	#assert(input("Type y if we are past two factor security\n") == "y")
	time.sleep(15)

	profile_Xpath = "//a[contains(@href, '/" + loginstring + "/')]"
	profile = driver.find_element(By.XPATH, profile_Xpath)
	profile.click()

	following_Xpath = "//a[contains(@href, '/following/')]"
	following_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, following_Xpath)))
	following_button.click()

	loadfollowing(driver)
	followings = getaccounts(driver)
	closefollowing(driver)

	file = open('followings.txt','w')
	for following in followings:
		file.write(following+"\n")
	file.close()

	follower_Xpath = "//a[contains(@href, '/followers/')]"
	follower_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, follower_Xpath)))
	follower_button.click()

	loadfollowers(driver)
	followers = getaccounts(driver)
	closefollowers(driver)

	file = open('followers.txt','w')
	for follower in followers:
		file.write(follower+"\n")
	file.close()

	driver.close()
	FollowBack()