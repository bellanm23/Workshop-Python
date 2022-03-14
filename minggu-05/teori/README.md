# 7. Input and Output

Ada beberapa cara untuk mempresentasikan keluaran / output suatu program. Data dapat dicetak dalam bentuk yang dapat dibaca oleh kita, atau ditulis ke berkas untuk digunakan di masa mendatang.

## 7.1. Fancier Output Formatting

Kita telah menemukan 2 cara penulisan nilai: *expression statements* dan fungsi **fungsi()**. Cara ketiga menggunakan **write()** metode objek berkas, berkas standar keluaran dapat dirujuk sebagai `sys.stdout`. Ada beberapa cara untuk memformat output:

* Untuk menggunakan **formatted string literals**, mulailah string dengan `f` atau `F` sebelum tanda kutip pembuka atau tanda kutip tigas. Di dalam string ini, kita bisa menulis ekspresi Python antara karakter `{` dan `}` yang dapat merujuk ke variable atau nilai literal.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

* Metode `str.format()` dari string membutuhkan lebih banyak upaya manual. Kita masih akan menggunakan `{` dan `}` untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformaatn terperinci, tetapi kita juga harus memberikan informasi yang akan diformat.

```python
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%' 
```

* Kita dapat melakukan semua string yang menangani diri kita sendiri dengan menggunakan operasi *slicing* stringg dan *concatenation* untuk membuat tata letak yang dapat kita bayangkan. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk string *padding* ke lebar kolom yang diberikan.

Jika kita hanya membutuhkan keluaran yang menarik tetapi hanya ingin tampilan cepat dari beberapa variable untuk keperluan debugging, kita dapat mengkonversi nilai apapun menjadi string dengan menggunakan fungsi `repr()` atau `str()`.

Fungsi `str()`, untuk mengembalikan representasi nilai - nilai yang terbaca oleh manusia, sedangkan `repr()`, untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau memaksa `SyntaxError` jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, `str()` akan mengembalikan nilai yang sama dengan `repr()`. 

### 7.1.1. Literal String Terformat

**Formatted string literals** (disebut f-string) memungkinkan kita menyertakan nilai ekspresi Python di dalam string dengan mengawali string dengan `f` atau `F` dan menulis ekspresi sebagai `{expression}`. Penentuan format opsional dapat mengikuti ekspresi. ini memungkinkan kontrol yang lebih besar atas bagaimana nilai diformat.

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

Melewatkan bilangan bulat setelah `:` akan menyebabkan *field* itu menjadi jumlah minimum lebar karakter. ini berguna utnuk membuat kolom berbaris.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

Pengubah lain dapat digunakan untuk mengkonversi nilai sebelum diformat. `!a` berlaku **ascii()**, `!s` berlaku **str()**, dan `!r` berlaku **repr()**:

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

### 7.1.2. Metode String format()

Penggunaan dasar metode **str.format()**:

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

Tanda kurung dna karakter di dalamnya (disebut *fields* format) diganti dengan objek yang diteruskan ke metode **str.format()**. ANgka dalam tanda kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam metode **str.format()**.

```python
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

Jika argumen *keyword argument* digunakan dalam metode **str.format()**, nilainya dirujuk dengan menggunakan nama argumen.

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

Untuk argumen posisi dan kata kunci dapat dikombinasikan secara bergantian:

```python
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
```

Jika kita memiliki string format yang panjang yang tidak ingin kita pisahkan, maka kita lebih baik menggunakan *dict* dan menggunakan tanda kurung siku `[]` untuk mengakses kunci dari *dict*.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Kita juga bisa memberikan table sebagai argumen *keyword argument* dengan notasi `**`.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

Ini sangat berguna dalam kombinasi dengan fungsi bawaan `vars()`, yang mengembalikan *directionary* yang berisi semua variable loka.

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

### 7.1.3. Pemformatan String Manual

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```

`print()`, digunakan sebagai menambah spasi di antara argumennya. Metode `str.rjust()` dari objek string meratakan kanan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri. Ada juga metode yang sama yaitu: `str.ljust()` dan `str.center()`. 

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
```

### 7.1.4. Pemformatan string lama

Operator % (modulo), digunakan untuk pemformatan string. Dimana diberikan `'string' % values` dari `%` in string diganti dengan nol atau elemen yang lebih dari `values`. Operasi ini umumnya dikenal sebagai interpolari string.

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

## 7.2. Membaca dan Menulis Berkas

`open()` digunakan untuk mengembalikan sebuah **file object**, dan paling umum digunakan dengan 2 argumen `open(filename, mode)`.

```python
>>> f = open('workfile', 'w')
```
Dimana kita bisa melihat pada script diatas, untuk argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi karakter yang menggambarkan cara berkas akan digunakan. 

1. Mode `r`, digunakan hanya untuk dibaca.
2. mode `w`, hanya untuk menulis (berkas yang ada dengan nama yang sama akan dihapus).
3. `a`, digunakan utnuk membuka berkas untuk ditambahkan, setiap data yang ditulis ke file secara otomatis ditambahkan ke bagian akhir.
4. `r+`, digunakan untuk diasumsikan jika dihilangkan.

`b` ditambahkan ke mode membuka berkas di *binary mode*, sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak mengandung teks.

Dalam mode teks, standar saat membaca adalah mengkonversi akhir baris spesifik platform (`\n` pada Unix, dan `\r\n` pada Windows) menjadi hanya `\n`. Modifikasi di balik layar ini untuk mengarsipkan data baik untuk file teks, tetapi akan merusak data biner seperti itu di `JPEG` atau `EXE`. Jadi jika kita menggunakan mode biner untuk saat membaca dan menulis harus berhati - hati. 

Ketika kita menggunakan kata kunci **with** saat berurusan dengan objek file itu sangat baik. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaiannya selesai, bahkan jika suatu pengecualian muncul di beberapa titik. Selain itu juga menggunakan **with** jauh lebih pendek daripada penulisan yang setara dengan **try**-blok **finally**

```python
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

