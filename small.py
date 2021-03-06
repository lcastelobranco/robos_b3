import requests
from bs4 import BeautifulSoup
from helper import *



def parser(data, linha):
    str_sql = "INSERT INTO small (data,ticker,nome,tipo,quantidadeteorica,participacao) values (%s,%s,%s,%s,%s,%s)"
    cursor.execute(str_sql, tuple([data] + linha.split('\n\n')[1:-1]))
    conn.commit()


conn ,cursor,engine = conection("robos_b3")
lista = contexto(cursor,"small")


url = "http://bvmf.bmfbovespa.com.br/indices/ResumoCarteiraTeorica.aspx?Indice=SMLL&idioma=pt-br"
html = requests.post(url)
soup = BeautifulSoup(html.text,'html.parser')
data = '20'+'-'.join(soup.find_all(id="ctl00_contentPlaceHolderConteudo_lblTitulo")[0].text.split()[-1].split('/')[::-1])


try:
    linhas = list(map(lambda x: x.text.replace('.','').replace(',','.'), soup.table.find_all('tr')))
    if data not in lista:
        for linha in linhas[2:]:
            parser(data,linha)

        with open(r"checklist.txt", 'r+') as checklist:
            content = checklist.read()
            checklist.seek(0, 0)
            checklist.writelines('SMALL\n' + content)

except:
    error('SMALL - algum erro do processo em geral')