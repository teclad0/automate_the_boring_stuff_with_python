#! python3
# play2048.py - script that plays the game 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://play2048.co/')
game_over_elem = browser.find_element_by_class_name('game-message')
htmlElem = browser.find_element_by_tag_name('html')

while game_over_elem.text == '':
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
print('I\'m done! ')
