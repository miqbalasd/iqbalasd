#         key    value
kamus = {'jkt':'Jakarta',
         'bdg':'Bandung',
         'jog':'Jogja'}

#print(namaDict[key])
print(kamus['bdg'])

#menambahkan data di dict
kamus['namaKey']='namaValue'
kamus['plg']='palembang'

#print(namaDict[key])
print('data ubah = ',kamus['namaKey'])

    
#merubah data di dict
kamus['namaKey']='ubahNamaValue'
print('data ubah = ',kamus['namaKey'])


#menghapus data di dict
del kamus['namaKey']
print(kamus)

#
