
from selenium import webdriver
from time import sleep

# setting the browser
browser = webdriver.Chrome()

# give the username password and 2fa here inside "******" 
username ="TN4237"
password = "Hrithik.krishna.1997"
password2 = "223611"

# load the zerodha kite login page
browser.get("https://kite.zerodha.com/?next=%2Fmargins#loggedout")
sleep(3)
# enter the username
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/input')\
    .send_keys(username)
sleep(3)
# enter the password
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/input')\
    .send_keys(password)
sleep(3)
# click the login
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button')\
    .click()
sleep(3)

# enter the 2fa
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/div/input')\
    .send_keys(password2)
sleep(2)
# click login
browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/button')\
    .click()

browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/div[2]/a/div/img')\
        .click()
sleep(2)




        
       





