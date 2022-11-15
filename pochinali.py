"""
ludmil@ludmil-Lenovo-G50-30:~$ bpython
bpython version 0.21 on top of Python 3.7.3 /usr/bin/python3
"""
import requests
import pandas as pd
# import csv
# from matplotlib import pyplot as plt
# следва линк към сайт съдържащ csv таблица
url = 'https://data.egov.bg/data/resource/embed/e59f95dd-afde-43af-83c8-ea2916badd19'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df) # отпечатва таблицата в терминала
df.to_csv('covid_razprostranenie.csv') # сейф на csv-файла в текущата дир.

filename = 'covid_razprostranenie.csv'
df = pd.read_csv('covid_razprostranenie.csv')
df.head()
# тук се изобразява началото на таблицата, като тест дали се отваря
import plotly.express as px
# следва определяне коя колона да се визуализира:
fig = px.line(df, x = 'Дата', y = 'Починали за денонощие', title='Разпределение по Починали за денонощие')
# избрах една колона(у) и ще я визуализирам по дати(х)
fig.show()
