from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook, load_workbook

url = 'https://www.otomoto.pl/osobowe/hyundai'

#Получаем веб-страницу
def request_html(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, "html.parser")



#Получаем ссылки на товары
raw_all = request_html(url)
links = raw_all.findAll('a',class_='offer-item__photo-link')
link_list = [link['href'] for link in links if link['href'][:30] == 'https://www.otomoto.pl/oferta/']
link_list_clear = []
for link in link_list:
    i = link.rfind('#')
    if i != -1:
        link = link[:i]
    link_list_clear.append(link)

# url2 = 'https://www.otomoto.pl/oferta/hyundai-ix35-2-0-crdi-salon-polska-serwis-aso-skora-navi-klimatronic-ID6EcQ4F.html'
products = []

def ret_product(url):
    raw_product = request_html(url)
    param_html = raw_product.findAll('span', class_='offer-main-params__item')
    product = []
    for text in param_html:
        t = text.text.replace(" ","")
        t = t.replace("\n","")
        if t not in product:
            product.append(t)

    # product = {
    #     'Год' : param_list[0],
    #     'Пробег' : param_list[1],
    #     'Топливо' : param_list[2],
    #     'Тип кузова' : param_list[3],
    # }
    price_html = raw_product.find('span', class_='offer-price__number')
    for text in price_html:
        t = text.text.replace(" ","")
        t = t.replace("\n","")
        try:
            if int(t):
                product.append(t)
                # product.update({'price':t})
        except ValueError:
            continue
    return product

for link in link_list_clear:
    product = ret_product(link)
    products.append(product)

# print(products)

# lista = [{'Год': '2005', 'Пробег': '191000km', 'Топливо': 'Diesel', 'Тип кузова': 'SUV', 'price': '13900'}, {'Год': '2011', 'Пробег': '220284km', 'Топливо': 'Diesel', 'Тип кузова': 'SUV', 'price': '37000'}, {'Год': '2012', 'Пробег': '159072km', 'Топливо': 'Diesel', 'Тип кузова': 'Minivan', 'price': '25000'}, {'Год': '2021', 'Пробег': '10km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '67990'}, {'Год': '2021', 'Пробег': '10km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '67990'}, {'Год': '2021', 'Пробег': '10km', 'Топливо': 'Benzyna', 'Тип кузова': 'SUV', 'price': '124900'}, {'Год': '2020', 'Пробег': '53786km', 'Топливо': 'Benzyna', 'Тип кузова': 'Kompakt', 'price': '67300'}, {'Год': '2012', 'Пробег': '31400km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '12000'}, {'Год': '2011', 'Пробег': '251000km', 'Топливо': 'Diesel', 'Тип кузова': 'SUV', 'price': '38900'}, {'Год': '2020', 'Пробег': '4727km', 'Топливо': 'Benzyna', 'Тип кузова': 'Kompakt', 'price': '59999'}, {'Год': '2017', 'Пробег': '68536km', 'Топливо': 'Benzyna', 'Тип кузова': 'Kompakt', 'price': '55900'}, {'Год': '2017', 'Пробег': '57633km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '31900'}, {'Год': '2011', 'Пробег': '184000km', 'Топливо': 'Benzyna+LPG', 'Тип кузова': 'SUV', 'price': '45900'}, {'Год': '2010', 'Пробег': '197525km', 'Топливо': 'Diesel', 'Тип кузова': 'SUV', 'price': '33500'}, {'Год': '2015', 'Пробег': '57428km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '40500'}, {'Год': '2012', 'Пробег': '51879km', 'Топливо': 'Benzyna', 'Тип кузова': 'Kompakt', 'price': '37900'}, {'Год': '2013', 'Пробег': '189000km', 'Топливо': 'Diesel', 'Тип кузова': 'Kompakt', 'price': '26990'}, {'Год': '2017', 'Пробег': '50221km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '39500'}, {'Год': '2019', 'Пробег': '26937km', 'Топливо': 'Diesel', 'Тип кузова': 'SUV', 'price': '65900'}, {'Год': '2014', 'Пробег': '94380km', 'Топливо': 'Benzyna', 'Тип кузова': 'SUV', 'price': '48900'}, {'Год': '2015', 'Пробег': '62000km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '34900'}, {'Год': '2017', 'Пробег': '83387km', 'Топливо': 'Benzyna', 'Тип кузова': 'Autamiejskie', 'price': '42900'}, {'Год': '2017', 'Пробег': '79713km', 'Топливо': 'Diesel', 'Тип кузова': 'SUV', 'price': '69900'}, {'Год': '2012', 'Пробег': '110000km', 'Топливо': 'Diesel', 'Тип кузова': 'Kombi', 'price': '21900'}]

wb = Workbook()
dest_filename = 'result.xlsx'
ws1 = wb.active
r = 1

ws1.append(['Год', 'Пробег', 'Топливо', 'Тип кузова', 'Цена'])
for t in products:
    ws1.append(t)



wb.save(filename = dest_filename)
