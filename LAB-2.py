print("==========PROGRAM MENGHITUNG LUAS DAN KELILING LAYANG-LAYANG==========")
print()

#Inputan dari pengguna
d1 = int(input("Masukkan panjang diagonal 1 (cm) : "))
d2 = int(input("Masukkan panjang diagonal 2 (cm) : "))
pendek = int(input("Masukkan sisi terpendek (cm) : "))
panjang = int(input("Masukkan sisi terpanjang (cm) : "))

#Proses perhitungan
luas = (d1 * d2) / 2
keliling = 2 * (pendek + panjang)
print()

#Output yang ditampilkan
print("Diperoleh : \nLuas layang-layang adalah %d cm \nKeliling layang-layang adalah %d cm" %(luas, keliling))
print()
print("=============================TERIMA KASIH=============================")
      
