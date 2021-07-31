from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://www.moneycontrol.com/india/stockpricequote/computers-software/wipro/W')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/finance-housing/housingdevelopmentfinancecorporation/HDF')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/icicibank/ICI02')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/kotakmahindrabank/KMB')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/personal-care/hindustanunilever/HU')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/axisbank/AB16')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/infrastructure-general/larsentoubro/LT')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/cigarettes/itc/ITC')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/bajajfinance/BAF')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/paintsvarnishes/asianpaints/AP31')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/bhartiairtel/BA08')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/computers-software/hcltechnologies/HCL02')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/auto-carsjeeps/marutisuzukiindia/MS24')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/steel-large/tatasteel/TIS')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")

browser.get('https://www.moneycontrol.com/india/stockpricequote/cement-major/ultratechcement/UTC01')
m_open = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.nseopn.bseopn')
m_preclose = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.nseprvclose.bseprvclose')
m_volume = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.nsevol.bsevol')
m_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.nsevalue.bsevalue')
m_vwap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.nsevwap.bsevwap')
m_high    = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(1) > td.nseHP.bseHP')
m_low     = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(2) > td.nseLP.bseLP')
m_uclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(3) > td.nseupper_circuit_limit.bseupper_circuit_limit')
m_lclimit = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(4) > td.nselower_circuit_limit.bselower_circuit_limit')
m_yrhigh  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(5) > td.nseH52.bseH52')
m_yrlow   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(2) > table > tbody > tr:nth-child(6) > td.nseL52.bseL52')
m_ttm_eps = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(1) > td.nseceps.bseceps')
m_ttm_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(2) > td.nsepe.bsepe')
m_sector_pe  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(3) > td.nsesc_ttm.bsesc_ttm')
m_book_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(4) > td.nsebv.bsebv')
m_p_b        = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(5) > td.nsepb.bsepb')
m_face_value = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.nsefv.bsefv')
m_market_cap = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(1) > td.nsemktcap.bsemktcap')
m_divident   = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(2) > td.nsedy.bsedy')
m_avgvoleume  = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(3) > td.nsev20a.bsev20a')
m_avgdelivery = browser.find_element_by_css_selector('#stk_overview > div.nsestock_overview.bsestock_overview > div.mob-hide > div:nth-child(4) > table > tbody > tr:nth-child(4) > td.nsed20ad.bsed20ad')
m_stock = browser.find_element_by_css_selector('#stockName > h1')

#= browser.find_element_by_css_selector('')
open         = m_open.text
preclose     = m_preclose.text
volume       = m_volume.text
value        = m_vwap.text
vwap         = m_vwap.text



stock        = m_stock.text
high         = m_high.text
low          = m_low.text
uclimit      = m_uclimit.text
lclimit      = m_lclimit.text
yrhigh       = m_yrhigh.text
yrlow        = m_yrlow.text
ttm_eps      = m_ttm_eps.text
ttm_pe       = m_ttm_pe.text
sector_pe    = m_sector_pe.text
bool_value   = m_book_value.text
pb           = m_p_b.text
face_value   = m_face_value.text
market_cap   = m_market_cap.text
divident     = m_divident.text
avg_voleme   = m_avgvoleume.text
avg_delivery = m_avgdelivery.text

print("                    ")
print("     ",stock,"     ")
print("open         : ",open)
print("preclose     : ",preclose)
print("volume       : ",volume)
print("vwap         : ",vwap)
print("high         : ",high)
print("low          : ",low)
print("uclimit      : ",uclimit)
print("lclimit      : ",lclimit)
print("yrhigh       : ",yrhigh)
print("yrlow        : ",yrlow)
print("ttm_eps      : ",ttm_eps)
print("ttm_pe       : ",ttm_pe)
print("sector_pe    : ",sector_pe)
print("bool_value   : ",bool_value)
print("pb           : ",pb)
print("face_value   : ",face_value)
print("market_cap   : ",market_cap)
print("divident     : ",divident)
print("avg_voleme   : ",avg_voleme)
print("avg_delivery : ",avg_delivery)
print("                    ")


browser.close()


