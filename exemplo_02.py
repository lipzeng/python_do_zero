# importação de bibliotecas
import pandas as pd

# carrega um arquivo do HD para a memoria
data = pd.read_csv('data/kc_house_data.csv')

# mostrar na tela as primeiras 6 linhas
# print(data.head())

# fução que converte de object (string) -> date
data['date'] = pd.to_datetime(data['date'])

# ====================================
# Como converter os tipos de variaveis
# ====================================

# inteiro -> float
# data['bedrooms'] = data['bedrooms'].astype(float)

# float -> int
# data['bedrooms'] = data['bedrooms'].astype(int)

# inteiro -> string
# data['bedrooms'] = data['bedrooms'].astype(str)

# string -> inteiro
# data['bedrooms'] = data['bedrooms'].astype(int)

# mostra os tipos de variaveis de cada coluna
# print(data.dtypes)3:5, 0:2]

# ====================================
# Criando novas variaveis
# ====================================

# data['nome_do_asher'] = "asher"
# data['data_ebretura_ds'] = pd.to_datetime('2021-02-28')
#
# print(data[['id', 'nome_do_asher', 'data_ebretura_ds']])
# print(data.dtypes)

# ====================================
# Deletando novas variaveis
# ====================================

# cols = ['nome_do_asher','data_ebretura_ds']
# data = data.drop(cols, axis=1)
# print(data.columns)

# mostra os tipos de variaveis de cada coluna
# print(data.dtypes)

# ====================================
# Seleção de dados
# ====================================

# Forma 01: Direto pelo nome das colunas
# print(data[['price', 'id', 'date']])
#
# # Forma 02: Pelo indices das linhas e colunas
# print(data.iloc[0:5, 0:5])
#
# # Forma 03: Pelo indices das linhas e nome das colunas
# print(data.loc[0:5, ['price']])
#
# # Forma 04: Indices booleanos
# cols = [True, True, False, True, True, False, True, True, False,
#         True, True, False, True, True, False, True, True, False, True, True, False]
# print(data.loc[0:3, cols])

# ====================================
# Respondendo as perguntas de negocio
# ====================================

# qual a data do imovel mais antigo do portfolio = 2014-05-02
# data_antiga = data['date'].sort_values(ascending=True)
# print(data_antiga)

# quantos imoveis possuem o numero maximo de andares = 8
# num_andares = data['floors'].unique()
# num_andares = data['floors'].max()
# qtd_andares = data[data['floors'] == num_andares]
# print(qtd_andares.shape)

# separar os imoveis pelo preço acima de 540000 e abaixo de 540000
# imoveis acima de 540000 classificar como high_level
# imoveis abaixo de 540000 classificar como low_level

# data['level'] = 'standart'
#
# data.loc[data['price'] > 540000, 'level'] = 'high_level'
# data.loc[data['price'] < 540000, 'level'] = 'low_level'
#
# print(data.head())

# passar relatorio ordenado pelo preço
#
# report = data[['id', 'price', 'bedrooms']]
#
# report.to_csv('data/report_aula02.csv', index=False)

# Plotly - Biblioteca que armazena uma função que desenha mapa
# Scater MapBox - Função que desenha mapa

# import plotly.express as px
#
# data_mapa = data[['id', 'lat', 'long', 'price']]
#
# mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id',
#                          hover_data=['price'], color_discrete_sequence=['fuchsia'],
#                          zoom=3, height=300)
#
# mapa.update_layout(mapbox_style='open-street-map')
# mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
# mapa.show()
#
# mapa.write_html('data/mapa_house_rocket.html')

# #########################===========================####################

# Novas perguntas do CEO:
#
# 1.Crie uma nova coluna chamada: "house_age"
#   -Se o valor da coluna "date" for maior que 2014-01-01 => "new_house"
#   -Se o valor da colna "date" for menor que 2014-01-01 => "old_house"

# data['house_age'] = 'standart'
# print(data['date'])
#
# data.loc[data['date'] > 2014-01-01, 'house_age'] = 'new_house'
# data.loc[data['date'] < 2014-01-01, 'house_age'] = 'old_house'

# 2.Crie uma nova coluna chamada: "dormitory_type"
#   -Se o valor da coluna "bedrooms" for igual a 1 => "studio"
#   -Se o valor da coluna "bedrooms" for igual a 2 => "apartament"
#   -Se o valor da coluna "bedrooms" for igual a 3 => "house"

data['dormitory_type'] = 'standart'

data.loc[data['bedrooms'] == 1, 'dormitory_type'] = 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type'] = 'apartament'
data.loc[data['bedrooms'] >= 3, 'dormitory_type'] = 'house'
#
# print(data['dormitory_type'].unique())

# 3.Crie uma nova coluna chamada: "condition_type"
#   -Se o valor da coluna "condition" for menor ou igual a 2 => "bad"
#   -Se o valor da coluna "condition" for igual 3 ou 4 => "regular"
#   -Se o valor da coluna "condition" for maior a 5 => "good"

# data['condition_type'] = 'standart'
#
# data.loc[data['condition'] <= 2, 'condition_type'] = 'bad'
# data.loc[data['condition'] == 3 & data['condition'] == 4, 'condition_type'] = 'regular'
# data.loc[data['condition'] > 5, 'condition_type'] = 'good'

# 4.Modifique o tipo a coluna "condition" para string

# data['condition'] = data['condition'].astype(str)

# 5.Delete as colunas "sqft_living15" e "sqft_lot15"
#
# cols = ['sqft_living15', 'sqft_lot15']
# data = data.drop(cols, axis=1)
# print(data.columns)

# 6.Modifique o tipo de coluna "yr_build" para date

# data['yr_build'] = pd.to_datetime(data['date'])

# 7.Modifique o tipo da coluna "yr_renovated" para date

# data['yr_renovated'] = pd.to_datetime(data['date'])

# 8.Qual a data mais antiga de construção de um imovel? = 20140502

# date_old = data['yr_build'].min()
# print(date_old)

# 9.Qual a data mais antiga de renovação de um imovel? 1991

# date_renovated = data['yr_renovated'].unique()
# print(date_renovated)

# 10.Quantos imoveis tem 2 andares? 8241

# qtd_andares = data['floors'] == 2
# print(data[qtd_andares].shape)

# 11.Quantos imoveis estão com a condição igual a "regular"

# imov_regular = data['condition_type'] == 'good'
# print(data[imov_regular].shape)
#
#
# print(data['condition_type'])

# 14.Qual  o valor do imavel mais caro do "studio" = 1247000.00

# print(data['dormitory_type'].unique())
# #
# imovel_studio = data['dormitory_type'] == 'studio'
# print(data[imovel_studio].max())

# 15.Qual o maior numero de quartos que um imovel do tipo "house" possui? 33
#
# imovel_house = data['dormitory_type'] == 'house'
# print(data[imovel_house].max())

# 15. Quantos imoveis do tipo "apartament" foram reformados em 2015?

# print(data.columns)
# qtd_reform_apartament = data[(data['dormitory_type'] == 'apartament') & (data['yr_renovated'] < 2015-1-1)].count()
#
# print(qtd_reform_apartament)
