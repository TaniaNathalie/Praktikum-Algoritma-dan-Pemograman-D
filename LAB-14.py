import re
print("========== Program Mengecek Nomor Telepon ==========")
print()

try:
    urutan = int(input("Masukkan urutan ke: "))
    nama = str(input("Masukkan nama temanmu: "))
    pesan = input("Masukkan pesan yang diterima: ")
    satu = re.split("\s", pesan)

    for i in satu:
        if re.search("\d", i) and len(i) == 12:
            print("Nomor telepon",nama,"adalah",i,"di urutan ke",urutan)
        elif re.search("\d", i) and len(i) < 12 or len(i) > 12:
            print("Nomor telepon",nama,"tidak terdeteksi")
except:
    print("Silahkan perhatikan inputan anda")
