# importação de bibliotecas
import pandas as pd

# carrega um arquivo do HD para a memoria
data = pd.read_csv('data/kc_house_data.csv')

# mostrar na tela as primeiras 6 linhas
#print(data.head())

# fução que converte de object (string) -> date
data['date'] = pd.to_datetime(data['date'])


# ====================================
# Como converter os tipos de variaveis
# ====================================

# inteiro -> float
#data['bedrooms'] = data['bedrooms'].astype(float)

# float -> int
#data['bedrooms'] = data['bedrooms'].astype(int)

# inteiro -> string
#data['bedrooms'] = data['bedrooms'].astype(str)

# string -> inteiro
#data['bedrooms'] = data['bedrooms'].astype(int)

# mostra os tipos de variaveis de cada coluna
#print(data.dtypes)

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
#print(data.dtypes)

# ====================================
# Seleção de dados
# ====================================

# Forma 01: Direto pelo nome das colunas
print(data[['price', 'id', 'date']])

# Forma 02: Pelo indices das linhas e colunas
print(data.iloc[0:5, 0:5])

# Forma 03: Pelo indices das linhas e nome das colunas
print(data.loc[0:5, ['price']])

# Forma 04: Indices booleanos
cols = [True, True, False, True, True, False, True, True, False,
        True, True, False, True, True, False, True, True, False, True, True, False]
print(data.loc[0:3, cols])


