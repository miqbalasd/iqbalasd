'''# Definisikan kelas
class mobil:
    #konstruktoruntuk inisiasi objek
    def __init__(self, merk, model, tahun):
        self.merk = merk 
        self.model = model 
        self.tahun = tahun 
    #metode untuk menampilkan informasi mobil
    def info(self):
        #menggunakan .format()
        return "Mobil: {} {} ({})".format(self.merk, self.model, self.tahun)

    #metode untuk menyalakan mesin mobil
    def nyalakan_mesin(self):
        #menggunakan .format()
        return "Mesin {} {} menyala".format(self.merk, self.model)

    #metode untuk menyalakan mesin mobil
    def matikan_mesin(self):
        #menggunakan .format()
        return "Mesin {} {} mati".format(self.merk, self.model)

#bagian utama program untuk memnuat objek dan memanggil metide
if __name__ == "__main__":
    #buat objek dari kelas
    mobil1 = mobil("Totota", "Corolla", 2020)
    mobil2 = mobil("Honda", "Civic", 2018)

    #Panggil metode informasi untuk melihat informasi mobil
    print("\n--- Ingformasi Mobil ---")
    print(mobil1.info())
    print(mobil2.info())

    #Panggil metode nyalakan_nesin dan matikan_mesin mobil
    print("\n--- Aksi Mesin ---")
    print(mobil1.nyalakan_mesin())
    print(mobil2.matikan_mesin())'''

'''# Definisikan kelas
class mobil:
    #konstruktoruntuk inisiasi objek
    def __init__(self, merk, model, tahun):
        self.__merk = merk #artibut private
        self.__model = model #artibut private
        self.__tahun = tahun #artibut private

    #metode untuk mendapatkan informasi merk
    def get_merk(self):
        return self.__merk

    #metode untuk mengatur informasi merk
    def set_merk(self, merk):
        return self.__merk

    #metode untuk mendapatkan informasi mobil
    def get_model(self):
        return self.__model

    #metode untuk mengatur informasi mobil
    def get_model(self, model):
        return self.__model

    #metode untuk mendapatkan informasi tahun
    def get_merk(self):
        return self.__tahun

    #metode untuk mengatur informasi
    def get_merk(self, tahum):
        return self.__tahun

#bagian utama program untuk memnuat objek dan memanggil metide
if __name__ == "__main__":
    #buat objek dari kelas
    mobil1 = mobil("Totota", "Corolla", 2020)
    mobil2 = mobil("Honda", "Civic", 2018)

    #Panggil metode informasi untuk melihat informasi mobil
    print("\n--- Ingformasi Mobil ---")
    print(mobil1.info())
    print(mobil2.info())

    #Panggil metode nyalakan_nesin dan matikan_mesin mobil
    print("\n--- Aksi Mesin ---")
    print(mobil1.nyalakan_mesin())
    print(mobil2.matikan_mesin())

    #menggunakan setter unruk mengubah nilai atribut
    mobil1.set_merk("NIssan")
    mobil1.set_model("Altima")
    mobil1.set_tahun(2021)

    #
    print(mobil1.info())
'''


    






    
