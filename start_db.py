# import library sqlalchemy untuk menginisiasi database yg ingin dipakai
import sqlalchemy
from sqlalchemy import create_engine, text

# konfigurasi database,
# buat variabel konfigurasi sebagai konstan,
# buat sqlite sebagai engine
ENGINE = create_engine("sqlite:///super-cashier.db")

# koneksi database
# buat variabel koneksi sebagai kontan
CONN = ENGINE.connect()

# fungsi untuk membuat table pada database


def create_table():
    query_buat_table = """
    CREATE TABLE 'transaction'(
        no_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_item STRING,
        jumlah_item INTEGER,
        harga INTEGER,
        total_harga INTEGER,
        diskon INTEGER,
        harga_diskon INTEGER
    )
    """
    # eksekusi query
    CONN.execute(text(query_buat_table))


create_table()
