# ===================================
# Warehouse Stock Management System (Sembako)
# ===================================
# Developed by. Emily Vitasya Haloho

# /************************************/

# /===== Daftar Menu (Main Menu Display) =====/
def show_menu():
    """Function to display main menu options
    """
    print("\n==========================================")
    print(" WAREHOUSE MANAGEMENT SYSTEM (SEMBAKO)    ")
    print("==========================================")
    print("1. Lihat Daftar Produk")
    print("2. Tambah Produk Baru")
    print("3. Riwayat Barang Masuk (Stock In)")
    print("4. Riwayat Barang Keluar (Stock Out)")
    print("5. Cek Peringatan Stok Minimum")
    print("6. Kelola Data Supplier")
    print("7. Keluar Program")


# /===== Data Model =====/
# Data dummy minimal 5 baris dengan penamaan ID yang diseragamkan (Primary & Foreign Key)

products = [
    {"id_product": 1, "name": "Beras Premium 5kg", "category": "Sembako", "stock": 25, "min_stock": 10},
    {"id_product": 2, "name": "Minyak Goreng 2L", "category": "Sembako", "stock": 8, "min_stock": 15},
    {"id_product": 3, "name": "Gula Pasir 1kg", "category": "Sembako", "stock": 40, "min_stock": 10},
    {"id_product": 4, "name": "Telur Ayam 1kg", "category": "Fresh Food", "stock": 12, "min_stock": 10},
    {"id_product": 5, "name": "Tepung Terigu 1kg", "category": "Sembako", "stock": 5, "min_stock": 10}
]

suppliers = [
    {"id_supplier": 1, "name": "PT Sumber Pangan", "phone": "081234567890", "address": "Jl. Merdeka No. 10"},
    {"id_supplier": 2, "name": "PT IndoMaju Jaya", "phone": "081398765432", "address": "Jl. Sudirman No. 45"},
    {"id_supplier": 3, "name": "Ternak Makmur Sejahtera", "phone": "082112345678", "address": "Jl. Peternakan No. 8"},
    {"id_supplier": 4, "name": "PT Bogasari Utama", "phone": "085678901234", "address": "Jl. Industri Raya No. 12"},
    {"id_supplier": 5, "name": "UD Berkah Tani", "phone": "087811223344", "address": "Jl. Pertanian No. 3"}
]

stock_ins = [
    {"id_stockins": 1, "id_product": 1, "id_supplier": 1, "qty": 30, "date": "2026-06-01"},
    {"id_stockins": 2, "id_product": 2, "id_supplier": 2, "qty": 20, "date": "2026-06-02"},
    {"id_stockins": 3, "id_product": 3, "id_supplier": 1, "qty": 50, "date": "2026-06-03"},
    {"id_stockins": 4, "id_product": 4, "id_supplier": 3, "qty": 15, "date": "2026-06-04"},
    {"id_stockins": 5, "id_product": 5, "id_supplier": 4, "qty": 25, "date": "2026-06-05"}
]

stock_outs = [
    {"id_stockouts": 1, "id_product": 1, "qty": 5, "date": "2026-06-06"},
    {"id_stockouts": 2, "id_product": 2, "qty": 12, "date": "2026-06-06"},
    {"id_stockouts": 3, "id_product": 3, "qty": 10, "date": "2026-06-07"},
    {"id_stockouts": 4, "id_product": 4, "qty": 3, "date": "2026-06-07"},
    {"id_stockouts": 5, "id_product": 5, "qty": 20, "date": "2026-06-08"}
]


# /===== Feature Program =====/
def read():
    """Function for read the data (Products)"""
    print("\n--- DAFTAR PRODUK (PRODUCTS) ---")
    for item in products:
        print(f"ID: {item['id_product']} | Nama: {item['name']} | Kategori: {item['category']} | Stok: {item['stock']} | Min Stok: {item['min_stock']}")
    return

def create():
    """Function for create the data"""
    print("\n--- TAMBAH PRODUK BARU ---")
    return

def read_stock_ins():
    """Function for reading stock ins data"""
    print("\n--- RIWAYAT BARANG MASUK (STOCK INS) ---")
    for item in stock_ins:
        print(f"ID Masuk: {item['id_stockins']} | ID Product: {item['id_product']} | ID Supplier: {item['id_supplier']} | Qty: {item['qty']} | Tanggal: {item['date']}")
    return

def read_stock_outs():
    """Function for reading stock outs data"""
    print("\n--- RIWAYAT BARANG KELUAR (STOCK OUTS) ---")
    for item in stock_outs:
        print(f"ID Keluar: {item['id_stockouts']} | ID Product: {item['id_product']} | Qty: {item['qty']} | Tanggal: {item['date']}")
    return

def low_stock_alert():
    """Function for low stock warning"""
    print("\n--- PERINGATAN STOK MINIMUM ---")
    alert_found = False
    for item in products:
        if item['stock'] < item['min_stock']:
            print(f"PERINGATAN: {item['name']} tersisa {item['stock']} (Di bawah batas minimum {item['min_stock']})")
            alert_found = True
    if not alert_found:
        print("Semua stok produk aman di atas batas minimum.")
    return

def manage_supplier():
    """Function for managing suppliers"""
    print("\n--- DATA SUPPLIER ---")
    for item in suppliers:
        print(f"ID Supplier: {item['id_supplier']} | Nama: {item['name']} | Telp: {item['phone']} | Alamat: {item['address']}")
    return


# /===== Main Program =====/
def main():
    """Function for main program"""
    while True:
        show_menu()
        input_user = input("\nInsert your option (1-7): ")
        
        if input_user == "1":
            read()
        elif input_user == "2":
            create()
        elif input_user == "3":
            read_stock_ins()
        elif input_user == "4":
            read_stock_outs()
        elif input_user == "5":
            low_stock_alert()
        elif input_user == "6":
            manage_supplier()
        elif input_user == "7":
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("\nInput is not valid !")


if __name__ == "__main__":
    main()
    