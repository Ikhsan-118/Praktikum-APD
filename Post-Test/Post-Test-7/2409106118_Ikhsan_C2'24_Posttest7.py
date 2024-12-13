from prettytable import PrettyTable

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

# Variabel global
total_konser = len(tiket_konser)
total_tiket_terjual = 0
total_pendapatan = 0

def tampilkan_menu():
    print(style.CBLUE2 + """
    ═════════════════════════════════════════════════════════
        Selamat Datang Di Aplikasi Pemesanan Tiket Konser
            Silahkan Pilih Opsi Sign-In atau Sign-Up
            
        ⒈   Daftar Akun
        ⒉   Login
        ⒊   Exit
        
        Copyrigth.IkhsanC2
    ═════════════════════════════════════════════════════════
          """)

def registrasi_akun():
    print(style.CGREEN2 + "Halo Pengguna baru! Ayo buat akun dulu")
    Username = input("Username: ")
    if Username in akun_pengguna:
        print(style.CRED2 + "Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
    else:
        Password = input("Password: ")
        role = input("Masukkan peran (admin/pengguna): ").lower()
        if role not in ['admin', 'pengguna']:
            print(style.CRED2 + "Peran tidak valid. Harus 'admin' atau 'pengguna'.")
            return
        akun_pengguna[Username] = {'password': Password, 'role': role, 'tiket': []}
        print(style.CGREEN2 + f"Akun Anda berhasil terdaftar dengan ID: {Username}")

def login_akun():
    print(style.CYELLOW2 + "Hi, Silahkan login dulu ya!")   
    Username = input("Username: ")
    Password = input("Password: ")
    if Username in akun_pengguna and akun_pengguna[Username]['password'] == Password:
        return Username
    else:
        print(style.CRED2 + "Username dan password anda salah, silahkan coba lagi\n")
        return None

def tampilkan_menu_admin(Username):
    print(style.CGREEN2 + f"""
    ═════════════════════════════════════════════════════════
                    Penjualan Tiket Konser Sanz
                        {Username} Di Menu Admin
            
        ⒈   Tambah Konser
        ⒉   Lihat Konser
        ⒊   Edit Konser
        ⒋   Hapus Konser
        ⒌   Lihat Statistik
        ⒍   Exit
        
        Copyrigth.IkhsanC2
    ═════════════════════════════════════════════════════════
          """)

def tampilkan_menu_pengguna(Username):
    print(style.CVIOLET2 + f"""
    ═════════════════════════════════════════════════════════
                    Penjualan Tiket Konser Sanz
                        {Username} Di Menu Pengguna
            
        ⒈   Beli Tiket Konser
        ⒉   Lihat Tiket Yang Sudah Di Beli
        ⒍   Exit
        
        Copyrigth.IkhsanC2
    ═════════════════════════════════════════════════════════
          """)

def tambah_konser():
    global total_konser
    judul_konser = input("Judul Konser: ")
    lokasi_konser = input("Lokasi Konser: ")
    tanggal_konser = input("Hari/Tanggal Konser: ")
    harga_tiket = input("Harga Tiket: ")
    tiket_konser[judul_konser] = {'lokasi': lokasi_konser, 'tanggal': tanggal_konser, 'harga': harga_tiket}
    total_konser += 1
    print(style.CGREEN2 + "Konser berhasil ditambahkan!\n")

def lihat_konser():
    table = PrettyTable()
    table.field_names = ["Judul Konser", "Lokasi Konser", "Hari/Tanggal Konser", "Harga Tiket"]
    for judul, tiket in tiket_konser.items():
        table.add_row([judul, tiket['lokasi'], tiket['tanggal'], tiket['harga']])
    print(table)

def edit_konser():
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
            print("Apa kamu yakin ingin mengedit konser ? ")
            print("1. Iya")
            print("2. Tidak")
            memastikan_edit = input("Pilih: ")
            if memastikan_edit == "1":
                del tiket_konser[judul_konser]
                tiket_konser[judul_baru] = {'lokasi': lokasi_baru, 'tanggal': tanggal_baru, 'harga': harga_baru}
                print(style.CGREEN2 + "Konser yang kamu pilih sudah di edit ya!\n")
            elif memastikan_edit == "2":
                print(style.CRED2 + "Aksi untuk mengedit konser dibatalkan")
            else:
                print(style.CRED2 + "Mohon pilih '1' atau '2'")
        else:
            print(style.CRED2 + "Tidak ada nomor konser yang kamu maksud, silahkan input ulang.\n")

def hapus_konser():
    global total_konser
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
                del tiket_konser[hapus]
                total_konser -= 1
                print("Konser yang kamu pilih sudah dihapus!\n")
            elif memastikan_hapus == "2":
                print("Aksi untuk menghapus konser dibatalkan")
            else:
                print("Mohon pilih '1' atau '2'")
        else:
            print("Tidak ada konser yang kamu maksud, silahkan input ulang.\n")

def beli_tiket(Username):
    global total_tiket_terjual, total_pendapatan
    for judul, tiket in tiket_konser.items():
        print(style.CGREEN2 + f"Judul Konser: {judul}\nLokasi Konser: {tiket['lokasi']}\nHari/Tanggal Konser: {tiket['tanggal']}\nHarga Tiket: {tiket['harga']}\n")
    judul_konser = input("Judul Konser: ")
    if judul_konser in tiket_konser:
        akun_pengguna[Username]['tiket'].append({'judul': judul_konser, 'lokasi': tiket_konser[judul_konser]['lokasi'], 'tanggal': tiket_konser[judul_konser]['tanggal'], 'harga': tiket_konser[judul_konser]['harga']})
        total_tiket_terjual += 1
        total_pendapatan += int(tiket_konser[judul_konser]['harga'].replace('Rp ', ''))
        print(style.CGREEN2 + "Tiket konser berhasil dibeli!\n")
    else:
        print(style.CRED2 + "Konser tidak tersedia.\n")

def lihat_tiket(Username):
    for tiket in akun_pengguna[Username]['tiket']:
        print (style.CGREEN2 + f"Judul Konser: {tiket['judul']}\nLokasi Konser: {tiket['lokasi']}\nHari/Tanggal Konser: {tiket['tanggal']}\nHarga Tiket: {tiket['harga']}\n")
    if not akun_pengguna[Username]['tiket']:
        print(style.CRED2 + "Opps, saat ini kamu belum punya tiket, silahkan beli tiket terlebih dahulu.\n")

def lihat_statistik():
    print(style.CGREEN2 + f"Total Konser: {total_konser}")
    print(style.CGREEN2 + f"Total Tiket Terjual: {total_tiket_terjual}")
    print(style.CGREEN2 + f"Total Pendapatan: Rp {total_pendapatan}")

while True:
    tampilkan_menu()
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        registrasi_akun()
    elif opsi == "2":
        Username = login_akun()
        if Username:
            while True:
                if akun_pengguna[Username]['role'] == 'admin':
                    tampilkan_menu_admin(Username)
                else:
                    tampilkan_menu_pengguna(Username)
                status = input("Pilih opsi: ")
                print(" ")

                if status == "1":
                    if akun_pengguna[Username]['role'] == 'admin':
                        tambah_konser()
                    else:
                        beli_tiket(Username)
                elif status == "2":
                    if akun_pengguna[Username]['role'] == 'admin':
                        lihat_konser()
                    else:
                        lihat_tiket(Username)
                elif status == "3":
                    if akun_pengguna[Username]['role'] == 'admin':
                        edit_konser()
                    else:
                        print("Anda tidak memiliki akses untuk mengedit konser.\n")
                elif status == "4":
                    if akun_pengguna[Username]['role'] == 'admin':
                        hapus_konser()
                    else:
                        print("Anda tidak memiliki akses untuk menghapus konser.\n")
                elif status == "5":
                    if akun_pengguna[Username]['role'] == 'admin':
                        lihat_statistik()
                    else:
                        print("Anda tidak memiliki akses untuk melihat statistik.\n")
                elif status == "6":
                        print("Aplikasi Pembelian Tiket Konser ditutup.\n")
                        break
                else:
                    print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
        else:
            continue
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