#Python 3.9.2 (default, Feb 28 2021, 17:03:44)
#[GCC 10.2.1 20210110] on linux
#Type "help", "copyright", "credits" or "license()" for more information.

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.moneycontrol.com/indian-indices/nifty-50-9.html')

focus = browser.find_element_by_css_selector('#mc_mainWrapper > div > div.sec_indice_detail > div.indices_namntab.clearfix > h1 > div')
day_preclose = browser.find_element_by_css_selector('#sp_previousclose')
day_open = browser.find_element_by_css_selector('#sp_open')
day_high = browser.find_element_by_css_selector('#sp_High')
day_low = browser.find_element_by_css_selector('#sp_low')
day_yrhigh = browser.find_element_by_css_selector('#sp_yrhigh')
day_yrlow = browser.find_element_by_css_selector('#sp_yrlow')

name       = focus.text 
preclose   = day_preclose.text
day_open   = day_open.text
day_high   = day_high.text
day_low    = day_low.text
day_yrhigh = day_yrhigh.text
day_yrlow  = day_yrlow.text

print("nifty 50") 
print("previous close : ",preclose)
print("open price     : ",day_open)
print("day high       : ",day_high)
print("day low        : ",day_low)
print("year high      : ",day_yrhigh)
print("year low       : ",day_yrlow)



#sp_open
#sp_previousclose
#sp_High
#sp_yrhigh
#sp_yrlow

#indi_contribute > div.clearfix > div.contribut_bx.FL > table > tbody > tr:nth-child(1) > td:nth-child(1) > a
#day_low.text
#'15,737.80'
