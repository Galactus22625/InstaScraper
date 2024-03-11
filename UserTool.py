from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import Accounts
from InstaFunctions import *
from FollowBack import FollowBack

if __name__ == "__main__":
    accounts = []
    driver = None
    while True:
        nextAction = input("State Action: ")
        match nextAction:
            case "Open Web":
                loginstring = Accounts.test.login
                passwordstring = Accounts.test.password
                driver = webdriver.Chrome()
                driver.get("https://www.instagram.com")
                log_in(driver, loginstring, passwordstring)

            case "Load Accounts":
                fileName = input("NameOfFile: ")
                file = open(fileName, "r")
                names = file.readlines()
                file.close()
                for person in names:
                    if person not in accounts:
                        if person == "\n":
                            continue
                        toadd = person.replace("%", "")
                        add = toadd.replace("?next=2F", "")
                        add2 = add.strip()
                        accounts.append(add2)

            case "Save Accounts":
                fileName = input("NameOfFile: ")
                file = open(fileName,'w')
                for person in accounts:
                    file.write(person + "\n")
                file.close()
            
            case "Wipe Accounts":
                accounts = []

            case "Load Followers":
                loadfollowers(driver)

            case "Scrape Accounts":
                nextBatch = getaccounts(driver)
                for person in nextBatch:
                    if person not in accounts:
                        accounts.append(person)

            case "Follow Back":
                followerfile = input("Follower File Name:  ")
                followingfile = input("Following File Name: ")
                FollowBack(followerfile,followingfile)

            case "Exit":
                if driver != None:
                    driver.close()
                break


