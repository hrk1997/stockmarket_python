import requests
from bs4 import BeautifulSoup

# INR/USD
url = 'https://in.finance.yahoo.com/quote/INR=X?p=INR=X'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
usd = soup.find_all('div',{'class':'D(ib) Mend(20px)'} )[0].find('span').text


#INR/EURO
url = 'https://in.finance.yahoo.com/quote/EURINR%3DX?p=EURINR%3DX'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
euro = soup.find_all('div',{'class':'D(ib) Mend(20px)'} )[0].find('span').text

#INR/JPY
url = 'https://in.finance.yahoo.com/quote/INRJPY%3DX?p=INRJPY%3DX'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
jpy = soup.find_all('div',{'class':'D(ib) Mend(20px)'} )[0].find('span').text


#INR/AED
url = 'https://in.finance.yahoo.com/quote/AEDINR%3DX?p=AEDINR%3DX'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
aed = soup.find_all('div',{'class':'D(ib) Mend(20px)'} )[0].find('span').text

#INR/GBP
url = 'https://in.finance.yahoo.com/quote/GBPINR%3DX?p=GBPINR%3DX'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
gbp = soup.find_all('div',{'class':'D(ib) Mend(20px)'} )[0].find('span').text

#INR/SGD
url = 'https://in.finance.yahoo.com/quote/SGDINR%3DX?p=SGDINR%3DX'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
sgd = soup.find_all('div',{'class':'D(ib) Mend(20px)'} )[0].find('span').text

print('                                                            ')
print('| USD/INR | EURO/INR | JPY/INR | AED/INR | GBP/INR | SGD/INR')
print('                            ')
print('EURO                          : INR/USD  : ' + usd)
print('                            ')
print('United States Dollar          : INR/EURO : ' + euro)
print('                            ')
print('United Arab Emirates Dirham   : INR/AED  : ' + aed)
print('                            ')
print('JAPAN                         : INR/JPY  : ' + jpy)
print('                            ')
print('POUND STERLING                : INR/GBP  : ' + gbp)
print('                            ')
print('SINGAPORE DOLLAR              : INR/SGD  : ' + sgd)
print('                            ')


