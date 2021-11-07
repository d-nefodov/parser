from libs.ParsingHTML import ParsingHTML

url = 'https://bell-bimbo.com/dostup/'


site = ParsingHTML(url)

body = site.clearing_html()