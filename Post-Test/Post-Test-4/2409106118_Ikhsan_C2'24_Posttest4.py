# Nama  :   Ikhsan
# Nim   :   2409106118
# Kelas :   C2'24

loop = 0
while loop < 3:
    print("Masukkan Nama Anda:")
    nama = input()
    print("Masukkan Password Anda:")
    password = int(input())
    if nama == "ikhsan" and password == 118:
        print("Apa Anda Ingin Mengakhiri Program Ini:(lanjut / berhenti)")
        program = input()
        if program == "berhenti":
            print("Program Anda Telah Selesai!")
            break
        else:
            print("Program Di Lanjut!")
        print("Masukkan Merk Mobil Yang Ingin Anda Beli:..!")
        merkmobil = input()
        print("Masukkan Harga Mobil:..!")
        harga = int(input())
        harga = harga
        if merkmobil == "tesla":
            diskon = harga * 0.17
            bayartotal = harga - diskon
            print(merkmobil)
            print(bayartotal)
            print("Terimakasih Telah Berbelanja")
            break
        else:
            if merkmobil == "toyota":
                diskon = harga * 0.21
                bayartotal = harga - diskon
                print(merkmobil)
                print(bayartotal)
                print("Terimakasih Telah Berbelanja")
                break
            else:
                if merkmobil == "hyundai":
                    diskon = harga * 0.23
                    bayartotal = harga - diskon
                    print(merkmobil)
                    print(bayartotal)
                    print("Terimakasih Telah Berbelanja")
                    break
                else:
                    print("Mobil Yang Anda Cari Tidak Ada!")
                    print("Terimakasih Telah Datang Kemari")
                    break
    else:
        print("Apa Anda Ingin Mengakhiri Program Ini:(lanjut / tidak)")
        program = input()
        if program == "lanjut":
            print("Program Anda Telah Selesai!")
            break
        else:
            loop = loop + 1
            print("Batas Percobaan Yang Tersisa Tinggal:!")
            print(loop)
