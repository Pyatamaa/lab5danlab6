print("Program Input Nilai")
print("=================")

daftar = {}

while True:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    perintah = input("(L) Lihat, (T) Tambah, (U) Ubah, \n"
                     "(H) Hapus, (C) Cari, (K) Keluar: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Keluar
    if perintah.lower() == 'k':
        break

    # Lihat data
    elif perintah.lower() == 'l':
        print("Daftar Nilai:")
        print("===================================================================")
        print("| No |      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
        print("===================================================================")
        no = 1
        for tabel in daftar.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                  (no, tabel[0],
                   tabel[1], tabel[2],
                   tabel[3], tabel[4], tabel[5]))
            no += 1
        print("===================================================================")

    # Tambahkan data
    elif perintah.lower() == 't':
        print("Data Mahasiswa")
        print("...")
        nama = input("Nama: ")
        nim = input("NIM: ")
        n_tugas = int(input("Tugas: "))
        n_UTS = int(input("UTS: "))
        n_UAS = int(input("UAS: "))
        a = n_tugas *.30
        b = n_UTS *.35
        c = n_UAS *.35
        n_akhir = a + b + c
        daftar[nama] = [nama, nim, n_tugas, n_UTS, n_UAS, n_akhir]

    # Ubah data
    elif perintah.lower() == 'u':
        nama = input("Masukan nama untuk mengubah data: ")
        if nama in daftar.keys():
            print("Masukan data yang ingin di ubah :")
            data = input("(Semua), (Nama), (NIM), "
                         "(Tugas), (UTS), (UAS) : ")
            if data.lower() == "semua":
                print("==========================")
                print("Ubah data {}.".format(nama))
                print("==========================")
                daftar[nama][1] = input("Edit NIM:")
                daftar[nama][2] = int(input("Edit Nilai Tugas: "))
                daftar[nama][3] = int(input("Edit Nilai UTS: "))
                daftar[nama][4] = int(input("Edit Nilai UAS: "))
                # print(daftar)
            elif data.lower() == "NIM":
                daftar[nama][1] = input("NIM:")
            elif data.lower() == "Tugas":
                daftar[nama][2] = int(input("Nilai Tugas: "))
            elif data.lower() == "UTS":
                daftar[nama][3] = int(input("Nilai UTS: "))
            elif data.lower() == "UAS":
                daftar[nama][4] = int(input("Nilai UAS: "))
            else:
                print("Perintah tidak ditemukan.")

        else:
            print("'{}' tidak ditemukan.".format(nama))

    # Cari data
    elif perintah.lower() == 'c':
        print("Mencari daftar nilai: ")
        print("=================================================")
        nama = input("Masukan nama untuk mencari daftar nilai : ")
        if nama in daftar.keys():
            print("Nama {0}, dengan NIM : {1}\n"
                  "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n"
                  "dan nilai akhir {5}".format(nama, daftar[nama][1],
                                               daftar[nama][2], daftar[nama][3],
                                               daftar[nama][4], daftar[nama][5]))
        else:
            print("'{}' tidak ditemukan.".format(nama))

    # Hapus data
    elif perintah.lower() == 'h':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in daftar.keys():
            del daftar[nama]
            print("Data '{}' dihapus.".format(nama))
        else:
            print("'{}' tidak ditemukan.".format(nama))

    else:
        print("Silahkan masukan perintah terlebih dahulu.")