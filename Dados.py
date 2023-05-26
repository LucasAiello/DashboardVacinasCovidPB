import pandas as pd
import numpy as np
import plotly.express as px
import zipfile as zf
import requests
import html

# ------------------------------------------------------- CONSTANTES ---------------------------------------------------------------------------------------

colors = {'background': '#03181e', 'text': '#2f6573'}
faixas_etarias = ['0 - 10', '11 - 20', '21 - 30', '31 - 40', '41 - 50', '51 - 60', '61 - 70',
                  '71 - 80', '81 - 90', '91 - 100', '101 - 110', '111 - 120', '121 - 130', '131 - 140']
meses = ['Jan', 'Fev', 'Mar', 'Abri', 'Maio', 'Jun', 'Jul', 'Agost', 'Set', 'Out', 'Nov', 'Dez']


#-------------------------------------------------- IMPORTANDO O ARQUIVO CSV -------------------------------------------------------------------------------

url = 'https://drive.google.com/u/2/uc?id=1CmBDqshRJ5wtYcYzSixXN1llF2jvUHqp&amp;export=download&amp;confirm=t&amp;uuid=ec1a9532-4e9c-4cf8-87b2-cf9e54f174a3&amp;at=AKKF8vxrlM05uYSqAyKaw4jsxSsM:1686761336577'

decoded_url = html.unescape(url)

req = requests.get(decoded_url)
open('dados-vacina_covid_pb.zip', "wb").write(req.content)

z = zf.ZipFile('dados-vacina_covid_pb.zip', mode="r")
print(z.namelist())

z.extractall()

vacina_covid_pb = pd.DataFrame(pd.concat([pd.read_csv(arquivo, sep=";", encoding="latin", parse_dates=["vacina_dataAplicacao"], low_memory=False) 
for arquivo in z.namelist()]))
#----------------------------------------------------------------------------------------------------------------------------------------

#vacina_covid_pb['paciente_dataNascimento'] = pd.to_datetime(vacina_covid_pb['paciente_dataNascimento'])
#vacina_covid_pb['vacina_dataAplicacao'] = pd.to_datetime(vacina_covid_pb['vacina_dataAplicacao'])

vaci_2020 = vacina_covid_pb[vacina_covid_pb['vacina_dataAplicacao'].dt.year == 2020]
vaci_2021 = vacina_covid_pb[vacina_covid_pb['vacina_dataAplicacao'].dt.year == 2021]
vaci_2022 = vacina_covid_pb[vacina_covid_pb['vacina_dataAplicacao'].dt.year == 2022]
vaci_2023 = vacina_covid_pb[vacina_covid_pb['vacina_dataAplicacao'].dt.year == 2023]

vaci_2020_meses = []
for i in range(1, 13):
    count = len(vaci_2020[vaci_2020['vacina_dataAplicacao'].dt.month == i])
    vaci_2020_meses.append(count)

vaci_2021_meses = []
for i in range(1, 13):
    count = len(vaci_2021[vaci_2021['vacina_dataAplicacao'].dt.month == i])
    vaci_2021_meses.append(count)
vaci_2021_meses

vaci_2022_meses = []
for i in range(1, 13):
    count = len(vaci_2022[vaci_2022['vacina_dataAplicacao'].dt.month == i])
    vaci_2022_meses.append(count)
vaci_2022_meses

vaci_2023_meses = []
for i in range(1, 13):
    count = len(vaci_2023[vaci_2023['vacina_dataAplicacao'].dt.month == i])
    vaci_2023_meses.append(count)
vaci_2023_meses


"""
nomes = ['F', 'M', 'I']
grafico_sexoBio = px.pie(values=vacina_covid_pb['paciente_enumSexoBiologico'].value_counts(), names=vacina_covid_pb['paciente_enumSexoBiologico'].unique())
"""

count = vacina_covid_pb['vacina_fabricante_nome'].value_counts()