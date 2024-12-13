# Inisialisasi data pengguna dan data tiket konser
akun_pengguna = {
    "penjual": {'password': '1', 'role': 'admin', 'tiket': []},
    "pembeli": {'password': '2', 'role': 'pengguna', 'tiket': []}
}
tiket_konser = {
    "Lyodra": {'lokasi': 'Samarinda', 'tanggal': '11-Oktober-2024', 'harga': 'Rp 200000'},
    "Tulus": {'lokasi': 'Balikpapan', 'tanggal': '12-Oktober-2024', 'harga': 'Rp 500000'},
    "Bruno Mars": {'lokasi': 'Jakarta', 'tanggal': '4-Desember-2024', 'harga': 'Rp 3000000'},
    "Denny Caknan": {'lokasi': 'Samarinda', 'tanggal': '1-Januari-2025', 'harga': 'Rp 80000'},
    "Payung Teduh": {'lokasi': 'Bandung', 'tanggal': '4-Januari-2025', 'harga': 'Rp 200000'}
}

# Menambahkan Warna
class style():
    CEND      = '\33[0m'
    CBOLD     = '\33[1m'
    CITALIC   = '\33[3m'
    CURL      = '\33[4m'
    CBLINK    = '\33[5m'
    CBLINK2   = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK  = '\33[30m'
    CRED    = '\33[31m' 
    CGREEN  = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE   = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE  = '\33[36m'
    CWHITE  = '\33[37m'

    CBLACKBG  = '\33[40m'
    CREDBG    = '\33[41m'
    CGREENBG  = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG   = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG  = '\33[46m'
    CWHITEBG  = '\33[47m'

    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

    CGREYBG    = '\33[100m'
    CREDBG2    = '\33[101m'
    CGREENBG2  = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2   = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2  = '\33[106m'
    CWHITEBG2  = '\33[107m'

