print("="*5,"Menghitung suku ke-n dan jumlah n Barisan dan Deret Aritmatika","="*5)

def barisan(a,n,b):
    u_n = a + (n-1)*b
    return u_n

def deret(a,n,b):
    s_n = (n/2) * (2*a + (n-1)*b)
    return s_n

try:
    print("1. Menghitung suku ke-n")
    print("2. Menghitung jumlah n")
    pilih = int(input("Masukkan pilihan anda: "))
    if pilih == 1:
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        n = int(input("Masukkan nilai n: "))
        print("Hasilnya adalah",barisan(a,n,b))
    elif pilih == 2:
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        n = int(input("Masukkan nilai n: "))
        print("Hasilnya adalah",deret(a,n,b))
    else:
        print("Maaf yang anda inputkan tidak valid")
except:
    print("Maaf yang anda inputkan harus berupa bilangan integer")
                  
