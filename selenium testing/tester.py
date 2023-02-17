from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from Selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:/Users/VINUBALAN/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
print("sample test1 case started")
driver.get("http://127.0.0.1:8000/")
driver.find_element_by_name('designationQuery').send_keys("computer vision engineer")
driver.find_element_by_name('searchQuery').send_keys("machine learning,python,opencv,html,css")
driver.find_element_by_name('searchLocation').send_keys("chennai")
driver.find_element_by_xpath('//*[@id="manual-input"]/div[4]/div[3]/button').send_keys(Keys.ENTER)

try:
    print("Search Completed")
    driver.find_element_by_xpath('/html/body/div/div[4]/a/button').click()
except:
    print("Search unsucessfull")
# driver.find_element_by_name('experience').send_keys("chennai")
# time.sleep(3)
# driver.find_element_by_xpath('/html/body/div[1]/form[1]/div[1]/div[2]/div[2]/input').send_keys("machine learning,python,opencv,html,css")
driver.find_element_by_xpath('/html/body/div/form/input[2]').send_keys('LAZZY PRO')
driver.find_element_by_xpath('/html/body/div/form/textarea').send_keys('You have been selected for next round.')
driver.find_element_by_xpath('/html/body/div/form/button').click()
try:
    driver.find_element_by_xpath('//*[@id="navbarNav"]/ul/li[1]').click()
    print("mail sent")
except:
    print("Mail not sent")

# time.sleep(3)
driver.close()
print("test1 completed")



# driver.close()