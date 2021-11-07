from libs.ParsingHTML import ParsingHTML

url = 'https://bell-bimbo.com/dostup/'


f = ParsingHTML(url)

print(f.raw_parse())
