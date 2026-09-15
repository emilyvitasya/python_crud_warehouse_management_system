# Warehouse Stock Management System (Sembako)

A comprehensive Python console application for managing warehouse stock and inventory data using Python dictionaries, featuring complete Create, Read, Update, and Delete (CRUD) operations along with transaction tracking.

## Business Understanding

This project caters to the **Retail and Wholesale Sembako (Groceries)** industry, specifically addressing the need to manage daily inventory stock, pricing, expiration tracking, and incoming/outgoing goods efficiently. Effective inventory tracking plays a crucial role in preventing stockouts and minimizing expired goods.

**Benefits:**
* Improved stock accuracy and real-time inventory visibility
* Streamlined tracking of product expiration and incoming shipments
* Enhanced decision-making through readily available inventory reports and transaction history
* Minimized stock discrepancies and optimized warehouse organization

**Target Users:**
This application is designed for **Warehouse Managers, Inventory Clerks, and Store Staff** to facilitate daily stock auditing, product searches, and transaction recording.

## Features

* **Create:**
    * Add new sembako items with essential details like unique code (SKU), name, category, quantity, price, entry date, and expiration duration.
    * Implement validation rules ensuring unique codes and non-negative values for stock and price.
* **Read:**
    * Display all stock items in a clean, dynamically formatted table view with currency formatting (`Rp`).
    * Flexible search capability to find specific products by code, name, or category.
* **Update:**
    * Modify existing product attributes (name, category, stock, price, entry date, or expiration) while keeping the unique code fixed.
    * Provide instant preview of updated details.
* **Delete:**
    * Safely remove discontinued item records from the active database with confirmation steps.
* **Transaction Management:**
    * Record incoming stock (Barang Masuk) and outgoing stock/sales (Barang Keluar) with automatic stock updates.
    * Track and view a complete history of all warehouse transactions.
* **Security & Validation:**
    * Robust input handling using `try-except` blocks to catch incorrect data types and negative integers.
    * Date validation ensuring incoming entry dates do not exceed the current system date.

## Installation

1. **Prerequisites:**
    * Python 3.8 or higher installed on your system.

2. **Installation & Setup:**
    ```bash
    git clone [https://github.com/emilyvitasya/python_crud_warehouse_management_system.git](https://github.com/emilyvitasya/python_crud_warehouse_management_system.git)
    cd python_crud_warehouse_management_system
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **Menu Navigation:**
    * **1. Report & Pencarian Stok Sembako:** View the full inventory table or search items flexibly.
    * **2. Menambahkan Data Stok Sembako Baru:** Input new product details with automated checks.
    * **3. Mengupdate Data Stok Sembako:** Edit specific attributes of existing items.
    * **4. Menghapus Data Sembako:** Remove items from the database.
    * **5. Manajemen Barang Masuk & Keluar (Transaksi):** Process stock flow and review transaction logs.
    * **6. Exit:** Close the application.

## Data Model
This project utilizes an in-memory **List of Dictionaries** structure to represent the inventory database. Each record contains the following keys:
* `kode`: (String) - Unique stock code identifier (e.g., `'S101'`).
* `nama`: (String) - Product name.
* `jenis`: (String) - Product category/type (e.g., `'Beras'`, `'Minyak'`).
* `stok`: (Integer) - Current available quantity.
* `harga`: (Integer) - Price per unit in IDR.
* `tanggal_masuk`: (Date) - Date when the item entered the warehouse.
* `kadaluarsa`: (String) - Expiration duration estimate (e.g., `'6 Bulan'`, `'1 Tahun'`).

## Contributing
We welcome contributions to this project! Please feel free to open a pull request or submit an issue if you encounter any problems or have suggestions for improvements.