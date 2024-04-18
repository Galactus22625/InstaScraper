to find who doesn't follow you back on instagram since there is no API.  
The code is a little messy since this was a weekend project and I did not have time to make a polished product.  I also had already achieved my goal.

Add Account information into Accounts.py, use the account login for the account you want to check if using autoscraper, otherwise just add any throwaway account that can view your account.

AutoScraper.py logs into account and finds followers and  following of the account,and who isn't follwoing back all automatically
Auto scraper is sometimes bugged where after finding one list, program will crash when trying to scroll the next one.  This is becuase selenium is trying to select a stale element.  Never fixed because using UserTools is more versatile.

accounts are accessed by scrolling down the following or followers list to load all the accounts onto the webpage
To use, user user tools to navigate to the account of interest, we will scape all followers, save them, scrape all following, save them, then run follow back

All functionality can be achieved in User Tool.
you can do several actions with user tools by typing in commands.
"Open Web" opens a web brower and logs into the instagram account
"Load Accounts" loads accounts from a text file into local memory
"Save Accounts" saves all accounts from local memory into a text file
"Wipe Accounts" deletes the accounts in local memory
"Load Followers" scrolls until all the accounts have loaded (sometimes bugs when tries to scroll a stale element)
"Scrape Accounts" Saves all the accounts that have already been loaded on the current page to local memory
"Follow Back" takes a text file for follower and one for following and prints out who isnt following you back
"Exit" closes the web page

There are two notable issues, which can be worked around.  The first is the scrolling function sometimes crashes when slelenium tries to scroll a stale element.  the second is that instagram only will load like 500 accounts.  so if there are more accounts, you have to do it a few times in order to make this work.  this means the method is a little impractible after like 1500 accounts, however pages that big probably arent thinking about who doesnt follow them back anyways