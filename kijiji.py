from selenium import webdriver
import time
import os
import pyautogui
from selenium.webdriver.common.keys import Keys
pyautogui.FAILSAFE = True

# These are some global sleep variables, for each of the expected sleep times
# May need to be changed depending how fast or slow a persons computer is
# For now we will pick some conservative times, so things should work out of the box

# For tabbing, arrow keys, and interacting with a single webpage
shortSleep = 0.2

# For all other loading, including file uploads, page refreshes or reloads, etc.
longSleep = 5

# Other hardcoded variables
postalCode = ""
phone = ""



# This will get the username and password from a text file
# Supports multiple logins, line separated
# Returns list of username,password
def getCredentials():

    # Open/read the file
    file = open("login.txt")
    file = file.read().splitlines()

    # Create list of usernames/passwords
    creds = []
    for credentials in file:
        credentials = credentials.split(", ")
        creds.append([credentials[0], credentials[1]])
    return creds


# This will retrieve the relevant info for the ad posting directory
# Returns title, price, description
def getAdInformation(directory):

    title, price, description = open("ads\\"+directory+"\\Ad.txt").read().split("\n", 2)
    return title, price, description


# This will return the absolute path to all images based on the directory
# Returns a list of absolute paths to images
def getAdImagePaths(directory):
    ads = os.getcwd() + "\\ads\\" + directory
    files = os.listdir(ads)

    # We will go through this list and remove the hidden files as well as Ad.txt
    # This will assume all remaining files are images so make sure they are!
    # Otherwise bad things might happen
    images = []
    for file in files:
        if file[0] != "." and file != "Ad.txt":
            images.append(ads + "\\" + file)
    return images


# This retrieves the directory name of each ad
# Returns list of ad folder names
def getAds():
    ads = os.getcwd() + "\\ads\\"
    ads = os.listdir(ads)
    return ads

# Initialize the browser, logging in with the given user/pass
# Returns browser object
def login(creds):

    # Init the browser, in this case firefox
    # Take us to kijiji and maximize the window
    # So, maybe only halfscreening the window is better for testing, then we can see the terminal output in real time
    browser = webdriver.Firefox()  # (executable_path='geckodriver')
    browser.maximize_window()
    browser.get('https://www.kijiji.ca/t-login.html')

    # Login by finding the correct fields by ID
    browser.find_element_by_id('LoginEmailOrNickname').send_keys(creds[0])
    browser.find_element_by_id("login-password").send_keys(creds[1])
    browser.find_element_by_id('SignInButton').click()

    # Wait for page load
    time.sleep(longSleep)

    return browser


# This will post an ad to the kijiji marketplace, takes browser object and directory
def postAd(browser, directory):

    # Get ad info
    title, price, description = getAdInformation(directory)

    # Skip category selection screen, go straight to ad post page
    # 236 is currently other
    # We can decide how to do this later
    category = 236
    browser.get("https://www.kijiji.ca/p-admarkt-post-ad.html?categoryId=%s&adTitle=%s" % (str(category), title))
    time.sleep(longSleep)

    # Input description
    browser.find_element_by_xpath('//*[@id="pstad-descrptn"]').send_keys(description)
    pyautogui.press("pagedown")
    time.sleep(shortSleep)

    # Select images
    browser.find_element_by_xpath('//*[@id="ImageUploadButton"]').click()
    time.sleep(longSleep)

    # Create the file string and enter it into the image selection window
    # Allow files to be uploaded
    # I think really slow internet could mess this part up, so we will give it some generous load time (5 seconds)
    # Need to replace \\ with / for some reason, mac vs windows inconsistencies are getting annoying
    images = getAdImagePaths(directory)
    files = ""
    for imagePath in images:
        files += '"' + imagePath.replace("//", "\\") + '" '

    time.sleep(longSleep)
    pyautogui.typewrite(files)
    time.sleep(shortSleep)
    pyautogui.press('enter')
    time.sleep(longSleep)
    pyautogui.press("pagedown")

    # Allow lots of time for pictures to upload, maybe like 10 seconds?
    time.sleep(10)

    # Enter postal code (also hard coded)
    # This only needs to be done once (ever?) so we can just use a try/except
    try:
        browser.find_element_by_xpath('//*[@id="location"]').send_keys(postalCode)
        time.sleep(longSleep)
        pyautogui.press("down")
        pyautogui.press("enter")
        pyautogui.press("tab")
    except:
        # Basically, skip this location part because it is already there
        pass
    pyautogui.press("pagedown")
    time.sleep(shortSleep)

    # Enter price and phone number (hard coded)
    browser.find_element_by_xpath('//*[@id="PriceAmount"]').send_keys(price.replace("$", "").replace(",", ""))
    browser.find_element_by_xpath('//*[@id="PhoneNumber"]').send_keys(phone)
    pyautogui.press("tab")
    pyautogui.press("pagedown")
    time.sleep(shortSleep)

    # Post Ad
    # Strange, it seems the full xpath only seems to work some of the time
    # It is *rarely* different when I get the path from the inspector
    # We will try this shortened path instead
    # browser.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/form/div/div[9]/button[1]').click()
    browser.find_element_by_xpath('//*[@id="MainForm"]/div[9]/button[1]').click()
    time.sleep(longSleep)



def main():

    # So because kijiji limits free accounts to 10 ads each, we must cycle through properly
    # Do this later
    credentials = getCredentials()

    # Get the ads
    ads = getAds()

    # We want to post 10 ads per account
    # Just increment and login to the new account every 10 ads
    counter = 0
    for creds in credentials:
        browser = login(creds)
        for i in range(10):
            try:
                ad = ads[counter]
            except:
                # No more ads to post
                # Program exits
                print("All ads posted")
                exit()

            postAd(browser, ad)
            counter += 1
        # Close the browser and start again with the new account
        # Could also just logout and login with the new account but not a big deal here
        browser.close()


main()
