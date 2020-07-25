from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



DRIVER_PATH = "/home/suryan0800/suryan/Softwares/chromedriver"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
#i = 121015098
for i in range(121015000,121015125):
	try:
		driver.get("https://sas.sastra.edu/cbcsres20/index2.php")
		#print(driver.page_source)
		current_url = driver.current_url
		driver.find_element_by_id('regno').send_keys(str(i))
		inputs = driver.find_elements_by_tag_name('input')
		inputs[1].send_keys(driver.find_elements_by_tag_name('span')[0].text)
		#print(inputs[0].get_attribute('name'))
		#print(inputs[1].get_attribute('name'))
		#print(inputs[2].get_attribute('name'))
		inputs[2].click()
		#print(submit)
		#print(driver.find_element_by_id('regno').text)

		WebDriverWait(driver, 15).until(EC.url_changes(current_url))

		#print(driver.current_url)

		ulist = driver.find_elements_by_tag_name('li')
		ulist[1].click()
		WebDriverWait(driver, 15).until(EC.url_changes(current_url))
		#print(driver.current_url)
		ids = driver.find_elements_by_id("fmbox")
		print(ids[1].text, ids[3].text, ids[7].text, ids[9].text,sep = ", ")

		hrefs = driver.find_elements_by_id("fmbox")
		hrefs[4].click()
		#WebDriverWait(driver, 15).until(EC.url_changes(current_url))
		#print(driver.current_url)
	except:
		pass

driver.quit()

'''
import requests
import json
from bs4 import BeautifulSoup
payload = {"regno":"121015098",
			"captcha_code":"",
			"studentloginbutton":"&#xf2f6  Submit"}


with requests.Session() as s:
	print(s.__dict__['cookies'])
	res = s.get("https://sas.sastra.edu/cbcsres20/index2.php")
	print(s.__dict__['cookies'])
	signin = BeautifulSoup(res._content,"html.parser")

	payload["captcha_code"] = signin.find('span').text
	print(json.dumps(payload))
	res1 = s.post("https://sas.sastra.edu/cbcsres20/index2.php",data = "regno=121015098&captcha_code=L9T4M6&studentloginbutton=%EF%8B%B6++Submit")

	print(res1.text)


'''