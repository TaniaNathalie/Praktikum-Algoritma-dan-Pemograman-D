set_satu = set()
set_dua = set()

try:
    nama1 = input("Masukkan nama orang pertama: ")
    nama2 = input("Masukkan nama orang kedua: ")
    print("="*50)
    data1 = int(input("Berapa kali akan memasukkan data orang pertama?: "))
    data2 = int(input("Berapa kali akan memasukkan data orang kedua?: "))
    print("="*50)

    print("Masukkan nama grup KPOP favorit anda")
    print("Group favorit",nama1)
    for i in range(data1):
        grup1 = input()
        set_satu.add(grup1)

    print("Group favorit",nama2)
    for j in range(data2):
        grup2 = input()
        set_dua.add(grup2)

    print("========== HASIL AKHIR ==========")
    print("Group KPOP favorit",nama1,"adalah",set_satu)
    print("Group KPOP favorit",nama2,"adalah",set_dua)

    gabungan = set_satu.union(set_dua)
    print("Grup KPOP yang terdata adalah",gabungan)

    sama = set_satu.intersection(set_dua)
    print("Grup KPOP yang sama adalah",sama)
except:
    print("Silahkan masukkan inputan dengan benar")
