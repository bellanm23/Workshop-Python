# 10. Brief Tour The Standard Library

## 10.1. Antarmuka Sistem

Modul ini os menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python310'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Ini akan menjaga agar tidak membayangi fungsi bawaan yang beroperasi jauh berbeda `import osfrom os import *` **os.open() open()**

Built-in `dir()` dan `help()` fungsi berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti *os*:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

Untuk tugas manajemen file dan direktori harian, `shutil` modul ini menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 10.2. File

Modul ini `glob` menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard:

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 10.3. Argumen Baris
SKrip utilitas umum sering kali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut *argv* **sys** modul sebagai daftar.

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

Modul ini **argparse** menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. 

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

Saat dijalankan pada baris perintah dengan, skripsi disetel ke dan ke `.python top.py --lines==5 alpha.txt beta.txtargs.lines5args.filenames['alpha.txt', 'beta.txt']

## 10.4. Error Output Redirection dan Penghentian

Modul **sys** ini juga memiliki atribut utnuk *stdin, stdout, dan stderr*. Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika *stdout* telah dialihkan:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

cara langsung untuk menghentikan skrip adalah dengan menggunakan `sys.exit()`.

# 10.5. Pencocokan Pola

Modul **re** menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. 

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

## 10.6. Matematika

Modul **math** memberikan akses ke fungsi pustaka C yang mendasari untuk matematika floating point:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

Modul **random** menyediakan alat untuk membuat pilihan acak:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

modul **statistics** menghitung properti statistik dasar (rata - rata, median, varians, dll) dari data numerik:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

Untuk proyek SciPy < [https://scipy.org](https://scipy.org/) > memiliki banyak modul lain untuk perhitungan numerik.

## 10.7. Akses Internet 

Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah [urlib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) untuk mengambil data dari URL dan [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) utnuk mengirimkan email:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

## 10.8. Tanggal dan Waktu

Modul [datetime](https://docs.python.org/3/library/datetime.html#module-datetime) menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Modul ini juga mendukung objek yang sadar zona waktu.

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 10.9. Kompresi Data

Pengarsipan data umum dan format kompresi secara langsung didukung oleh modul termasuk: [zzip](https://docs.python.org/3/library/zlib.html#module-zlib), [gzip](https://docs.python.org/3/library/gzip.html#module-gzip), [bz2](https://docs.python.org/3/library/bz2.html#module-bz2), [lzma](https://docs.python.org/3/library/lzma.html#module-lzma), [zipfile](https://docs.python.org/3/library/zipfile.html#module-zipfile), [tarfile](https://docs.python.org/3/library/tarfile.html#module-tarfile).

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 10.10 Pengukuran Kinerja

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekaatn yang berbeda utnuk masalah yang sama. Python menyediaakn alat pengukuran yang menjawab peratnyaan - pertanyaan itu dengan segera. Contohnya, mungkin tergoda utnuk menggunakan fitur pengepakan dan pembongkaran Tuple alih - alih pendekatan tradisonal untuk bertukar argumen. Modul [timeit](https://docs.python.org/3/library/timeit.html#module-timeit) dengan cepat menunjukkan keunggulan kinerja sederhana:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

Berbeda dengan [timeit](https://docs.python.org/3/library/timeit.html#module-timeit) tingkat granularitas yang bagus, modul `**profile**` dan `**pstats**` menyedaiakn alat untuk mengidentifikasi bagian kritis waktu dalam blok kode yang lebih besar.

## 10.11. Kontrol Kualitas

Modul [doctest](https://docs.python.org/3/library/doctest.html#module-doctest) menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program.

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

Modul [unittest](https://docs.python.org/3/library/unittest.html#module-unittest) ini tidak semudah [doctest](https://docs.python.org/3/library/doctest.html#module-doctest) modul, tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

## 10.12. Batteries Included

- Modul [xmlrpc.client](https://docs.python.org/3/library/xmlrpc.client.html#module-xmlrpc.client) dan [xmlrpc.server](https://docs.python.org/3/library/xmlrpc.server.html#module-xmlrpc.server) membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak ada pengetahuan langsung atau penanganan XML yang diperlukan.

- Paket [email] adalah perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnta. Dokumen pesan berbasis **RFC 2822**. Tidak seperti [smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib) dan [poplib](https://docs.python.org/3/library/poplib.html#module-poplib) yang beanr - benar mengirim dan menerima pesan, paket email memiliki perangkat langkap untuk membangun atau mendekode struktur pesan yang kompleks (termasuk lampiran) dan untuk menerapkan pengkodeaan internet dan protokol header.

- paket [json](https://docs.python.org/3/library/json.html#module-json) menyediakan dukungan kuat untuk menguraikan format pertukaran data populer ini. Modul [csv](https://docs.python.org/3/library/csv.html#module-csv) mendukung pembacaan dan penulisan file secara langsung dlama format Comma-Separated Value, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh `**xml.etree.ElementTree*`, `*xml.dom**`, dan `**xml.sax**` paket. Bersama - sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

- Modul [sqlite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3) adalah pembungkus untuk pustaka database SQLite, menyedaiakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

- Internasionalisasi didukung oleh sejumlah modul termasuk `**gettext**`, `**locale**`, dan `**codecs**` paket.


# 11. Brief Tour of the Standard Library — Part II

Modul ini jarang muncul dalam skrip kecil.

## 11.1 Output Formatting 

Modul `**reprlib**` menyediakan versi yang `**repr()**` disesuaikan untuk tampilan singkat wadah besar atau bersarang dalam:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

Modul `*pprint*` menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan objek yang ditentukan pengguna dengan cara yang dapat dibaca oleh penerjemah.

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

modul `**textwrap**` memformat paragref teks agar sesuai dengan lebar layar yang diberikan:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

Modul `**locale**` mengakses database format data spesifik budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung untuk memformat angka dengan pemisah grup:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

## 11.2 Templating

Modul `**string**` mencakup kelas serbaguna `**Template**` dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir. hal ini memungkinkan pengguna untuk menyesuaikan apliksi mereka tanpa harus mengubah aplikasi.

Formatnya menggunakan nama placeholder yang dibentuk `$` dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan kurung memungkinkan untuk diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis `$$` membuat satu pelarian `$`:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

Metode `**substitute()**` memunculkan a KeyErrorketika placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan `**safe_substitute()**` metodenya mungkin lebih tepat — ini akan membuat placeholder tidak berubah jika data tidak ada:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```
Subkelas template dapat menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

