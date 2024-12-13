# Nama  : Ikhsan
# Nim   : 2409106118
# Kelas : C 2024

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
harga_setiap_mobil = int(input("Masukkan harga setiap mobil: "))

diskon_tesla = 0.17  # 17%
diskon_toyota = 0.21  # 21%
diskon_hyundai = 0.23  # 23%

harga_tesla_setelah_diskon = harga_setiap_mobil - (harga_setiap_mobil * diskon_tesla)
harga_toyota_setelah_diskon = harga_setiap_mobil - (harga_setiap_mobil * diskon_toyota)
harga_hyundai_setelah_diskon = harga_setiap_mobil - (harga_setiap_mobil * diskon_hyundai)

modulus_nim = int(nim) % 7

output = (f"{nama} Dengan Nim {nim},"
          f"Mobil Tesla seharga {harga_setiap_mobil} diskon 17% menjadi {harga_tesla_setelah_diskon}, "
          f"Mobil Toyota seharga {harga_setiap_mobil} diskon 21% menjadi {harga_toyota_setelah_diskon}, "
          f"Mobil Hyundai seharga {harga_setiap_mobil} diskon 23% menjadi {harga_hyundai_setelah_diskon}, "
          f"dan {harga_setiap_mobil} modulus 7 adalah {modulus_nim}.")

print(output)
