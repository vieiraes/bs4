import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.defesacivil.sc.gov.br/avisos-meteorologicos/'
page = requests.get(url)

soup = bs(page.text, 'html.parser')

bd_titles = []
# list_titles = soup.find_all('a', class_='czr-title') #temq ue descobrir qual o item que quer buscar
list_news = soup.find_all(class_='czr-wp-the-content') #temq ue descobrir qual o item que quer buscar

print(list_news)
# print(len(list_news))



for item in list_news:
    titulo = item.get_text()
    bd_titles.append(titulo)

print(bd_titles)




# # # Imprimir os títulos
# # for titulo in titulos:
# #     print(titulo)




# soup = bs(a, "lxml")
# lst = soup.find_all("a")
# lst = [item["href"] for item in lst]
# return lst


# page_prettyficado = page.prettify()
# print(scrap)
# print(len(scrap))

# print(page_prettyficado)
# print(body_return.text)
