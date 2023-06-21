from scrapper import *

#Load OLX data
olx_offers = get_olx_offers()
olx_iterator = 0
for url in olx_offers:
    offer_data = get_olx_offer_details(url)
    #Save to DB
    olx_iterator += 1

#Load Otomoto data
otomoto_offers = get_otomoto_offers()
otomoto_iterator = 0
for url in otomoto_offers:
    offer_data = get_otomoto_offer_details(url)
    #Save to DB
    otomoto_iterator += 1

print(f'Done. Loaded {olx_iterator} offers from OLX and {otomoto_iterator} offers from Otomoto.')