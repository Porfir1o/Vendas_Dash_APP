import json
import pandas as pd

<<<<<<< HEAD
file = open("C:\\Users\\Porfirio\\PycharmProjects\\GUPPE\\Dashboard_Vendas\\src\\vendas.json")
=======
file = open('src/vendas.json')
#open('C:\\Users\\Porfirio\\PycharmProjects\\GUPPE\\venv\\dados\\vendas.json')
>>>>>>> a48339631f86511cb278f26907d2d1e54d548782
data = json.load(file)

#print(data)

df = pd.DataFrame.from_dict(data)

#print(df)

#print(df['Data da Compra'])

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()
