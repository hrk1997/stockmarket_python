import requests
from bs4 import BeautifulSoup

# bitcoinprice
url = 'https://in.finance.yahoo.com/quote/BTC-INR?p=BTC-INR'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
bitcoin = soup.find_all('div',{'class':'D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)'} )[0].find('span').text


#nifty
url = 'https://in.finance.yahoo.com/quote/%5ENSEI?p=^NSEI'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
nifty = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text



#bse
url = 'https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
bse = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text


#usd
url = 'https://in.finance.yahoo.com/quote/%5EBSESN?p=^BSESN'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
usd = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'} )[0].find('span').text
print('| USD/INR | NIFTY | BITCOIN | BSE')
print('                            ')
print('usd/inr  : ' + usd)
print('                            ')
print('nifty    : ' + nifty)
print('                            ')
print('bitcoin  : ' + bitcoin)
print('                            ')
print('bse      : ' + bse)
print('                            ')

