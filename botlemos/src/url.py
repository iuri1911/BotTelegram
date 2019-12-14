import requests

url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
r = requests.get(url)
data = r.json()
dolar = float(data['USD']['ask'])
print('{:.2f}'.format(dolar))
