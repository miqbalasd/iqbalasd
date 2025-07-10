#Menambahkan List Item

#Menampilkan data buah
buah = ['tomat', 'ceri', 'durian', 'jeruk']

print (buah)

#Menampilkan data dari index
print(buah[2])
'''

#Merubah Isi List
# namalist[index ke-] = perubahan
buah[2] = "anggur"
print(buah)

##Menambahkan isi list 
# namalist.append(value) #(hanya 1 item)
buah.append("mangga")
print(buah)

#menambahkan item berupa list maka item tersebut akan menjadi list didalam list
#  namalist.append([value,value])
buah.append(["mangga", "rambutan"])
print(buah)

## Menambahkan item berdasarkan index
# namalist.insert(index,value)
buah.insert(-4,"apel")
print(buah)

##menambahkan item baru di akhir list dan tipe data dari item tersebut akan melebur menjadi satu list.

# namalist.extend(value)
buah.extend(['semangka','pepaya'])
print(buah)

## Hapus Item List

# Del (menghapus sebuah item dari list sesuai dengan indexnya)
del buah[2]
print(buah)

# Remove (menghapus isi list sesuai dengan nama item tersebut)
buah.remove('tomat')
print(buah)
'''

## Mengurutkan Item List

#sorted(buah, reverse=False) ini googlab
buah.sort()
print(buah)

## Menampilkan list perbaris
for elemen in buah:
 print(elemen)

#tuples fungsinya sama dengan list
# apa bedanya?
tup_buah =('tomat', 'ceri', 'durian', 'jeruk')
print(tup_buah)

#tup_buah.append("anggur")

#pencarian data tuple
print(tup_buah[2])


#Set
buah.append("ceri")
print(buah)
set_buah= set(buah)
print(set_buah)
#tambah
set_buah.add("kelengkeng")
print(set_buah)
#hapus data tertentu
set_buah.remove("ceri")
print(set_buah)
set = {'a','b','c','d','e'}
print(set)







