import sqlite3

data_customer = {
    "customer": [],
    "item": {}
}


def transaction(cust_input):
    # tampilan yang akan pertama kali dilihat oleh user
    # customer memasukkan pilihan
    cust_append = data_customer["customer"].append([cust_input])
    return cust_append


def add_item(item, qty_item, harga_item):
    try:
        items_exist = data_customer['item']
        items_exist.update({item: [qty_item, harga_item]})

        print(f"Item yang dibeli adalah: {items_exist}")
    except:
        print("terdapat kesalahan dalam menginput data")

# function untuk edit nama item


def update_item_name(nama_item, nama_baru):
    items_exist = data_customer['item']
    print(f"Item sebelum diedit: {items_exist}")
    items_exist[nama_baru] = items_exist.pop(nama_item)
    print(f"Item setelah diedit: {items_exist}")


def update_item_qty(nama_item, qty_baru):
    items_exist = data_customer['item']
    print(f"Item sebelum diedit: {items_exist}")
    items_exist[nama_item][0] = qty_baru
    print(f"Item setelah diedit: {items_exist}")


def update_item_price(nama_item, harga_item):
    items_exist = data_customer['item']
    print(f"Item sebelum diedit: {items_exist}")
    items_exist[nama_item][1] = harga_item
    print(f"Item setelah diedit: {items_exist}")


def delete_item(nama_item):
    items_exist = data_customer['item']
    print(f"Item sebelum dihapus: {items_exist}")
    items_exist.pop(nama_item)
    print(f"Item setelah dihapus: {items_exist}")


def delete_item(nama_item):
    items_exist = data_customer['item']
    print(f"Item sebelum dihapus: {items_exist}")
    items_exist.pop(nama_item)
    print(f"Item setelah dihapus: {items_exist}")


def reset_transaction():
    items_exist = data_customer['item']
    print(f"Item sebelum dihapus: {items_exist}")
    items_exist.clear()
    print(f"Semua item telah terhapus")


def check_order():
    items_exist = data_customer['item']
    transaksi = data_customer['customer']

    diskon = 0

    # variabel untuk menampung total belanjaan
    total_item = 0

    # variabel untuk menampung potongan harga
    potongan_harga = 0

    #  hitung belanjaan dengan while loop
    for nama in items_exist:
        qty_item = items_exist[nama][0]
        harga_item = items_exist[nama][1]
        total_item = qty_item * harga_item
        if total_item > 200000 and total_item < 300000:
            diskon = 5/100
            potongan_harga = total_item * diskon
            total_setelah_diskon = total_item - potongan_harga
        elif total_item > 300000 and total_item < 500000:
            diskon = 6/100
            potongan_harga = total_item * diskon
            total_setelah_diskon = total_item - potongan_harga
        elif total_item > 500000:
            diskon = 7/100
            potongan_harga = total_item * diskon
            total_setelah_diskon = total_item - potongan_harga
        else:
            total_setelah_diskon = total_item

        # membuat koneksi dengan file sql
        conn = sqlite3.connect("super_cashier.db")

        # untuk mengeksekusi perintah sql
        cursor = conn.cursor()

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
