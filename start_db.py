# import library sqlite untuk menginisiasi database yg ingin dipakai
import sqlite3


# membuat koneksi dengan file sql
conn = sqlite3.connect("super_cashier.db")

# untuk mengeksekusi perintah sql
cursor = conn.cursor()

# query untuk membuat tabel
query_buat_table = """ CREATE TABLE IF NOT EXISTS 'transaction'(
        no_id TEXT,
        nama_item TEXT,
        jumlah_item INTEGER,
        harga INTEGER,
        total_harga INTEGER,
        diskon INTEGER,
        harga_diskon INTEGER);
    """
# eksekusi query
cursor.execute(query_buat_table)

# query untuk select
query_select = """ SELECT * FROM 'transaction'"""

# eksekusi query
cursor.execute(query_select)

for row in cursor.fetchall():
    print(row)
