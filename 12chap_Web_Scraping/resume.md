# Cap 12 - Web Scraping

**webbrowser** Comes with Python and opens a browser to a specific page.

**requests** Downloads files and web pages from the internet.

**bs4** Parses(extract) HTML, the format that web pages are written in.

**selenium** Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.

## WEBBROWSER

import webbrowser
webbrowser.open('https://')

## REQUESTS
import requests
res = requests.get('https://'), download the file
res.status_code == requests.codes.ok # check if went fine
res.text()
res.raise_for_status() # this will raise an exception if there was an error downloading the file and will do nothing if the download succeeded

* ### saving downloaded files to the hard drive
	*opens files in binary*
	for chunk in res.iter_content(100000):
        file.write(chunk)

## BS4
soup = bs4.BeautifulSoup(res.text, 'html.parser'),
Selector passed to the select() method
Will match . . .

soup.select('div')
All elements named <div>

soup.select('#author')
The element with an id attribute of author

soup.select('.notice')
All elements that use a CSS class attribute named notice

soup.select('div span')
All elements named <span> that are within an element named <div>

soup.select('div > span')
All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')
All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]')
All elements named <input> that have an attribute named type with value button

.getText() # returns the element's text, or inner HTML
.attrs # returns a dictionary with the element's attribute 
str() # returns a string with the starting and closing tags and the element's text
.get() # method for Tag objects makes it simple to access attribute values from an elemnt

## SELENIUM
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://')

Selenium’s WebDriver Methods for Finding Elements
Method name
WebElement object/list returned


browser.find_element_by_class_name(name)
browser.find_elements_by_class_name(name)
Elements that use the CSS
class name

browser.find_element_by_css_selector(selector)
browser.find_elements_by_css_selector(selector)
Elements that match the CSS
selector

browser.find_element_by_id(id)
browser.find_elements_by_id(id)
Elements with a matching id
attribute value

browser.find_element_by_link_text(text)
browser.find_elements_by_link_text(text)
<a> elements that completely
match the text provided

browser.find_element_by_partial_link_text(text)
browser.find_elements_by_partial_link_text(text)
<a> elements that contain the
text provided

browser.find_element_by_name(name)
browser.find_elements_by_name(name)
Elements with a matching name
attribute value

browser.find_element_by_tag_name(name)
browser.find_elements_by_tag_name(name)
Elements with a matching tag name
(case-insensitive; an <a> element is
matched by 'a' and 'A')

Table 12-4: WebElement Attributes and Methods

Attribute or method
Description

tag_name
The tag name, such as 'a' for an <a> element

get_attribute(name)
The value for the element’s name attribute

text
The text within the element, such as 'hello' in <span>hello </span>

clear()
For text field or text area elements, clears the text typed into it

is_displayed()
Returns True if the element is visible; otherwise returns False

is_enabled()
For input elements, returns True if the element is enabled; otherwise returns False

is_selected()
For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

location
A dictionary with keys 'x' and 'y' for the position of the element in the page

linkElem.click() # follows a link
userElem.send_keys('your_real_username_here') # sends keystrockes to texts fields
passwordElem.submit()

Table 12-5: Commonly Used Variables in the selenium.webdriver.common.keys Module

Attributes
Meanings

Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT
The keyboard arrow keys

Keys.ENTER, Keys.RETURN
The ENTER and RETURN keys

Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP
The HOME, END, PAGEDOWN, and PAGEUP keys

Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE
The ESC, BACKSPACE, and DELETE keys

Keys.F1, Keys.F2, . . . , Keys.F12
The F1 to F12 keys at the top of the keyboard

Keys.TAB
The TAB key

browser.back() Clicks the Back button.
browser.forward() Clicks the Forward button.
browser.refresh() Clicks the Refresh/Reload button.
browser.quit() Clicks the Close Window button.
