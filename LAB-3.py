print("==========Program Menghitung Sifat Koligatif Larutan Nonelektrolit==========")
print()
print("Inputkan 1 jika anda ingin menghitung 'Penurunan Tekanan Uap Jenuh Larutan'")
print("Inputkan 2 jika anda ingin menghitung 'Kenaikan Titik Didih Larutan'")
print("Inputkan 3 jika anda ingin menghitung 'Penurunan Titik Beku Larutan'")
print("Inputkan 4 jika anda ingin menghitung 'Tekanan Osmosis Larutan'")
print()
try:
    pilih = int(input("Masukkan pilihan anda: "))
    print()
    if pilih == 1:
        a = float(input("Tekanan uap pelarut: "))
        b = float(input("Fraksi mol zat terlarut: "))
        deltaP = a * b
        print("Penurunan Tekanan Uap Jenuh Larutan adalah %.2f" %deltaP)
    elif pilih == 2:
        c = float(input("Molalitas zat terlarut: "))
        d = float(input("Tetapan kenaikan titik didih molal: "))
        deltaTb = c * d
        print("Kenaikan Titik Didih Larutan adalah %.2f" %deltaTb)
    elif pilih == 3:
        e = float(input("Molalitas zat terlarut: "))
        f = float(input("Tetapan penurunan titik beku molal: "))
        deltaTf = e * f
        print("Penurunan Titik Beku Larutan adalah %.2f" %deltaTf)
    elif pilih == 4:
        g = float(input("Kemolaran larutan: "))
        h = float(input("Suhu (Kelvin): "))
        phi = g * 0.082 * h
        print("Tekanan Osmosis Larutan adalah %.2f" %phi)
    else:
        print("Maaf, terjadi kesalahan")
except:
    print("Maaf, yang anda inputkan tidak valid")
    
