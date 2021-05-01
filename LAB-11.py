hari = ("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")
x = 0
lst_matkul = []
lst_sesi = []
try:
    for i in range(len(hari)):
        matkul = input("Masukkan mata kuliah di hari %s : " %(hari[x]))
        x = x + 1
        sesi = int(input("Masukkan sesi ke- : "))
        print("="*50)
        lst_matkul.append(matkul)
        lst_sesi.append(sesi)

    z = 0
    print("==========Jadwal Kuliah==========")
    for j in range(len(hari)):
        print("Mata kuliah di hari %s adalah %s pada sesi ke- %s" %(hari[z],lst_matkul[z],lst_sesi[z]))
        z = z + 1
except:
    print("Silahkan perhatikan inputan anda")
