# import requests
# import bs4
# res = requests.get('https://www.sanignacio.pr')
# res.raise_for_status()
# SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(SanIgnaciopr))
from operator import index
import requests
import bs4
res = requests.get('https://www.sanignacio.pr/sobre-csi/historia-del-colegio')
res.raise_for_status()
SanIgnaciopr = bs4.BeautifulSoup(res.content, 'html.parser')
elems = SanIgnaciopr.select('p')
print(type(SanIgnaciopr))
print(len(elems))
str(elems)
print(elems[2].getText())
print(elems[3].getText())