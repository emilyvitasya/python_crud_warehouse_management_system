# ===================================
# Warehouse Stock Management System (Sembako)
# ===================================
# Developed by. Emily Vitasya Haloho

from datetime import datetime, date

# Kelas Sembako
class Sembako:
    def __init__(self, kode, nama, jenis, stok, harga, tanggal_masuk, kadaluarsa):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.stok = stok
        self.harga = harga
        self.tanggal_masuk = tanggal_masuk
        self.kadaluarsa = kadaluarsa

# Database sementara
datasembako = [
    Sembako('S101', 'Beras Premium 5kg', 'Beras', 25, 65000, '1-11-2024', '6 Bulan'),
    Sembako('S102', 'Minyak Goreng Bimoli 2L', 'Minyak', 40, 38000, '1-11-2024', '1 Tahun'),
    Sembako('S103', 'Gula Pasir Gulaku 1kg', 'Gula', 50, 16000, '1-11-2024', '1 Tahun'),
    Sembako('S104', 'Tepung Terigu Segitiga Biru', 'Tepung', 30, 14500, '1-11-2024', '8 Bulan'),
    Sembako('S105', 'Telur Ayam Ras 1kg', 'Telur', 20, 28000, '1-11-2024', '2 Minggu')
]

# Fungsi ShowList untuk format tabel dinamis
def ShowList(data_sembako):
    header = ["Kode", "Nama", "Jenis", "Stok", "Harga", "Tanggal_Masuk", "Kadaluarsa"]
    
    lebar_kolom_min = {
        "Harga": 15,
        "Tanggal_Masuk": 15,
        "Kadaluarsa": 12
    }
    
    lebar_kolom = {
        kolom: max(
            lebar_kolom_min.get(kolom, 8),
            max(len(str(getattr(item, kolom.lower()))) for item in data_sembako)
        ) for kolom in header
    }
    
    for kolom in header:
        print(f"{kolom:<{lebar_kolom[kolom]}} ", end="")
    print()
    
    for lebar in lebar_kolom.values():
        print("-" * lebar, end=" ")
    print()
    
    for item in data_sembako:
        for kolom in header:
            nilai = getattr(item, kolom.lower())
            if kolom == "Harga":
                nilai = f"Rp{nilai:,}"
            elif kolom == "Tanggal_Masuk":
                if isinstance(nilai, date):
                    nilai = nilai.strftime("%d-%m-%Y")
                else:
                    nilai = datetime.strptime(nilai, "%d-%m-%Y").date().strftime("%d-%m-%Y")
            else:
                nilai = str(nilai)
            print(f"{nilai:<{lebar_kolom[kolom]}} ", end="")
        print()

# Fungsi Pencarian
def SearchList(Input):
    return list(filter(lambda data: data.kode == str(Input), datasembako))

def tampilkan_data_sembako():
    if not datasembako:
        print("Tidak ada data sembako.")
        return
    ShowList(datasembako)

