handle = open("tabungan.txt","r+")
handle_1 = handle.read()

print("==========Program Mencatat dan Menampilkan Tabungan")
print("1. Mencatat Tabungan")
print("2. Menampilkan Tabungan")
print()

try:
    pilih = int(input("Masukkan pilihan anda: "))
    if pilih == 1:
        tabungan = int(input("Masukkan tabungan anda : "))
        tulisan = "Tabungan = " + str(tabungan) + ",00\n"
        print("Tabungan anda berhasil dicatatkan")
        handle.write(tulisan)
    elif pilih == 2:
        i = 0
        for line in handle_1:
            hasil = handle_1.split(",00\n")
            while i <= 5:
                print(hasil[i])
                i = i + 1
    else:
        print("Silahkan masukan pilihan yang tepat")
    handle.close()
except:
    print("Maaf, yang anda inputkan tidak valid")
    
