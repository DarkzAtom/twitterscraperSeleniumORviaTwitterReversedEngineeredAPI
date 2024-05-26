# Twitter account's posts scraper

Selenium Part

This scraper (main.py) is built using Selenium lib, Python. Scrapes all the tweets of the account until it reaches the rate limit (I don't remember the particular number of tweets it was scraping but the result was far better than via official API). Finally, the parsed data is stored in the .csv file name "output.csv"

Twitter's reversed-engineered part

The second, alternate scraper (reverseengineeredupdated.py), takes the API that Twitter uses to fetch the data to its UI. The navigation through items happens via the cursor pagination. It scrapes 1000 tweets/couple minutes, which is way faster than the Selenium version, but has higher chances of logged user in the session getting blocked in the abusive usage scenario (however mine's never broken though, this is what I've heard, that potentially could happen with using the RE API's). Finally, the parsed data is stored in the .csv "outputresp.csv"
