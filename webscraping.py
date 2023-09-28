from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

# #Extract Text from any web pages.
# entry_url = input("Enter Your URL : ")
def Extract_text_From_Url(entry_url):
    #driver = webdriver.Chrome()
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(entry_url)
    except:
        print(f"Couldn't open {entry_url}")
    time.sleep(1)
    driver.maximize_window()
    text = driver.find_element(By.XPATH, "/html/body").text
    all_text = text.replace("\n"," ")
    # #print(all_text)
    driver.quit()

    return all_text