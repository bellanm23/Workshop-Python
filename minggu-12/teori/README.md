# Pertemuan Minggu 12

# Struktur Data

## More on Lists
Berikut adalah semua metode daftar objek:

list. append(x)
Tambahkan item ke akhir daftar. Setara dengan a[len(a):] = [x].

list. extend(iterable))
Perpanjang daftar dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable.

list. insert(i, x)
Menyisipkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang sebelumnya untuk dimasukkan, sehingga a.insert(0, x) menyisipkan di bagian depan daftar, dan a.insert(len(a), x) setara dengan a.append(x).

list. remove(x)
Hapus item pertama dari daftar yang nilainya sama dengan x. Ini menimbulkan ValueError jika tidak ada item seperti itu.

list. pop([i])
Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() akan menghapus dan mengembalikan item terakhir dalam daftar.

list. clear()
Hapus semua item dari daftar. Setara dengan del a[:].

list. index(x[, mulai[, akhir]])
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Meningkatkan ValueError jika tidak ada item seperti itu.
list. count(x)
Kembalikan berapa kali x muncul dalam daftar.

list. sort(*, key=None, reverse=False)
Urutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan penyesuaian, lihat sorted() untuk penjelasannya).

list. reverse()
Membalikkan elemen-elemen daftar yang ada.

list. copy()
Kembalikan salinan daftar yang dangkal. Setara dengan a[:].

### Using Lists as Stacks
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari bagian atas tumpukan, gunakan pop() tanpa indeks eksplisit. 

### Menggunakan Daftar sebagai Antrean
ntuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out"); namun, daftar tidak efisien untuk tujuan ini. Sementara embel-embel dan pops dari akhir daftar cepat, melakukan sisipan atau pops dari awal daftar lambat (karena semua elemen lain harus digeser oleh satu).
Untuk menerapkan antrian, gunakan collections.deque yang dirancang untuk memiliki pelengkap dan pop cepat dari kedua ujungnya.

### List Comprehensions
Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan pada setiap anggota urutan lain atau dapat diederasi, atau untuk membuat subsequence dari elemen-elemen yang memenuhi kondisi tertentu.
Pemahaman daftar terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, kemudian nol atau lebih for atau if klausa. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks for dan if klausa yang mengikutinya. 

### Nested List Comprehensions
Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi sewenang-wenang, termasuk pemahaman daftar lain. Pemahaman daftar berikut akan mengubah baris dan kolom.


## Pernyataan del
cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kami lakukan sebelumnya dengan penetapan daftar kosong ke irisan). del juga dapat digunakan untuk menghapus seluruh variabel.


## Tuples dan Urutan
aftar dan string memiliki banyak properti umum, seperti operasi pengindeksan dan mengiris. keduanya adalah dua contoh tipe data urutan (lihat Tipe Urutan - daftar, tuple, rentang). Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple.

Tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, pada tuple output selalu tertutup dalam tanda kurung, sehingga tuple bersarang ditafsirkan dengan benar; mereka mungkin masukan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung diperlukan (jika tuple adalah bagian dari ekspresi yang lebih besar). Tidak mungkin untuk menetapkan ke item individu dari tuple, namun dimungkinkan untuk membuat tuple yang berisi objek yang dapat diubah, seperti daftar.
Meskipun tuple mungkin tampak mirip dengan daftar, mereka sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuple tidak berubah, dan biasanya berisi urutan elemen heterogen yang diakses melalui pembongkaran (lihat nanti di bagian ini) atau pengindeksan (atau bahkan dengan atribut dalam kasus namedtuples). Daftar dapat diubah, dan elemennya biasanya homogen dan diakses dengan mengulangi daftar.

Masalah khusus adalah pembangunan tuple yang berisi 0 atau 1 item: sintaks memiliki beberapa kebiasaan ekstra untuk mengakomodasi ini. Tuple kosong dibangun oleh sepasang tanda kurung kosong; tuple dengan satu item dibangun dengan mengikuti nilai dengan koma (tidak cukup untuk melampirkan nilai tunggal dalam tanda kurung). Jelek, tapi efektif. 


