'''
#Percabangan if else
nilai =int(input('Masukan nilai ujian: '))

if nilai >=75 and nilai <=100:
    print('Selamat, Anda lulus!')
elif nilai >100:
    print('Selamat, Anda mendapatkan nilai anomali!')
else:
    print('Selamat, Anda tidak lulus!')'''
'''
#Percabangan
total_pembelian =int(input('masukan total pembelian: Rp.'))

if total_pembelian <50000:
    diskon = 0
    total_diskon = 0*total_pembelian
elif total_pembelian <100000:
    diskon = 10
    total_diskon = 0.1*total_pembelian
else:
    diskon = 15
    total_diskon = 0.15*total_pembelian

total_bayar = total_pembelian - total_diskon
print(f"\nDiskon: {diskon}%\nTotal Diskon: Rp.{total_diskon}\nTotal Pembayaran: Rp.{total_bayar}")'''

#Pengulangan for
kamus = {'jkt': 'Jakarta',
         'bdg': 'Bandung',
         'jog': 'Jogja',
         'sby': 'Surabaya'
         }

for key , value in kamus.items():
    print("Kunci: ",key,"\tNilai: ",value)
