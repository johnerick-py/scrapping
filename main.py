import requests
from bs4 import BeautifulSoup

uf = [
    'Acre',
    'Alagoas',
    'Amapa',
    'Amazonas',
    'Bahia',
    'Ceara',
    'Espirito Santo',
    'Goias',
    'Maranhao',
    'Mato%20Grosso',
    'Mato%20Grosso%20do%20Sul',
    'Minas%20Gerais',
    'Para',
    'Paraiba',
    'Parana',
    'Pernambuco',
    'Piaui',
    'Rio%20de%20Janeiro',
    'Rio%20Grande%20do%20Norte',
    'Rio%20Grande%20do%20Sul',
    'Rondonia',
    'Roraima',
    'Santa%20Catarina',
    'Sao%20Paulo',
    'Sergipe',
    'Tocantins',
    'Distrito Federal'
]


for i in uf:
    url = f'http://www.fenabrave.org.br/relatorios/rel_MaisVendidos.asp?UF={i}&cap=&segmento=1&periodo=11,2022'
    
    page = requests.get(url)
    
    # criando um objeto soup com o conteudo da pagina, usando o html parser para pegar o conteuo de uma div especifica
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', id='linha')
    # print(results)
    state = i.replace("%20", " ")
    print(f"Estado: {state}")
    
    for result in results:
        
        cars = result.find('div', id='marca')
        sold_amount = result.find('div', id='val')
        print(f"    Modelo: {cars.text} | Quantidade vendida: {sold_amount.text}")
        
