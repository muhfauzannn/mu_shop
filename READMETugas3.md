
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
- [x] Melakukan add-commit-push ke GitHub.