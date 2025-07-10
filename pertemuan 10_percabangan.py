'''#kasus 1
nilai = int(input("Masukan nilai ujian: "))

if nilai >= 75:
    print("selamat anda lulus.")
else:
    print("Maaf, anda tidak lulus.")
    '''
'''#kasus 2
def luas_persegi_panjang(panjang, lebar):
    #isi Function
    luas = panjang * lebar
    return luas

panjang = int(input("masukan panjang: "))
lebar = int(input("masukan lebar: "))

#memanggil function
luas_persegi = luas_persegi_panjang(panjang, lebar)
print("luas persegi panjang: ", luas_persegi_panjang(panjang, lebar),"cm2")'''

#tugas no.4
#daftar menu makanana
menu = {"mie ayam": 12000,
        "kwetiaw": 13000,
        "nasi goreng": 15000,
        "ayam bakar": 20000,
        "roti canai": 10000 }
print("Daftar  menu: ")

#menampilkan daftar menu makanana
for food, harga in menu.items():
    print(f"- {food.title()} : Rp.{harga}")

#fungsi untuk memesan makanan
print("Pilih menu: ")
def pesan_makanan():
    pilih = input("Pilih menu makanan yang ingin dipesan: ").strip().lower()

    if pilih in daftar_menu:
        try:
            jumlah = int(input("masukan jumlah makanan: "))
            if jumlah <= o:
                print("jumlah harus lebih dari 1")
                return
        except value_eror:
            print("masukan angka yang valid untuk jumlah.")
            return

        harga_satuan = menu [pilih]
        total = harga_satuan * jumlah
        print(f"\nAnda memesan {jumlah} porsi{pilih.title()}")
        print(f"harga per porsi: rp.{harga_satuan}")
        print(f"total harga: rp.{total}")
        
    else:
        print("menu tidak tersedia.")

#memanggil fungsi
pesan_makanan()
