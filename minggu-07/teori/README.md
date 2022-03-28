# 9. Classes

*Classes* atau kelas - kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Setiap instance dari class dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya. Instance dari sebuah class juga memiliki metode untuk memodifikasi kondisinya. Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambah kelas dengan minimum sintaksis dan semantik baru.

Ini adalah campuran dari mekanisme kelas yang ditemukan dalam C++ dan modula-3. Objek dapat berisi jumlah dan jenis data yang berubah - ubah. Dalam termologi C++, biasanya anggota kelas adalah public, dan semua fungsi anggota adalah *virtual*. Seperti dalam Smalltalk, kelas itu sendiri adalah objek .

Ini memberikan semantik untuk mengimport dan mengganti nama. Tidak seperti C++ dan modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C++, sebagai besar operator bawaan dengan sintaks khusus dapat didefinisikan ulang untuk instance kelas.

## 9.1. A Word About Names and Objects

Objek memiliki individualitas, dan banyak nama dapat terikat ke objek yang sama. Ini biasanya tidak dihargai pada pandangan pertama pada Python, dan dapat diabaikan dengan nama ketika berhadapan dengan tipe dasar yang tidak dapat diubah. Namun, *aliasing* memiliki efek yang mungkin mengejutkan pada semantik code Python yang melibatkan objek yang bisa berubah seperti daftar *list*, kamus *dictionary*, dan sebagian besar jenis lainnya.

## 9.2. Python Scopes and Namespaces

Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda tentang aturan ruang lingkup scope Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama *namespaces*, dan Anda perlu tahu bagaimana ruang lingkup dan ruang nama *namespaces* bekerja untuk sepenuhnya memahami apa yang terjadi. Kebetulan, pengetahuan tentang subjek ini berguna untuk programmer Python tingkat lanjut.

Sebuah *namespace* adalah pemetaan dari nama ke objek. Sebagian besar ruang nama *namespace* saat ini diimplementasikan sebagai kamus *dictionary* Python, tetapi itu biasanya tidak terlihat dengan cara apa pun , dan itu mungkin berubah di masa depan. Contoh ruang nama *namespace* adalah: himpunan nama bawaan (berisi fungsi seperti `abs()`). Dalam arti himpunan atribut suatu objek juga membentuk *namespace*. 


Ngomong-ngomong, saya menggunakan kata attribute untuk nama apa pun yang mengikuti titik --- misalnya, dalam ekspresi `z.real`, `real` adalah atribut dari objek `z` .

Dalam kasus terakhir, pemberian nilai ke atribut dimungkinkan. Atribut yang dapat ditulis `modname.the_answer = 42`, juga dapat dihapus dengan pernyataan `del`. Sebagai contoh, `del modname.the_answer` akan menghapus atribut **the_answer** dari objek yang dinamai oleh `modname`. 

Namespace dibuat pada saat yang berbeda dan memiliki masa hidup yang berbeda. Namespace yang berisi nama-nama bawaan dibuat ketika interpreter Python dimulai, dan tidak pernah dihapus. Pernyataan yang dieksekusi oleh pemanggilan *interpreter* tingkat atas, baik membaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut **__main__** sehingga mereka memiliki namespace global sendiri. 

Namespace lokal untuk suatu fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi kembali returns atau memunculkan pengecualian yang tidak ditangani dalam fungsi tersebut. Tentu saja, pemanggilan rekursif masing-masing memiliki ruang-nama namespace lokal mereka sendiri.

Suatu *scope* adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. "Directly accessible" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha menemukan nama tersebut di *namespace*. 

Meskipun cakupan scopes ditentukan secara statis, mereka digunakan secara dinamis. 

- Ruang lingkup *scope* terdalam, yang dicari pertama kali, berisi nama - nama lokal.
- Lingkup *scope* dari setiap fungsi penutup, yang dicari dimulai dengan lingkup penutup terdekat, berisi nama - nama non - lokal, tetapi juga non - global.
- Lingkup berikutnya *next-to-lash* berisi nama global modul saat ini.
- Ruang lingkup *scope* terluar (dicari terakhir) adalah *namespace* yang mengandung nama bawaan.

Jika sebuah nama dinyatakan global, maka semua referensi dan penugasan langsung ke lingkup scope tengah yang berisi nama global modul. Untuk mengembalikan variabel yang ditemukan di laur cakupan terdalam, pernyataan `nonlocal` dapat digunakan; jika tidak dideklarasikan nonlokal, variabel-variabel itu hanya baca-saja (upaya untuk menulis ke variabel seperti itu hanya akan membuat variabel lokal baru dalam cakupan terdalam, membiarkan variabel luar yang dinamai identik tidak berubah).

Biasanya, cakupan lokal merujuk nama lokal dari fungsi saat ini. Definisi kelas menempatkan namespace lain dalam lingkup lokal. Sebuah kekhasan khusus dari Python adalah bahwa -- jika tidak ada pernyataan global atau pernyataan nonlocal yang berlaku -- pemberian nilai untuk nama selalu masuk ke ruang lingkup terdalam. Pemberian nilai tidak menyalin data --- mereka hanya mengikat nama ke objek.

### 9.2.1. Scopes and Namespaces Example