# Fungsi Tambah Produk
def tambah_produk():
    while True:
        tampilkan_data_sembako()
        
        while True:
            kode_sembako = input('\nMasukkan Kode Sembako baru (minimal 4 karakter, kombinasi huruf dan angka): ')
            if len(kode_sembako) >= 4 and kode_sembako.isalnum():
                if any(sembako.kode == kode_sembako for sembako in datasembako):
                    print('Kode sudah ada di database, silahkan masukkan kode baru.')
                else:
                    break
            else:
                print('Kode tidak valid. Minimal 4 karakter, kombinasi huruf dan angka.')

        nama = input('Nama Sembako: ').capitalize()
        jenis = input('Jenis Sembako: ').capitalize()

        while True:
            try:
                stok = int(input('Stok Sembako: '))
                if stok < 0:
                    raise ValueError("Stok harus berupa bilangan positif.")
                break
            except ValueError:
                print('Stok harus angka.')

        while True:
            try:
                harga = int(input('Harga: '))
                if harga < 0:
                    raise ValueError("Harga harus berupa bilangan positif.")
                break
            except ValueError:
                print('Harga harus angka.')

        while True:
            tanggal_str = input('Tanggal Masuk (format DD-MM-YYYY): ')
            try:
                tanggal_masuk = datetime.strptime(tanggal_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print('Format tanggal tidak valid. Gunakan DD-MM-YYYY.')

        kadaluarsa = input('Durasi Kadaluarsa (contoh: 6 Bulan / 1 Tahun): ')
        konfirmasi = input('Apakah anda yakin data ini akan ditambahkan (Y/T)? ').capitalize()
        if konfirmasi == 'Y':
            datasembako.append(Sembako(kode_sembako, nama, jenis, stok, harga, tanggal_masuk, kadaluarsa))
            tampilkan_data_sembako()
            print('\n Stok Sembako Berhasil ditambahkan')
            return
        elif konfirmasi == 'T':
            print('\nData Sembako Tidak Jadi ditambahkan')
            return

def MenambahData():
    while True:
        create_data = input('''
========== Menu Menambah Stok Sembako ==========
1. Menambah Stok Sembako ke database
2. Kembali ke menu utama
Silahkan pilih menu diatas : ''')
        
        if create_data == '1':
            tambah_produk()
        elif create_data == '2':
            break
        else:
            print('\nPilihan yang anda masukkan salah, Silahkan Masukkan pilihan range [1-2]')

# Fungsi Update Data (Sudah Diperbaiki)
def UpdateData():
    while True:
        Updatedatacust = input('''
======= Menu Ubah Data Sembako =======
1. Update Stok Sembako
2. Cek data terupdate
3. Kembali ke main menu
Silahkan pilih menu diatas : ''')        
        if Updatedatacust == '1':
            tampilkan_data_sembako()
            kode_cari = input("Masukkan Kode Sembako yang ingin diubah: ")
            produk_ditemukan = SearchList(kode_cari)
            if produk_ditemukan:
                ShowList(produk_ditemukan)
                konfirmasi = input("Apakah data ingin di ubah (Y/T)?: ").capitalize()
                if konfirmasi == 'Y':
                    while True:
                        try:
                            kolom = int(input('''Kategori Database Stok Sembako
    1. Kode Sembako
    2. Tanggal Masuk
    3. Nama Sembako
    4. Jenis Sembako
    5. Stok Sembako
    6. Harga
    7. Durasi Kadaluarsa
    Masukkan kolom data yang ingin diubah: '''))
                            if 1 <= kolom <= 7:
                                break
                            print("Pilihan tidak valid, masukkan angka 1-7.")
                        except ValueError:
                            print("Harus memasukkan angka.")
                    kolom_nama = ['kode', 'tanggal_masuk', 'nama', 'jenis', 'stok', 'harga', 'kadaluarsa'][kolom - 1]
                    masukan_data = input(f"Masukkan {kolom_nama} baru: ")
                    # Validasi input per kolom
                    if kolom == 1:
                        if len(masukan_data) >= 4 and masukan_data.isalnum():
                            if any(s.kode == masukan_data for s in datasembako):
                                print('Kode sudah ada di database.')
                                continue
                        else:
                            print('Kode tidak valid. Minimal 4 karakter, kombinasi huruf dan angka.')
                            continue
                    elif kolom == 2:
                        try:
                            masukan_data = datetime.strptime(masukan_data, "%d-%m-%Y").date()
                        except ValueError:
                            print('Format tanggal tidak valid. Gunakan DD-MM-YYYY.')
                            continue
                    elif kolom in [5, 6]:
                        try:
                            masukan_data = int(masukan_data)
                            if masukan_data < 0:
                                raise ValueError()
                        except ValueError:
                            print('Input harus berupa bilangan positif.')
                            continue
                    elif kolom == 7:
                        try:
                            durasi = int(masukan_data)
                            if durasi <= 0:
                                raise ValueError()
                            masukan_data = f"{durasi} Tahun"
                        except ValueError:
                            pass 
                    setattr(produk_ditemukan[0], kolom_nama, masukan_data)
                    print("\nData sudah diperbarui!, Silahkan cek data terupdate pada menu 2")
                elif konfirmasi == 'T':
                    print("\nData tidak jadi diubah")
            else:
                print("\nData tidak ditemukan")
        elif Updatedatacust == '2':
            tampilkan_data_sembako()
        elif Updatedatacust == '3':
            break
        else:
            print('\nMasukkan yang anda input salah, silahkan input nomor dari range 1 - 3')

# Fungsi Delete Data
def DeletedData():
    while True:
        inputDel = int(input('''
Menu Menghapus Daftar Sembako:
1. Menghapus Daftar Sembako dari stok data
2. Kembali ke menu utama
Masukkan angka menu yang ingin dijalankan: '''))
        if inputDel == 1:
            tampilkan_data_sembako()
            DelKodeID = input("\nMasukkan Kode Sembako yang ingin dihapus: ")
            produk_ditemukan = SearchList(DelKodeID)           
            if not produk_ditemukan:
                print("\nData yang ingin anda hapus tidak ada!")
            else:
                ShowList(produk_ditemukan)
                hapus = input("Hapus Data (Ya/Tidak)? ").lower()
                if hapus == "ya":
                    datasembako.remove(produk_ditemukan[0])
                    print("\n Data berhasil terhapus!")
                    tampilkan_data_sembako()
                else:
                    print("\n Data tidak berhasil terhapus!")
        elif inputDel == 2:
            break
        else:
            print("\nPilihan salah, masukkan angka 1 atau 2.")
# Menu Data Sembako (Report)
def MenuDataSembako():
    while True:
        print('''
==== Menu Menampilkan Stok Sembako ====
1. Menampilkan semua Stok Sembako
2. Menampilkan data tertentu
3. Kembali ke menu utama
''')
        SubMenu = input('Silahkan pilih daftar diatas [1-3]: ')

        if SubMenu == '1' and datasembako:
            ShowList(datasembako)
        elif SubMenu == '2' and datasembako:
            CodeStok = input('\nMasukkan Kode Sembako yang ingin anda cari: ')
            hasil_pencarian = SearchList(CodeStok)
            if hasil_pencarian:
                ShowList(hasil_pencarian)
            else:
                print('\n Data Tidak Ditemukan')
        elif SubMenu == '3':
            break
        else:
            print('\nSilahkan masukkan pilihan yang sesuai [1-3]')

# Menu Utama
def MenuAwal():
    while True:
        print('''
----- Selamat Datang Di Toko Sembako Berkah -----

----- Daftar Pilihan : -----

1. Report Stok Sembako
2. Menambahkan Data Stok Sembako
3. Mengupdate Data Stok Sembako
4. Menghapus Data
5. Exit
''')
        PilihanMenu = input('\nMasukkan nomor yang dipilih[1-5]: ')
        if PilihanMenu == '1':
            MenuDataSembako()
        elif PilihanMenu == '2':
            MenambahData()
        elif PilihanMenu == '3':
            UpdateData()  
        elif PilihanMenu == '4':
            DeletedData()
        elif PilihanMenu == '5':
            print('\n=== Terima kasih dan Sampai Jumpa lagi :) === \n')
            exit()
        else:
            print('Anda memasukkan pilihan yang salah \nsilahkan pilih menu yang benar antara [1-5] ')

if __name__ == "__main__":
    MenuAwal()