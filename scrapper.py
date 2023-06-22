
import requests
from bs4 import BeautifulSoup
import re
from utils import clean_tags

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

olx_url = 'https://www.olx.pl/motoryzacja/samochody'
olx_pagination = '?page='
olx_start = 'olx.pl'

otomoto_url = 'https://www.otomoto.pl/osobowe'
otomoto_pagination = '?page='
otomoto_start = 'otomoto.pl'

def get_olx_offers():
    #Get main page
    main_page = requests.get(olx_url).text
    soup = BeautifulSoup(main_page, "html.parser")
    #Regex find
    total_pages = re.findall(r'totalPages\\":\d*', main_page)
    total_pages = int(total_pages[0].replace('totalPages\\":', ''))
    page_addresses = []
    #Iterate over all pages 
    for page in range(1, total_pages+1):
        url = olx_url + olx_pagination + str(page)
        page = requests.get(url, headers=headers).text
        #Bs4 find all a href
        soup = BeautifulSoup(page, "html.parser")
        all_link = soup.find_all('a', href=True)
        #Regex find all links
        for link in all_link:
            address = re.findall(r'\"/d/oferta\/.*\.html', str(link))
            if address:
                address = address[0].replace('"', '')
                if address not in page_addresses:
                    page_addresses.append(address)
    return page_addresses

def get_olx_offer_details(url):
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page, "html.parser")
    #Get data from HTML
    #Title - h1_title
    h1_title = soup.find('h1')
    h3_price = soup.find('h3')
    p_data = soup.find_all('p')
    city = re.findall(r'\"cityName\\":\\"[a-zA-Z ].*\",\\"cityId', page)
    city = city[0].replace('"cityName\\":\\"', '').replace('\\",\\"cityId', '')
    description = re.findall(r'description\\":\\"(.*)\\",\\"category\\":{', page)
    description = clean_tags(description[0])
    id = re.findall(r':{\\"id\\":([0-9]{1,12}),\\"title', page)
    manufacturer = re.findall(r'"/motoryzacja/samochody/([a-z A-Z]*)/"', page)
    #description = description[0].replace('\\"description\\":\\"', '').replace('\\",\\"category', '')
    offer_data = {'id': id[0], 'title': h1_title.text, 'description': description, 'manufacturer': manufacturer[0], 'model': '', 'fuel': '', 'engine': '', 'mileage': '',
                  'horsepower': '', 'gearbox': '', 'year': '', 'body': '', 'price': h3_price.text, 'city': city}
    for p in p_data:
        p_content = p.text
        if 'Model' in p_content:
            offer_data['model'] = p_content.replace('Model: ', '')
        if 'Paliwo' in p_content:
            offer_data['fuel'] = p_content.replace('Paliwo: ', '')
        if 'Typ nadwozia' in p_content:
            offer_data['body'] = p_content.replace('Typ nadwozia: ', '')
        if 'Poj. silnika:' in p_content:
            offer_data['engine'] = p_content.replace('Poj. silnika: ', '')
        if 'Rok produkcji' in p_content:
            offer_data['year'] = p_content.replace('Rok produkcji: ', '')
        if 'Moc silnika' in p_content:
            offer_data['horsepower'] = p_content.replace('Moc silnika: ', '')
        if 'Przebieg' in p_content:
            offer_data['mileage'] = p_content.replace('Przebieg: ', '')
        if 'Skrzynia biegów' in p_content:
            offer_data['gearbox'] = p_content.replace('Skrzynia biegów: ', '')
    return offer_data

        

def get_otomoto_offers():
    main_page = requests.get('https://www.otomoto.pl/osobowe?page=1').text
    max_pages = re.findall(r'\?page=([0-9]{3,6})', main_page)
    #max_pages = int(max_pages[0])
    max_pages = 2
    all_addresses = []
    for page in range(1, max_pages+1):
        page_url = otomoto_url + otomoto_pagination + str(page)
        page = requests.get(page_url, headers=headers).text
        soup = BeautifulSoup(page, "html.parser")
        all_link = soup.find_all('a', href=True)
        for link in all_link:
            address = re.findall(r'/osobowe/oferta/.*\.html"', str(link))
            if address:
                if address[0] not in all_addresses:
                    adr = address[0].replace('"', '')
                    all_addresses.append(adr)
    return all_addresses

def get_otomoto_offer_details(url):
    page = requests.get(url, headers=headers).text
    soup = BeautifulSoup(page, "html.parser")
    title = soup.find('h1').text
    title = title.replace('\n', '').replace('\t', '')
    price = soup.find('span', class_='offer-price__number').text
    price = price.replace('\n', '').replace('\t', '').replace(' ', '').replace('PLN', '')

    description = soup.find('div', class_='offer-description__description').text
    offer_id = re.findall(r'"ad_id":([0-9]{4,15}),"', page)
    
    city = soup.find('span', class_='seller-box__seller-address__label').text
    city = city.strip()

    parameters = soup.find_all('li', class_='offer-params__item')

    offer_data = {'id': offer_id[0], 'title': title, 'description': description, 'manufacturer': '', 'model': '', 'fuel': '', 'engine': '', 'mileage': '',
                  'horsepower': '', 'gearbox': '', 'year': '', 'body': '', 'price': price, 'city': city}

    for param in parameters:
        category = param.find('span', class_='offer-params__label').text
        value = param.find('div', class_='offer-params__value').text
        if 'Marka pojazdu' in category:
            offer_data['manufacturer'] = value.strip()
        if 'Model pojazdu' in category:
            offer_data['model'] = value.strip()
        if 'Pojemność skokowa' in category:
            offer_data['engine'] = value.strip()
        if 'Rok produkcji' in category:
            offer_data['year'] = value.strip()
        if 'Przebieg' in category:
            offer_data['mileage'] = value.strip()
        if 'Rodzaj paliwa' in category:
            offer_data['fuel'] = value.strip()
        if 'Skrzynia biegów' in category:
            offer_data['gearbox'] = value.strip()
        if 'Typ' in category:
            offer_data['body'] = value.strip()
        if 'Moc' in category:
            offer_data['horsepower'] = value.strip()

    return offer_data