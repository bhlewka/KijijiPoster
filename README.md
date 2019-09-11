# KijijiPoster
Automated kijiji ad poster using selenium

### Requirements
- Latest release of Python3
- Selenium3 for Python
- Pyautogui
- Geckodriver (by Mozilla, found [here](https://github.com/mozilla/geckodriver/releases))
- Ublock origin for firefox (specifically the .xpi file, found [here](https://addons.mozilla.org/en-CA/firefox/addon/ublock-origin/))
- Mozilla Firefox
### Instructions
1. Make sure the geckodriver.exe and uBlock0@raymondhill.net.xpi, login.txt, and ads directory are in the same directory as kijiji.py
    ```
    Documents\KijijiProgram\kijiji.py
    Documents\KijijiProgram\geckodriver.exe
    Documents\KijijiProgram\uBlock0@raymondhill.net.xpi
    Documents\KijijiProgram\ads\couch\...
    Documents\KijijiProgram\ads\chair\...
    ```
2. login.txt should an email and a password on a single line, separated by a comma **followed by a space**
    ```
    username@email.com, password123
    ```
    - If you would like for multiple accounts to post the same ads simply add more login details on separate lines
    ```
    username@email.com, password123
    person@email.com, livinglife
    toronto@email.com, mapleleafs
    ```

2. Make sure each ad contains an Ad.txt and at least one image

    ```
    Documents\KijijiProgram\ads\chair\Ad.txt
    Documents\KijijiProgram\ads\chair\chairPicture.jpg
    ```
3. Make sure Ad.txt is properly formatted
    - The first line should be the item name
    - The second line should be the category
        - Refer to the category ID's here (sorted alphabetically)
            ```
            246 = Beds and Mattressses            
            249 = Bookcases & Shelving Units
            245 = Chairs and Recliners          
            241 = Coffee Tables                  
            238 = Couches and Futons             
            239 = Desks                          
            243 = Dining Tables & Sets           
            247 = Dressers and Wardrobes          
            250 = Hutches & Display Cabinets
            237 = Multi-Item                     
            236 = Other                         
            244 = Other Tables                    
            242 = TV Tables & Entertainment Units
            ```
    - The third line should be the item price
    - Everything else should be the item description
    ```
    Climbing Shoes
    245
    $100
    Never worn, in the packaging
    Size 42, excellent for slab problems
    If interested call or text 123-456-7890
    ```
5. Edit kijiji.py (on 18th line) and add in your postal code and phone number
    ```
    # Other hardcoded variables
    postalCode = "G1F 4G2"
    phone = "1234567890"
    ```
    
4. Run kijiji.py from a power shell terminal
    - Let your computer sit by itself for around 30 seconds per ad
    - Because the program uses your mouse and keyboard, you cannot use your computer while it runs
    - You will know it is finished when it stops for longer than 10 seconds (When the last ad from the ads folder is posted)
    - Or when the terminal closes
    - You'll figure it out, its not like it does anything cool like shoot fireworks

### Future Improvements
- Script to run both programs
- ~~More robust Ad.txt (or a spreadsheet) for extra information, such as the ad category~~
- ~~Scroll into view using selenium, instead of hardcoding page down~~
    - Turns out you don't need to scroll things into view with in order for them to be clickable
    *however* I think the extra "human" inputs help circumvent the spam filter?
- Bypass the file upload window
    - Supposedly this is easy to do, but I cant seem to get it working yet
- ~~Install extensions on firefox to block ads, making things run way faster~~
    - This was an incredible idea, sometimes selenium would timeout because some of the ads took
    way too long to load
- Would definitely be cleaner to create an ad object that just gets created and passed in to the postAd function each
time it is called I think

### Notes
- Could probably make a script that runs both of these in sequence just by being clicked on,
rather than expecting people to use the command line themselves
- A template for ads that is compatible with both programs would help, as well as provide us more date
to work from without hardcoding
- This inconsistency with the slashes is getting annoying, how can we fix this?
- Try to get os.cwd working on the work mac as well, just will take a few minutes of figuring out I'm sure
- We should go back to marketplace and try to use sendkeys instead of pyautogui as much
as we can
    - We should also be able to use the javascript xpath instead of all the tabbing
    - You just need to let the javascript elements load I think
- Kijiji has a complicated category selection, so there are a few ways we can battle it
    - Each item category has a unique id, so we could skip this first ad page and go straight
    to the next one, assuming we use a URL with the correct category
    - For now we will just use "Other", https://www.kijiji.ca/p-admarkt-post-ad.html?categoryId=236&adTitle=
- Kijiji actually uses ID's on lots of things so we might be able to use those instead of xpath every time, but doesnt
seem like a big deal right now
- In the future could delete all current ads first before listing new ones
