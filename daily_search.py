import pyautogui
import time
import webbrowser
import requests
import random

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

url = 'https://www.bing.com/'

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
words = response.text.splitlines()

numOfSearches = int(input("Enter number of searches: "))

for i in range(numOfSearches + 1):
    f = open('Path to textfile for usedKeywords.txt', 'r')
    used = f.read().splitlines()
    new = Diff(words, used)
    search = random.choice(new)
    f = open('Path to textfile for usedKeywords.txt', 'a')
    f.write(search + "\n")
    f.close()
    webbrowser.open_new_tab(url)
    sleep = random.randint(3, 6)
    time.sleep(sleep)
    pyautogui.typewrite(search, interval = 0.01)
    pyautogui.typewrite('\n', interval = 0.1)
    pyautogui.hotkey('ctrl', 'w')
