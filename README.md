
# Steam Account Gen and Editor

**If you like this repo, please consider giving it a star** ⭐️


The purpose of this program was solely to enhance skills in web automation, both for scraping and automated actions. There is much room for improvement in the code, but considering it was done in less than 1 hour, you can get a good idea of how automation works. Perhaps you can enhance it on your own, making it more efficient regardless of the situation in which you'll use it.

The code is heavily commented in Portuguese, my native language, but i can potentially update it to have all comments in English.

* This is a project with SOLELY EDUCATIONAL PURPOSES made in Python that creates a Steam account in the main.py file, requiring only the captcha solution to proceed. 
* The accounts generated with main.py are saved in contas.txt in the following format: **Username:Password >> email**. 
* The customize.py file then accesses each of the accounts, sets a random name, and changes the profile picture to one of the 4 recommended by Steam at the moment.

**Be aware of account creation abuse.**

If you use the code to generate many accounts in sequence, you will likely encounter a timeout, which will prevent you from creating more accounts.
Perhaps it would be interesting to enhance the code to use proxies, enabling a greater number of accounts to be generated before encountering the temporary block.



## Temp Email - Info

The email we're using for account creation is https://tuamaeaquelaursa.com, which generates a public email that can be revisited if it's necessary to retrieve the two-factor authentication code, without any hassle.

Feel free to modify the code and use it as you see fit. If you encounter any issues, please open an "issue," and we'll try to resolve it together!


## How to use

Just install all dependencies using:

```bash
  pip install -r requirements.txt
```
    
## Improvement

Surely, we could use **WebDriverWait** to wait for the appearance of the element instead of always using sleep(x), considering that we imported sleep from time.



```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define maximum waiting time in seconds
max_wait_time = 10

# Waits until the element with ID "my_element" is visible
element = WebDriverWait(driver, max_wait_time).until(
    EC.visibility_of_element_located((By.ID, "my_element"))
)

# Clicks on the element after it becomes visible
element.click()
```

Therefore, as I said, this code was made only for testing purposes in less than 1 hour and worked perfectly for the purpose for which I made it.

Feel free to add or remove whatever you want.
## External Dependencies

 - [Names by treyhunner](https://github.com/treyhunner/names) - Imported using: import names


## Thanks!

![MIT License](https://img.shields.io/badge/Leave%20a-STAR%E2%AD%90%EF%B8%8F-brightgreen?style=for-the-badge&logoColor=100%2C100%2C200&labelColor=255%2C255%2C255&color=100%2C100%2C200)
