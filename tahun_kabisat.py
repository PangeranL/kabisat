# nama file :tahun_kabisat.py
# pembuat : Ahmad Fahrezi (24060122140146)
# tanggal : 02-09-2022
# deskripsi : menentukan tahun kabisat berdasarkan syarat

# definisi dan spesifikasi
# kabisat (a) : integer --> bolean
# artinya tahun yang diinput
# true artinya tahun input merupakan tahun kabisat
# false artinya tahun input bukan tahun kabisat

# realisasi
def tahun(a) :
    return a%400 == 0 or a%4 == 0 and a%100 !=0

# aplikasi
print(tahun(2003))
print(tahun(1984))
print(tahun(1945))
print(tahun(2024))
print(tahun(2035))
