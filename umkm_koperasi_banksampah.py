# umkm_koperasi_banksampah.py

# Query 1: Membuat Class untuk Sistem UMKM
class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000  # Rp50 juta

    # Query 2: Method untuk Menambah Anggota UMKM
    def tambah_anggota(self, nama, jumlah_pinjaman):
        self.anggota.append({"nama": nama, "pinjaman": jumlah_pinjaman})

    # Query 3: Method untuk Menghitung Pengembalian Pinjaman
    def hitung_pengembalian(self, nama_anggota, tahun):
        for anggota in self.anggota:
            if anggota["nama"] == nama_anggota:
                bunga = 0.05 * tahun * anggota["pinjaman"]
                return anggota["pinjaman"] + bunga
        return None

# Query 4: Membuat Class untuk Koperasi
class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    # Query 5: Method untuk Mencatat Transaksi Koperasi
    def catat_transaksi(self, nama_anggota, jenis, jumlah):
        self.transaksi.append({"nama": nama_anggota, "jenis": jenis, "jumlah": jumlah})

    # Query 6: Method untuk Menghitung Keuntungan Koperasi
    def hitung_keuntungan(self):
        total_jual = sum(t["jumlah"] for t in self.transaksi if t["jenis"] == "jual")
        total_beli = sum(t["jumlah"] for t in self.transaksi if t["jenis"] == "beli")
        return total_jual - total_beli

# Query 7: Membuat Class untuk Bank Sampah
class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}  # Format: {"nama": {"plastik": 2, "kertas": 3}}

    # Query 8: Method untuk Mencatat Data Sampah
    def catat_sampah(self, nama_anggota, jenis_sampah, jumlah):
        if nama_anggota not in self.data_sampah:
            self.data_sampah[nama_anggota] = {}
        if jenis_sampah not in self.data_sampah[nama_anggota]:
            self.data_sampah[nama_anggota][jenis_sampah] = 0
        self.data_sampah[nama_anggota][jenis_sampah] += jumlah

    # Query 9: Method untuk Menghitung Nilai Tukar Sampah
    def hitung_nilai_tukar(self, nama_anggota):
        harga = {"plastik": 5000, "kertas": 2000}
        total = 0
        if nama_anggota in self.data_sampah:
            for jenis, jumlah in self.data_sampah[nama_anggota].items():
                total += jumlah * harga.get(jenis, 0)
        return total

    # Query 10: Method untuk Pesan Edukasi Lingkungan
    def pesan_edukasi(self, nama_anggota):
        total_kg = sum(self.data_sampah.get(nama_anggota, {}).values())
        if total_kg > 10:
            return "Hebat! Kamu pahlawan lingkungan."
        elif total_kg > 5:
            return "Bagus! Teruskan semangat daur ulangmu."
        elif total_kg > 0:
            return "Ayo, lebih giat lagi kumpulkan sampah."
        else:
            return "Yuk mulai peduli dengan lingkungan dari sekarang!"

# Query 11: Mengintegrasikan Semua Komponen
if __name__ == "__main__":
    nama_umkm = input("Masukkan nama UMKM: ")
    koperasi = Koperasi(nama_umkm)
    banksampah = BankSampah(nama_umkm)

    while True:
        print("\nMenu:\n1. Tambah Anggota\n2. Catat Transaksi\n3. Catat Sampah\n4. Laporan\n5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Nama anggota: ")
            pinjaman = int(input("Jumlah pinjaman: "))
            koperasi.tambah_anggota(nama, pinjaman)
            banksampah.tambah_anggota(nama, pinjaman)

        elif pilihan == "2":
            nama = input("Nama anggota: ")
            jenis = input("Jenis transaksi (beli/jual): ")
            jumlah = int(input("Jumlah (Rp): "))
            koperasi.catat_transaksi(nama, jenis, jumlah)

        elif pilihan == "3":
            nama = input("Nama anggota: ")
            jenis = input("Jenis sampah (plastik/kertas): ")
            jumlah = float(input("Jumlah (kg): "))
            banksampah.catat_sampah(nama, jenis, jumlah)

        elif pilihan == "4":
            print("\n--- Laporan ---")
            for anggota in koperasi.anggota:
                nama = anggota["nama"]
                print(f"Anggota: {nama}")
                print(f"  Pinjaman: Rp{anggota['pinjaman']}")
                print(f"  Pengembalian (1 tahun): Rp{koperasi.hitung_pengembalian(nama, 1)}")
                print(f"  Nilai Tukar Sampah: Rp{banksampah.hitung_nilai_tukar(nama)}")
                print(f"  Pesan Edukasi: {banksampah.pesan_edukasi(nama)}")
            print(f"Total Keuntungan Koperasi: Rp{koperasi.hitung_keuntungan()}")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem UMKM System.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")
