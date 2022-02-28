# Data Structures

## 5.1 Membahas mengenai lebih lanjut tentang Daftar Lists
Tipe data daftar *list* memiliki beberapa metode dari objek daftar *list* sebagai berikut:

1. **list.append(x)** -> menambahkan objek objek ke daftar *list*. setara dengan `a[len(a):] [x]`.
2. **list.extend(*iterable*)** -> perpanjang daftar *list* dengan menambahkan semua item dari *iterable* Setara dengan `a[len(a):] = iterable`.
3. **list.insert(i,x)** -> dimana akan memasukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum memasukkan, jadi `a.insert(0, x)` dimasukkan di bagian depan daftar *list*, dan `a.insert(len(a), x) sama dengan a.append(x).
4. **list.remove(x)** -> digunakan untuk menghapus item pertama dari daftar list yang nilainya sama dengan *x*. maka akan memunculkan `ValueError` jika tidak ada item seperti ini.
5. **list.pop([i])** -> digunakan untuk menghapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, maka `a.pop()` menghapus dan mengembalikan item terakhir dalam daftar.
6. **list.clear()** -> digunakan untuk menghapus semua item dari daftar list. Sama dnegan `del a[:]`
7. **list.index(x[,start[,end]])** -> untuk kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan *x*. Akan muncul `ValueError` jika tidak ada item seperti ini. 
8. **list.count(x)** -> jumlah pengembalian berapa kali *x* muncul dalam daftar.
9. **list.sort(*,key=Nona, reverse=False)** -> mengurutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan ubah sesuai *customization*)
10. **list.reverse()** -> mengembalikan elemen daftar *list* di tempatnya.
11. **list.copy()** -> mengembalikan salinan daftar list yang dangkal. Setara dengan `a[:]`

### 5.1.1. Menggunakan Daftar Lists sebagai Tumpukan stacks

Metode daftar membuat sangat mudah untuk menggunakan daftar *lust* sebagai tumpukan *stack*. dimana elemen terakhir yang ditambahkan adalah elemen pertama yang akan diambil atau bisa kita sebut sebagai **last-in, first-out**. 

- **append()** -> digunakan untuk menambahkan item ke atas tumpukan (stack).
- **pop() tanpa indeks eksplisit** -> digunakan untuk mengambil item dari atas tumpukan. 

### 5.1.2. Menggunakan Daftar Lists sebagai Antrian *Queues*

Memungkinkan untuk menggunakan daftar sebagai antria, dimana elemen pertama yang ditambahkan adalam elemen yang diambil yang kita sebut sebagai **first-in, first-out** namun, daftar kurang efisien untuk tujuan ini. 

Untuk mengimplementasikan antrian, kita bisa menggunakan `collections.deque` yang dirancang utnuk menambahkan dan muncul dengan cepat dari kedua ujungnya.

### 5.1.3. Daftar List Comprehensions

Daftar List Comprehensions menyediakan cara singkat untuk membuat daftar. Dalam daftar ini terdiri dari tanda kurung yang berisi ekspresi kemudian diikuti oleh klausa **for**, lalu nol atau lebih klausa **for** atau **if**.

### 5.1.4 Pemahaman Daftar List Comprehensions Bersarang

Ekspresi awal dapat berupa ekspresi acak *arbitrary*, termasuk pemahaman daftar *list comprehension* lainnya. *listcomp* bersarang dievaluasi dalam konteks `for` yang mengikutinya.

## 5.2 Pernyataan *del*

Pernyataan ini berbeda dengan metode `pop()` yang mengembalikan nilai. Tetapi metode ini juga dapat digunakan sebagai menghapus irisan dari daftar *list* atau menghapus seluruh daftar *list*. Selain itu juga dapat digunakan utnuk menghapus seluruh variable.

## 5.3 Tuples dan Urutan Sequences

Ada 2 contoh tipe data *sequence* yaitu `list, tuple, rangr`. Karena Python merupakan bahasa pemrograman yang berkembang, maka tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lain yaitu *tuple*. Walaupun *tuple* mungkin mirip dnegan daftar, *tuple* sering digunakan dalam situassi yang berbeda dan untuk tujuan yang berbeda. *Tuple* adalah **immutable**, dan biasanya berisi urutan elemen yang heterogen yang diakses melalu *unpacking* atau pengindeksan.

## 5.4. Himpunan Set

Python juga menyertakan tipe data untuk *sets*. Himpunan atau *Set* adalah koleksi yang tidak terurutkan tanpa elemen duplikat. 

kurung kurawal atau fungsi `set()` dapat digunakan untuk membuat himpunan. 

## 5.5 Kamus Dictionaries

Kamus dictionary terkadang ditemukan dalam bahasa lain sebagai **"assosiative memories"** atau **"assosiative array"**. Tidak seperti urutan *sequences*, yang diindeks oleh sejumlah angka, kamus *dictionary* diindeks oleh *keys*, yang dapat berupa jenis apa pun yang tidak dapat diubah *immutable type*, string dan angka sellau bisa menjadi kunci *key*. *Tuples* dapat digunakan sebagai kunci jika hanya berisi string, angka, atau *tuple*, jika sebuah tuple berisi objek yang bisa berubah baik secara langsung atau tidak maka tidak dapat digunakan sebagai kunci *key*. Untuk memeriksa apakah ada satu kunci dalam kamus, gunakan kata kunci `in`.

## 5.6 Teknik Perulangan

Pada saat mengulang kmaus *dictionaries*, kunci *key* dan nilai *value* terkait dapat diambil pada saat yang sama menggunakan metode `items()`. Ketika mengulang melalui urutan, indeks posisi dan nilai terkait dapat diambil pada saat yang sama dengan menggunakan fungsi `enumerate()`. Untuk mengulang urutan secara terbalik, pertama tentukan urutan dalam arah maju dan kemudian panggil Fungsi `reversed()`. Jika ingin mengulai sebuah urutan *sequence* dalam susunan yang diurutkan, gunkana fungsi `sort()` yang mengembalikan daftar terurut baru dnegan membiarkan sumber tidak diubah.

## 5.7. Lebih lanjut tentang Kondisi

Dalam kondisi yang digunakan dalam pernyataan `while` dan `if` dapat berisi operator apapun, bukan hanya perbandingan. Perbandingan bisa dibuat berantai, perbandingan juga dapat digabungkan menggunakan operator Boolean `and` dan `or` dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan `not`. Operator Boolean `and` dan `or` disebut sebagai operator *short-circuit*, argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti setelah hasilnya ditentukan.

## 5.8. Membandingkan Urutan Sequences dan Jenis Lainnya.

Objek urutan *sequence* biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan *lexicographical* pertama 2 item pertama dibandingkan, dan jika mereka berbeda ini menentukan hasil perbandingan, dan jika mereka sama, 2 item berikutnya dibandingkan, dan seterusnya, sampai urutan dimana pun habis. 