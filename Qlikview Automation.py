import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib
import datetime
import requests
import shutil
import os
import glob
driver = webdriver.Chrome(executable_path=r"C:\QlikView\Synseal\Published\Freshdesk\Python Script\chromedriver.exe")
time.sleep(2)
driver.get("https://k2conservatories.freshdesk.com/support/login")
username = driver.find_element_by_id("user_session_email").send_keys("conv_freshworks@convergytics.net")
password = driver.find_element_by_id("user_session_password")
password.send_keys("#Converge1")
driver.find_element_by_class_name("btn-login").click()
time.sleep(2)
driver.get("https://helpdesk.synseal.com/reports/scheduled_exports/9023471511453598/download_file")
time.sleep(15)
username = driver.find_element_by_id("user_session_email")
password = driver.find_element_by_id("user_session_password")
username.send_keys("conv_freshworks@convergytics.net")
password.send_keys("#Converge1")
time.sleep(5)
driver.find_element_by_class_name("btn-login").click()
time.sleep(8)
dest1 = r'C:\QlikView\Synseal\Published\Freshdesk\Data\Raw Data'
time.sleep(15)
for file in glob.glob(r'C:\Users\administrator.SYNSEAL\Downloads\tickets-hourly*'):
    shutil.copy(file, dest1)
    print file
    try:
        os.remove(dest1+os.path.basename(file))
    except WindowsError:
        print "Cannot find file specified."
driver.close()
