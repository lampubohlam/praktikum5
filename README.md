# praktikum5

# Latihan
membuat dictinory kontak
![Screenshot (134)](https://user-images.githubusercontent.com/116137169/204531902-273a86c7-f572-46da-934a-e9363b6c4c49.png)
Langkah pertama buatlah program seperti dibawah ini
![Screenshot (144)](https://user-images.githubusercontent.com/116137169/204546984-55ef1cda-2f86-4450-8c8d-5f9265fefb30.png)
        
        
        print('NAMA :Abdul aziz')
        print('NIM : 312210022')
        print(50*'=')
        kontak={'Ari':'081278888','Dina':'087677776'}

        print('|Ari                      : ',kontak['Ari'],'\n')

        kontak['|Riko']='087654544'
        print('Menambah kontak Riko     : ',kontak,'\n')

        kontak['|Dina']='0889997890'
        print('Mengubah kontak Dina     : ',kontak,'\n')

        print('Menampilkan semua Nama   :',kontak.keys(),'\n')
        print('Menampilkan semua Nomor  :',kontak.values(),'\n')

        print('Semua Kontak             :',kontak,'\n')

       del kontak['Dina']
       print('Menghapus kontak Dina    :',kontak'\n')           
   

HASIL RUN
![Screenshot (132)](https://user-images.githubusercontent.com/116137169/204533658-0e38eaef-9a8a-4dc4-9f75-7ffac501417c.png)
# TUGAS PRAKTIKUM
![Screenshot (135)](https://user-images.githubusercontent.com/116137169/204535469-b28f651e-0bb7-4983-9381-1ca6c3c18cac.png)

BUATLAH PROGRAM SEPERTI DIBAWAH INI
![Screenshot (141)](https://user-images.githubusercontent.com/116137169/204537751-a877e8d4-2230-446a-9c38-eafe4da80b3f.png)
![Screenshot (142)](https://user-images.githubusercontent.com/116137169/204542062-1882454d-d02f-4c48-99c3-4abfc6929685.png)
![Screenshot (143)](https://user-images.githubusercontent.com/116137169/204542107-8560d156-bcfa-4811-81ca-f766f70a94c8.png)

    print(30*"=")
    print("======>  Program Input Nilai  <======")
    print(40*"=")
    data = {}
    while True:
    print("")
    m = input("===>> (L)Lihat, (T)Tambah, (U)Ubah, (H)Hapus, (C)Cari, (K)Keluar : <=== ")
    print(35*"=")
    print("| NO |  Nama     |   Nim    |  Tugas  |  UTS  |  UAS  |   Akir |")
    print(35*"=")
    print(">>>>>>>>>>>>>>>>>>>>>>>> TIDAK ADA DATA <<<<<<<<<<<<<<<<<<<<<<<<")
    if m.lower() == 'k':
        break

    elif m.lower() == 'l':
        print("----- DAFTAR NILAI -----")
        print(35*"=")
        print("| NO |   NAMA     |   NIM        |  TUGAS   |   UTS     |   UAS      |  AKHIR    |")
        print(35*"=")
        i = 0
        for x in data.items():
            i += 1
            print("|  1 |{0:9}   |{1:9}     |{2:9} |{3:9}  |{4:9}   |{5:9}  |" .format(x[0], x[1][0],
                                                                                       x[1][1], x[1][2], x[1][3],
                                                                                       x[1][4], i))

        else:
            print("====================>>>>>>>>>>>>> Tidak Ada Data <<<<<<<<<<<<<====================")

    elif m.lower() == 't':
        print("--------------- Tambah Data ---------------")
        nama = input("Nama                  : ")
        nim = input("Nim                   : ")
        tugas = float(input("Masukan Nilai Tugas   : "))
        uts = float(input("Masukan Nilai UTS     : "))
        uas = float(input("Masukan Nilai UAS     : "))
        akhir = (int(tugas) * .30) + (int(uts) * .35) + (int(uas) * .35)
        data[nama] = nim, tugas, uts, uas, akhir

    elif m.lower() == 'u':
        print("----- Ubah Data Mahasiswa -----")
        nama = input("Nama  : ")
        if nama in data.keys():
            nim = input("Nim : ")
            tugas = float(input("masukan nilai tugas : "))
            uts = float(input("masukan nilai Uts : "))
            uas = float(input("masukan nilai uas : "))
            akhir = (int(tugas) * .30) + (int(uts) * .35) + (int(uas) * .35)
            data[nama] = nim, tugas, uts, uas, akhir

        else:
            print("Tidak Ada data")

    elif m.lower() == 'h':
        print("Hapus Data Mahasiswa")
        nama = input("nama : ")
        if nama in data.keys():
            print("Datanya", nama, "adalah {0}".format(data[nama]))
        else:
            print("Tidaak Ada Data")

    else:
        print("Pilih menu yang tersedia")


![Screenshot (145)](https://user-images.githubusercontent.com/116137169/204545813-e67c5e52-f4d8-4773-bd0e-2933b611aba7.png)

#FLOWCAHRT
![204461520-6e8c31f7-97be-4c92-a107-cee19bc521d4](https://user-images.githubusercontent.com/116137169/204548328-c059e2a3-5d26-4818-bb8a-451e8b7d5e63.png)
