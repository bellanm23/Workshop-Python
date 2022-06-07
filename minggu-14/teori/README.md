# Pertemuan 14

# An introduction to machine learning with scikit-learn

# Machine learning: the problem setting

Secara umum, masalah pembelajaran mempertimbangankan satu set n sampel data dan kemudian mencoba memprediksi sifat data yang tidak diketahui. Jika setipa sampel lebih dari satu angka dan misalnya entri multidimensi (data multivariat), dikatakan memiliki beberapa atribut atau fitur.

Learning problems terbagi dalam beberapa kategori yaitu:

1. **Supervised Learning**, dimana data dilengkapi dengan atribut tambahan yang ingin kami prediksi. Masalah ini dapat berupa:

- **Klasifikasi**, sampel milik dia atau lebih kelas dan ingin belajar dari data yang sudah berlabel bagaimana memprediksi kelas data yang tidak berlabel.
- **Regresi**, jika keluaran yang diinginkan terdiri dari satu atau lebih variabel kontinu, maka tugas tersebut disebut dengan regresi.

2. **Unsupervised learning**, dimana data pelatihan terdiri dari satu set vektor input x tanpa nilai target yang sesuai. Tujuannya memungkinkan untuk menemukan kelompok contoh serupa dalam data, yang disebut dengan **clustering**, atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai **density estimation**, atau untuk memproyeksikan data dari dimensi tinggi 2 dimensi dan 3 dimensi untuk tujuan *visualisasi*.

# Loading an example dataset

`scikit-learn` dilengkapi dengan beberapa kumpulan data standar, misalnya kumpulan data **iris** dan **angka** untuk klasifikasi dan kumpulan data diabetes untuk regresi.

Berikut ini, untuk memulai interpreter Python dari shell dan kemudian memuat `iris` dan `digits` set data. Konvensi notasi kami adalah yang `$` menunjukkan prompt shell semester `>>>` menunjukkan prompt bahasa Python:

```python
$ python
>>> from sklearn import datasets
>>> iris = datasets.load_iris()
>>> digits = datasets.load_digits()
```

Dataset adalah objek seperti kamus yang menyimpna semua data dan beberapa metadat tentang tersebut. Data ini disimpan dalam `.data` anggota, yang merupakan array. Rincian lebih lanjut kumpulan data yang berbeda dapat di temukan khusus `.n_samples, n_features .traget`. Kumpuulan data digit, `digits.data` memberikan akses ke fitur yang dapat digunakan untuk mengklasifikasikan sampe digit:

```pyhton
>>> print(digits.data)
[[ 0.   0.   5. ...   0.   0.   0.]
 [ 0.   0.   0. ...  10.   0.   0.]
 [ 0.   0.   0. ...  16.   9.   0.]
 ...
 [ 0.   0.   1. ...   6.   0.   0.]
 [ 0.   0.   2. ...  12.   0.   0.]
 [ 0.   0.  10. ...  12.   1.   0.]]
```

`digits.target` memberikan kebenaran dasar untuk kumpulan data digit, yaitu angka yang sesuai dengan setiap gambar digit yang kami coba pelajari:

```python
>>> digits.target
array([0, 1, 2, ..., 8, 9, 8])
```

**Bentuk array data**

Data selalu berupa larik 2D, bentuk, meskipun data asli mungkin memiliki bentuk yang berbeda. Dalam hal digit, setiap sampel asli adalah gamabr bentuk dan dapat diakses menggunakan: (n_samples, n_features)(8,8)

```python
>>> digits.images[0]
array([[  0.,   0.,   5.,  13.,   9.,   1.,   0.,   0.],
       [  0.,   0.,  13.,  15.,  10.,  15.,   5.,   0.],
       [  0.,   3.,  15.,   2.,   0.,  11.,   8.,   0.],
       [  0.,   4.,  12.,   0.,   0.,   8.,   8.,   0.],
       [  0.,   5.,   8.,   0.,   0.,   9.,   8.,   0.],
       [  0.,   4.,  11.,   0.,   1.,  12.,   7.,   0.],
       [  0.,   2.,  14.,   5.,  10.,  12.,   0.,   0.],
       [  0.,   0.,   6.,  13.,  10.,   0.,   0.,   0.]])
```

# Learning and predicting

Dalam kasus kumpulan data digit, tugasnya adalah memprediksi, dengan memberikan gambar, digit mana yang diwakilinya. `estimator` untuk dapat memprediksi kelas yang termasuk dalam sampel tak terlihat.

Dalam scikit-learn, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode dan `.fit(X, y) predict(T)`. Contoh estimator adalah kelas `sklearn.svm.SVC`, yang mengimplementasikan `support vector classification`. Konstruktor estimator mengambil parameter model sebagai argumen.

