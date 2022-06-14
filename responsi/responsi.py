import requests

# parameter pertama yang diperlukan dari metode 'get' adalah 'url':
x = requests.get('https://data.jakarta.go.id/dataset/data-penumpang-kapal-dari-dan-ke-kepulauan-seribu-tahun-2020/resource/fa34ebae-a2c4-40ad-afee-248489fb0120')

#print the response text (isi dari file yang diminta):
print(x.text)


import pandas as pd

path = "C:/Users/Bella/responsi/data-penumpang-kapal-bulan-juni-2020.csv"
df = pd.read_csv(path)
df.head()