# 6. Modules
Jika kita berhenti *interpreter* Python dan memasukkannya lagi, definisi yang kita buat (fungsi dan variabel) akan hilang. Karena itu, jika kita ingin menulis program yang agak lebih panjang, kita lebih baik menggunakan editor teks untuk menyiapkan input bagi penerjemah dan menjalankannya dengan file itu sebagai input. ini dikenal sebagai membuat script. 

Untuk mendukung ini, Python memiliki cara untuk meletakkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari *interpreter*. File seperti itu disebut dengan *module*; definisi dari modul dapat *imported* ke modul lain atau ke modul *main* (kumpulan variabel yang kita memiliki akses ke dalam skrip yang dieksekusi di tingkat atas dan dalam mode kalkulator).

Modul adalah file yang berisi defini dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran `.py`. Nama modul (sebagai string) tersedia sebagai nilai variabek global `_name_`. contoh `fibo.py`.

Untuk masuk interpreter Python dan import modul dengan perintah : `import fibo`

## 6.1. Lebih lanjut tentang modul
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya pertama kali nama modul ditemui dalam pernyataan import.

Setiap modul memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, penulis modul dapat menggunakan variabel global pengguna. Di sisi lain, jika kita tahu apa yang kita lakukan, kita dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, `modname.itemname.`

Modul dapat mengimport modul lain. Biasanya, tetapi tidak diperlukan untuk menempatkan semua pernyataan **import** di awal modul. Nama - nama modul yang diimport ditempatkan di tabel simbol global modul impor. Ada varian dari pernyataan **import** yang mengimport nama dari modul langsung ke tabel simbol modul impor.

ini mengimpor semua nama kecuali yang dimulai dengan garis bawah (`_`). Dalam kebanyakan kasus, programmer Python tidak menggunakan fasilitas ini karena ia memperkenalkan sekumpulan nama yang tidka diketahui ke dalam *interpreter*, mungkin menyembunyikan beberapa hal yang sudah kita definisikan.

Secara umum praktik mengimpor `*` dari modul atau paket tidak disukai, karena sering menyebabkan kode yang kurang dapat di baca. Namun, boleh saja menggunakannya untuk menghemat pengetikan di sesi interaktif. Jika nama modul diikuti oleh **as**, maka nama setelah **as** terikat langsung ke modul yang diimpor.

Ini secara efektif mengimport modul dengan cara yang sama dengan `import fibo` akan dilakukan, dengan satu - satunya perbedaan adalah `fib`. itu juga dapat digunakan ketika menggunakan `from` dengan efek yang sama.

[^Catatan: Untuk alasan efisiensi, setiap modul hanya diimport satu kali per sesi *interpreter* -- atau, jika hanya satu modul yang ingin kita uji secara interaktif, gunakan `importlib.reload()`, mis. `import importlib; importlib.reload(modulename)`]

### 6.1.1. Mengoperasikan modul sebagai skrip
Ketika kita mengoperasikan modul Python dengan 

```
pyhton fibo.py <arguments>
```
Kode dalam modul akan dieksekusi, sama seperti jika kita mengimportnya, tetapi dengan `__name__ diatur ke "__main__"`. itu berarti bahwa dengan menambahkan kode ini diakhir modul kita.

