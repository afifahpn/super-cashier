from modul import *

while (True):
    print("""
    SELAMAT DATANG DI SUPERMARKET ANDI
    1. tambah id transaksi baru
    2. tambah item
    3. edit item
    4. delete item
    5. chek out
    """)
    cust_menu_input = input("""Silahkan Pilih: """)
    if cust_menu_input == '1':
        cust_input = input("Silahkan Masukkan id transaksi anda: ")
        transaction(cust_input)
    elif cust_menu_input == '2':
        item = input("Masukkan item: ")
        qty_item = input("Masukkan jumlah: ")
        harga_item = input("Masukkan harga: ")
        add_item(item, qty_item, harga_item)
    elif cust_menu_input == '3':
        print("1. update nama item \n2. update jumlah item \n3. update harga item")
        cust_edit = input("Silahkan Pilih: ")
        if cust_edit == '1':
            nama_item = input("Nama Item: ")
            nama_baru = input("Nama Item Baru: ")
            update_item_name(nama_item, nama_baru)
        elif cust_edit == '2':
            nama_item = input("Nama Item: ")
            qty_baru = input("Jumlah Item Baru: ")
            update_item_qty(nama_item, qty_baru)
        elif cust_edit == '3':
            nama_item = input("Nama Item: ")
            harga_item = input("Harga Item Baru: ")
            update_item_price(nama_item, harga_item)
    elif cust_menu_input == '3':
        :
        print("delete")
