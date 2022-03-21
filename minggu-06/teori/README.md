# 8. Errors and Exceptions

Ada 2 jenis kesalahan yang dapat dibedakan : *syntax errors* dan *exceptions*.

## 8.1. Syntax Errors

Kesalahan sintaksis, juga dikenal sebagai keselahan *parsing*, mungkin merupakan jenis keluhan paling umum yang kita dapatkan saat kita masih belajar Python:

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

Pengurai *parser* mengulangi baris yang menyinggung dan menampilkan sedikit 'arrow' yang menunjuk pada titik paling awal di baris dimana kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token *preceding* panah: dalam contoh, kesalahan terdeteksi pada fungsi `print()`, karena titik dua (`':'`) hilang sebelum itu. Nama file dan nomor baris dicetak sehingga kita tahu ke mana harus mencari kalau - kalau masukan berasal dari skrip.

## 8.2. Exceptions

Bahkan jika suatu pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut *exceptions* dan tidak fatal tanpa syarat: kita akan segera belajar cara menanganinya dalam program Python.

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian ada berbagai jenis yang berbeda, dan tipe dicetak sebagai bagian dari pesan: tipe dalam contoh adalah **ZeroDivisionError, NameError** dan **TypeError**. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Ini berlaku untuk semua semua pengecualian bawaan, tertapi tidak harus sama untuk pengecualian yang dibuat pengguna(meskipun ini adalah konvesi yang bermanfaat). Nama pengecualian standar adalah pengindetifikasi bawaan (buka kata kunci yang dipesan *reserved keyword*)

## 8.3. Handling Exceptions

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pernyataan `try` berfungsi sebagai berikut:
* *try clause* (pernyataan(-pernyataan)di antara kata kunci `try` dan `except`) dieksekusi.
* Jika tidak pengecualian terjadi, *except clause* dilewati dan eksekusi pernyataan :keyword:*try* selesai.
* jika exception terjadi selama eksekusi klausa try, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan exceptions yang dinamai dengan kata kunci except, klausa kecuali dijalankan, dan kemudian eksekusi berlanjut setelah pernyataan try.
* Jika exceptions terjadi yang tidak cocok dengan exceptions yang disebutkan dalam *clause except*, itu diteruskan ke pernyataan try luar; jika tidak ada yang ditemukan, itu adalah exceptions yang tidak tertangani dan eksekusi berhenti dengan pesan.

Pernyataan *try* mungkin memiliki lebih dari satu except clause, utnuk menentukan penangan untuk exceptions yang berbeda. paling banyak penangan akan dieksekusi. penangan hanya menangani exceptions yang terjadi pada *try clause* yang sesuai, bukan pada penangan lain dari pernyataan try yang sama.

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

kelas dalam except clause cocok dengan exception jika kelasnya sama atau kelas dasarnya (tetapi bukan sebaliknya - clause yang mencantumkan kelas turunan tidka kompatibel dengan kelas dasar).

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Semua exceptions mewarisi dari **BaseException**, sheingga dapat digunakan untuk berfungsi sebagai wildcard. Gunakan ini dengan sangat hati - hati, karena mudha untuk menutupi kesalahan pemrograman yang sebenernya dengan cara ini! itu juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian menaikkan kembali exception (memungkinkan caller untuk emnangani exception juga)

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Pernyataan try... except memiliki clause opsional lain, yang, jika ada, harus mengikuti semua ... except clause. Ini berguna untuk kode yang ahrus dijalankan jika klausa try tidak menimbulkan exception.

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

penggunaan klausa else lebih baik daripada menambahkan kode tambahan ke klausa **try** karena klausa menghindari secara tidka sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh try... :except: !*except*.

Except clause dapat menentukan variabel setelah nama exception. Variabel terikat ke instance exception dengan argumen yang disimpan di `instance.args`. Untuk kenyamanan, instance exception mendefinisikan `_str_()` sehingga argumen dapat dicetak langsung tanpa harus merujuk .args. Seseorang juga dpaat membuat instantiate exception terlebih dahulu sebelum menaikkannya dan menambahkan atribut apapun yang diinginkan. 

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

Exception handlers tidak hanya menangani exception jika terjadi segera di *try clause*, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langusng) dalam try clause.

## 8.4. Raising Exceptions

Pernyataan *raise* memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi.

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu - satunya argumen untuk `raise` menunjukkan pengecualian yang dimunculkan. Ini harus berupa *instance* exception atau class exception (kelas yang berasal dari **exception**)

```python
raise ValueError  # shorthand for 'raise ValueError()'
```
```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5. Exception Chaining

Pernyataan *raise* memungkinkna opsional yang memungkinkan exception chaining.

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```
Ini bisa diguankan saat kira mengubah exception.

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```
Exception chaining terjadi secara otomatis ketika exception dinaikkan di dalam bagian kecuali atau akhir.

```python
try:

    open('database.sqlite')

except OSError:

    raise RuntimeError from None


Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

## 8.6. User-defined Exceptions
Program dapat memberi nama exception mereka sendiri dnegan membuat kelas exception baru. Exception biasanya berasal dari kelas **Exception**, baik secara langsung maupun tidak langusng.

## 8.7. Defining Clean-up Actions

Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang ahrus dijalankan dalam semau keadaan. 

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Jika ada klausa **finally**, klausa untuk finally akan dijalankan sebagai tugas terakhir sebelum pernyataan untuk **try** selesai. Klausa finally dapat berjalan baik atau tidak apabila pernyataan try menghasilkan suatu pengecualian. point berikut membahas kasus yang terjadi lebih kompleks ketika exception terjadi:

* Jika exception terjadi selama eksekusi klausa try, exception dapat ditangani oleh klausa *except*. Jika pengecualian tidak di tangani oelh klausa :keyword: !except, maka pengecualian dimunculkan kembali setelah klausa finally dieksekusi.
* Pengecualian dapat terjadi selama pelaksanaan klausa except atau else. Sekali lagi pengecualian akan mucnul kembali setelah klausa finally telah dieksekusi.
* Jika finally clause mengeksekusi pernyataan break, continue atau return, exceptions tidak dimunculkan kembali.
* Jika pernyataan kalusa untuk try mencapai klausa **break, continue** atay :keyword:'return' maka, pernyataan untuk klausa finally akan dieksekusi sebelum break, continue atau return dieksekusi.
* Jika klausa untuk :keyword:!finally' telah menyertakaan pernyataan return, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk finally dan dari klausa return, bukan niali dari try pernyataan untuk return.

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Klausa finally dieksekusi dalam peristiwa apapun. **TyoeError** yang ditimbulkan dengan membagi dua string tidak ditangani oleh klausa **except** dan karenanya kembali muncul setelah klausa finally telah dieksekusi.

## 8.8. Predefined Clean-up Actions

Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperluka, terlepas dari apakah operasi menggunakan objek berhasil atau gagal.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Pernyataan `with` memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dieksekusi, file *f* selalu ditutup, bahkan jika ada masalah saat pemrosesan baris - baris. Objek yang, seperti berkas - berkas, memberikan tindakna pembersihan yang telah ditentukan, akan menunjukkan ini dalam dokumentasinya.