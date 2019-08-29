# KijijiPoster
Automated kijiji ad poster using selenium

### Requirements
- Latest release of Python3
- Selenium for Python
- Pyautogui
- Geckodriver (by Mozilla, found [here](https://github.com/mozilla/geckodriver/releases))
- Mozilla Firefox
### Instructions
1. Make sure the geckodriver.exe, login.txt, and ads directory are in the same directory as kijiji.py
    ```
    Documents\KijijiProgram\kijiji.py
    Documents\KijijiProgram\geckodriver.exe
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
    - The second line should be the item price
    - Everything else should be the item description
    ```
    Climbing Shoes
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
