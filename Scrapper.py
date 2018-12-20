import time
from selenium import webdriver
import io
import re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chardet

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(executable_path=r"C:\Users\Momo\Anaconda3\envs\Python\Scripts\chromedriver.exe",desired_capabilities=d)
driver.maximize_window()
driver.get("https://www.gobodyguard.fr/try")
file = open('data.txt', 'a')
x=0

while x<3:

    element = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]')
    element.click()
    time.sleep(1)

    te = driver.find_element_by_xpath('//*[@id="textarea"]')



    json = driver.get_log('browser')

    text = str(json[0])
    print(type(text))
    bin = str.encode(text)
    print(type(bin))
    the_encoding = chardet.detect(bin)['encoding']
    print(the_encoding)
    result = bin.decode('unicode-escape').encode('utf-8')
    print(te.text)
    ''' 
    
    
    
    text = text.split('text', 1)[-1]
    text = text[7:]
    text = text.partition("insult")[0]
    text = text[:-7]
    text = text.replace(',', ' ')
    #text.decode('unicode-escape')
    result = str(json[1])
    result = result.split('type', 1)[-1]
    result = result[7:]
    result = result.partition("type_int")[0]
    result = result[:-7]

    

    file.write(text)
    file.write(',')
    file.write(result)
    file.write('\n')
    '''


    driver.get_log('browser').clear()
    x+=1


#driver.close()

