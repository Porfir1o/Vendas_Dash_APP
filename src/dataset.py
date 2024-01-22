import json
import pandas as pd

file = open('src/vendas.json')

data = json.load(file)

df = pd.DataFrame.from_dict(data)

#print(df['Data da Compra'].head())

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y', utc=False).dt.normalize()

colunas = df.columns.tolist()

file.close()
