from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.chrome(executable_path="/Users/talhaDocs/Downloads/chromedriver")

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")
sleep(3)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys("email here")
driver.find_element_by_xpath('//*[@id="identifierNext]').click()
sleep(3)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("password here")
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(3)
for i in range(20):
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    sleep(3)
    driver.find_element_by_class_name("vO").send_keys("recipient here")
    driver.find_element_by_class_name("aoT").send_keys("subject here")
    driver.find_element_by_css_selector("div[aroa-label='Message body']").send_keys("la la land")
    driver.find_element_by_xpath("//div[text()='Send']").click()
    sleep(3)