def rekursif(x1,xn):
    for i in range(xn):
        if xn == x1:
            return x1
        else:
            return 2 * rekursif(x1,xn-1) + 1

print("========== Kalkulator Rekursif ==========")
print("Rumus umum = (2 * Xn-1) + 1")
print()
try:
    x1 = int(input("Masukkan nilai X1: "))
    xn = int(input("Masukkan n yang dicari: "))
    print("Hasil X%d = " %(xn),end="")
    print(rekursif(x1,xn))
except:
    print("Maaf yang anda inputkan tidak valid")
