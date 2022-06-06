# Pertemuan 13 Python Untuk Data Analytics

# 10 minutes to pandas

```python
import numpy as np

import pandas as pd
```

# Object creation

**Series** -> array berlabel satu dimensi yang mampu menampung semua tipe data (bilangan bulat, string, angka, floating point, objek Python, dll). Label sumbu secara korelatif disebut sebagai *index*. Metode dasar untuk membuat Series adalah memanggil **pd.Series(data, index=index).**

Membuat **Series**

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])

s
Out[4]: 
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
```

Membuat **DataFrame** dengan melewatkan Numpy array dengan indeks *datatime* serta kolom yang memiliki label:

```python
dates = pd.date_range("20130101", periods=6)

dates
Out[6]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df
Out[8]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

Membuat **DataFrame** dengan melematkan kamus objek yang dapat diubah menjadi struktur seperti series:

```python
df2 = pd.DataFrame(

    {

        "A": 1.0,

        "B": pd.Timestamp("20130102"),

        "C": pd.Series(1, index=list(range(4)), dtype="float32"),

        "D": np.array([3] * 4, dtype="int32"),

        "E": pd.Categorical(["test", "train", "test", "train"]),

        "F": "foo",

    }

)



df2
Out[10]: 
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
```

Membuat kolom dengan hasil dari penggunaan DataFrame yang memiliki dtypes berbeda

```python
df2.dtypes
Out[11]: 
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
```


# Viewing data

Untuk melihat sampel kecil objek Series atau DataFrame, menggunakan metode `head()` dan `tail()`. Jumlah elemen default untuk ditampilkan adalah lima, tetapi dapat dirubah dengan mengcustom jumlahnya.

Melihat baris dari bagian atas hingga bawah data:

```python
df.head()
Out[13]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401

df.tail(3)
Out[14]: 
                   A         B         C         D
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
```

Menampilkan indeks dari kolom:

```python
df.index
Out[15]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

df.columns
Out[16]: Index(['A', 'B', 'C', 'D'], dtype='object')
```

Untuk itu df (DataFrame)dari semua nilai floating - point, **DataFrame.to_numpy()** akan lebih cepat penggunaannya karena tidak memerlukan penyalinan data.

```python
df.to_numpy()
Out[17]: 
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
```

```python
df2.to_numpy()
Out[18]: 
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
```

**describe()** menunjukkan ringkasan statistik cepat dari data yang dimiliki. 

```python
df.describe()
Out[19]: 
              A         B         C         D
count  6.000000  6.000000  6.000000  6.000000
mean   0.073711 -0.431125 -0.687758 -0.233103
std    0.843157  0.922818  0.779887  0.973118
min   -0.861849 -2.104569 -1.509059 -1.135632
25%   -0.611510 -0.600794 -1.368714 -1.076610
50%    0.022070 -0.228039 -0.767252 -0.386188
75%    0.658444  0.041933 -0.034326  0.461706
max    1.212112  0.567020  0.276232  1.071804
```

Perintah untuk melakukan transpos data:

```python
df.T
Out[20]: 
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A    0.469112    1.212112   -0.861849    0.721555   -0.424972   -0.673690
B   -0.282863   -0.173215   -2.104569   -0.706771    0.567020    0.113648
C   -1.509059    0.119209   -0.494929   -1.039575    0.276232   -1.478427
D   -1.135632   -1.044236    1.071804    0.271860   -1.087401    0.524988
```

```python
df.sort_index(axis=1, ascending=False)
Out[21]: 
                   D         C         B         A
2013-01-01 -1.135632 -1.509059 -0.282863  0.469112
2013-01-02 -1.044236  0.119209 -0.173215  1.212112
2013-01-03  1.071804 -0.494929 -2.104569 -0.861849
2013-01-04  0.271860 -1.039575 -0.706771  0.721555
2013-01-05 -1.087401  0.276232  0.567020 -0.424972
2013-01-06  0.524988 -1.478427  0.113648 -0.673690
```

