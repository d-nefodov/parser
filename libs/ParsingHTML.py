from bs4 import BeautifulSoup
import requests


class ParsingHTML():
    
    
    def __init__(self, url):
        self.url = url

    def raw_parse(self):
        page = requests.get(self.url)
        if page.status_code == 200:
            return BeautifulSoup(page.text, "html.parser")
        else:
            return 'Problem with connection...'