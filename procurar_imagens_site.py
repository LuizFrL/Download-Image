from bs4 import BeautifulSoup as bs
import urllib.request
import requests
import os

url_page = 'https://www.clubemontreal.com.br/hoteis-cidade/3998-barra-de-saao-miguel-AL/'

html_page = requests.get(url=url_page).content
pagina_object = bs(html_page, 'html.parser')

imagens_object = pagina_object.find_all('img')
path = 'images_site'

if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)

for c, img in enumerate(imagens_object):
    link_image = img['src']
    try:
        urllib.request.urlretrieve(link_image, 'image' + str(c) + '.jpg')
    except Exception as error:
        print(error)
        continue
    print(link_image)
    c += 1
