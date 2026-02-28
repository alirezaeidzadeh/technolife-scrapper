'''این فایل خروجی فایل scrapper 
رو میگیره و بعد بر اساس اطلاعات دریافتی یک فایل csv
میسازه'''

import pandas as pd

def save_csv(file_name,products_info):
    df = pd.DataFrame(products_info)
    df.to_csv(f'C:/Users/RAD/Dropbox/دوره منتورینگ پایتون پیشرفته/2nd week/technolife scrapper/output/{file_name}.csv',encoding='utf-8-sig')