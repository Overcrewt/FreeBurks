from selenium import webdriver
from requests import *

userCode


driver = webdriver.Firefox("/home/overcrewt/geckodriver")
driver.get("https://mcdonalds.fast-insight.com/voc/ee/en")
input = driver.find_element_by_id('receiptCode')
button = driver.find_element_by_tag_name('button')
input.send_keys(userCode)
