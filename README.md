# KijijiPoster
Automated kijiji ad poster using selenium

### Notes
- Also this inconsistency with the slashes is getting annoying, how can we fix this?
- Try to get os.cwd working on the work mac as well, just will take a few minutes of figuring out I'm sure
- We should go back to marketplace and try to use sendkeys instead of pyautogui as much
as we can
- Kijiji has a complicated category selection, so there are a few ways we can battle it
    - Each item category has a unique id, so we could skip this first ad page and go straight
    to the next one, assuming we use a URL with the correct category
    - For now we will just use "Other", https://www.kijiji.ca/p-admarkt-post-ad.html?categoryId=236&adTitle=
- Kijiji actually uses ID's on lots of things so we might be able to use those instead of xpath every time