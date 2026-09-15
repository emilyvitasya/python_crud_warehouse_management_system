# ===================================
# Warehouse Stock Management System (Sembako) - Versi Dictionary
# ===================================
# Developed by. EMILY

from datetime import datetime, date

# Database sementara menggunakan List of Dictionary
datasembako = [
    {
        'kode': 'S101', 
        'nama': 'Beras Premium 5kg', 
        'jenis': 'Beras', 
        'stok': 25, 
        'harga': 65000, 
        'tanggal_masuk': date(2025, 11, 1), 
        'kadaluarsa': '6 Bulan'
    },
    {
        'kode': 'S102', 
        'nama': 'Minyak Goreng Bimoli 2L', 
        'jenis': 'Minyak', 
        'stok': 40, 
        'harga': 38000, 
        'tanggal_masuk': date(2025, 11, 11), 
        'kadaluarsa': '1 Tahun'
    },
    {
        'kode': 'S103', 
        'nama': 'Gula Pasir Gulaku 1kg', 
        'jenis': 'Gula', 
        'stok': 50, 
        'harga': 16000, 
        'tanggal_masuk': date(2026, 7, 1), 
        'kadaluarsa': '1 Tahun'
    },
    {
        'kode': 'S104', 
        'nama': 'Tepung Terigu Segitiga Biru', 
        'jenis': 'Tepung', 
        'stok': 30, 
        'harga': 14500, 
        'tanggal_masuk': date(2026, 9, 1), 
        'kadaluarsa': '8 Bulan'
    },
    {
        'kode': 'S105', 
        'nama': 'Telur Ayam Ras 1kg', 
        'jenis': 'Telur', 
        'stok': 20, 
        'harga': 28000, 
        'tanggal_masuk': date(2025, 11, 19), 
        'kadaluarsa': '2 Minggu'
    },
    {
        'kode': 'S106', 
        'nama': 'Kecap Manis Bango 550ml', 
        'jenis': 'Bumbu', 
        'stok': 35, 
        'harga': 27500, 
        'tanggal_masuk': date(2026, 2, 2), 
        'kadaluarsa': '1 Tahun'
    },
    {
        'kode': 'S107', 
        'nama': 'Saus Tomat ABC 275ml', 
        'jenis': 'Bumbu', 
        'stok': 25, 
        'harga': 12000, 
        'tanggal_masuk': date(2026, 3, 2), 
        'kadaluarsa': '9 Bulan'
    },
    {
        'kode': 'S108', 
        'nama': 'Mie Instan Indomie Goreng', 
        'jenis': 'Mie', 
        'stok': 120, 
        'harga': 3100, 
        'tanggal_masuk': date(2025, 11, 30), 
        'kadaluarsa': '6 Bulan'
    },
    {
        'kode': 'S109', 
        'nama': 'Susu Kental Manis Indomilk', 
        'jenis': 'Susu', 
        'stok': 45, 
        'harga': 13500, 
        'tanggal_masuk': date(2026, 4, 3), 
        'kadaluarsa': '1 Tahun'
    },
    {
        'kode': 'S110', 
        'nama': 'Teh Celup Sosro Box', 
        'jenis': 'Minuman', 
        'stok': 60, 
        'harga': 9000, 
        'tanggal_masuk': date(2026, 5, 23), 
        'kadaluarsa': '2 Tahun'
    }
]

# Riwayat Transaksi Barang Masuk/Keluar
riwayat_transaksi = []

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
            max(len(str(item[kolom.lower()])) for item in data_sembako)
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
            nilai = item[kolom.lower()]
            if kolom == "Harga":
                nilai = f"Rp{nilai:,}"
            elif kolom == "Tanggal_Masuk":
                if isinstance(nilai, date):
                    nilai = nilai.strftime("%d-%m-%Y")
                else:
                    nilai = datetime.strptime(str(nilai), "%d-%m-%Y").date().strftime("%d-%m-%Y")
            else:
                nilai = str(nilai)
            print(f"{nilai:<{lebar_kolom[kolom]}} ", end="")
        print()

