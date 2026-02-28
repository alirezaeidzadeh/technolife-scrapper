'''این فایل ورودی رو از کاربر میگیره و به سایت تکنولایف درخواست میده و 
فایل رو سرچ میکنه و بعد اطلاعات محصولات رو دریافت میکنه'''

import requests
from bs4 import BeautifulSoup
import time

def fetch_page(query):
    try:
        response = requests.get(f'https://www.technolife.com/product/list/search?keywords={query}')
        if response.status_code == 200:
            return response.text
        else:
            print('we could not open your link, try few minutes later.')
    except Exception as e:
        print('we could not open your link, try few minutes later.')
        print(e)




def parse_products(html):
    soup = BeautifulSoup(html, 'html.parser')
    products_info = {
        'name':[],
        'price':[],
        'link':[]
    }
    
    cards = soup.find_all('div', class_='px-4 pt-6')
    
    for i, card in enumerate(cards[:10]):
        name = card.find('h2', class_='yekanbakh-en line-clamp-3 h-[75px] overflow-hidden text-sm font-medium leading-6.5 -tracking-0.5 text-gray-800')
        price_div = card.find_next_sibling('div', class_='pt-6')
        price = price_div.find('p', class_='text-[22px] font-semiBold leading-5 text-gray-800') if price_div else None
        
        if name and price:
            products_info['name'].append(name.text.strip())
            products_info['price'].append(price.text.strip())
            products_info['link'].append('https://www.technolife.com' + name.parent['href'])
           
    
    return products_info


