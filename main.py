'''این فایل برای هماهنگی سایر فایل ها و ماژول ها ساخته و
 قسمت های مختلف پروژ] رو به هم وضل میکند.'''

from scrapper import fetch_page , parse_products
from csv_exporter import save_csv

def main(product):
    try:
        save_csv(product,parse_products(fetch_page(product)))
        print('file has created')
    except Exception as e:
        print(e)


product = input('enter what you want : ')
main(product)