JIka kita tidak menggunakan kata kunci **with**, maka kita harus menggunakan `f.close()` untuk menutup file dan membebaskan sumber data sistem yang digunakan secara langsung.

> Peringatan: Memanggil `f.write()` tanpa menggunakan kata kunci `with` atau memanggil `f.close()` **dapat** menyebabkan argumen - argumen dari `f.write()` tidak dituliskan ke dalam *disk* secara utuh, meskipun program berhenti dengan sukses.

Setelah objek file ditutup, baik dengan pernyataan **with** atau dengan memanggil `f.close()`, upaya untuk menggunakan objek file akan secara otomatis gagal.

```python
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

### 7.2.1. Metode Objek Berkas

Pada contoh - contoh diatas telah menganggap bahwa objek berkas bernama `f` telah dibuat. Untuk membaca konten file, apnggil `f.read(size)`, yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). *size* merupakan argumen numerik opsional. Ketika *size* dihilangkan atau negatid, seluruh isi file akan dibaca dan dikembalikan. itu masalah kita jika file tersebut dua kali lebih besar dari memori penyimpanan pada perangkat kita. Kalau tidak, paling banyak *size* karakter (dalam mode teks) atau *size* byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, maka `f.read()` akan mengembalikan string kosong (`''`)

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```

`f.readline()`, digunakan untuk membaca satu baris dari file, karakter barus baru (`\n`) dibiarkan diakhir string, dan hanya dihapus pada baris terakhir file jika file tidak berakhir pada baris abru. `f.readline()`, juga digunakan untuk mengembalikan string kosong, akhir file telah tercapai, sementara baris kosong diwakili oleh `\n`, string yang hanya berisi satu baris baru.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
```

Untuk membaca baris dari file, kita dapat mengulangi objek berkas. Ini digunakan untuk menghemat memori, cpeat dan mengarah ke kode yang sederhana.

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
```

Jika kita ingin membaca semua baris file dalam daftar *list*, kita bisa menggunakan `list(f)` atau `f.readlines()`.

`f.write(string)`, menulis konten *string* ke berkas, mengembalikan jumlah karakter yang kita tuliskan.

```python
>>> f.write('This is a test\n')
15
```

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
```

`f.tell()`, digunakan untuk mengembalikan integer yang memberikan posisi file saat ini dalam berkas yang direpresentasikan sebagai jumlah byte dari awal berkas ketika dalam mode biner dan angka buram *opaque* ketika dalam mode teks.

Kemudian untuk mengubah posisi file, gunakan `f.seek(offset, whence)`. Posisi dihitung dari menambahkan *offset* ke titik referensi, titik referensi dipilih oleh argumen *whence*. Nilai A *whence* dari 0 mengukur dari awal berkas, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. *whence* dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referenci.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
```

### 7.2.2. Menyimpan data terstruktur dengan json

String daoat dengan mudah ditulis dan dibaca dari file. ANgka membutuhkan sedikit usaha, karena metode **read()** hanya mengembalikan string, yang ahrus diteruskan ke fungsi seperti **int()**, yang mengambil string seperti `123` dan mengembalikan nilai numerik 123. 

Karena pengguna terus - menurus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke berkas, Python memungkinkan kita untuk menggunakan format pertukaran data populer yang disebut dengan **JSON (JavaScript Object Notation)**. Modul standar bernama json dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serializing. Merekonstruksi data dari representasi string disebut deserializing. Antara serializing dan deserializing, string yang mewakili objek mungkin telah disimpan dalam berkas atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.

```python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```

fungsi `dumps()`, dengan mudah membuat serialisasi objek menjadi :term: *text file*. Jadi jika `f` adalah objek **text file** dibuka untuk menulis, kita dapat melakukan ini:

```
json.dump(x, f)
```

Untuk menerjemahkan decode objek lagi, jika `f` adalah objek text file yang telah dibuka untuk membaca:

```
x = json.load(f)
```

Teknik serialisasi sederhana ini dapat menangani daftar list dan dictionary, tetapi membuat serialisasi instance kelas yang berubah-ubah arbitrary di JSON membutuhkan sedikit usaha ekstra.