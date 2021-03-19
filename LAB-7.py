print("="*10,"Program Pengolah Kalimat","="*10)
print("1. Mengubah kalimat menjadi huruf kecil")
print("2. Mengubah kalimat menjadi huruf kapital")
print("3. Mengubah kalimat menjadi pesan rahasia")
print("4. Mengubah kalimat menjadi kebalikannya")
print()

pilihan = int(input("Pilihan anda: "))
kalimat = input("Masukkan kalimat: ")

if pilihan == 1:
    hasil = kalimat.lower()
    print(hasil)
elif pilihan == 2:
    hasil = kalimat.upper()
    print(hasil)
elif pilihan == 3:
    hasil = kalimat[::-1]
    print(hasil)
elif pilihan == 4:
    hasil = kalimat.swapcase()
    print(hasil)
else:
    print("Maaf yang anda inputkan salah")

