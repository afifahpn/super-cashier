
def transaction():
    # tampilan yang akan pertama kali dilihat oleh user
    print("""
    Selamat datang di supermarket andi. 
    """)
    # customer memasukkan pilihan
    cust_input = input(" Silahkan Masukkan id transaksi anda: ")
    print(".....................")
    return cust_input


def add_item(item, qty, harga):
    # item = input("Masukkan item: ")
    # qty = input("Masukkan jumlah: ")
    # harga = input("Masukkan harga: ")
    group = [qty, harga]
    item_dic = {item: group}
    return (item_dic)


transaction()
