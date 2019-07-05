from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

todos={} #Dicionario criado com os dados para cada anuncio
lista=[] #Lista de dicionarios com todos os anuncios
href=[] #Lista com os links de todos os anuncios
ul=[] 
page = 1 #Contador das páginas
links=[] # todos as tags a q contém o endereço de cada anuncio

while (page <= 100): #Percorre até a página 100
	href=[]
	print('Página:',page)
	end = "https://rn.olx.com.br/autos-e-pecas?o="+str(page) #Endereço das páginas com as lista dos anuncios
	print(end)
	page+=1
	url = urlopen(end)
	soup = BeautifulSoup(url.read(),"html.parser") #Leio o html
	links = soup.findAll("a", {"class":"OLXad-list-link"}) #pego as tags <a>
	for valores in links:
		href.append(valores['href']) #pego os endereços de cada anuncio contido no href
	print(len(href))
	cont=1
	for j in href: #para cada anuncio ele percorrerá o html
		try:		
			url=urlopen(j)
			print('Anúncio:',cont)
			cont+=1
			soup = BeautifulSoup(url.read(),"html.parser")
			#Começa a pegar os dados dos componentes
			todos['titulo']=soup.findAll("h1", {"class": "OLXad-title"})[0].string
			todos['preco']=soup.findAll("span", {"class": "actual-price"})[0].string
			temp=soup.findAll("div", {"class": "atributes"})[0].findAll("strong",{"class":"description"})
			#Pego todos os <li> contido na div, mas somentes aqueles anuncios que tem todos os detalhes especificados
			if(len(temp) == 14):# 14 é a quantidade de detalhes para os carros, caso tenha menos não é salvo o anuncio
				todos['motor']=temp[2].getText() # percorro os li e pego os dados
				todos['portas']=temp[3].getText()
				todos['tipo']=temp[5].getText()
				todos['ano']=temp[6].getText()
				todos['combustivel']=temp[7].getText()
				todos['km']=temp[8].getText()
				todos['cor']=temp[11].getText()
				lista.append(todos)
				print(todos)
			else:
				todos={}#entra aqui os anuncios que tem menos de 14 especificações, eu apago o dicionario
			todos={}
		except IndexError:#Aqui entra os anuncios que nao especificaram algum tipo de elemento
			print(ImportError)
			todos={}

df = pd.DataFrame(lista)#armazeno em um dataframe e trato os espaços e vírgulas em excesso
df['titulo'] = df['titulo'].str.replace('([\n\t])', '')
df['titulo'] = df['titulo'].str.replace('(\s{3,})', '')
df['titulo'] = df['titulo'].str.replace(',', '')
df['preco'] = df['preco'].str.replace('([\n\t])', '')
df['preco'] = df['preco'].str.replace('(\s{3,})', '')
df['motor'] = df['motor'].str.replace('([\n\t])', '')
df['motor'] = df['motor'].str.replace('(\s{3,})', '')
df['portas'] = df['portas'].str.replace('([\n\t])', '')
df['portas'] = df['portas'].str.replace('(\s{3,})', '')
df['tipo'] = df['tipo'].str.replace('([\n\t])', '')
df['tipo'] = df['tipo'].str.replace('(\s{3,})', '')
df['ano'] = df['ano'].str.replace('([\n\t])', '')
df['ano'] = df['ano'].str.replace('(\s{3,})', '')
df['combustivel'] = df['combustivel'].str.replace('([\n\t])', '')
df['combustivel'] = df['combustivel'].str.replace('(\s{3,})', '')
df['km'] = df['km'].str.replace('([\n\t])', '')
df['km'] = df['km'].str.replace('(\s{3,})', '')
df['cor'] = df['cor'].str.replace('([\n\t])', '')
df['cor'] = df['cor'].str.replace('(\s{3,})', '')

print(df.columns.values)
print(df)
df.to_csv('webscraping.csv')#converto em arquivo .csv