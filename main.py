import mysql.connector
#  pip install mysql-connector-python

class Buku:
    def __init__(self, judul, pengarang, isbn):
        self.judul = judul
        self.pengarang = pengarang
        self.isbn = isbn

    def tampilkan_info(self):
        print(f"Judul: {self.judul}, Pengarang: {self.pengarang}, ISBN: {self.isbn}")

class Perpustakaan:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
        )
        self.kursor = self.koneksi.cursor()
        self.kursor.execute("CREATE DATABASE IF NOT EXISTS `5190411053`")
        self.kursor.execute("USE `5190411053`")
        self.buat_tabel()

    def buat_tabel(self):
        query = """CREATE TABLE IF NOT EXISTS buku (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        judul VARCHAR(255),
                        pengarang VARCHAR(255),
                        isbn VARCHAR(20)
                    )"""
        self.kursor.execute(query)
        self.koneksi.commit()

    def tambah_buku(self, buku):
        query = "INSERT INTO buku (judul, pengarang, isbn) VALUES (%s, %s, %s)"
        nilai = (buku.judul, buku.pengarang, buku.isbn)
        self.kursor.execute(query, nilai)
        self.koneksi.commit()
        print("Buku berhasil ditambahkan!")

    def tampilkan_daftar_buku(self):
        query = "SELECT * FROM buku"
        self.kursor.execute(query)
        hasil = self.kursor.fetchall()
        for baris in hasil:
            print("=="*15)
            print(f"ID: {baris[0]}\nJudul: {baris[1]}\nPengarang: {baris[2]}\nISBN: {baris[3]}")
            print("=="*15)
    def hapus_buku(self, id_buku):
        query = "DELETE FROM buku WHERE id = %s"
        nilai = (id_buku,)
        self.kursor.execute(query, nilai)
        self.koneksi.commit()
        print(f"Buku dengan ID {id_buku} berhasil dihapus.")
    def update_buku(self, id_buku, judul_baru, pengarang_baru, isbn_baru):
        query = "UPDATE buku SET judul=%s, pengarang=%s, isbn=%s WHERE id=%s"
        nilai = (judul_baru, pengarang_baru, isbn_baru, id_buku)
        self.kursor.execute(query, nilai)
        self.koneksi.commit()
        print(f"Informasi buku dengan ID {id_buku} berhasil diperbarui.")



perpustakaan = Perpustakaan()

while True:
    print("1.tampilkan buku")
    print("2.tambah buku")
    print("3.hapus buku")
    print("4.edit data buku")
    menu = input("menu :")
    if menu =="1":
        perpustakaan.tampilkan_daftar_buku()
    elif menu == "2":
        perpustakaan.tambah_buku(Buku(input("judul buku :"),input("nama pengarang :"),input("isbn buku :")))
    elif menu == "3":
        perpustakaan.tampilkan_daftar_buku()
        perpustakaan.hapus_buku(input("masukan id buku :"))
    elif menu =="4":
        perpustakaan.tampilkan_daftar_buku()
        perpustakaan.update_buku(input("id buku :"),input("judul buku :"),input("nama pengarang :"),input("isbn buku :"))