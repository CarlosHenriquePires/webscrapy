from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

todos=[]
page = 1
while (page < 3):
    url = urlopen("https://rn.olx.com.br/autos-e-pecas?o="+str(page))
    soup = BeautifulSoup(url.read(),"html.parser")
    titulo= soup.findAll("h2", {"class": "OLXad-list-title"})
    detalhes=soup.findAll("p", {"class": "text detail-specific"})
    preco=soup.findAll("p", {"class": "OLXad-list-price"})
    local=soup.findAll("p", {"class": "text detail-region"})
    page+=1
for title in titulo:
    title = title.getText()
    title = title.replace("\n", "")
    title = title.replace("\t", "")
    for detail in detalhes:
        detail = detail.getText()
        detail = detail.replace("\n", "")
        detail = detail.replace("\t","")
        for price in preco:
            price = price.getText()
            price = price.replace("\n", "")
            price = price.replace("\t","")
            for origen in local:
                origen = origen.getText()
                origen = origen.replace("\n", "")
                origen = origen.replace("\t","")
    todos.append([title,detail,price,origen])
df = pd.DataFrame(todos,columns=('Titulo','Detalhes','Preço','Local'))
df.to_csv('webscraping.csv')