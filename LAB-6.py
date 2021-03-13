print("="*20,"Toko Buku","="*20)
print("Menjual: ")
print("1. Buku Komik       :Rp.50.000")
print("2. Buku Novel       :Rp.70.000")
print("3. Buku Pengetahuan :Rp.100.000")
print()
total1 = 0
total2 = 0
total3 = 0
total = 0
try:
    pilihan = "lanjut"
    while pilihan == "lanjut":
        kode = int(input("Masukkan kode angka yang ingin dibeli: "))
        banyak = int(input("Banyaknya jumlah yang akan dibeli: "))
        pilihan = str(input("lanjut/berhenti? : "))
        if kode == 1:
            komik = 50000
            total1 = komik * banyak
            total = total + total1
        elif kode == 2:
            novel = 70000
            total2 = novel * banyak
            total = total + total2
        elif kode == 3:
            pengetahuan = 100000
            total3 = pengetahuan * banyak
            total = total + total3
    else:
        total = total1 + total2 + total3
        print("Total belanjaan anda adalah Rp.",total)
except:
    print("Silahkan periksa inputan anda")
    