## 11.3. Working with Binary Data Record Layouts

Modul [struct](https://docs.python.org/3/library/struct.html#module-struct) menyediakan [pack()] (https://docs.python.org/3/library/struct.html#struct.pack) dan [unpack()](https://docs.python.org/3/library/struct.html#struct.unpack) berfungsi untuk bekerja dengan format record biner dengan panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan `**zipfile**` modul. Kemas kode `"H"` dan `"I"` mewakili dua dan empat byte nomor unsigned masing-masing. Ini `"<"` menunjukkan bahwa mereka adalah ukuran standar dan dalam urutan byte little-endian:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

## 11.4. Multi-threading

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Kode berikut menunjukkan bagaimana [threading](https://docs.python.org/3/library/threading.html#module-threading) modul tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

## 11.5. Logging

Modul [logging](https://docs.python.org/3/library/logging.html#module-logging) ini menawarkaan sistem logging berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke `sys.stderr`:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

Ini menghasilkan output berikut:

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

Secara default, pesan informasi dan debugging ditekan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk perutean pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih perutean yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.

Sistem logging dapat dikonfigurasi langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk logging yang disesuaikan tanpa mengubah aplikasi.

## 11.6. Weak References

Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah utnuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir dihilangkan. Modul [weakref](https://docs.python.org/3/library/weakref.html#module-weakref) menyediakan alat untuk melacak objek tanpa membuat referensi.

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
```

## 11.7. Tools for Working with Lists

Modul [array](https://docs.python.org/3/library/array.html#array.array) menyediakan [array()](https://docs.python.org/3/library/array.html#array.array) objek yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya lebih kompak. Contoh berikut menunjukkan larik angka yang disimpan sebagai dua byte angka biner tidak bertanda (typecode `"H"`) daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

Modul [collections](https://docs.python.org/3/library/collections.html#collections.deque) menyediakan [deque()](https://docs.python.org/3/library/collections.html#module-collections) objek yang seperti daftar dengan penambahan dan kemunculan yang lebih cepat dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

Selain implementasi daftar alternatif, perpustakaan juga menawarkan alat lain seperti [bisectmodul](https://docs.python.org/3/library/bisect.html#module-bisect) dengan fungsi untuk memanipulasi daftar yang diurutkan:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

Modul [heapq](https://docs.python.org/3/library/heapq.html#module-heapq) menyediakan fungsi untuk mengimplementasikan heap berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan pengurutan daftar lengkap:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```

## 11.8. Decimal Floating Point Arithmetic

Modul [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) menawarkan [Decimal](https://docs.python.org/3/library/decimal.html#module-decimal) tipe data untuk aritmatika titik mengambang desimal. Dibandingkan dengan [float](https://docs.python.org/3/library/functions.html#float) implementasi built-in dari floating point biner, kelas ini sangat membantu untuk:

- Aplikasi keuangan dan penggunaan lain yang memerlukan representasi desimal yang tepat,
- Kontrol atas presisi,
- Kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
- pelacakan tempat desimal yang signifikan, atau
- aplikasi di mana pengguna mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan dengan tangan.

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```
Hasilnya [Decimal](https://docs.python.org/3/library/decimal.html#module-decimal) tetap nol, secara otomatis menyimpulkan signifikansi empat tempat dari perkalian dengan signifikansi dua tempat. 

Representasi yang tepat memungkinkan [Decimal](https://docs.python.org/3/library/decimal.html#module-decimal) kelas untuk melakukan perhitungan modulo dan tes kesetaraan yang tidak cocok untuk floating point biner:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```

Modul [decimal](https://docs.python.org/3/library/decimal.html#module-decimal) menyediakan aritmatika dengan presisi sebanyak yang diperlukan:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```