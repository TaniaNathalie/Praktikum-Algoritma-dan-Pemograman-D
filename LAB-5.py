print("="*10,"Program Menghitung Jumlah Pengeluaran Dalam Satu Hari","="*10)
print("Catatan:")
print("Ketikan 'lanjut' jika anda ingin terus memasukkan pengeluaran anda")
print("Ketikan 'berhenti' jika anda ingin melihat total pengeluaran anda")
print()
inp = 'lanjut'
i = 0
total = 0
try:
    while inp == 'lanjut':
        pengeluaran = int(input("Masukkan pengeluaran anda: "))
        total = total + pengeluaran
        i = i + 1
        print("Pengeluaran %d anda adalah Rp%d" %(i,pengeluaran))
        print()
        inp = str(input("lanjut/berhenti? : "))
        print()
    else:
        print("Total pengeluaran anda hari ini adalah Rp",total)
except:
    print("Maaf yang anda inputkan tidak valid")