# Fungsi Pencarian Berdasarkan Kode (Eksak)
def SearchList(Input):
    return list(filter(lambda data: data['kode'].lower() == str(Input).lower(), datasembako))

# Fungsi Pencarian Fleksibel (Berdasarkan Kode, Nama, atau Jenis)
def cari_barang_flex(keyword):
    keyword = keyword.lower()
    return [
        item for item in datasembako 
        if keyword in item['kode'].lower() or keyword in item['nama'].lower() or keyword in item['jenis'].lower()
    ]

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
                if any(sembako['kode'].lower() == kode_sembako.lower() for sembako in datasembako):
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
            tanggal_str = input('Tanggal Masuk (format DD-MM-YYYY) [Kosongkan untuk hari ini]: ')
            if tanggal_str == "":
                tanggal_masuk = date.today()
                break
            try:
                tanggal_masuk = datetime.strptime(tanggal_str, "%d-%m-%Y").date()
                if tanggal_masuk > date.today():
                    print('Tanggal masuk tidak boleh melebihi hari ini!')
                    continue
                break
            except ValueError:
                print('Format tanggal tidak valid. Gunakan DD-MM-YYYY.')

        kadaluarsa = input('Durasi Kadaluarsa (contoh: 6 Bulan / 1 Tahun): ')
        konfirmasi = input('Apakah anda yakin data ini akan ditambahkan (Y/T)? ').capitalize()
        
        if konfirmasi == 'Y':
            baru = {
                'kode': kode_sembako,
                'nama': nama,
                'jenis': jenis,
                'stok': stok,
                'harga': harga,
                'tanggal_masuk': tanggal_masuk,
                'kadaluarsa': kadaluarsa
            }
            datasembako.append(baru)
            riwayat_transaksi.append(f"Barang Baru Masuk: {nama} ({stok} unit) pada {date.today().strftime('%d-%m-%Y')}")
            tampilkan_data_sembako()
            print('\nStok Sembako Berhasil ditambahkan')
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

# Fungsi Update Data
def UpdateData():
    while True:
        Updatedatacust = input('''
======= Menu Ubah Data Sembako =======
1. Update Data Sembako
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
    1. Tanggal Masuk
    2. Nama Sembako
    3. Jenis Sembako
    4. Stok Sembako
    5. Harga
    6. Durasi Kadaluarsa
    Masukkan kolom data yang ingin diubah (1-6): '''))
                            if 1 <= kolom <= 6:
                                break
                            print("Pilihan tidak valid, masukkan angka 1-6.")
                        except ValueError:
                            print("Harus memasukkan angka.")
                    
                    kolom_nama = ['tanggal_masuk', 'nama', 'jenis', 'stok', 'harga', 'kadaluarsa'][kolom - 1]
                    masukan_data = input(f"Masukkan {kolom_nama} baru: ")
                    
                    if kolom_nama == 'tanggal_masuk':
                        try:
                            masukan_data = datetime.strptime(masukan_data, "%d-%m-%Y").date()
                            if masukan_data > date.today():
                                print('Tanggal masuk tidak boleh melebihi hari ini.')
                                continue
                        except ValueError:
                            print('Format tanggal tidak valid. Gunakan DD-MM-YYYY.')
                            continue
                    elif kolom_nama in ['stok', 'harga']:
                        try:
                            masukan_data = int(masukan_data)
                            if masukan_data < 0:
                                raise ValueError()
                        except ValueError:
                            print('Input harus berupa bilangan positif.')
                            continue
                            
                    produk_ditemukan[0][kolom_nama] = masukan_data
                    print("\nData sudah diperbarui!")
                    print("-" * 40)
                    print("Detail Data Terupdate:")
                    ShowList(produk_ditemukan)
                    print("-" * 40)
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
        try:
            inputDel = int(input('''
Menu Menghapus Daftar Sembako:
1. Menghapus Daftar Sembako dari stok data
2. Kembali ke menu utama
Masukkan angka menu yang ingin dijalankan: '''))
        except ValueError:
            print("\nMasukkan angka yang valid!")
            continue

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
                    print("\nData berhasil terhapus!")
                    tampilkan_data_sembako()
                else:
                    print("\nData tidak jadi dihapus!")
        elif inputDel == 2:
            break
        else:
            print("\nPilihan salah, masukkan angka 1 atau 2.")