```python
>>> from sklearn import svm
>>> clf = svm.SVC(gamma=0.001, C=100.)
```

**Memilih parameter model**

Contoh ini, kita menetapkan nilai *gamma* secara manual. Untuk menemukan nilai yang baik untuk parameter ini, kita dapat menggunakna tools seperti **grid search** dan **cross validation**.

Instance estimator (`clf` untuk pengklasifikasi) pertama dipasang ke model yaitu harus belajar dari model. Ini dilakukan dengan meneruskan set pelatihan ke `fit` metode. Set pelatihan dengan `[:-1]` sintaks Python, yang menghasilkan array baru yang berisi semua kecuali item terakhir dari `digits.data`:

```python
>>> clf.fit(digits.data[:-1], digits.target[:-1])
SVC(C=100.0, gamma=0.001)
```

Memprediksi nilai baru dari `digits.data`.

```python
>>> clf.predict(digits.data[-1:])
array([8])
```

# Conventions

Scikit-learn estimator mengikuti aturan tertentu untuk membuat perilaku mereka lebih prediktif. 

## Type Casting

Kecuali ditentukan lain, masukan akan diberikan ke `float64`

```python
>>> import numpy as np
>>> from sklearn import kernel_approximation

>>> rng = np.random.RandomState(0)
>>> X = rng.rand(10, 2000)
>>> X = np.array(X, dtype='float32')
>>> X.dtype
dtype('float32')

>>> transformer = kernel_approximation.RBFSampler()
>>> X_new = transformer.fit_transform(X)
>>> X_new.dtype
dtype('float64')
```

Dalam contoh ini, `x` adalah `float32`, yang dilemparkan `float64` oleh `fit_transform(X)`. Target regresi diberikan `float64` dan target klasifikasi dipertahankan:

```python
>>> from sklearn import datasets
>>> from sklearn.svm import SVC
>>> iris = datasets.load_iris()
>>> clf = SVC()
>>> clf.fit(iris.data, iris.target)
SVC()

>>> list(clf.predict(iris.data[:3]))
[0, 0, 0]

>>> clf.fit(iris.data, iris.target_names[iris.target])
SVC()

>>> list(clf.predict(iris.data[:3]))
['setosa', 'setosa', 'setosa']
```

Pertama `predict()` mengembalikan array integer, karena `iris.target` (array integer) digunakan dalam `fit`. Kedua `predict()` mengembalikan array string, karena `iris.target_names` untuk pemasangan.

## Refitting and updating parameters

Hyper-parameters estimator dapat diperbarui setelah dibangun melalui metode **set_params()**. Memanggil `fit()` lebih dari sekali akan menimpa apa yang dipelajari oleh sebelumnya `fit()`:

```python
>>> import numpy as np
>>> from sklearn.datasets import load_iris
>>> from sklearn.svm import SVC
>>> X, y = load_iris(return_X_y=True)

>>> clf = SVC()
>>> clf.set_params(kernel='linear').fit(X, y)
SVC(kernel='linear')
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])

>>> clf.set_params(kernel='rbf').fit(X, y)
SVC()
>>> clf.predict(X[:5])
array([0, 0, 0, 0, 0])
```

Kernel default `rbf` pertama kali diubah menjadi `linear` via `SVC.set_params()` setelah estimator dibuat, dan diubah kembali ke `rbf` untuk menyesuaikan estimator dan membuat prediksi kedua.

## Multiclass vs. multilabel fitting

Pada saat menggunakan, tugas pembelajaran dan prediksi yang dilakukan bergantung pada format data target yang sesuai dengan **multiclass classifiers**

```python
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])
```

Dalam kasus diatas, pengklasifikasi cocok pada larik 1d dari label multikelas dan oleh `predict()` karena itu metode ini menyediakan prediksi multikelas yang sesuai. Dimungkinkan juga untuk menyesuaikan pada array 2d indikator label biner:

```python
>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```

Pengklasifikasi berada `fit()` pada representasi label biner 2d dari `y`, menggunakan **LabelBinarizer**. Dalam hal ini `predict()` mengembalikan array 2d yang mewakili prediksi multilabel yang sesuai. 

Perhatikan bahwa contoh keempat dan kelima mengembalikan semua nol, menunjukkna bawha mereka tidak cocok dengan tiga label `fit`. Dengan keluaran multilabel, sebuah instance juga dapat diberi beberapa label:

```python
>>> from sklearn.preprocessing import MultiLabelBinarizer
>>> y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
>>> y = MultiLabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```

Dalam hal ini, pengklasifikasi cocok pada instance yang masing - masing diberi beberapa label. Digunakan untuk binerisasi **MultiLabelBinarizer** array 2d dari multilabel ke `fit` atas. Akibatnya, `predict()` kembalikan larik 2d dengan beberapa label yang diprediksi untuk setiap instance.