# Latar Belakang Super-cashier
 Sistem cashier supermarket sederhana dengan menggunakan bahasa pemrograman python dan database sqlite3
 
# Requirement/objective super-cashier
1. membuat program super-cashier yang dapat:
    - membuat id transaksi
    - memasukkan item yang ingin dibeli
    - mengedit item yang telah dimasukkan
    - menghapus item yang telah dimasukkan
    - melakukan checkout dan tersimpan automatis ke dalam database
       - jika total item tidak melebihi dari 20000 maka tidak mendapatkan potongan
       - jika total item lebih besar dari 200000 dan lebih kecil sama dengan 300000 maka mendapat potongan 5%
       - jika total item lebih besar dari 300000 dan lebih kecil sama dengan 500000 maka mendapat potongan 6%
       - jika total item lebih besar dari 500000 maka mendapat potongan 7%

# Flowchart

![customer journey@2x](https://user-images.githubusercontent.com/55918778/232315551-7797a783-bec1-44c3-87c8-4be2e2175025.png)



# Deskripsi Task
1. Module 'start_db.py' digunakan untuk membuat koneksi ke sqlite dan untuk membuat database.
2. Module 'modul.py' berisi function-function yang akan dijalankan oleh program
3. Module 'main.py' berisi daftar menu super cashier.

# Cara Menggunakan Program
1. Download/pull file repo ke dalam satu direktori lokal.
2. Buka terminal dan sesuaikan lokasi direktori lokal.
3. Jalankan module python start_db.py di terminal.
4. Jalankan module python main.py di terminal.

# Hasil test Case
1. Customer membuat id transaksi customer

![image](https://user-images.githubusercontent.com/55918778/232314736-675aa653-4e69-47fb-973d-49c5a9c01b7e.png)

2. Customer menambahkan 2 item

![image](https://user-images.githubusercontent.com/55918778/232315052-678d5fb8-a899-4a6b-bb2c-c5704ee7f4e5.png)

3. Customer ingin menghapus item Pasta Gigi

![image](https://user-images.githubusercontent.com/55918778/232315094-bf79d74e-cc91-49a0-97c4-d9cd817b31cf.png)

4. Customer ingin menghapus semua item

![image](https://user-images.githubusercontent.com/55918778/232315148-d1465ce1-4919-45d9-9991-264b64ac467b.png)

# Future Work
1. Customer wajib mengisi id transaksi, jika id transaksi tidak diisi maka tidak dapat melakukan edit, hapus dan check out
