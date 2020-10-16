from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd



chromedriver_path = 'C:/Users/nsignia/Downloads/python selenium/chrome driver/chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)


webdriver.get('https://eu-gb.assistant.watson.cloud.ibm.com/eu-gb/crn:v1:bluemix:public:conversation:eu-gb:a~2Ff375ced0a4f14b7ab68628b884b575d6:e7d67249-e064-46e1-9af3-0ef538a542d5::/skills/21eac87c-61ef-4925-817e-a39f9c0da1b8/build/intents#intent=COVID_Transmission')
sleep(75)

file = pd.read_excel("ibm_data.xlsx")
stringdata = file["data"].tolist()
for i in stringdata:
    data = webdriver.find_element_by_xpath('//*[@id="intent_new_example"]')
    data.send_keys(i)

    button = webdriver.find_element_by_xpath('//*[@id="submit-add-value"]')
    button.click()
    sleep(5)