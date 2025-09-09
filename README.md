# MU Shop

**Nama:** Muhammad Fauzan  
**Kelas:** E
**NPM:** 2406496302

## 🔗 Link Aplikasi PWS
[MU Shop - PWS Deployment](https://muhammad-fauzan44-mushop.pbp.cs.ui.ac.id/)

---

## 📋 Implementasi Checklist Step-by-Step

### 1. Membuat Proyek Django Baru
```bash
# Membuat virtual environment
python -m venv mu_shop_env

# Mengaktifkan virtual environment
source mu_shop_env/bin/activate 

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
- [PWS Documentation](https://pbp.cs.ui.ac.id/)