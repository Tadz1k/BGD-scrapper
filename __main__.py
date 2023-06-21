import os
import threading
import time

def run_flask():
    os.system('flask run --reload')

def fetch_offers():
    print("Fetching offers")
    time.sleep(5)
    print("Offers fetched")

def main():
    try:
        t1 = threading.Thread(target=run_flask, args=()).start()
        t2 = threading.Thread(target=fetch_offers, args=()).start()
    except:
        print("Error: unable to start thread")



if __name__ == '__main__':
    print("Starting app")
    main()