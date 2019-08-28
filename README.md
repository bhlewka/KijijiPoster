# KijijiPoster
Automated kijiji ad poster using selenium

### Notes
- We should go back to marketplace and try to use sendkeys instead of pyautogui as much
as we can
- Kijiji has a complicated category selection, so there are a few ways we can battle it
    - Each item category has a unique id, so we could skip this first ad page and go straight
    to the next one, assuming we use a URL with the correct category
    - For now we will just use "Other", https://www.kijiji.ca/p-admarkt-post-ad.html?categoryId=236&adTitle=