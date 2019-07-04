from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

todos={}
lista=[]
href=[]
ul=[]
page = 1

end = "https://rn.olx.com.br/autos-e-pecas"
url = urlopen(end)
soup = BeautifulSoup(url.read(),"html.parser")
links = soup.findAll("a", {"class":"OLXad-list-link"})

for valores in links:
	href.append(valores['href'])
for j in href:
	try:		
		url=urlopen(j)
		soup = BeautifulSoup(url.read(),"html.parser")
		todos['titulo']=soup.findAll("h1", {"class": "OLXad-title"})[0].string
		todos['preco']=soup.findAll("span", {"class": "actual-price"})[0].string
		detalhes=soup.findAll("ul", {"class": "list square-gray"})
		for i in detalhes:
			ul.append(i[''])
		print(ul)
		lista.append(todos)
		todos={}
	except IndexError:
		todos={}
'''
df = pd.DataFrame(lista)
df['titulo'] = df['titulo'].str.replace('([\n\t])', '')
df['titulo'] = df['titulo'].str.replace('(\s{3,})', '')


print(df.columns.values)
df.to_csv('webscraping.csv')

	

while (page <= 1):
    end = "https://rn.olx.com.br/autos-e-pecas?o="+str(page)
    url = urlopen(end)
    print(end)
    page=page+1
    soup = BeautifulSoup(url.read(),"html.parser")
    todos['titulo']= soup.findAll("h2", {"class": "OLXad-list-title"})[0].string
    todos['detalhes']=soup.findAll("p", {"class": "text detail-specific"})[0].string
    todos['preco']=soup.findAll("p", {"class": "OLXad-list-price"})[0].string
    todos['local']=soup.findAll("p", {"class": "text detail-region"})[0].string
    lista.append(todos)
df = pd.DataFrame(lista)
df['titulo'] = df['titulo'].str.replace('([\n\t])', '')
df['titulo'] = df['titulo'].str.replace('(\s{3,})', '')
df['detalhes'] = df['detalhes'].str.replace('([\n\t])', '')
df['preco'] = df['preco'].str.replace('(\s{3,})', '')
df['preco'] = df['preco'].str.replace('([\n\t])', '')
df['local'] = df['local'].str.replace('(\s{3,})', '')
df['local'] = df['local'].str.replace('(\s{3,})', '')
print(df.columns.values)
df.to_csv('webscraping.csv')
'''
