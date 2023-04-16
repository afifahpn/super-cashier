"""file modul.py ini berisikan function yang digunakan selama program berjalan
 file ini tidak akan tampil di terminal """

# import library sqlite untuk koneksi ke database
import sqlite3


# membuat koneksi dengan file sql
conn = sqlite3.connect("super_cashier.db")


# untuk mengeksekusi perintah sql
cursor = conn.cursor()

# menginisiasi id transaksi dan data item ke dalam variabel data_customer dengan tipe data dictionary
data_customer = {
    "transaksi": [],
    "item": {}
}


# function untuk menyimpan id transaksi dalam variable cust_append
def transaction(cust_input):
    cust_append = data_customer["transaksi"].append([cust_input])


# function untuk menambahkan item
def add_item(item, qty_item, harga_item):
    # jika customer sesuai dalam menginput data, maka item akan tersimpan dalam variabel  items_exist
    try:
        items_exist = data_customer['item']
        items_exist.update({item: [qty_item, harga_item]})

        print(f"Item yang dibeli adalah: {items_exist}")

    # sebaliknya, jika customer salah dalam menginput data maka akan muncul notifikasi
    except:
        print("terdapat kesalahan dalam menginput data")


# function untuk edit nama item
def update_item_name(nama_item, nama_baru):
    items_exist = data_customer['item']
    print(f"Item sebelum diedit: {items_exist}")

    # dictionary tidak memiliki method untuk mengganti key, maka menggunakan method pop untuk mengganti key baru
    items_exist[nama_baru] = items_exist.pop(nama_item)
    print(f"Item setelah diedit: {items_exist}")


# function untuk edit quantity item
def update_item_qty(nama_item, qty_baru):
    items_exist = data_customer['item']
    print(f"Item sebelum diedit: {items_exist}")
    items_exist[nama_item][0] = qty_baru
    print(f"Item setelah diedit: {items_exist}")


# function untuk edit harga item
def update_item_price(nama_item, harga_item):
    items_exist = data_customer['item']
    print(f"Item sebelum diedit: {items_exist}")
    items_exist[nama_item][1] = harga_item
    print(f"Item setelah diedit: {items_exist}")


# function untuk menghapus salah satu item
def delete_item(nama_item):
    items_exist = data_customer['item']
    print(f"Item sebelum dihapus: {items_exist}")
    items_exist.pop(nama_item)
    print(f"Item setelah dihapus: {items_exist}")


# function untuk menghapus semua item
def reset_transaction():
    items_exist = data_customer['item']
    print(f"Item sebelum dihapus: {items_exist}")
    items_exist.clear()
    print(f"Semua item telah terhapus")


# function untuk melakukan chek order sekaligus input ke database
def check_order():

    # jika customer sesuai dalam menginput data, maka item akan diproses
    try:
        print("Pemesanan sudah benar\n")
        items_exist = data_customer['item']
        transaksi = data_customer['transaksi']

        # variabel untuk menampung diskon
        diskon = 0

        # variabel untuk menampung total item
        total_item = 0

        # variabel untuk menampung potongan harga
        potongan_harga = 0

        # hitung item dengan while loop
        for nama in items_exist:
            qty_item = items_exist[nama][0]
            harga_item = items_exist[nama][1]

            # total = jumlah * harga
            total_item = qty_item * harga_item

            # jika total item lebih besar dari 200000 dan lebih kecil sama dengan 300000 maka mendapat potongan 5%
            if total_item > 200000 and total_item <= 300000:
                diskon = 5/100
                potongan_harga = total_item * diskon
                total_setelah_diskon = total_item - potongan_harga

            # jika total item lebih besar dari 300000 dan lebih kecil sama dengan 500000 maka mendapat potongan 6%
            elif total_item > 300000 and total_item <= 500000:
                diskon = 6/100
                potongan_harga = total_item * diskon
                total_setelah_diskon = total_item - potongan_harga

            # jika total item lebih besar dari 500000 maka mendapat potongan 7%
            elif total_item > 500000:
                diskon = 7/100
                potongan_harga = total_item * diskon
                total_setelah_diskon = total_item - potongan_harga

            # jika total item tidak melebihi dari 20000 maka tidak mendapatkan potongan
            else:
                total_setelah_diskon = total_item

            # perintah sql untuk menginput data ke tabel transaksi
            sqlinsert = f"""
                    INSERT INTO 'transaction' (no_id, nama_item, jumlah_item, harga, total_harga, diskon, harga_diskon)
                    VALUES('{transaksi}', '{nama}', {qty_item},{harga_item},{total_setelah_diskon},{diskon},{total_item});
                    """

            # mengeksekusi perintah sql
            cursor.execute(sqlinsert)
            conn.commit()

        # total yang harus dibayarkan
        total_item += total_setelah_diskon
        print(f"Item yang dibeli adalah: {items_exist}")
        print(f"total yang harus dibayar: {total_item}")

    # sebaliknya, jika customer salah dalam menginput data maka akan muncul notifikasi
    except:
        print("Terdapat kesalahan input data\n")
