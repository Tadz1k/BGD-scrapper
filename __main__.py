import os
import threading
import time
from scrapper import *
from mongo_utils import *


def fetch_otomoto():
    print("Fetching OTOMOTO...")
    offers = get_otomoto_offers()
    print("Inserting to database... OTOMOTO")
    for offer in offers:
        url = 'https://www.otomoto.pl' + offer
        
        # Insert to database
        try:
            details = get_olx_offer_details(url)
            insert('otomoto', details)
        except:
            pass

def fetch_olx():
    print("Fetching OLX...")
    offers = get_olx_offers()
    print("Inserting to database... OLX")
    for offer in offers:
        url = 'https://www.olx.pl' + offer

        # Insert to database
        try:
            details = get_olx_offer_details(url)
            insert('olx', details)
        except:
            pass   


def main():
    try:
        t1 = threading.Thread(target=fetch_olx, args=()).start()
        t2 = threading.Thread(target=fetch_otomoto, args=()).start()
    except:
        print("Error: unable to start thread")



if __name__ == '__main__':
    print("Starting threads...")
    main()