while True:
    print(style.CBLUE2 + "Halo! Selamat Datang di Pemesanan Tiket Konser")  
    print(style.CWHITE + "Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print(style.CGREEN2 + "╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
    print(style.CBEIGE2 + "╠ 1. Daftar akun                          ╣")
    print(style.CGREEN2 + "╠ 2. Login                                ╣")
    print(style.CRED2 +   "╠ 3. Exit                                 ╣")
    print(style.CBLUE2 +  "╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print(style.CGREEN2 + "Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        if Username in akun_pengguna:
            print(style.CRED2 + "Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (admin/pengguna): ").lower()
            if role not in ['admin', 'pengguna']:
                print(style.CRED2 + "Peran tidak valid. Harus 'admin' atau 'pengguna'.")
                continue
            akun_pengguna[Username] = {'password': Password, 'role': role, 'tiket': []}  # Simpan username, password , dan tiket (sebagai list kosong)
            print(style.CGREEN2 + f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    elif opsi == "2":
        print(style.CYELLOW2 + "Hi, Silahkan login dulu ya!")   
        Username = input("Username: ")
        Password = input("Password: ")
        if Username in akun_pengguna and akun_pengguna[Username]['password'] == Password:  # Cocokkan username dan password
            while True:
                print(style.CGREEN2 +      f"\nSelamat datang {Username}!")
                print(style.CYELLOW2 +      "╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
                if akun_pengguna[Username]['role'] == 'admin':
                    print(style.CBEIGE2 +   "╠ 1. Tambah konser                        ╣")
                    print(style.CGREEN2 +   "╠ 2. Lihat konser                         ╣")
                    print(style.CYELLOW2 +  "╠ 3. Edit konser                          ╣")
                    print(style.CRED2 +     "╠ 4. Hapus konser                         ╣")
                else:
                    print(style.CBEIGE2 +   "╠ 1. Beli tiket konser                    ╣")
                    print(style.CGREEN2 +   "╠ 2. Lihat tiket konser yang sudah dibeli ╣")
                print(style.CBLUE2 +        "╠ 5. Exit                                 ╣")
                print(style.CGREEN2 +       "╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝")

                status = input("Pilih opsi: ")
                print(" ")

                if status == "1":
                    if akun_pengguna[Username]['role'] == 'admin':
                        judul_konser = input("Judul Konser: ")
                        lokasi_konser = input("Lokasi Konser: ")
                        tanggal_konser = input("Hari/Tanggal Konser: ")
                        harga_tiket = input("Harga Tiket: ")
                        tiket_konser[judul_konser] = {'lokasi': lokasi_konser, 'tanggal': tanggal_konser, 'harga': harga_tiket}  # Menambahkan tiket ke dalam dictionary
                        print(style.CGREEN2 + "Konser berhasil ditambahkan!\n")
                    else:
                        for judul, tiket in tiket_konser.items():
                            print(style.CGREEN2 + "Tiket Yang Tersedia: ")
                            print(style.CGREEN2 + f"Judul Konser: {judul}\nLokasi Konser: {tiket['lokasi']}\nHari/Tanggal Konser: {tiket['tanggal']}\nHarga Tiket: {tiket['harga']}\n")
                        judul_konser = input("Judul Konser: ")
                        if judul_konser in tiket_konser:
                            akun_pengguna[Username]['tiket'].append({'judul': judul_konser, 'lokasi': tiket_konser[judul_konser]['lokasi'], 'tanggal': tiket_konser[judul_konser]['tanggal'], 'harga': tiket_konser[judul_konser]['harga']})  # Menambahkan tiket ke dalam list
                            print(style.CGREEN2 + "Tiket konser berhasil dibeli!\n")
                        else:
                            print(style.CRED2 + "Konser tidak tersedia.\n")

                elif status == "2":
                    if akun_pengguna[Username]['role'] == 'admin':
                        for judul, tiket in tiket_konser.items():  
                            print(style.CGREEN2 + f"Judul Konser: {judul}\nLokasi Konser: {tiket['lokasi']}\nHari/Tanggal Konser: {tiket['tanggal']}\nHarga Tiket: {tiket['harga']}\n")
                        if not tiket_konser:
                            print(style.CRED2 + "Opps, saat ini belum ada konser, silahkan tambah konser terlebih dahulu.\n")
                    else:
                        for tiket in akun_pengguna[Username]['tiket']:  
                            print(style.CGREEN2 + f"Judul Konser: {tiket['judul']}\nLokasi Konser: {tiket['lokasi']}\nHari/Tanggal Konser: { tiket['tanggal']}\nHarga Tiket: {tiket['harga']}\n")
                        if not akun_pengguna[Username]['tiket']:
                            print(style.CRED2 + "Opps, saat ini kamu belum punya tiket, silahkan beli tiket terlebih dahulu.\n")
                elif status == "3":
                    if akun_pengguna[Username]['role'] == 'admin':
                        if not tiket_konser:
                            print(style.CRED2 + "Tidak ada konser yang bisa diedit.")
                        else:
                            print("Daftar Konser:")
                            for i, (judul, tiket) in enumerate(tiket_konser.items()):
                                print(f"{i+1}. {judul}")
                            edit = int(input("Masukkan nomor konser yang ingin diedit: ")) - 1
                            if 0 <= edit < len(tiket_konser):
                                judul_konser = list(tiket_konser.keys())[edit]
                                judul_baru = input("Masukkan judul yang baru: ")
                                lokasi_baru = input("Masukkan lokasi yang baru: ")
                                tanggal_baru = input("Masukkan hari/tanggal konser baru: ")
                                harga_baru = input("Masukkan harga yang baru: ")
                                print("Apa kamu yakin ingin mengedit konser ?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    del tiket_konser[judul_konser]
                                    tiket_konser[judul_baru] = {'lokasi': lokasi_baru, 'tanggal': tanggal_baru, 'harga': harga_baru}  # Mengedit konser
                                    print(style.CGREEN2 + "Konser yang kamu pilih sudah di edit ya!\n")
                                elif memastikan_edit == "2":
                                    print(style.CRED2 + "Aksi untuk mengedit konser dibatalkan")
                                else:
                                    print(style.CRED2 + "Mohon pilih '1' atau '2'")
                            else:
                                print(style.CRED2 + "Tidak ada nomor konser yang kamu maksud, silahkan input ulang.\n")
                    else:
                        print("Anda tidak memiliki akses untuk mengedit konser.\n")

                elif status == "4":
                    if akun_pengguna[Username]['role'] == 'admin':
                        if not tiket_konser:
                            print("Tidak ada konser yang bisa dihapus.")
                        else:
                            hapus = input("Masukkan judul konser yang ingin dihapus: ")
                            if hapus in tiket_konser:
                                print(f"Apa kamu yakin ingin menghapus konser ? ")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del tiket_konser[hapus]  # Menghapus konser dari dictionary
                                    print("Konser yang kamu pilih sudah dihapus!\n")
                                elif memastikan_hapus == "2":
                                    print("Aksi untuk menghapus konser dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada konser yang kamu maksud, silahkan input ulang.\n")
                    else:
                        print("Anda tidak memiliki akses untuk menghapus konser.\n")

                elif status == "5":
                    print("Aplikasi Pembelian Tiket Konser ditutup.\n")
                    break

                else:
                    print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
        else:
            print("Username dan password anda salah, silahkan coba lagi\n")

    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar dari aplikasi? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")