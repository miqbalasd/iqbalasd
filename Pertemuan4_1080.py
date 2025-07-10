#list
#index list dimulai dari 0
angka = [1,"2",3.0,4,5]
print (angka)

'''contoh list dengan menggunakn banyak data'''

data = [1, 'dua', 3, 4.0, 'lima', 6, 7, 8.0, 'sembilan']
print (data)

###akses list


## Slicing

#menanggil semua data
print(data)

#memanggil index data ke 1
print(data[-1])

#memanggil data dari depan dan sebelum index data ke 2 
print(data[:2])

#memanngil data dimulai dari index data ke 2  
print(data[2:])

#memanggil data dari belakang dan sampai index data ke -2
print(data[-2:])

#memanggil data dari belakang dan dimulai dari index data ke -2 serta interval 2 dari kanan ke kiri
print(data[-2::-2])

#memanggil data dari belakang dan dimulai dari index data ke 2 serta interval 2 dari kiri ke kanan
print(data[2::2])

#memanggil data dari index datake 3 dan sebelum index data ke 7
print(data[3:7])
