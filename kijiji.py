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

# This will get the username and password from a text file
# Supports multiple logins, line separated
# Returns list of username,password
def getCredentials():

    # Open/read the file
    file = open("login.txt")
    file = file.read().splitlines()
    creds = []
    for credentials in file:
        credentials = credentials.split(", ")
        creds.append([credentials[0], credentials[1]])
    return creds

# This will retrieve the relevant info for the ad posting
# Returns title, price, description
def getAdInformation(directory):

    title, price, description = open("ads/"+directory+"/Ad.txt").read().split("\n", 2)
    return title, price, description

# This will return the absolute path to all images
# Returns a list of absolute paths to images
def getAdImagePaths(directory):
    ads = os.getcwd() + "/ads/" + directory
    files = os.listdir(ads)

    # We will go through this list and remove the hidden files as well as Ad.txt
    # This will assume all remaining files are images so make sure they are!
    # Otherwise bad things might happen
    images = []
    for file in files:
        if file[0] != "." and file != "Ad.txt":
            images.append(ads + "/" + file)
    return images

# This retrieves the directory name of each ad
# Returns list of ad folder names
def getAds():
    ads = os.getcwd() + "/ads/"
    ads = os.listdir(ads)
    return ads

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

# This will post an ad to the kijiji marketplace
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
    images = getAdImagePaths(directory)

    files = ""
    for imagePath in images:
        files += '"' + imagePath + '" '

    time.sleep(longSleep)
    pyautogui.typewrite(files)
    time.sleep(shortSleep)
    pyautogui.press('enter')
    time.sleep(longSleep)

    # Enter postal code
    browser.find_element_by_xpath('//*[@id="location"]').send_keys("T5S 2R9")
    pyautogui.press("tab")
    pyautogui.press("pagedown")
    time.sleep(shortSleep)

    # Enter price
    browser.find_element_by_xpath('//*[@id="PriceAmount"]').send_keys(price)
    pyautogui.press("tab")
    pyautogui.press("pagedown")
    time.sleep(shortSleep)

    # Post Ad
    browser.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/form/div/div[9]/button[1]').click()
    pyautogui.press("tab")
    pyautogui.press("pagedown")
    time.sleep(shortSleep)



def main():

    # So because kijiji limits free accounts to 10 ads each, we must cycle through properly
    # Do this later
    credentials = getCredentials()

    # Get the ads
    ads = getAds()

    for creds in credentials:
        browser = login(creds)

        postAd(browser, ads[0])

main()