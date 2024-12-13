# Nama  :   Ikhsan
# Nim   :   2409106118
# Kelas :   C2'24

# Inisialisasi data pengguna dan data tiket konser
akun_pengguna = []
tiket_konser = []

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
        akuna = False
        for akun in akun_pengguna:
            if akun[0] == Username:  # Memeriksa apakah username sudah ada
                akuna = True
                break
        if akuna:
            print(style.CRED2 + "Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            role = input("Masukkan peran (admin/pengguna): ").lower()
            if role not in ['admin', 'pengguna']:
                print(style.CRED2 + "Peran tidak valid. Harus 'admin' atau 'pengguna'.")
                continue
            akun_pengguna.append([Username, Password, role, []])  # Simpan username, password, dan tiket (sebagai list kosong)
            print(style.CGREEN2 + f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    elif opsi == "2":
        print(style.CYELLOW2 + "Hi, Silahkan login dulu ya!")   
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akun_pengguna:
            if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
                while True:
                    print(style.CGREEN2 +      f"\nSelamat datang {Username}!")
                    print(style.CYELLOW2 +      "╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
                    if akun[2] == 'admin':
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
                        if akun[2] == 'admin':
                            judul_konser = input("Judul Konser: ")
                            lokasi_konser = input("Lokasi Konser: ")
                            tanggal_konser = input("Hari/Tanggal Konser: ")
                            harga_tiket = input("Harga Tiket: ")
                            tiket_konser.append([judul_konser, lokasi_konser, tanggal_konser, harga_tiket])  # Menambahkan tiket ke dalam list
                            print(style.CGREEN2 + "Konser berhasil ditambahkan!\n")
                        else:
                            judul_konser = input("Judul Konser: ")
                            for tiket in tiket_konser:
                                if tiket[0] == judul_konser:
                                    akun[3].append([judul_konser, tiket[1], tiket[2], tiket[3]])  # Menambahkan tiket ke dalam list
                                    print(style.CGREEN2 + "Tiket konser berhasil dibeli!\n")
                                    break
                            else:
                                print(style.CRED2 + "Konser tidak tersedia.\n")

                    elif status == "2":
                        if akun[2] == 'admin':
                            for tiket in tiket_konser:  
                                print(style.CGREEN2 + f"Judul Konser: {tiket[0]}\nLokasi Konser: {tiket[1]}\nHari/Tanggal Konser: {tiket[2]}\nHarga Tiket: {tiket[3]}\n")
                            if not tiket_konser:
                                print(style.CRED2 + "Opps, saat ini belum ada konser, silahkan tambah konser terlebih dahulu.\n")
                        else:
                            for tiket in akun[3]:  
                                print(style.CGREEN2 + f"Judul Konser: {tiket[0]}\nLokasi Konser: {tiket[1]}\nHari/Tanggal Konser: {tiket[2]}\nHarga Tiket: {tiket[3]}\n")
                            if not akun[3]:
                                print(style.CRED2 + "Opps, saat ini kamu belum punya tiket, silahkan beli tiket terlebih dahulu.\n")
                    elif status == "3":
                        if akun[2] == 'admin':
                            if not tiket_konser:
                                print(style.CRED2 + "Tidak ada konser yang bisa diedit.")
                            else:
                                edit = int(input("Konser nomor berapa yang ingin kamu edit: ")) - 1
                                if 0 <= edit < len(tiket_konser):
                                    judul_baru = input("Masukkan judul yang baru: ")
                                    lokasi_baru = input("Masukkan lokasi yang baru: ")
                                    tanggal_baru = input("Masukkan hari/tanggal konser baru: ")
                                    harga_baru = input("Masukkan harga yang baru: ")
                                    print("Apa kamu yakin ingin mengedit konser ?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_edit = input("Pilih: ")
                                    if memastikan_edit == "1":
                                        tiket_konser[edit] = [judul_baru, lokasi_baru, tanggal_baru, harga_baru]  # Mengedit konser
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
                        if akun[2] == 'admin':
                            if not tiket_konser:
                                print("Tidak ada konser yang bisa dihapus.")
                            else:
                                hapus = int(input("Konser nomor berapa yang ingin dihapus: ")) - 1
                                if 0 <= hapus < len(tiket_konser):
                                    print(f"Apa kamu yakin ingin menghapus konser ? ")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del tiket_konser[hapus]  # Menghapus konser dari list
                                        print("Konser yang kamu pilih sudah dihapus!\n")
                                    elif memastikan_hapus == "2":
                                        print("Aksi untuk menghapus konser dibatalkan")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor konser yang kamu maksud, silahkan input ulang.\n")
                        else:
                            print("Anda tidak memiliki akses untuk menghapus konser.\n")

                    elif status == "5":
                        print("Aplikasi Pembelian Tiket Konser ditutup.\n")
                        break

                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break
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