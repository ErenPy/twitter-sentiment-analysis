import csv
import time
import requests as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def TweetParser(phrase) :
    list1 = []
    for elem in phrase:
        elem = str(elem)
        parsedElem = elem.split('>')
        result = []
        for element in parsedElem :
            if element:
                if element[0] != "<":
                    result.append(element)
        cont = []
        for phrase in result:
            if phrase :
                flag = False
                tweet = ''
                for letter in phrase:
                    if letter == '<':
                        flag = True
                    if letter == '>':
                        flag = False
                    if flag != True:
                        tweet += letter
            cont.append(tweet)
        while cont[-1].isnumeric():
            cont.pop(-1)
        
        if cont[-1] != "Promoted":
            tweet = ""
            cont.pop(2)
            if len(cont) > 3:
                for i in cont[3:]:
                    tweet += i
                cont[3] = tweet
            list1.append(cont[0:4])
    return list1
def Organizer(tweets):
    with open(f'tweets_2.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ',')
        spamwriter.writerows(TweetParser(tweets))
def scroll_down(self):
    """A method for scrolling the page."""
    scroll_pause_time = 2 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = browser.execute_script("return window.screen.height;")   # get the screen height of the web
    scroll_height = browser.execute_script("return document.body.scrollHeight;")  
    i = 2

    while True:
    # scroll one screen height each time
        browser.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        if (screen_height) * i > (scroll_height - 1000) :
            scroll_pause_time = 5
        else :
            scroll_pause_time = 1
        time.sleep(scroll_pause_time)
        element = browser.find_element_by_xpath("//*")
        html = browser.execute_script("return arguments[0].outerHTML;", element)
        soup = BeautifulSoup(html)
        tweets = soup.findAll('div',attrs={'data-testid':'tweet'})
        Organizer(tweets)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = browser.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break
        # Get scroll height.
        last_height = self.execute_script("return document.body.scrollHeight")
accounts_list = []
with open('Desktop/names.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        for elements in row: 
            accounts_list.append(elements)
browser = webdriver.Safari()
browser.maximize_window()
arr = 0
for element in accounts_list:
    wordToSearch = element
    URL = f'https://mobile.twitter.com/{wordToSearch}?p=s'
    browser.get(URL)
    time.sleep(2)
    scroll_down(browser)