## Set
Python juga menyertakan tipe data untuk set. Satu set adalah koleksi yang tidak diurutkan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Mengatur objek juga mendukung operasi matematika seperti persatuan, persimpangan, perbedaan, dan perbedaan simetris.

Kawat gigi keriting atau fungsi set() dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, struktur data yang kita bahas di bagian berikutnya.


## Dictionaries
Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus (lihat Tipe Pemetaan - dict). Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "kenangan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh berbagai angka, kamus diindeks oleh kunci, yang dapat berupa jenis yang tidak berubah; string dan angka selalu bisa menjadi kunci. Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tuple; jika tuple berisi objek yang dapat diubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penetapan indeks, irisan tugas, atau metode seperti append() dan extend().
Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstraksi nilai yang diberikan kunci. Dimungkinkan juga untuk menghapus pasangan key:value dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci tersebut akan dilupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.
Melakukan list(d) pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, cukup gunakan sorted(d) sebagai gantinya). Untuk memeriksa apakah satu kunci ada di kamus, gunakan kata kunci in.


## Teknik Looping
Saat looping melalui kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan metode items()). Saat looping melalui urutan, indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi enumerate()). Untuk loop lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan zip()). Untuk loop atas urutan secara terbalik, pertama-tama tentukan urutan dalam arah maju dan kemudian memanggil fungsi reversed()). untuk memutar urutan dalam urutan yang diurutkan, gunakan fungsi sorted() yang mengembalikan daftar yang diurutkan baru sambil membiarkan sumber tidak berubah. Menggunakan set() pada urutan menghilangkan elemen duplikat. Penggunaan sorted() dalam kombinasi dengan set() di atas urutan adalah cara idiomatik untuk melingkari elemen unik dari urutan dalam urutan yang diurutkan.


## Lebih lanjut tentang Kondisi
Kondisi yang digunakan dalam while dan if pernyataan dapat berisi operator apa pun, bukan hanya perbandingan.

Operator perbandingan in dan not in adalah tes keanggotaan yang menentukan apakah suatu nilai ada di (atau tidak dalam) kontainer. Operator is dan is not membandingkan apakah dua objek benar-benar objek yang sama. Semua operator perbandingan memiliki prioritas yang sama, yang lebih rendah dari semua operator numerik.

Perbandingan dapat dirantai. Misalnya, a < b == c apakah a kurang dari b dan apalagi b sama dengan c.

Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas yang lebih rendah daripada operator perbandingan; di antara mereka, not memiliki prioritas tertinggi dan or terendah, sehingga A and not B or C setara dengan (A and (not B)) or C. Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.

Operator Boolean and dan or disebut operator sirkuit pendek: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika A dan C benar tetapi B salah, A and B and C tidak mengevaluasi ekspresi C. Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai pengembalian operator korsleting adalah argumen terakhir yang dievaluasi. Dimungkinkan untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel.


## Membandingkan Urutan dan Jenis Lainnya
Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan urutan leksografis: pertama dua item pertama dibandingkan, dan jika berbeda ini menentukan hasil perbandingan; jika sama, dua item berikutnya dibandingkan, dan seterusnya, sampai kedua urutan habis. Jika dua item yang akan dibandingkan adalah urutan sendiri dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan dibandingkan sama, urutan dianggap sama. Jika satu urutan adalah sub-urutan awal dari yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih rendah). Urutan leksiografis untuk string menggunakan nomor titik kode Unicode untuk memesan karakter individu.
membandingkan objek dari berbagai jenis dengan < atau > adalah legal asalkan objek memiliki metode perbandingan yang sesuai. Misalnya, tipe numerik campuran dibandingkan sesuai dengan nilai numeriknya, jadi 0 sama dengan 0,0, dll. Jika tidak, alih-alih memberikan pemesanan sewenang-wenang, penerjemah akan menaikkan pengecualian TypeError.
