from bs4 import BeautifulSoup
import requests
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

url2 = 'https://www.otomoto.pl/oferta/hyundai-ix35-2-0-crdi-salon-polska-serwis-aso-skora-navi-klimatronic-ID6EcQ4F.html'
products = {}

raw_product = request_html(url2)
product_html = raw_product.findAll('span', class_='offer-main-params__item')
print(product_html)
