from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

titulos=[]
detalhes_=[]
precos_=[]
locais=[]
page = 1
while(page < 3):
    url = urlopen("https://rj.olx.com.br/autos-e-pecas?o="+str(page))
    print(url)
    soup = BeautifulSoup(url.read(),"html.parser")
    titulo = soup.findAll("h2", {"class": "OLXad-list-title"})
    detalhes=soup.findAll("p", {"class": "text detail-specific"})
    preco=soup.findAll("p", {"class": "OLXad-list-price"})
    local=soup.findAll("p", {"class": "text detail-region"})
    for title in titulo:
        text = title.getText()
        text = text.replace('\n','\t\t\t\t\t\t\t')
        titulos.append(text)
    for detail in detalhes:
        detalhes_.append(detail.getText())
    for price in preco:
        precos_.append(price.getText())
    for origen in local:
        locais.append(origen.getText())
    page = page + 1

test = list(zip(titulos,detalhes_,precos_,locais))
df = pd.DataFrame(test)
print(df)

