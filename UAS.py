
# Daftar buku
books = []

# Fungsi untuk menambahkan buku baru
def add_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama pengarang: ")
    genre = input("Masukkan genre buku: ")
    books.append({"title": title, "author": author, "genre": genre})
    print(f"Buku '{title}' berhasil ditambahkan.\n")

# Fungsi untuk menghapus buku berdasarkan judul
def delete_book():
    title = input("Masukkan judul buku yang ingin dihapus: ")
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print(f"Buku '{title}' berhasil dihapus.\n")
            return
    print(f"Buku dengan judul '{title}' tidak ditemukan.\n")

# Fungsi untuk mencari buku berdasarkan pengarang atau genre
def search_book():
    search_type = input("Cari berdasarkan (1) Pengarang atau (2) Genre? (Masukkan 1 atau 2): ")
    keyword = input("Masukkan kata kunci pencarian: ").lower()
    results = []
    if search_type == "1":
        results = [book for book in books if book["author"].lower() == keyword]
    elif search_type == "2":
        results = [book for book in books if book["genre"].lower() == keyword]
    else:
        print("Pilihan tidak valid.\n")
        return

    if results:
        print("\nBuku ditemukan:")
        for book in results:
            print(f"- Judul: {book['title']}, Pengarang: {book['author']}, Genre: {book['genre']}")
    else:
        print("Tidak ada buku yang cocok dengan kata kunci.\n")
    print()

# Fungsi untuk menampilkan semua judul buku
def show_books():
    if not books:
        print("Belum ada buku yang terdaftar.\n")
    else:
        print("Daftar semua judul buku:")
        for book in books:
            print(f"- {book['title']}")
        print()

# Menu utama
def main_menu():
    while True:
        print("=== Pengelola Daftar Buku ===")
        print("1. Tambah Buku Baru")
        print("2. Hapus Buku Berdasarkan Judul")
        print("3. Cari Buku (Pengarang/Genre)")
        print("4. Tampilkan Semua Judul Buku")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ")
        print()

        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Menjalankan program
if __name__ == "__main__":
    main_menu()
 
