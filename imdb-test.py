from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions
import time

option = ChromeOptions()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notifications")

 
PATH = Service(r'C:\Program Files\chromedriver.exe')
driver = webdriver.Chrome(service=PATH)

url_imdb = "https://www.imdb.com/"
url_google = "https://www.google.com/"

driver.get(url_imdb)
print(driver.title)


'''
search = "dolar"
searchKeyInput = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(search)
searchKeyInputClick = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
'''

menu = driver.find_element_by_xpath('//*[@id="imdbHeader-navDrawerOpen--desktop"]/div').click()
time.sleep(5)
top250 = driver.find_element_by_xpath('//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[3]/span').click()
time.sleep(5)

rank = "rank alinamadi"
#rank =driver.find_element_by_xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/text()').text
#name = driver.find_elements_by_xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a').text
#rating = driver.find_elements_by_xpath('//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[3]').text

print(rank)
#print(name)
#print(rating)


time.sleep(15)
driver.quit()