# Menu Barang Masuk & Barang Keluar (Transaksi)
def MenuTransaksi():
    while True:
        pilih = input('''
==== Menu Transaksi Stok Sembako ====
1. Barang Masuk (Tambah Stok Existing)
2. Barang Keluar (Kurangi Stok/Terjual)
3. Lihat Riwayat Transaksi
4. Kembali ke Menu Utama
Silahkan pilih menu [1-4]: ''')
        
        if pilih == '1' or pilih == '2':
            tampilkan_data_sembako()
            kode = input("\nMasukkan Kode Sembako: ")
            hasil = SearchList(kode)
            if not hasil:
                print("Barang tidak ditemukan.")
                continue
            
            item = hasil[0]
            ShowList(hasil)
            try:
                jml = int(input(f"Masukkan jumlah barang {'masuk' if pilih == '1' else 'keluar'}: "))
                if jml <= 0:
                    print("Jumlah harus lebih besar dari 0.")
                    continue
            except ValueError:
                print("Jumlah harus berupa angka.")
                continue
            
            if pilih == '1':
                item['stok'] += jml
                ket = f"BARANG MASUK: +{jml} {item['nama']} (Stok total: {item['stok']})"
            else:
                if jml > item['stok']:
                    print("Stok tidak mencukupi!")
                    continue
                item['stok'] -= jml
                ket = f"BARANG KELUAR: -{jml} {item['nama']} (Sisa stok: {item['stok']})"
            
            riwayat_transaksi.append(f"{ket} pada {date.today().strftime('%d-%m-%Y')}")
            print(f"\nBerhasil! {ket}")
            ShowList([item])
            
        elif pilih == '3':
            print("\n--- Riwayat Barang Masuk & Keluar ---")
            if not riwayat_transaksi:
                print("Belum ada transaksi tercatat.")
            else:
                for idx, r in enumerate(riwayat_transaksi, 1):
                    print(f"{idx}. {r}")
        elif pilih == '4':
            break
        else:
            print("Pilihan tidak valid.")

# Menu Data Sembako (Report & Pencarian Fleksibel)
def MenuDataSembako():
    while True:
        print('''
==== Menu Menampilkan Stok Sembako ====
1. Menampilkan semua Stok Sembako
2. Mencari barang (Berdasarkan Kode, Nama, atau Jenis misal: Tepung)
3. Kembali ke menu utama
''')
        SubMenu = input('Silahkan pilih daftar diatas [1-3]: ')

        if SubMenu == '1' and datasembako:
            ShowList(datasembako)
        elif SubMenu == '2' and datasembako:
            keyword = input('\nMasukkan kata kunci pencarian (Kode/Nama/Jenis): ')
            hasil_pencarian = cari_barang_flex(keyword)
            if hasil_pencarian:
                print(f"\nDitemukan {len(hasil_pencarian)} produk:")
                ShowList(hasil_pencarian)
            else:
                print('\nData Tidak Ditemukan')
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

1. Report & Pencarian Stok Sembako
2. Menambahkan Data Stok Sembako Baru
3. Mengupdate Data Stok Sembako
4. Menghapus Data Sembako
5. Manajemen Barang Masuk & Keluar (Transaksi)
6. Exit
''')
        PilihanMenu = input('\nMasukkan nomor yang dipilih[1-6]: ')
        if PilihanMenu == '1':
            MenuDataSembako()
        elif PilihanMenu == '2':
            MenambahData()
        elif PilihanMenu == '3':
            UpdateData()  
        elif PilihanMenu == '4':
            DeletedData()
        elif PilihanMenu == '5':
            MenuTransaksi()
        elif PilihanMenu == '6':
            print('\n=== Terima kasih dan Sampai Jumpa lagi :) === \n')
            exit()
        else:
            print('Anda memasukkan pilihan yang salah \nsilahkan pilih menu yang benar antara [1-6] ')

if __name__ == "__main__":
    MenuAwal()
    