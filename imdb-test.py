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

PATH = (r'C:\Program Files\chromedriver.exe')
driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)

url_imdb = "https://www.imdb.com/"

driver.get(url_imdb)
print(driver.title)
time.sleep(2)

rank = "rank alinamadi"
name = "name alinamadi"
rating = "rating alinamadi"
genre_name = "alinmadi"

# * Function for IMDb Top 250
def top250():
    menu = driver.find_element_by_xpath('//*[@id="imdbHeader-navDrawerOpen--desktop"]/div').click()
    time.sleep(2)
    top250 = driver.find_element_by_xpath('//*[@id="imdbHeader"]/div[2]/aside/div/div[2]/div/div[1]/span/div/div/ul/a[3]/span').click()
    time.sleep(2)

    for i in range(1,26):
        name = driver.find_elements_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr["+ str(i) +"]/td[2]/a")
        date = driver.find_elements_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr["+ str(i) +"]/td[2]/span")
        rate = driver.find_elements_by_xpath("//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr["+ str(i) +"]/td[3]")
        
        print(str(i)+ ". " + name[0].text + " " + date[0].text + " " + rate[0].text)
        #time.sleep(2)

top250()
print("*"*75)

def userChoice():
    print("-"*30)
    print("1- Action")
    print("2- Adventure")
    print("3- Animation")
    print("4- Biography")
    print("5- Comedy")
    print("6- Crime")
    print("7- Drama")
    print("8- Family")
    print("9- Fantasy")
    print("10- Film-Noir")
    print("11- History")
    print("12- Horror")
    print("13- Music")
    print("14- Musical")
    print("15- Mystery")
    print("16- Romance")
    print("17- Sci-Fi")
    print("18- Sport")
    print("19- Thriller")
    print("20- War")
    print("21- Western")
    print("-"*30)
    choice = input("Seçiminiz: ")
    print("-"*30)

    if choice == "1":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[1]/a").click()
    elif choice == "2":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[2]/a").click()
    elif choice == "3":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[3]/a").click()
    elif choice == "4":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[4]/a").click()
    elif choice == "5":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[5]/a").click()
    elif choice == "6":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[6]/a").click()
    elif choice == "7":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[7]/a").click()
    elif choice == "8":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[8]/a").click()
    elif choice == "9":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[9]/a").click()
    elif choice == "10":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[10]/a").click()
    elif choice == "11":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[11]/a").click()
    elif choice == "12":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[12]/a").click()
    elif choice == "13":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[13]/a").click()
    elif choice == "14":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[14]/a").click()
    elif choice == "15":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[15]/a").click()
    elif choice == "16":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[16]/a").click()
    elif choice == "17":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[17]/a").click()
    elif choice == "18":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[18]/a").click()
    elif choice == "19":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[19]/a").click()
    elif choice == "20":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[20]/a").click()
    elif choice == "21":
        genre_name = driver.find_element_by_xpath("//*[@id='sidebar']/div[5]/span/ul/li[21]/a").click()
    else:
        print("Yanlis secim yaptiniz.")
        userChoice()

    return genre_name


userChoice()

def genre():
    #_genre = genre_name.click()
    time.sleep(2)
    title = driver.find_element_by_xpath("//*[@id='main']/div/h1").text
    print(title)
    print("-"*75)

    for i in range(1,26):
        name = driver.find_element_by_xpath("//*[@id='main']/div/div[3]/div/div["+ str(i) +"]/div[3]/h3/a")
        date = driver.find_element_by_xpath("//*[@id='main']/div/div[3]/div/div["+ str(i) +"]/div[3]/h3/span[2]")
        rate = driver.find_element_by_xpath("//*[@id='main']/div/div[3]/div/div["+ str(i) +"]/div[3]/div/div[1]/strong")

        print(str(i)+ ". " + name.text + " " + date.text + " " + rate.text)
        #time.sleep(2)

    driver.back()
    time.sleep(3)

# ! genre bittikten sonra bir yazı ekle
# ? Top250 fonksiyonu çaılşmadan genre seçilebilir mi?
# TODO for döngüsü yap ve genre testi oluştur.
genre()

time.sleep(3)
driver.quit()