```python
df.sort_values(by="B")
Out[22]: 
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
```

# Selection

Bagian ini memperlihatkan bagaimana dilakukan selection data seperti memilih salah satu kolom dengan nama tertentu. Memilih dengan mengirim baris dari baris yang dimaksud hingga baris yang ditentukan.

# Missing data

NaN sebagai penanda bahwa nilai hilang standar karena alasan kecepatan dan kenyamana komputasi, kita harus dapat dengan mudah mendeteksi nilai ini dengan data dari berbagai jenis yaitu:

* floating point
* integer
* boolean, dan 
* objek umum

Dalam pembahasan ini membahas mengenai missing data seperti menampilkan, menghapus, dan mengisi data.

# Operations

Operasi secara umum mengecualikan data yang hilang. Operasi yang dimaksud adalah statistik, apply, histogramming, string method.

# Merge

Pandas menyediakan berbagai fasilitas untuk dengan mudah menggabungkan objek Series dan DataFrame dengan berbagai jenis logika yang ditetapkan untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi join / merge - type.

# Grouping

Dengan "Group by", mengacu pada proses yang melibatkna satu atau lebih langkah - langkah berikut ini:

- **Splitting** -> data ke dalam kelompok berdasarkan beberapa kritesia.
- **Applying** -> fungsi untuk masing - masing kelompok secara mandiri
- **Combining** -> hasilnya menjadi struktur data

# Reshaping

Metode ini dirancang untuk bekerja dengan obejk MultiIndex. Berikut ini pada dasarnya apa yang dilakukan metode ini:

- stack -> "pivot" tingkat label kolom (mungkin hierarkis), mengembalikan DataFramem dengan indeks dengan label baris paling baru paling dalam.
- unstack -> (operasi invers tumpukan) "pivot" tingkat indeks baris (mungkin hierarkis) ke sumbu kolom, menghasilkan DataFrame yang dibentuk kembali dengan tingkat abru paling dalam label kolom. Fungsi `pivot_table()` dapat digunakan utnuk membuat tabel pivit gaya spreadsheet.

# Time series

Pandas berisi kemampuan dan fitur yang luas untuk bekerja dengan data deret waktu untuk semua domain. Menggunakan datum64 NumPy dan timedelta64 dtypes, pandas telah konsolidasikan sejumlah besar fitur dari pustaka Python lain seperti `scikits.timeseries` serta menciptakan sejumlah besar fungsi baru untuk memanipulasi data deret waktu.

# Categoricals

Categoricals adalah tipe data panda yang sesuai dengan variabel kategorikal dalam statistika. Variabel kategorikal mengembalikan sejumlah nilai yang mungkin terbatas (dan biasanya tetap, dalam kategori R).

```python
df = pd.DataFrame(

    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}

)
```

```python
df["grade"] = df["raw_grade"].astype("category")

df["grade"]
Out[125]: 
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): ['a', 'b', 'e']
```

```python
df["grade"].cat.categories = ["very good", "good", "very bad"]
```

```python
df["grade"] = df["grade"].cat.set_categories(

    ["very bad", "bad", "medium", "good", "very good"]

)



df["grade"]
Out[128]: 
0    very good
1         good
2         good
3    very good
4    very good
5     very bad
Name: grade, dtype: category
Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']
```

```python
df.sort_values(by="grade")
Out[129]: 
   id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
```

```python
df.groupby("grade").size()
Out[130]: 
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
```

# Plotting

```python
import matplotlib.pyplot as plt

plt.close("all")
```

```python
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

ts = ts.cumsum()

ts.plot();
```

```python
plt.show();
```

```python
df = pd.DataFrame(

    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]

)


df = df.cumsum()

plt.figure();

df.plot();

plt.legend(loc='best');
```

# Getting data in/out

# Gotchas

```python
if pd.Series([False, True, False]):

    print("I was true")
Traceback
    ...
ValueError: The truth value of an array is ambiguous. Use a.empty, a.any() or a.all().
```

Sumber by (https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html).