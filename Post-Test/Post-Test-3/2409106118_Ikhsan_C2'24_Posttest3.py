merkmobil = input("Masukkan Merk Mobil Yang Ingin Anda Beli:..!")
harga = int(input("Masukkan Harga Mobil:..!"))
if merkmobil == "tesla":
    diskon = harga * 0.17
    bayartotal = int(harga - diskon)
    print(
        f"{merkmobil},{bayartotal}. Terimakasih Telah Berbelanja"
        )
elif merkmobil == "toyota":
    diskon = harga * 0.21
    bayartotal = harga - diskon
    print(
        f"{merkmobil},{bayartotal}. Terimakasih Telah Berbelanja"
        )
elif merkmobil == "hyundai":
    diskon = harga * 0.23
    bayartotal = harga - diskon
    print(
        f"{merkmobil},{bayartotal}. Terimakasih Telah Berbelanja"
        )
else:
    print("Mobil Yang Anda Cari Tidak Ada!")
    print("Terimakasih Telah Datang Kemari")
