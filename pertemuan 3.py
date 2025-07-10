'''nama = input ("masukan nama panggilan : ")
print (nama)

ipk = float ( input ( "masukan ipk : "))
print ( ipk )

#menyambungkan variable nama dan ipk 
sambung = f"{nama} memiliki ipk {ipk}"
print (sambung)
print (nama, "memiliki ipk", ipk)'''

'''
# f menupakan interpolasi(untuk mendeklarasikan variable yang ada di dalam kurung kurawa.)

#operator
sks = int(input("\nmasukan jumlah sks: "))
spp_var = 50000
hitung = sks * spp_var
print(f"\n{nama} memiliki ipk {ipk},\nharus membayar spp sebesar {hitung}")

print(hitung >= spp_var)
if hitung >= spp_var:
    print("\njumlah sks valid")
else:
    print("\njumlah sks tidak valid")'''


#tugas pertemuan 3
nama = input ("Masukan Nama : ")
nim = int ( input ( "Masukan NIM : "))
jawaban = int ( input ( "Masukan jawaban yang benar : "))
matkul = input ("Masukan Matakuliah : ")

#
nilai = jawaban * 10
print(f"\n{nama} dengan NIM {nim} mendapatkan nilai {nilai} dari Matakuiah {matkul})
