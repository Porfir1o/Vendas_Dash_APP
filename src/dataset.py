import json
import pandas as pd

<<<<<<< HEAD
file = open("C:\\Users\\Porfirio\\PycharmProjects\\GUPPE\\Dashboard_Vendas\\src\\vendas.json")
=======
#file = open("C:\\Users\\Porfirio\\PycharmProjects\\GUPPE\\Dashboard_Vendas\\src\\vendas.json")
file = open('src/vendas.json')
#open('C:\\Users\\Porfirio\\PycharmProjects\\GUPPE\\venv\\dados\\vendas.json')

data = json.load(file)
>>>>>>> a32e1aa63ee067ea17ffdba10d7926ea29a36a90

# file = open('src/vendas.json')
# open('C:\\Users\\Porfirio\\PycharmProjects\\GUPPE\\venv\\dados\\vendas.json')

data = json.load(file)

df = pd.DataFrame.from_dict(data)

#print(df['Data da Compra'].head())

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y', utc=False).dt.normalize()

#df['Tipo de pagamento'] = df['Tipo de pagamento'].replace(['cartao_credito'], '')

#print(df['Tipo de pagamento'].head())

colunas = df.columns.tolist()

file.close()
