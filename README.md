**Nama:** Muhammad Fauzan  
**Kelas:** E
**NPM:** 2406496302

# README TUGAS 2

## 🔗 Link Aplikasi PWS
[MU Shop - PWS Deployment](https://muhammad-fauzan44-mushop.pbp.cs.ui.ac.id/)

---

## 📋 Implementasi Checklist Step-by-Step

### 1. Membuat Proyek Django Baru
```bash
# Membuat virtual environment
python -m venv env

# Mengaktifkan virtual environment
source env/bin/activate 

# Install Django
pip install django

# Membuat proyek Django
django-admin startproject mu_shop
cd mu_shop
```

### 2. Membuat Aplikasi Main
```bash
# Membuat aplikasi main
python manage.py startapp main

# Menambahkan 'main' ke INSTALLED_APPS di settings.py
```

### 3. Routing Proyek ke Aplikasi Main
- Menambahkan path ke `main/urls.py` di file `mu_shop/urls.py`
- Menggunakan `include()` untuk menghubungkan URL proyek dengan aplikasi

### 4. Membuat Model Product
Membuat model di `main/models.py` dengan atribut:
- `name`: CharField untuk nama item
- `price`: IntegerField untuk harga
- `description`: TextField untuk deskripsi
- `thumbnail`: URLField untuk gambar
- `category`: CharField untuk kategori
- `is_featured`: BooleanField untuk status unggulan

### 5. Membuat View dan Template
- Membuat fungsi view di `main/views.py` yang mengembalikan context
- Membuat template HTML di `main/templates/main/` untuk menampilkan informasi

### 6. Routing Aplikasi Main
Membuat file `main/urls.py` dan memetakan URL ke fungsi view yang telah dibuat

### 7. Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Deployment ke PWS
-Login menggunakan SSO
-Membuat Project
-Memasukan env
-menghubungkan repo dengan remote repository pws
-melakukan push

---

## 🏗️ Bagan Alur Request-Response Django

<img width="1132" height="447" alt="Screenshot 2025-09-10 at 00 41 20" src="https://github.com/user-attachments/assets/e729ee72-3ec3-41a2-9b46-50852f773fc8" />

urls.py: Peta rute. Mencocokkan URL yang diminta lalu mengarahkan ke fungsi/kelas di views.py.

views.py: Menerima request, ambil/ubah data via models.py, lalu render template atau kirim JSON/redirect.

models.py: Pintu ke database lewat ORM. Definisi tabel & relasi. Dipanggil dari views.py untuk query/menyimpan data.

Template HTML: Tampilan. Berkas .html yang diisi data (context) dari view lalu dikirim sebagai response ke browser.

---

## ⚙️ Peran settings.py dalam Proyek Django

`settings.py` adalah file konfigurasi utama yang mengatur:

1. **Database Configuration**: Pengaturan koneksi database
2. **Installed Apps**: Daftar aplikasi yang digunakan dalam proyek
3. **Middleware**: Komponen yang memproses request/response
4. **Template Settings**: Konfigurasi engine template
5. **Static Files**: Pengaturan file statis (CSS, JS, images)
6. **Security Settings**: Konfigurasi keamanan (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
7. **Internationalization**: Pengaturan bahasa dan zona waktu
8. **Email Configuration**: Pengaturan untuk pengiriman email

---

## 🗄️ Cara Kerja Migrasi Database di Django
**Deteksi Perubahan**: Django mendeteksi perubahan pada models.py
**Membuat Migration Files**: `python manage.py makemigrations` membuat file migrasi
**Aplikasi Migrasi**: `python manage.py migrate` menerapkan perubahan ke database

---

## Mengapa Django untuk Pembelajaran Pengembangan Software?
Karena Django itu mudah, cepat, dan praktis buat belajar bikin aplikasi web. Dan yang terpenting menggunakan python, karena di ddp1 menggunakan python makanya lebih cepat beradaptasi

---

## Feedback untuk Asisten Dosen Tutorial 1
Asdos menurut saya sudah sangat membantu, apalagi jika di dalam lab saya pribadi merasa sangat terbantu
---

## 📚 Referensi
- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [PBP Tutorial](https://pbp-fasilkom-ui.github.io/ganjil-2026/)

---
# Readme Tugas 3


- [x] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Membuat 4 fungsi baru di views.py yang ada di direktori main, dimana ada show_xml() yang mereturn semua data produk dalam format XML, show_json() mereturn semua data produk dalam format JSON, show_xml_by_id() yang akan menerima parameter id yang nantinya akan mereturn data berdasarkan id nya dalam format XML, show_json_by_id() yang akan menerima parameter id yang nantinya akan mereturn data berdasarkan id nya dalam format JSON

- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
- Membuka urls.py lalu mengimport fungsi yang tadi dibuat dalam views.py. Lalu kita akan memasukan untuk setiap route nya kedalam path yang sudah kita rencanakan supaya dapat diakses jika terjadi match antara route nya maka akan mengembalikan fungsi yang ada didalam views

- [x] Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
- Mengambil semua data nya lalu menambahkan nya kedalam context, supaya bisa diakses oleh main.html, lalu di main.html datanya akan ditampilkan ke client. Untuk tombol "add" kita hanya perlu menambahkan anchor tag yang nantinya akan diredirect ke page add product yang akan merender halaman create_product.html, begitupula dengan show_product.html

- [x] Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
- Pertama membuat terlebih dahulu forms.py nya, lalu kita membuat create_product.html yang menerima context sesuai dari yang mau kita berikan ke database. Jika form disubmit maka akan melakukan request POST ke server dan datanya akan ditambahkan.

- [x] Membuat halaman yang menampilkan detail dari setiap data objek model.
- Membuat route terlebih dahulu untuk menghandle detail produk, dimana route ini akan menerima product id, setelah client mengakses route tersebut maka server akan mengirimkan show_product.html yang akan menampilkan context product detail

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
    - Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Kita membutuhkan data delivery karena jika kita membuat sebuah platform apalagi yang lumayan kompleks serta data yang sering berubah-ubah kita tidak bisa mengachieve nya hanya dengan membuat statis, data delivery merupakan solusi yang dimana jadi penghubung antara platform dengan database, jika platform membutuhkan data dia bisa merequest ke database dan kita bakal mendapatkan data yang terbaru serta memudahkan untuk melakukan manipulasi data.

    - Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, JSON lebih baik dibandingkan XML untuk kebutuhan platform modern karena formatnya lebih simpel, ringan, mudah dibaca, dan cepat diproses oleh hampir semua bahasa pemrograman, terutama JavaScript di web. Sementara XML cenderung lebih berat karena banyak tag tambahan dan lebih cocok dipakai di sistem lama yang butuh struktur data sangat kompleks. JSON lebih populer karena praktis, langsung kompatibel dengan teknologi web dan mobile, serta sudah menjadi standar de facto dalam pembuatan API masa kini.

    - Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() pada form Django berfungsi untuk mengecek apakah data yang dikirim melalui form sudah sesuai dengan aturan validasi yang ditentukan, seperti field wajib terisi, format data benar (misalnya email valid atau angka pada field harga), dan aturan tambahan lain. Jika is_valid() bernilai True, data aman dipakai atau disimpan ke database, sedangkan jika False, Django akan menampilkan pesan error. Dengan begitu, method ini penting agar data yang masuk tetap bersih, valid, dan tidak merusak sistem maupun database.

    - Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Kita membutuhkan csrf_token saat membuat form di Django karena token ini berfungsi sebagai pelindung dari serangan Cross-Site Request Forgery (CSRF). Token ini adalah kode unik yang ditempel Django di setiap form, lalu dicek lagi saat form dikirim ke server. Kalau kita tidak menambahkan csrf_token, penyerang bisa memanfaatkan sesi login aktif pengguna untuk mengirim request palsu tanpa sepengetahuan mereka, misalnya membuat akun baru, menghapus data, atau melakukan transaksi berbahaya. Dengan kata lain, tanpa csrf_token, website jadi rentan disalahgunakan karena server tidak bisa membedakan antara request asli dari pengguna dengan request jahat buatan penyerang.

    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Sudah dijawab sesuai checklist tugasnya
    
    - Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Tidak ada menurut saya asdos sudah sangat baik dalam melakukan tugasnya.

- [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
      <img width="1209" height="808" alt="Screenshot 2025-09-14 at 14 50 04" src="https://github.com/user-attachments/assets/34f58916-8575-4f2f-b155-9ea3f2917e6b" />
<img width="1208" height="808" alt="Screenshot 2025-09-14 at 14 49 53" src="https://github.com/user-attachments/assets/393ee470-26aa-47ee-be5f-81f7fd448677" />
<img width="1219" height="814" alt="Screenshot 2025-09-14 at 14 49 46" src="https://github.com/user-attachments/assets/f952d4a0-00af-4e3e-a29e-6fd9cc92cd66" />
<img width="1213" height="810" alt="Screenshot 2025-09-14 at 14 49 23" src="https://github.com/user-attachments/assets/32c27950-0860-40b1-8892-9bcdf3828afc" />

- [x] Melakukan add-commit-push ke GitHub.


---
# Readme Tugas 4

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
- Saya buat form registrasi dengan UserCreationForm, lalu view login/logout menggunakan AuthenticationForm dan fungsi login() serta logout() bawaan Django. Setelah itu, saya tambahkan middleware dan decorator @login_required agar akses aplikasi menyesuaikan status login pengguna.

- [x] Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
- Menjalankan website nya, lalu melakukan registrasi 2 akun, dan masing-masing membuat 3 data dummy untuk mengecek fungsionalitas

- [x] Menghubungkan model Product dengan User.
- Saya tambahkan field user = models.ForeignKey(User, on_delete=models.CASCADE) di model Product untuk menghubungkan produk dengan pemiliknya. Lalu saat menyimpan produk di view, saya set forms_entry.user = request.user agar setiap produk otomatis terikat ke user yang sedang login.

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
- Saya ambil data user yang sedang login lewat dan kirim ke template untuk ditampilkan. Untuk cookies last_login, saya manfaatkan field bawaan User Django yang otomatis terupdate saat login, lalu render nilainya di halaman utama.

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

    - [x] Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    - Django AuthenticationForm adalah form bawaan untuk login yang otomatis menyediakan field username dan password serta terhubung dengan sistem autentikasi Django. Kelebihannya yaitu praktis karena tidak perlu membuat form manual, sudah terintegrasi penuh dengan validasi login, dan langsung menangani error jika data salah. Namun, kekurangannya kurang fleksibel untuk kebutuhan khusus (misalnya login dengan email, OTP, atau captcha) dan tampilannya sederhana sehingga biasanya perlu dimodifikasi agar sesuai desain aplikasi.
    - [x] Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    - Autentikasi adalah proses memastikan identitas pengguna (misalnya login dengan username dan password), sedangkan otorisasi adalah proses menentukan hak akses pengguna setelah identitasnya terverifikasi (misalnya hanya admin yang boleh menghapus data). Di Django, autentikasi ditangani oleh sistem django.contrib.auth yang menyediakan model User, login/logout, dan validasi kredensial. Sementara otorisasi ditangani lewat permission, group, dan decorator seperti @login_required atau @permission_required, yang mengatur apakah pengguna boleh mengakses view atau melakukan aksi tertentu.
    - [x] Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    - Session menyimpan data di server, sedangkan browser hanya menyimpan session ID lewat cookie. Kelebihannya: lebih aman karena data sensitif tidak langsung disimpan di browser, kapasitas data bisa lebih besar, dan mudah diatur masa berlakunya. Kekurangannya: membebani server karena harus menyimpan data untuk banyak user, serta butuh mekanisme tambahan jika aplikasi dijalankan di banyak server (distributed). Cookie menyimpan data langsung di browser pengguna. Kelebihannya: sederhana, tidak membebani server, dan bisa dipakai untuk menyimpan preferensi user tanpa perlu login. Kekurangannya: kapasitas kecil, rawan manipulasi atau pencurian jika tidak dienkripsi, dan bisa dihapus pengguna kapan saja.
    - [x] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    - Penggunaan cookies tidak sepenuhnya aman secara default karena bisa dicuri atau dimanipulasi jika tidak diberi proteksi (misalnya lewat serangan XSS atau sniffing jaringan). Django mengatasinya dengan memberi fitur keamanan bawaan seperti menandai cookie penting dengan HttpOnly (tidak bisa diakses JavaScript), Secure (hanya dikirim lewat HTTPS), serta SESSION_COOKIE_SAMESITE untuk mencegah CSRF. Selain itu, Django juga menyimpan data sensitif (seperti session) di server, jadi cookie di browser hanya menyimpan ID acak, bukan data asli.
- [x] Melakukan add-commit-push ke GitHub.