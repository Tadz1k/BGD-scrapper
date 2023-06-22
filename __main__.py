import os
import threading
import time
from scrapper import *
from mongo_utils import *


def fetch_otomoto():
    iterator = 0
    print("Fetching OTOMOTO...")
    offers = get_otomoto_offers()
    print("Inserting to database... OTOMOTO")
    for offer in offers:
        url = 'https://www.otomoto.pl' + offer
        
        # Insert to database
        try:
            details = get_otomoto_offer_details(url)
            iterator += insert('otomoto', details)
        except:
            pass
    print(f"Inserted {iterator} offers to [otomoto] database")

def fetch_olx():
    iterator = 0
    print("Fetching OLX...")
    offers = get_olx_offers()
    print("Inserting to database... OLX")
    for offer in offers:
        url = 'https://www.olx.pl' + offer

        # Insert to database
        try:
            details = get_olx_offer_details(url)
            iterator += insert('olx', details)
        except:
            pass   
    print(f"Inserted {iterator} offers to [olx] database")

def main():
    try:
        t1 = threading.Thread(target=fetch_olx, args=()).start()
        t2 = threading.Thread(target=fetch_otomoto, args=()).start()
    except:
        print("Error: unable to start thread")



if __name__ == '__main__':
    print("Starting threads...")
    main()