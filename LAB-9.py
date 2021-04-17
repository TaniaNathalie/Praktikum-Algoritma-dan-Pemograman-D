try:
    lst_nama = []
    lst_matkul = []
    lst_nilai = []
    berapa = int(input("Berapa kali anda akan memasukkan data?: "))
    for i in range(berapa):
        nama = input("Nama: ")
        matkul = input("Mata Kuliah: ")
        nilai = int(input("Nilai: "))
        print()
        lst_nama.append(nama)
        lst_matkul.append(matkul)
        lst_nilai.append(nilai)

    print("==========Hasil Survei==========")
    print("| Nama | Matkul | Nilai |")
    x = 0
    for j in range(berapa):
        print("| %s | %s | %s |" %(lst_nama[x],lst_matkul[x],lst_nilai[x]))
        x = x + 1
except:
    print("Silahkan memasukkan inputan dengan bilangan")
