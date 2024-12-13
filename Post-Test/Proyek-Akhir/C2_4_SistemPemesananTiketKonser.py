# Memanggil Fitur Menghapus Terminal Secara Otomatis
import os

# Memanggil Fitur Privasi Password
import pwinput

# Memanggil fitur PrettyTable (Membuat table)
from prettytable import PrettyTable 

# Inisialisasi data pengguna dan data tiket konser
akun_pengguna = {
    "admin": {'password': 'admin', 'role': 'admin', 'tiket': []},
    "ikhsan": {'password': 'ikhsan123', 'role': 'pengguna', 'tiket': [
        {'judul': 'Lyodra', 'lokasi': 'Samarinda', 'tanggal': '11-Oktober-2024', 'harga': '200000'}
    ]},
    "ocha": {'password': 'ochaocha', 'role': 'pengguna', 'tiket': [
        {'judul': 'Tulus', 'lokasi': 'Balikpapan', 'tanggal': '12-Oktober-2024', 'harga': '500000'},
        {'judul': 'Bruno Mars', 'lokasi': 'Jakarta', 'tanggal': '4-Desember-2024', 'harga': '3000000'}
    ]},
    
}

# Data tiket konser yang tersedia
tiket_konser = {
    "Lyodra": {'lokasi': 'Samarinda', 'tanggal': '11-Oktober-2024', 'harga': '200000'},
    "Tulus": {'lokasi': 'Balikpapan', 'tanggal': '12-Oktober-2024', 'harga': '500000'},
    "Bruno Mars": {'lokasi': 'Jakarta', 'tanggal': '4-Desember-2024', 'harga': '3000000'},
    "Denny Caknan": {'lokasi': 'Samarinda', 'tanggal': '1-Januari-2025', 'harga': '80000'},
    "Payung Teduh": {'lokasi': 'Bandung', 'tanggal': '4-Januari-2025', 'harga': '200000'},
    "Raisa": {'lokasi': 'Surabaya', 'tanggal': '15-Februari-2025', 'harga': '250000'},
    "Noah": {'lokasi': 'Jakarta', 'tanggal': '20-Maret-2025', 'harga': '300000'},
    "Glenn Fredly": {'lokasi': 'Yogyakarta', 'tanggal': '10-April-2025', 'harga': '350000'},
    "Isyana Sarasvati": {'lokasi': 'Medan', 'tanggal': '25-April-2025', 'harga': '220000'},
    "Pashmina": {'lokasi': 'Bali', 'tanggal': '5-Mei-2025', 'harga': '180000'},
    "Kunto Aji": {'lokasi': 'Bandung', 'tanggal': '15-Mei-2025', 'harga': '240000'},
    "Rizky Febian": {'lokasi': 'Jakarta', 'tanggal': '30-Mei-2025', 'harga': '300000'},
    "Siti Nurhaliza": {'lokasi': 'Kuala Lumpur', 'tanggal': '10-Juni-2025', 'harga': '500000'},
    "Marshmello": {'lokasi': 'Jakarta', 'tanggal': '20-Juni-2025', 'harga': '1500000'},
    "Kahitna": {'lokasi': 'Semarang', 'tanggal': '1-Juli-2025', 'harga': '200000'},
    "RAN": {'lokasi': 'Jakarta', 'tanggal': '15-Juli-2025', 'harga': '300000'},
    "Bunga Citra Lestari": {'lokasi': 'Surabaya', 'tanggal': '30-Juli-2025', 'harga': '250000'},
    "Kerispatih": {'lokasi': 'Bandung', 'tanggal': '10-Agustus-2025', 'harga': '220000'},
    "Cinta Laura": {'lokasi': 'Jakarta', 'tanggal': '20-Agustus-2025', 'harga': '300000'},
    "KOTAK": {'lokasi': 'Bali', 'tanggal': '5-September-2025', 'harga': '200000'},
}
# Menambahkan Warna
class style():
# Menghapus Warna
    CEND      = '\33[0m'
# Kode Warna
    CGREY    = '\33[90m'
    CRED2    = '\33[91m'
    CGREEN2  = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2   = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2  = '\33[96m'
    CWHITE2  = '\33[97m'

# Variabel global (Lihat Statistik)
total_konser = len(tiket_konser)
total_tiket_terboking = sum(len(user['tiket']) for user in akun_pengguna.values())


# Fitur Otomatis Clear Terminal
def hapus_terminal():
    os.system('cls')

# Menu Awal Sistem Pembelian Tiket Konser
def tampilkan_menu():
    hapus_terminal()
    print(style.CBLUE2 + """
    ═════════════════════════════════════════════════════════
            Selamat Datang Di Pemesanan Tiket Konser
            Silahkan Pilih Opsi Sign-In atau Sign-Up
            
        ⒈   Daftar Akun
        ⒉   Login
        ⒊   Exit
        
        Copyrigth Kelompok 4 C2
    ═════════════════════════════════════════════════════════
          """)