```
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
Kita dapat membuat berkas dapat digunakan sebagai script dan juga modul yang dapat diimpor, karena kode yang mengurai *parsing* barus perintah hanya beroperasi jika modul dieksekusi sebagai berkas "main":

```
import fibo
```
Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul sebagai script mengeksekusi rangkaian pengujian)

### 6.1.2. Jalur Pencarian Modul
Ketika sebuah modul bernama *spam* diimpor, *interpreter* pertama - tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, ia kemudain mencari berkas bernama `spam.py` dalam daftar direktori yang diberikan oleh variabel `sys.path.sys.path` diinisialisasi dari lokasi ini:

- direktori yang berisi script masukkan (atau direktori saat ini ketika tidak ada file ditentukan).
- `PYTHONPATH`(daftar nama direktori, dengan sintaksis yang sama dengan variabel shell `PATH`).
- The installation - dependent default(by convention including a *site-packages* directory, handled by the *site* module)

Setelah inisialisasi, program pyhton dapat memodifikasi: data :*sys.path*. Direktori yang berisi script yang dijalankan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar. 

### 6.1.3. Berkas Python "Compiled"
Untuk mempercepat memuat modul, Python menyimpan *cache* versi tekompilasi dari setiap modul di direktori `__pycache__` dengan nama `module. version.pyc`, dimana versi menyandikan format berkas terkompulasi; umumnya berisi nomor versi Python.

Python tidak memeriksa *cache* dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, itu tidak memeriksa *cache* jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (dikompilasi saja), modul yang dikompilasi harus ada di direktori sumber, dan tidka boleh ada modul sumber. Ada beberapa tips untuk para ahli yaitu:

1. Kita dapat menggunakan `-O` atau `-OO` mengaktifkan perintah Python untuk mengurangi ukuran modul yang dikompilasi. Saklar `-O` menghapus pernyataan tegas *assert*, saklar `-OO` menghapus pernyataan tegas *assert* dan string __doc__. karena beberapa program bergantung pada ketersediaannya, kita hanya boleh menggunakan opsi ini jika kita tahu apa yang kita lakukan . Modul "Optimized" memiliki tag `opt-` dan biasanya lebih kecil. Rilis di masa depan dapat mengubah efek pengoptimalan.
2. Suatu program tidak berjalan lebih cepat ketika itu dibaca dari file `.pyc` daripada ketika itu dibaca dari fiel `.py`; satu - satunya hal yang lebih cepat tentang berkas `.pyc` adalah kecepatan memuatnya.
3. Modul `compileall` dapat membuat berkas.pyc untuk semua modul dalam direktori.
4. Ada detail lebih lanjut tentang proses ini, termasuk bagan alaur keputusan di **PEP 3147**.

## 6.2. Modul Standar
Python dilengkapi dengan pustaka modul standar, yang dijelaskna dalam dokumen terpisah, Referensi Pustaka Python ("Library Reference" hereafter). Beberapa modul dibangun ke dalam interpreter; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti pemanggilan sistem. 

Modul `winreg` hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: `sys`, yang dibangun ke dalam setiap interpreter Pyhton. variabel `sys.ps` dan `sys.ps2` menentukan string yang digunakan sebagai prompt primer dan sekunder.

variabel `sys.path` adalah daftar string yang menentukan jalur pencarian *interpreter* untuk modul. ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan **PYTHONPATH**, atau dari bawaan jika **PYTHONPATH** tidak disetel.

## 6.3 Fungsi dir()
Fungsi ini digunakan untuk mencari tahu nama - nama yang ditentukan oleh modul. ia mengembalikan *list* string yang diurutkan.

Tanpa argumen, **dir()** mencantumkan nama yang telah kita tentukan saat ini. Perhatikan bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll. `dir()` tidak mencantumkan nama fungsi dan veriabel bawaan. Jika kita ingin daftar itu, mereka didefinisikan dalam modul standar `builtins`

## 6.4 Packages
Paket adalah cara penataan *namespace* modul Python dengan menggunakan "dotted module names". Misalkan kita ingin merancang koleksi modul ("paket) untuk penanganan berkas suara dan data suara yang seragam. Ada banyak format berkas suara yang berbeda (biasanya dikenali oleh ekstensi mereka, misalnya: `.wav`, `.aiff`, .`.au`), jadi kita mungkin perlu membuat dan memelihara koleksi modul yang terus bertambah untuk konversi antara berbagai format file. Ada juga banyak operasi berbeda yang mungkin ingin kita lakukan pada data suara (seperti mencampur, menambahkan gema, menerapkan fungsi equalizer, menciptakan efek stereo buatan), jadi selain itu kita akan menulis aliran modul tanpa henti untuk melakukan operasi ini.

Saat mengimport package, Python mencari melalui direktori pada `sys.path` mencari subdirektori package. Berkas `__init__.py` diperlukan untuk membuat Python memperlakukan direktori yang berisi file sebagai paket. Ini mencegah direktori dengan nama umum, seperti `string`, menyembunyikan modul valid yang muncul kemudian pada jalur pencarian modul. Dalam kasus yang paling sederhana, :file:*__init__.py* dapat berupa file kosong, tetapi jika dapat menjalankan kode inisialisasi untuk paket atau mengatur variabel `__all__`.

Ketika menggunakan `from package import item`, item tersebut dapat berupa submodul (atau subpaket) dari paket, atau beberapa nama lain yang ditentukan dalam paket, seperti fungsi, kelas atau variabel. 

### 6.4.1. Mengimport * Dari Paket
Satu - satunya solusi adalah bagi pembuatan paket untuk memberikan indeks pada secara eksplisit. Pernyataan `import` menggunakan konvensi berikut:
- Jika suatu paket punya kode `__init__.py` yang mendefinisikan daftar bernama `__all__`, itu diambil sebagai daftar nama modul yang harus diimpor ketika `from package import*` ditemukan. 

### 6.4.2. Referensi Intra-paket
Ketika paket disusun menjadi subpaket(seperti pada paket **sound** pada contoh), kita dapat menggunakan impor absolut untuk merujuk pada submodul of siblings packages. contohnya jika modul `sound.filters.vocoder` perlu menggunakan modul `echo` dalam paket `sound.effects`, ia dapat menggunakan `from sound.effects import echo`.

Kita juga dapat menulis import relatif, dengan bentuk `from module import name` pada pernyataan impor. Impor ini menggunakan titik - titik di awalan untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif. Dari modul **surround**.

### 6.4.3. Paket di Beberapa Direktori
Paket mendukung satu atribut khusus lagi, `__path__`. ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan file paket: *__init__.py* sebelum kode dalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi; hal itu memengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket. Meskipun fitur ini tidak sering dibutuhkan, fitur ini dapat digunakan untuk memperluas rangkaian modul yang ditemukan dalam suatu paket.