import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import openpyxl
import csv

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("window_size=1280,800")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-save-password-bubble")
options.add_argument("--lang=en")



driver = webdriver.Chrome(options=options)
email = 'technologie.komputerowe2022@gmail.com'
password = 'gogojojolala'
twitterlogin = 'popologodo45302'
profilelink = 'https://twitter.com/marc_louvion'

driver.get("https://twitter.com/")
time.sleep(10)
current_window = driver.current_window_handle
cookies_accept = driver.find_element(By.XPATH, '//span[contains(text(), "Accept all cookies")]').click()
con = driver.find_element(By.XPATH,'//span[contains(text(), "Sign in")]').click()
time.sleep(6)
providelogin = driver.find_element(By.XPATH, '//input').send_keys(email)
time.sleep(2)
gotothepassword = driver.find_element(By.XPATH, '//span[contains(text(), "Next")]').click()
time.sleep(5)

try:
    providepassword = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
except NoSuchElementException:
    provideusername = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(twitterlogin)
    time.sleep(3)
    proceednext = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span').click()
    time.sleep(2)
    providepasswordagain = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
    time.sleep(1)
    proceed = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
time.sleep(3)

try:
    finalloginbutton = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()
except NoSuchElementException:
    pass
time.sleep(10)

driver.get(profilelink)
time.sleep(7)

loopcounter = 0
listoftweets = []
seen_tweet_ids = set()
actions = ActionChains(driver)

previous_scroll_height = 0
scroll_attempts = 0
max_scroll_attempts = 10

while True:
    tweets = driver.find_elements(By.CSS_SELECTOR, 'div.css-175oi2r.r-1adg3ll.r-1ny4l3l')
    for tweet in tweets:
        try:
            tweet_id = tweet.find_element(By.CSS_SELECTOR, 'div.css-1rynq56.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim > span').text
            if tweet_id not in seen_tweet_ids:
                if tweet.find_element(By.CSS_SELECTOR, 'div.css-175oi2r.r-sdzlij.r-1udh08x.r-u8s1d.r-ggadg3.r-8jfcpp > a[href="/marc_louvion"]'):
                    seen_tweet_ids.add(tweet_id)
                    arialabel = tweet.find_element(By.CSS_SELECTOR, 'div.css-175oi2r.r-1kbdv8c.r-18u37iz.r-1wtj0ep.r-1ye8kvj.r-1s2bzr4').get_attribute('aria-label')
                    parts = arialabel.split(', ')
                    desc = tweet.find_element(By.CSS_SELECTOR, 'div.css-1rynq56.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim > span').text
                    publishedtime = tweet.find_element(By.CSS_SELECTOR, 'div.css-175oi2r.r-18u37iz.r-1q142lx > a > time').text
                    views = next((part for part in parts if 'view' in part), None)
                    bookmarks = next((part for part in parts if 'bookmark' in part), None)
                    likes = next((part for part in parts if 'like' in part), None)
                    reposts = next((part for part in parts if 'repost' in part), None)
                    replies = next((part for part in parts if 'repl' in part), None)
                    try:
                        tweeturl = tweet.find_element(By.CSS_SELECTOR, 'a.css-1rynq56').get_attribute('href')
                    except NoSuchElementException:
                        tweeturl = None
                        pass
                    try:
                        contenturl = tweet.find_element(By.CSS_SELECTOR, 'img.css-9pa8cd').get_attribute('src')
                    except NoSuchElementException:
                        contenturl = None
                        pass
                    dictoftweet = {
                        'publishedtime': f'{publishedtime}',
                        'desc': f'{desc}',
                        'likes': f'{likes}',
                        'reposts': f'{reposts}',
                        'views': f'{views}',
                        'replies': f'{replies}',
                        'bookmarks': f'{bookmarks}',
                        'tweeturl': f'{tweeturl}',
                        'contenturl': f'{contenturl}'
                    }
                    listoftweets.append(dictoftweet)
        except (IndexError, NoSuchElementException):
            pass


    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1.5)

    current_scroll_height = driver.execute_script("return document.body.scrollHeight")
    if current_scroll_height == previous_scroll_height:
        scroll_attempts += 1
        if scroll_attempts >= max_scroll_attempts:
            break
    else:
        scroll_attempts = 0
    previous_scroll_height = current_scroll_height
    print(len(listoftweets))


keys = listoftweets[0].keys()

with open('output.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(listoftweets)


with open('sodsf.txt', 'w', encoding='utf-8') as file:
    for tweet in listoftweets:
        file.write(str(tweet) + '\n')

with open('sodsf.txt', 'a') as file:
    file.write(str(len(listoftweets)))