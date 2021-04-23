print("==========Program mencatat biodata peserta==========")
kamus = dict()
lst_nama = []
lst_umur = []
x = 0
try:
    berapa = int(input("Berapa kali anda akan memasukkan data mahasiswa?: "))
    for i in range(berapa):
        nama = input("Masukkan nama: ")
        umur = int(input("Masukkan umur: "))
        print("="*30)

        lst_nama.append(nama)
        lst_umur.append(umur)

    for j in range(berapa):
        kamus[lst_nama[x]] = lst_umur[x]
        x = x + 1

    print()
    print("==========Hasil pencatatan biodata peserta==========")
    print(kamus)

    kamus2 = dict()
    urutan = sorted(kamus.values())
    kunci = kamus.keys()

    for a in urutan:
        for b in kunci:
            if kamus[b] == a:
                kamus2[b] = a

    print("==========Program mencatat biodata peserta setelah diurutkan==========")
    print(kamus2)
except:
    print("Inputan anda tidak valid")
    
