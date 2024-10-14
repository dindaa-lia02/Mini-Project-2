from prettytable import PrettyTable

table = PrettyTable()

daftar_baju = []
riwayat_sewa = []

'''==============================================================================================================================='''
'''                                                             Read (Melihat daftar baju)                                        '''
'''==============================================================================================================================='''

def tampilkan_daftar_baju():
    table.clear_rows()
    table.field_names = ["Kode_baju", "Nama", "Masa Sewa", "Harga Sewa", "Status"]
    for baju in daftar_baju:
        status = "Tersedia" 
        if baju["tersedia"]: 
            status = "Tersedia"
        else: 
            status = "Disewa"
        table.add_row([baju["Kode_baju"], baju["nama"], baju["masa_sewa"], f"Rp {baju['harga_sewa']}", status])
    print(table)

'''==============================================================================================================================='''
'''                                                           Create (Menambah daftar baju)                                       '''
'''==============================================================================================================================='''

def tambah_baju(Kode_baju, nama, masa_sewa, harga_sewa):
    baju = {
        "Kode_baju": Kode_baju,
        "nama": nama,
        "masa_sewa": masa_sewa,
        "harga_sewa": harga_sewa,
        "tersedia": True
    }
    daftar_baju.append(baju)

'''==============================================================================================================================='''
'''                                                             Update (Mengupdate daftar baju)                                   '''
'''==============================================================================================================================='''

def update_baju(Kode_baju, nama, masa_sewa, harga_sewa):
    for baju in daftar_baju:
        if baju["Kode_baju"] == Kode_baju:
            baju["nama"] = nama
            baju["masa_sewa"] = masa_sewa
            baju["harga_sewa"] = harga_sewa
            print("Data baju adat berhasil diupdate.")
            return
    print("Baju adat dengan Kode tersebut tidak ditemukan.")

'''==============================================================================================================================='''
'''                                                             Delete (Menghapus daftar baju)                                        '''
'''==============================================================================================================================='''

def hapus_baju(Kode_baju):
    for baju in daftar_baju:
        if baju["Kode_baju"] == Kode_baju:
            daftar_baju.remove(baju)
            print("Baju adat berhasil dihapus.")
            return
    print("Baju adat dengan Kode tersebut tidak ditemukan.")

def sewa_baju(Kode_baju, nama_penyewa, lama_sewa):
    for baju in daftar_baju:
        if baju["Kode_baju"] == Kode_baju and baju["tersedia"]:
            baju["tersedia"] = False
            harga_total = 0
            if lama_sewa <= baju["masa_sewa"]:
                harga_total = baju["harga_sewa"]
            else:
                harga_normal = baju["harga_sewa"]
                hari_tambahan = lama_sewa - baju["masa_sewa"]
                harga_tambahan = int(harga_normal * 0.1) * hari_tambahan  
                harga_total = harga_normal + harga_tambahan
            
            riwayat_sewa.append({
                "penyewa": nama_penyewa,
                "baju": baju,
                "lama_sewa": lama_sewa,
                "harga_total": harga_total
            })
            print(f"Baju berhasil disewa. Total harga sewa: Rp {harga_total}")
            return
    print("Baju tidak tersedia atau Kode tidak valid.")

def kembalikan_baju(Kode_baju):
    for baju in daftar_baju:
        if baju["Kode_baju"] == Kode_baju and not baju["tersedia"]:
            baju["tersedia"] = True
            print("Baju berhasil dikembalikan.")
            return
    print("Baju tidak ditemukan atau sudah tersedia.")

def tampilkan_riwayat_sewa():
    table.clear_rows()
    table.field_names = ["Penyewa", "Kode Baju", "Nama Baju", "Lama Sewa", "Total Harga Sewa"]
    for sewa in riwayat_sewa:
        table.add_row([sewa["penyewa"], sewa["baju"]["Kode_baju"], sewa["baju"]["nama"], f"{sewa['lama_sewa']} hari", f"Rp {sewa['harga_total']}"])
    print(table)

'''==============================================================================================================================='''
'''                                                             Menu Admin                                                        '''
'''==============================================================================================================================='''

def menu_admin():
    while True:
        print("\n⏖⏖⏖ Menu Admin ⏖⏖⏖")
        print("1. Lihat Daftar Baju")
        print("2. Tambah Baju Adat")
        print("3. Update Baju Adat")
        print("4. Hapus Baju Adat")
        print("5. Lihat Riwayat Sewa")
        print("6. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tampilkan_daftar_baju()
        elif pilihan == "2":
            Kode_baju = input("Masukkan Kode baju: ")
            nama = input("Masukkan nama baju: ")
            masa_sewa = int(input("Masukkan masa sewa normal (dalam hari): "))
            harga = int(input("Masukkan harga sewa: "))
            tambah_baju(Kode_baju, nama, masa_sewa, harga)
            print("Baju adat berhasil ditambahkan.")
        elif pilihan == "3":
            Kode_baju = input("Masukkan Kode baju yang akan diupdate: ")
            nama = input("Masukkan nama baru: ")
            masa_sewa = int(input("Masukkan masa sewa normal baru (dalam hari): "))
            harga = int(input("Masukkan harga sewa baru: "))
            update_baju(Kode_baju, nama, masa_sewa, harga)
        elif pilihan == "4":
            Kode_baju = input("Masukkan Kode baju yang akan dihapus: ")
            hapus_baju(Kode_baju)
        elif pilihan == "5":
            tampilkan_riwayat_sewa()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid.")

'''==============================================================================================================================='''
'''                                                             Menu Customer                                                     '''
'''==============================================================================================================================='''

def menu_customer():
    while True:
        print("\n⏖⏖⏖ Menu Customer ⏖⏖⏖")
        print("1. Lihat Daftar Baju")
        print("2. Sewa Baju")
        print("3. Kembalikan Baju")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tampilkan_daftar_baju()
        elif pilihan == "2":
            Kode_baju = input("Masukkan Kode baju yang ingin disewa: ")
            nama_penyewa = input("Masukkan nama Anda: ")
            lama_sewa = int(input("Masukkan lama sewa (dalam hari): "))
            sewa_baju(Kode_baju, nama_penyewa, lama_sewa)
        elif pilihan == "3":
            Kode_baju = input("Masukkan Kode baju yang ingin dikembalikan: ")
            kembalikan_baju(Kode_baju)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

'''==============================================================================================================================='''
'''                                                             Login Admin dan Customer                                          '''
'''==============================================================================================================================='''

users = {
    "admin": {"password": "dinda076", "role": "admin"},
    "customer": {"password": "customer283", "role": "customer"}
}

def login():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in users and users[username]["password"] == password:
            print(f"Login berhasil sebagai {users[username]['role']}.")
            return users[username]["role"]
        else:
            print("Username atau password salah. Silakan coba lagi.")

def main():
    tambah_baju("B001", "Kebaya", 3, 100000)
    tambah_baju("B002", "Baju Bodo", 4, 150000)
    tambah_baju("B003", "Ulos", 5, 120000)

    while True:
        print("\n⏖⏖⏖ Sistem Penyewaan Baju Adat ⏖⏖⏖")
        print("1. Admin")
        print("2. Customer")
        print("3. Keluar")
        pilihan = input("Silahkan pilih menu (1-3): ")

        if pilihan == "1":
            role = login()
            if role == "admin":
                menu_admin()
        elif pilihan == "2":
            role = login ()
            if role == "customer":
                menu_customer()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem penyewaan baju adat.")
            break
        else:
            print("Pilihan tidak valid. Silahkan coba lagi.")

if __name__ == "__main__":
    main()