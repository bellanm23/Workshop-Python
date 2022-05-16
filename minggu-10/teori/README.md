# Build a Python App with CockroachDB and psycopg2

**Langkah 1. Start CockroachDB**

## Use CockroachDB Serverless (beta)

**Buat Cluster gratis**

1. JIka kita belum melakukannya, daftar akun CockroachDB Cloud.
2. Masuk ke akun CLoud CockroachDB.
3. Pada Halaman Cluster, klik buat cluster.
4. Pada halaman buat cluster, pilih tanpa Server
5. Klik Buat Cluster.

**Buat Pengguna SQL**

1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik buat dan simpan kata sandi.
3. Salin kata sandi yang dihasillkan dan disimpan.
4. Klik berikut.

**Daparkan String Koneksi**

Buka bagian **General connection string**, lalu salin connection string yang disediakan dan disimpan.

**Langkah 2. Get the sample code**

Melakukan cloning repo GitHub kode sampel:

```
git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```

Kode sampe di `example.py` melakukan hal berikut ini:

- Membuat `account` tabel dan menyisipkan beberapa baris.
- Mentrasfer dana antara dua akun dalam suatu transaksi.
Hapus akun dari tabel sebelum keluar sehingga kita dapat menjalankan kembali kode contoh.

**Langkah 3. Install the psycopg2 driver**

`psycopg2-binary` merupakan satu - satunya dependensi modul pihak ketiga aplikasi sampel.

Untuk menginstal `psycopg2-binary`, dengan menjalankan perintah berikut ini:

```
pip install psycopg2-binary
```

**Langkah 4. Run the code**

1. Setel `DATABASE_URL` environment variable ke string koneksi ke cluster CockroachDB Cloud kita:

```
export DATABASE_URL="{connection-string}"
```

Dimana `{connection-string}` string koneksi yang kita peroleh dari CockroachDB Cloud Console. Aplikais menggunakan string koneksi yang disimpan ke `DATABASE_URL` environment variable untuk terhubung ke cluster kita dan mengeksekusi kode.

2. Menjalankan code:

```
cd hello-world-python-psycopg2
```
```
python example.py
```
Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana yaitu:

```
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
```

# Build a Simple CRUD Python App with CockroachDB and SQLAlchemy

langkah 1. Pada awal untuk memulai CockroachDB sama seperti pembahasan diatas yaitu tentang `Build a Python App with CockroachDB and psycopg2` jadi bisa kita bisa mulai ke tahap berikutnya yaitu

Langkah 2. Melakukan clone repo GitHub:

```
git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```

Dalam projek diatas memiliki struktur direktori berikut ini:

```
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```

Pada file `requirements.txt` menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk `sqlalchemy-cockroachdb` Python package, yang menjelaskna beberapa perbedaan antara CockroachDB dan PostgresSQL:

```
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```

Pada file `dbinit.sql` menginisialisasi skema database yang digunakan aplikasi yaitu:

```python
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```

Menggunakan SQLAlchemy `models.py` untuk memetakan `Accounts` tabel ke objek Python:

```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```

File `main.py` digunakan untuk memetakan metode Python ke operasi SQL:

```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```

`main.py` juga mengeksekusi main metode program.

**Langkah 3. install persyaratan aplikasi**

Langkah - langkah menggunakan `virtualenv` utnuk manajemen ketergantungan.

1. Instal virtualenv

```
pip install virtualenv
```

2. Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual:

```
virtualenv env
```

```
source env/bin/activate
```

3. Instal modul yang akan digunakan atau diperlukan ke lingkungan virtual:

```
pip install -r requirements.txt
```

**Langkah 4. Menginstal database**

1. Setel `DATABASE_URL` environment variable ke string koneksi untuk cluster:

```
export DATABASE_URL="{connection-string}"
```

Dimana `{connection-string}` string koneksi yang kita peroleh dari CockroachDB Cloud Console.

2. Untuk menginisialisasi database contoh, gunakan Cockroach SQL perintah untuk mengeksekusi pernyataan SQL dalam `dbinit.sqlfile`: 

```
cat dbinit.sql | cockroach sql --url $DATABASE_URL
```

Pernyataan SQL dalam file inisialisasi harus dijalankan:

```
CREATE TABLE

Time: 102ms
```

**Langkah 5 Menjalankan code**

`main.py` menggunakan string koneksi yang disimpan ke `DATABASE_URL` environment variable untuk terhubung ke cluster kita dan mengeksekusi code.

menjalankan aplikasi:

```
python main.py
```

Aplikasi yang akan terhubung ke COckroachDB, kemudain melakukan beberapa penyisipan baris sederhana, pembaruan, dan kemudian penghapusan.

Maka hasil output akan terlihat seperti berikut ini:

```
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```

Kemudian terlihat dalam shell SQL yang terhubung ke cluster, kita dapat verifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus.

```
SELECT COUNT(*) FROM accounts;
```

```
  count
---------
     95
(1 row)
```