# Fitur Registrasi Akun
def registrasi_akun():
    hapus_terminal()
    print(style.CGREEN2 + "Halo Pengguna baru! Ayo buat akun dulu")
    Username = input("Username: ")
    # Cek apakah username sudah ada atau digunakan
    if Username in akun_pengguna:
        print(style.CRED2 + "Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
    else:
        # Menentukan Password Yang Ingin Digunakan
        Password = pwinput.pwinput("Password: ")
        # Ini Di gunakan apa bila password kurang dari 8 karakter
        if len(Password) < 8:
            print(style.CRED2 + "\nPassword tidak boleh kurang dari 8 karakter." + style.CEND)
        else:
            # Apabila password lebih dari 8, maka proses lanjut untuk menginput ke dalam (akun_pengguna) sebagai acc baru
            akun_pengguna[Username] = {'password': Password, 'role': 'pengguna', 'tiket': []}
            print(style.CGREEN2 + f"Akun Anda berhasil terdaftar dengan ID: {Username}")
        input("Tekan Enter Untuk Melanjutkan Program")

# Fitur Login Akun
def login_akun():
    hapus_terminal()
    print(style.CYELLOW2 + "Hi, Silahkan login dulu ya!")   
    Username = input("Username: ")
    Password = pwinput.pwinput("Password: ")
    # Proses ini untuk mencari akun yang sudah terdata di (akun_pengguna)
    if Username in akun_pengguna and akun_pengguna[Username]['password'] == Password:
        return Username
    else:
        print(style.CRED2 + "Username dan password anda salah, silahkan coba lagi\n")
        input("Tekan Enter Untuk Melanjutkan Program")
        return None
    
# Menu Tampilan Admin
def tampilkan_menu_admin(Username):
    hapus_terminal()
    print(style.CGREEN2 + f"""
    ═════════════════════════════════════════════════════════
                    Pemesanan Tiket  Konser
                    {Username} Di Menu Admin
            
        ⒈   Tambah Konser
        ⒉   Lihat Konser
        ⒊   Edit Konser
        ⒋   Hapus Konser
        ⒌   Lihat Statistik
        ⒍   Exit
        
        Copyrigth Kelompok 4 C2
    ═════════════════════════════════════════════════════════
          """)
    
# Menu Tampilan Pengguna
def tampilkan_menu_pengguna(Username):
    hapus_terminal()
    print(style.CVIOLET2 + f"""
    ═════════════════════════════════════════════════════════
                    Pemesanan Tiket Konser
                    {Username} Di Menu Pengguna
            
        ⒈   Booking Tiket Tiket Konser
        ⒉   Lihat Tiket Yang Sudah Di Booking
        ⒍   Exit
        
        Copyrigth Kelompok 4 C2
    ═════════════════════════════════════════════════════════
          """)

# Fitur Create (Membuat/Menambah)
def tambah_konser():
    hapus_terminal()
    
    # ini menambahkan ke variable global
    global total_konser
    judul_konser = input("Judul Konser: ")
    if judul_konser in tiket_konser:
        print(style.CRED2 + "Nama Konser Sudah Terpakai")
        input("Tekan Enter Untuk Melanjutkan Program ")
    else:
        lokasi_konser = input("Lokasi Konser: ")
        tanggal_konser = input("Tanggal Konser: ")
        harga_tiket = input("Harga Tiket: ")
        tiket_konser[judul_konser] = {'lokasi': lokasi_konser, 'tanggal': tanggal_konser, 'harga': harga_tiket}
        total_konser += 1
        print(style.CGREEN2 + "Konser berhasil ditambahkan!\n")
        input("Tekan Enter Untuk Melanjutkan Program")

# Fitur Read (Melihat/Menampilkan)
def lihat_konser():
    hapus_terminal()
    print(style.CBLUE2 + """
  _______  _  _          _     _  __                               
 |__   __|(_)| |        | |   | |/ /                               
    | |    _ | | __ ___ | |_  | ' /  ___   _ __   ___   ___  _ __  
    | |   | || |/ // _ \| __| |  <  / _ \ | '_ \ / __| / _ \| '__| 
    | |   | ||   <|  __/| |_  | . \| (_) || | | |\__ \|  __/| |    
    |_|   |_||_|\_\ \___|\__| |_|\_\\___/ |_| |_||___/ \___||_|    
          """)
    table = PrettyTable()
    table.field_names = ["Judul Konser", "Lokasi Konser", "Hari/Tanggal Konser", "Harga Tiket"]
    for judul, tiket in tiket_konser.items():
        table.add_row([judul, tiket['lokasi'], tiket['tanggal'], tiket['harga']])
    print(table)
    input("Tekan Enter Untuk Melanjut Pemrograman!")

# Fitur Update (Meperbaharui/Mengedit)
def edit_konser():
    hapus_terminal()
    try:
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
                harga_baru = int(input("Masukkan harga yang baru: "))
                print("Apa kamu yakin ingin mengedit konser ? ")
                print("1. Iya")
                print("2. Tidak")
                memastikan_edit = input("Pilih: ")
                if memastikan_edit == "1":
                    del tiket_konser[judul_konser]
                    tiket_konser[judul_baru] = {'lokasi': lokasi_baru, 'tanggal': tanggal_baru, 'harga': harga_baru}
                    print(style.CGREEN2 + "Konser yang kamu pilih sudah di edit ya!\n")
                    input("Tekan Enter Untuk Melanjutkan Program")
                elif memastikan_edit == "2":
                    print(style.CRED2 + "Aksi untuk mengedit konser dibatalkan")
                    input("Tekan Enter Untuk Melanjutkan Program")
                else:
                    print(style.CRED2 + "Mohon pilih '1' atau '2'")
                    input("Tekan Enter Untuk Melanjutkan Program")
                    return
            else:
                print(style.CRED2 + "Tidak ada nomor konser yang kamu maksud, silahkan input ulang.\n")
                input("Tekan Enter Untuk Melanjutkan Program")
            return
    except ValueError:
        print(style.CRED2 + "\nInput tidak valid." + style.CEND)
        input("Tekan Enter Untuk Melanjutkan Program")
        
# Fitur Delete (Menghapus) 
def hapus_konser():
    hapus_terminal()
    print(style.CRED2 + """
 __   __  _______  _______  __   __  _______   ___   _  _______  __    _  _______  _______  ______   
|  | |  ||   _   ||       ||  | |  ||       | |   | | ||       ||  |  | ||       ||       ||    _ |  
|  |_|  ||  |_|  ||    _  ||  | |  ||  _____| |   |_| ||   _   ||   |_| ||  _____||    ___||   | ||  
|       ||       ||   |_| ||  |_|  || |_____  |      _||  | |  ||       || |_____ |   |___ |   |_||_ 
|       ||       ||    ___||       ||_____  | |     |_ |  |_|  ||  _    ||_____  ||    ___||    __  |
|   _   ||   _   ||   |    |       | _____| | |    _  ||       || | |   | _____| ||   |___ |   |  | |
|__| |__||__| |__||___|    |_______||_______| |___| |_||_______||_|  |__||_______||_______||___|  |_| 
          """)
    table = PrettyTable()
    table.field_names = ["Judul Konser", "Lokasi Konser", "Hari/Tanggal Konser", "Harga Tiket"]
    for judul, tiket in tiket_konser.items():
        table.add_row([judul, tiket['lokasi'], tiket['tanggal'], tiket['harga']])
    print(style.CGREEN2)
    print(table)
    input("Tekan Enter Untuk Melanjut Pemrograman!")
    
    global total_konser
    if not tiket_konser:
        print("Tidak ada konser yang bisa dihapus.")
        input("Tekan Enter Untuk Melanjutkan Program")
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
                input("Tekan Enter Untuk Melanjutkan Program")
            elif memastikan_hapus == "2":
                print("Aksi untuk menghapus konser dibatalkan")
                input("Tekan Enter Untuk Melanjutkan Program")
            else:
                print("Mohon pilih '1' atau '2'")
                input("Tekan Enter Untuk Melanjutkan Program")
                return
        else:
            print("Tidak ada konser yang kamu maksud, silahkan input ulang.\n")
            input("Tekan Enter Untuk Melanjutkan Program")
            return

# Fitur Booking / Create (Membuat/Menambahkan)
def booking_tiket(Username):
    hapus_terminal()
    # Menambah data ke variable global
    global total_tiket_terboking
    # Untuk Memanggil data di variable lokal (tiket_konser) lalu di print
    for judul, tiket in tiket_konser.items():
        print(style.CGREEN2 + f"Judul Konser: {judul}\nLokasi Konser: {tiket['lokasi']}\nHari/Tanggal Konser: {tiket['tanggal']}\nHarga Tiket: {tiket['harga']}\n")
    judul_konser = input("Judul Konser: ")
    # Jika Sudah memilih tiket yang di booking, maka akan masuk ke data pengguna yang booking
    if judul_konser in tiket_konser:
        akun_pengguna[Username]['tiket'].append({'judul': judul_konser, 'lokasi': tiket_konser[judul_konser]['lokasi'], 'tanggal': tiket_konser[judul_konser]['tanggal'], 'harga': tiket_konser[judul_konser]['harga']})
        total_tiket_terboking += 1
        print(style.CGREEN2 + "Tiket konser berhasil dibooking!\n")
        input("Tekan Enter Untuk Melanjutkan Program")
    else:
        print(style.CRED2 + "Konser tidak tersedia.\n")
        input("Tekan Enter Untuk Melanjutkan Program")

# Fitur Read Untuk Pengunna (Melihat/Menampilkan)
def lihat_tiket(Username):
    hapus_terminal()
    print(style.CVIOLET2 + """
 _______  _______  _______  ___   _  ___  __    _  _______ 
|  _    ||       ||       ||   | | ||   ||  |  | ||       |
| |_|   ||   _   ||   _   ||   |_| ||   ||   |_| ||    ___|
|       ||  | |  ||  | |  ||      _||   ||       ||   | __ 
|  _   | |  |_|  ||  |_|  ||     |_ |   ||  _    ||   ||  |
| |_|   ||       ||       ||    _  ||   || | |   ||   |_| |
|_______||_______||_______||___| |_||___||_|  |__||_______|
          """)
    # Untuk Menggunakan Fitur PrettyTable
    table = PrettyTable()
    table.field_names = ["Judul Konser", "Lokasi Konser", "Hari/Tanggal Konser", "Harga Tiket"]
    for tiket in akun_pengguna[Username]['tiket']:
        table.add_row([tiket['judul'], tiket['lokasi'], tiket['tanggal'], tiket['harga']])
    print(table)
    input("Tekan Enter Untuk Melanjutkan Program")

# Fitur Read KHUSUS ADMIN (Melihat/Menampilkan)
def lihat_statistik():
    hapus_terminal()
    print(style.CBLUE2 + """
 _______  _______  _______  _______  ___  _______  _______  ___  ___   _ 
|       ||       ||   _   ||       ||   ||       ||       ||   ||   | | |
|  _____||_     _||  |_|  ||_     _||   ||  _____||_     _||   ||   |_| |
| |_____   |   |  |       |  |   |  |   || |_____   |   |  |   ||      _|
|_____  |  |   |  |       |  |   |  |   ||_____  |  |   |  |   ||     |_ 
 _____| |  |   |  |   _   |  |   |  |   | _____| |  |   |  |   ||    _  |
|_______|  |___|  |__| |__|  |___|  |___||_______|  |___|  |___||___| |_|
          """)
    table = PrettyTable()
    table.field_names = ["Total Konser Yang Tersedia", "Total Tiket Terboking"]
    table.add_row([total_konser,total_tiket_terboking])
    print(table)
    input("Tekan Enter Untuk Melanjutkan Program")

# Men
# 
# 
# jalankan Program
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
                
                # Opsi Menambah (Create)
                if status == "1":
                    if akun_pengguna[Username]['role'] == 'admin':
                        tambah_konser()
                    else:
                        booking_tiket(Username)
                # Opsi Melihat (Read)   
                elif status == "2":
                    if akun_pengguna[Username]['role'] == 'admin':
                        lihat_konser()
                    else:
                        lihat_tiket(Username)
                # Opsi Editing (Update) Hanya Untuk Admin
                elif status == "3":
                    if akun_pengguna[Username]['role'] == 'admin':
                        edit_konser()
                    else:
                        print("Anda tidak memiliki akses untuk mengedit konser.\n")
                        input("Tekan Enter Untuk Melanjutkan Program")
                # Opsi Menghapus (Delete) Hanya Untuk Admin
                elif status == "4":
                    if akun_pengguna[Username]['role'] == 'admin':
                        hapus_konser()
                    else:
                        print("Anda tidak memiliki akses untuk menghapus konser.\n")
                        input("Tekan Enter Untuk Melanjutkan Program")
                # Opsi Statistik (Hanya Untuk Admin)
                elif status == "5":
                    if akun_pengguna[Username]['role'] == 'admin':
                        lihat_statistik()
                    else:
                        print("Anda tidak memiliki akses untuk melihat statistik.\n")
                        input("Tekan Enter Untuk Melanjutkan Program")
                # Opsi Keluar Dri Program
                elif status == "6":
                        print("Aplikasi Pembelian Tiket Konser ditutup.\n")
                        input("Tekan Enter Untuk Melanjutkan Program")
                        break
                else:
                    print("Input tidak valid, silahkan pilih 1, 2, 3, 4, 5, atau 6.\n")
                    input("Tekan Enter Untuk Melanjutkan Program")
        else:
            continue
    # Opsi ini untuk memberi pengguna pilihan, memberhentikan program atau lanjut
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
            input("Tekan Enter Untuk Melanjutkan Program")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")
        input("Tekan Enter Untuk Melanjutkan Program")