Contoh yang menunjukkan cara mereferensikan lingkup *scopes* dan ruang nama *namespaces* yang berbeda, dan bagaimana **global** dan **nonlocal** memengaruhi pengikatan variabel:

```Python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
Hasil outputnya dari code diatas:
```Python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

## 9.3. A First Look at Classes

Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

### 9.3.1 Class Definition Syntax
```Python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
Definisi kelas, seperti definisi fungsi (pernyataan **def**) harus dieksekusi sebelum mereka memiliki efek.

### 9.3.2 class Objects

Objek kelas mendukung dua jenis operasi: referensi atribut dan instansiasi. *Attribute references* menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: `obj.name`. Nama atribut yang valid adalah semua nama yang ada di *namespace* kelas saat objek kelas dibuat.
```Python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

`MyClass.i` dan `MyClass.f` adalah referensi atribut yang valid, masing - masing mengembalikan integer dna objek fungsi. **__doc__** juga merupakan atribut yang valid, mengembalikan *docstring* milik kelas: `"A simple example class"`.

*instantiaton* kelas menggunakan notasi fungsi.
```Python
x = MyClass()
```
Membuat *instance* baru dari kelas dan menetapkan objek ini ke variabel lokal `x`.

```python
def __init__(self):
    self.data = []
```

```Python
x = MyClass()
```

```Python 
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3. Instance Objects
Data attributes sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan.

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

### 9.3.4. Method Objects

Biasanya, metode dipanggil tepat setealh itu terikat:

```python
x.f()
```

Dalam contoh MyClass, ini akan mengembalikan string `'hello world'`. Namun, tidak perlu memanggil metode segera: `x.f` adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu:

```python
xf = x.f
while True:
    print(xf())
```
Akan terus mencetak `hello world` hingga akhir waktu.

### 9.3.5. Class and Instance Variables

Variabel *instance* adalah untuk data unik untuk setiap instance dan variabel kelas adalah utnuk atribut dan metode yang dibagikan oleh semua *instance* kelas:

```Python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
```Python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Desain kelas yang benar harus menggunakan variabel *instance* sebagai gantinya:

```Python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```
## 9.4. Random Remarks

Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance
```Python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
Seringkali, argument pertama dari suatu metode disebut `self`.

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```
Sekarang `f`, `g`, dan `h` adalah semau atribut class C yang merujuk ke objek - objek fungsi, dan akibatnya semaunya adalah metode instance dari C -- `h` sama persis dengan `g`.

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen `self`:
```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

## 9.5 Inheritance
```Python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Nama *BaseClassName* harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi berubah-ubah arbitrary lainnya juga diperbolehkan.

```python
class DerivedClassName(modname.BaseClassName):
```
Eksekusi definisi kelas turunan menghasilkan sama seperti untuk kelas dasar. Tidak ada yang istimewa tentang instance kelas turunan: `DerivedClassName()` membuat instance baru di kelas. 

Python memiliki dua fungsi bawaan yang bekerja dengan warisan:
- Gunakan **ininstance()** untuk memeriksa jenis instance: `isintance(obj, int)` akan menjadi `True` hanya jika `obj.__class__` adalah **init** atau beberapa kelas yang diturunkan dari **init**.
- Gunakan **issubclass()** untuk memeriksa warisn kelas: `issubclass(bool, int) ``adalah ``True ` karena **bool** adalah subkelas dari **int**. Namun, `issubclass(float, int)` adalah `False` karena **float** bukan subkelas dari **int**.

### 9.5.1. Multiple Inheritance

Python mendukung bentuk pewarisan berganda. 
```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

## 9.6. Private Variables

Variabel instance "Private" yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Setiap pengidentifikasi dari bentuk `__spam` (setidaknya dua garis bawah utama, paling banyak satu garis bawah garis bawah) secara teks diganti dengan `_classname__spam`, di mana `classname`adalah nama kelas saat ini dengan garis(-garis) bawah utama dilucuti. Mangling ini dilakukan tanpa memperhatikan posisi sintaksis pengidentifikasi, asalkan terjadi dalam definisi kelas.

*Name mangling* sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass. 
```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

## 9.7. Odds and Ends

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
Kita dapat mendefinisikan kelas dengan metode *read()* dan *readline()* yang mendapatkan data dari buffer string sebagai gantinya, dan meneruskan itu sebagai argumen. metode instance memiliki atribut, juga: `m.__self__` adalah objek instan dengan metode *m()*, dan `m.__func__`adalah objek fungsi yang sesuai dengan metode tersebut.

## 9.8. Iterators

Sekarang kita mungkin telah memperhatikan bahwa sebagian besar objek penampungan *container* dapat dibuat perulangan menggunakan pernyataan **for**:
```Python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 9.9. Generators

**Generators** adalah sebuah  tool yang sederhana dan simpel untuk membuat sebuah iterasi. Itu ditulis seperti fungsi biasa tapi menggunakan pernyataan **yield** setiap kali ingin mengembalikan sebuah data. Tiap kali **next()** itu dipanggil, generators tersebut akan melanjutkan di mana hal itu berhenti (itu akan mengingat semua nilai dan pernyataan mana yang terakhir dieksekusi).

```Python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```

```Python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

## 9.10. Generator Expressions
Beberapa pembangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar list comprehensions setara.

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```
