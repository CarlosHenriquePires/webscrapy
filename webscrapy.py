from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

todos={}
lista=[]
href=[]
ul=[]
page = 1
links=[]

while (page <= 2):
	print('Página:',page)
	end = "https://rn.olx.com.br/autos-e-pecas?o="+str(page)
	print(end)
	page+=1
	url = urlopen(end)
	soup = BeautifulSoup(url.read(),"html.parser")
	links = soup.findAll("a", {"class":"OLXad-list-link"})
	for valores in links:
		href.append(valores['href'])
	print(len(href))
cont=1
for j in href:
	try:		
		url=urlopen(j)
		print('Anúncio:',cont)
		cont+=1
		soup = BeautifulSoup(url.read(),"html.parser")
		todos['titulo']=soup.findAll("h1", {"class": "OLXad-title"})[0].string
		todos['preco']=soup.findAll("span", {"class": "actual-price"})[0].string
		temp=soup.findAll("div", {"class": "atributes"})[0].findAll("strong",{"class":"description"})
		todos['motor']=temp[2].getText()
		todos['portas']=temp[3].getText()
		todos['tipo']=temp[5].getText()
		todos['ano']=temp[6].getText()
		todos['combustivel']=temp[7].getText()
		todos['km']=temp[8].getText()
		todos['cor']=temp[11].getText()
		print(todos)
		lista.append(todos)
		todos={}
	except IndexError:
		print(ImportError)
		todos={}

df = pd.DataFrame(lista)
df['titulo'] = df['titulo'].str.replace('([\n\t])', '')
df['titulo'] = df['titulo'].str.replace('(\s{3,})', '')
df['preco'] = df['preco'].str.replace('([\n\t])', '')
df['motor'] = df['motor'].str.replace('([\n\t])', '')
df['portas'] = df['portas'].str.replace('([\n\t])', '')
df['tipo'] = df['tipo'].str.replace('([\n\t])', '')
df['ano'] = df['ano'].str.replace('([\n\t])', '')
df['combustivel'] = df['combustivel'].str.replace('([\n\t])', '')
df['km'] = df['km'].str.replace('([\n\t])', '')
df['cor'] = df['cor'].str.replace('([\n\t])', '')


print(df.columns.values)
df.to_csv('webscraping.csv')