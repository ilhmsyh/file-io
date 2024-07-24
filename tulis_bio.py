print ("Selamat Datang di Program Biodata")
print ("==================================")

nama = raw_input("nama: ")
umur = input("umur: ")
alamat = raw_input("alamat ")

teks = ("nama: {}\nUmur: {}\nAlamat:: {}".format(nama, umur, alamat))
file_bio = open("biodata")