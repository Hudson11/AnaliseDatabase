import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('diabetes.csv')

# a - numero de linhas da base
print('Linhas do Database ', df.count()[1])

# b - Quantidade e tipo das colunas
print(df.info())

# c - Max e Min de Cada coluna
print(df.max())
print(df.min())

# d - valores faltosos
print(df.isnull().sum()) # verifica cada coluna.
print(df.isnull().sum(axis=1)) # verifica cada linha.

# e - Descubra a coorelação entre os atributos do DataFrame
# Retorna a relação entre os atributos da base, quanto mais próximo de 1
# significa que a uma alta coorelação entre os campos, em outras palavras, a alteração de
# valor de um influência na variação do valor do outro.
print(df.corr())

# f - grave em um outro arquivo, normalizar valores entre o e 1, substituir
# valores altosos pela média da coluna

df.fillna(value=df.mean(), inplace=True)
print(df)
df_aux = df.drop('class', axis=1)
print(df_aux)
df_norm = (df_aux - df_aux.min()) / (df_aux.max() - df_aux.min())
print(df_norm)
df_norm.to_csv('data.csv')

# g - edentifique outros 5 dados da base
data_1 = df[df['class'] == 'tested_positive']['plas']
data_2 = df[df['class'] == 'tested_negative']['plas']
data_3 = df[df['class'] == 'tested_positive']['pres']
data_4 = df[df['pres'] > df['pres'].mean()]['mass']
data_5 = df[df['preg'] > 2]['age']

print(data_1) # Níveis de Plasma para Testes Positivos 
print(data_2) # Níveis de Plasma para Testes Negativos
print(data_3) # Pressão arterial em (mm Hg) dos teste positivos.
print(data_4) # Índice de Massa corporal dos pacientes que apresentaram pressão
# arterial acima da média dos pacientes com o teste positivo.
print(data_5) # Idade de pacientes que engravidarão mais de duas vezes.

# h - Visualizar dados usando o matplotlib.pyplot


data_1.plot.hist(title='frequência de níveis de Plasma para Testes positivos', edgecolor='black')
plt.show()

data_2.plot.hist(title='frequência de níveis de Plasma para Testes negativos', edgecolor='black')
plt.show()

data_3.head(10).plot.bar(title='Pressão arterial em (mm hg) dos teste positivos')
# Nota: como são muitos dados resolvi apenas plotar os 10 primeiros da sequência. 
plt.show()

data_4.head(10).plot.bar(title='índice de massa corporal para pacientes com pressão arterial acima da média')
# Nota: como são muitos dados resolvi apenas plotar os 10 primeiros da sequência. 
plt.show()

data_5.head(10).plot.bar(title='idades de pacientes que já engravidaram mais que 2 vezes')
plt.show()