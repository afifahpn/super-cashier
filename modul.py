
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
    items_exist = data_customer['item']
    items_exist.update({item: [qty_item, harga_item]})

    print(f"Item yang dibeli adalah: {items_exist}")

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

"""
data yang perlu disimpan:
1. item
2. quantity item
3. harga item

"""


# transaction()
