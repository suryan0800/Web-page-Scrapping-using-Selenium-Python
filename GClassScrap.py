# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:36:50 2021

@author: suryan0800
"""

from selenium import webdriver
import time
import pickle
import os 
os.chdir('/home/suryan0800/Lab/Python')

#Constants that you need to set to run this program properly
DRIVER_LOCATION = r'/home/suryan0800/suryan/driver/chromedriver'

CLASSROOM_LINK = 'https://classroom.google.com/u/0/w/Mjc1MTA4OTEyODI3/t/all'
USERNAME = 'yourReg@sastra.ac.in'
PASSWD = 'yourpassword'

#No need to set. Let the value be existing
COOKIES_PICKLE = "loginCookies.pkl"

#File extenstiosn that you liked to download and the download location
FILE_EXTENSIONS = ['.pptx','.doc','.ppt','docx','.rtf']
FILE_SAVE_LOCATION = '/home/suryan0800/Downloads/Files'


try:
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.headless = True
    prefs = {'download.default_directory' : FILE_SAVE_LOCATION}
    chrome_options.add_experimental_option('prefs', prefs)
    
    browser = webdriver.Chrome(options=chrome_options,executable_path = DRIVER_LOCATION)


    
    
    if os.path.exists(COOKIES_PICKLE):
        browser.get('https://www.google.com')
        fl1 = open(COOKIES_PICKLE, "rb")
        cookies = pickle.load(fl1)
        
        for cookie in cookies:
            browser.add_cookie(cookie)
    
        time.sleep(10)
        browser.get(CLASSROOM_LINK)
    else:
    
        browser.get(CLASSROOM_LINK)
        print(browser.page_source)
        
        
        time.sleep(15)
        lst = browser.find_elements_by_xpath("//input[(@type = 'email')]")
        lst[0].send_keys(USERNAME)
        
        lst = browser.find_elements_by_tag_name("button")
        for but in lst:
            if but.text == "Next":
                but.click()
                break
                
        time.sleep(15)
        lst = browser.find_elements_by_xpath("//input[(@type = 'password')]")
        lst[0].send_keys(PASSWD)
        
        lst = browser.find_elements_by_tag_name("button")
        for but in lst:
            if but.text == "Next":
                but.click()
                break
                
        time.sleep(30)
        pickle.dump( browser.get_cookies() , open(COOKIES_PICKLE,"wb"))
            
    
    time.sleep(30)
    lst = browser.find_elements_by_class_name("xVnXCf")
    print("List of folders in the classroom that will be searched for: ")
    print([ele.text for ele in lst])
    
    lst3 = set()
    for val1 in lst:
        val1.click()
        time.sleep(10)
        
    lst2 = browser.find_elements_by_tag_name("a")
    #print([ele.get_attribute('title') for ele in lst2])
    
    print("List of files that are to be downloaded to " + FILE_SAVE_LOCATION)
    for doc in lst2:
        title1 = (doc.get_attribute('title'))  
        if any(ext in title1 for ext in FILE_EXTENSIONS) and not (os.path.exists(FILE_SAVE_LOCATION + '/' + title1)):
            print(title1)
            href1 = (doc.get_attribute('href'))
            lst3.add(href1)
                
             
    print("Set of Links to be contacted to download files that doesn't already exist in the " + FILE_SAVE_LOCATION)
    print(lst3)
    
    for val in lst3:
        
        href1 = val 
        browser.get(href1)
        time.sleep(15)
        #print(browser.page_source)
        currentURL = browser.current_url;
        start_ind = (currentURL.find('d/')) + 2 
        end_ind = (currentURL.find('/view'))
        print(currentURL[32:65])
        downloadhref = "https://drive.google.com/u/0/uc?id={}&export=download".format(currentURL[start_ind:end_ind])
        browser.get(downloadhref)
        time.sleep(5)
        
        #doc.click()

finally:
    try:
        browser.close()
    except:
        print("An Exception/Error occurred")
    
    