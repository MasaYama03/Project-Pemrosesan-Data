
# Pemrosesan Data untuk Riset Harga dan Produk Fashion

Proyek ini adalah implementasi pemrosesan data untuk analisis harga dan produk dari industri fashion, menggunakan Python sebagai alat utama untuk melakukan **web scraping**, **transformasi data**, serta **integrasi dengan database** dan **Google Sheets**. Proyek ini bertujuan untuk mendalami teknik pemrograman dan pengolahan data untuk aplikasi yang berhubungan dengan riset pasar dan analisis kompetitor.

## Deskripsi

Dalam proyek ini, kita akan mengumpulkan dan menganalisis data produk dari website **Fashion Studio** yang terkenal dengan berbagai produk fashion. Data yang diambil termasuk harga, ukuran, rating, warna, dan jenis kelamin produk. Selanjutnya, data tersebut akan diproses dan dianalisis untuk membantu perusahaan memahami tren harga dan produk kompetitor. Dengan menggunakan **web scraping**, kita dapat secara otomatis mengambil data dari halaman produk dan melakukan transformasi serta analisis lanjutan.

## Studi Kasus

Sebagai seorang data engineer di perusahaan retail fashion, Anda ditugaskan untuk melakukan riset terhadap harga dan produk dari pesaing perusahaan yang ada di pasar. **Fashion Studio** adalah kompetitor yang dipilih, yang dikenal dengan variasi produk fashion seperti kaos, celana, jaket, dan outerwear. Melalui proyek ini, Anda akan mengumpulkan informasi mengenai harga produk dan karakteristik lainnya untuk membantu tim dalam menghadapi persaingan yang semakin ketat.

Website **Fashion Studio**: [Fashion Studio](https://fashion-studio.dicoding.dev/)

## Fitur

Fitur utama dari proyek ini meliputi:

- **Web Scraping**: Mengambil data produk dari halaman **Fashion Studio** yang berisi informasi tentang harga, rating, warna, ukuran, dan gender.
- **Data Transformation**: Mengonversi data mentah yang diambil dari website menjadi bentuk yang lebih terstruktur dan siap untuk dianalisis lebih lanjut.
- **Pengolahan dan Penyimpanan Data**: Menyimpan hasil pengolahan data ke dalam **PostgreSQL database** dan **Google Sheets** untuk kemudahan akses dan analisis lebih lanjut.
- **Unit Testing**: Menerapkan pengujian untuk memastikan semua fungsi berjalan dengan baik dan menghasilkan hasil yang benar.

## Instalasi

Untuk memulai dengan proyek ini, Anda perlu memastikan bahwa Python terinstal di sistem Anda. Anda juga perlu menginstal beberapa dependensi yang diperlukan.

### 1. Mengkloning Repository

Unduh proyek ini menggunakan Git dengan menjalankan perintah berikut di terminal:

```bash
git clone https://github.com/MasaYama03/Project-Pemrosesan-Data.git
cd Project-Pemrosesan-Data
```

### 2. Instalasi Dependensi

Jika proyek ini memiliki dependensi eksternal, instal pustaka-pustaka yang diperlukan menggunakan pip:

```bash
pip install -r requirements.txt
```

Pastikan Anda berada dalam direktori **`Project-Pemrosesan-Data`** saat menjalankan perintah ini.

### 3. Menjalankan Skrip Utama

Untuk menjalankan skrip utama yang mengelola alur ETL (Extract, Transform, Load), gunakan perintah berikut:

```bash
python main.py
```

### 4. Menjalankan Unit Test

Proyek ini mencakup pengujian unit untuk memastikan bahwa fungsi-fungsi bekerja dengan benar. Untuk menjalankan unit test yang ada dalam folder **`tests`**, gunakan perintah berikut:

```bash
python -m unittest discover tests
```

### 5. Menjalankan Test Coverage

Untuk memeriksa seberapa banyak kode yang teruji oleh pengujian, Anda dapat menjalankan pengujian dengan coverage menggunakan perintah berikut:

```bash
coverage run -m unittest discover tests
```

### 6. Melihat Laporan Coverage

Setelah menjalankan pengujian dengan coverage, Anda dapat melihat laporan hasilnya dengan perintah:

```bash
coverage report -m
```

Laporan ini akan menampilkan informasi tentang seberapa banyak baris kode yang telah diuji selama pengujian, membantu Anda memahami seberapa baik pengujian Anda.

## Deskripsi Kode

- **`main.py`**: Skrip utama untuk menjalankan alur **ETL**, yang mencakup ekstraksi data produk, transformasi data, dan pemuatan data ke **PostgreSQL** serta **Google Sheets**.
- **`utils/extract.py`**: Fungsi untuk mengekstrak data produk dari website **Fashion Studio** menggunakan teknik **web scraping**.
- **`utils/transform.py`**: Fungsi untuk mentransformasi data yang sudah diekstraksi menjadi format yang lebih terstruktur dan siap digunakan.
- **`utils/load.py`**: Fungsi untuk memuat data ke dalam **PostgreSQL database** dan **Google Sheets** untuk penyimpanan dan analisis lebih lanjut.

## Teknologi yang Digunakan

- **Python**: Digunakan sebagai bahasa pemrograman utama untuk pengolahan data dan otomasi tugas.
- **BeautifulSoup**: Digunakan untuk melakukan **web scraping** pada halaman **Fashion Studio** dan mengekstrak data produk.
- **pandas**: Digunakan untuk mengolah dan mentransformasi data yang diekstraksi.
- **PostgreSQL**: Digunakan untuk menyimpan data yang telah diproses dalam format yang terstruktur.
- **Google Sheets API**: Digunakan untuk memuat dan menyimpan data ke dalam **Google Sheets** secara otomatis.

## Catatan

Pastikan Anda telah memiliki **kredensial Google Sheets API** yang valid untuk menyimpan data ke **Google Sheets**. Jika Anda belum mengonfigurasi kredensial, ikuti petunjuk di [Dokumentasi Google Credentials API](https://developers.google.com/workspace/guides/create-credentials).

kemudian setelah mendapatkan credentials dalam bentuk json, anda bisa ke menu Enabled APIs & service untuk mengatur Google Sheets API menjadi enable