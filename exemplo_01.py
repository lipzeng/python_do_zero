# carregue o conjunto de dados kc_house_data.csv do HD para o codigo

# função - read_csv()
# biblioteca pandas

import pandas as pd
data = pd.read_csv('data/kc_house_data.csv')

# mostre as 5 primeiras linhas do conjunto de dados
#print(data.head())

# mostre o numero de colunas e de linhas do conjunto de dados
#print(data.shape)

# mostre o nome das colunas do conjunto de dados
#print(data.columns)

# mostre o conjunto de dados ordenados pela coluna price
#print(data[['id','price']].sort_values('price', ascending=False))

# 1 quantas casas estão disponiveis para compra = 21613
#print(data['id'])

# 2 quais são os atributos das casas = resposta nas colunas
#print(data.columns)

# 3 qual a casa mais cara = id'7252' - 7700000.0
#print(data[['price']].sort_values('price', ascending=False))

# 4 qual casa com maior numero de quartos = id'15870' - 33
#print(data[['bedrooms']].sort_values('bedrooms', ascending=False))

# qual a soma total de quartos do conjunto de dados = 72854
# print(sum(data['bedrooms']))

# qual preço medio de todas as casas do conjunto de dados = 540.088
#media = data.mean()
#print(media)

# qual preço medio de casa com 2 banheiros
#media = data['price'].sum
#print(media)

