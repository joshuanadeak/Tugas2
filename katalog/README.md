# Tugas 2: Pengenalan Aplikasi dan MVT pada Django
---
Tautan URLnya dapat diklik di link [berikut](https://tugas2pbpjoshuanadeak.herokuapp.com/katalog/)
Untuk _design_, _all credits to_ Daniel Christian Mandolang. Saya melampirkan penerapan saya pribadi, tapi saya memakai yang ada pada program dia, karena bentuknya lebih bagus sekaligus mempelajari cara kerja CSS.

## Bagan _Request-Response Client_
---
![](../katalog/bagan.png?raw=true)
Pertama-tama, _client_ mengirim suatu _request_ ke server, nantinya server akan meneruskan _request_ tersebut ke Django. Setelah sampai di Django, _request_ tersebut akan melakukan _parse_ URL yang diterima dan melakukan _routing_ berdasarkan _path_ URL ke _view function_ di file urls.py, di mana hal tersebut diproses ke views.py. Setelah itu, akan dilakukan proses _query_ ke database melalui model yang telah dibuat di models.py. Nantinya, HTML tersebut akan di-_render_ berdasarkan template yang ada pada template.html. Terakhir, hasil yang telah dirender tersebut akan "diberikan" ke views.py dan nantinya akan dikirim dan tampilkan ke _client_.

## _Virtual Environment_
---
### Mengapa kita menggunakan virtual environment?
Suatu _Virtual environment_ merupakan sebuah _development environment_/infrastruktur _environment_ yang digunakan oleh framework, seperti pada kasus ini adalah Django, di mana fungsinya adalah menjaga konsistensi dari _dependency_ yang ada di proyek tersebut, hal ini dilakukan dengan memisahkan satu proyek dengan proyek lain. Tujuan dari hal tersebut adalah sehingga tidak terjadi konflik antarproyek yang bisa menimbulkan kerusakan data ataupun _error_, karena suatu project seringkali memiliki _dependency_ yang berbeda dengan proyek lain. Sehingga pada kasus ini, _virtual environment_ bisa mendukung proses pengembangan suatu produk/aplikasi, seperti _web_.
### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Ya, kita dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_. Walaupun begitu, tentunya penerapan seperti itu tidak baik dan rawan terkena permasalahan. Alasannya adalah karena tanpa suatu _virtual environment_, berbagai _dependency_ suatu proyek akan diunduh secara global dan dengan begitu tentunya akan berpotensi menciptakan konflik antarproyek yang kita kerjakan.

## Implementasi
---
### Membuat sebuah fungsi pada views.py
Pertama-tama, dibuat suatu fungsi `show_katalog(request)` pada file `views.py`, sesuai instruksi yang diberikan. Fungsi ini nantinya akan menerima _request_ dari _client_ yang akan diacukan sebagai parameter, lalu akan dibentuk _query_ untuk meminta semua data dari `CatalogItem`. _Return_ dari fungsi ini adalah semua data yang didapat dari `katalog.html` dengan `context` yang sesuai.
### Membuat sebuah routing
Lalu, perlu dibentuk `urlpatterns` baru untuk `katalog` yang terdapat di file `urls.py`. Setelah itu, perlu dicantumkan semua _route_ yang dihubungkan ke fungsi `show_katalog(request)` pada `views.py`. Terakhir, semua _route_ tersebut harus juga ditaruh pada `urlpatterns` milik `urls.py` sehingga fungsinya dapat dijalankan.
### Memetakan data yang didapatkan ke dalam HTML
Sebelum lupa, lakukan terlebih dahulu _migration_ sehingga bisa dipetakan ke template.html, sehingga data yang akan diproses sama dengan databasenya, serta juga lakukan _loaddata_ pada file json-nya. Setelah itu, kita bisa lakukan _looping_ untuk membuat masing-masing data yang tersedia ke suatu bentuk tabel yang rapi. Pada kesempatan ini, saya kebetulan melihat-lihat ada milik teman saya, Daniel Christian Mandolang yang bentuknya bagus, sehingga saya mencoba meniru punyanya sekaligus mempelajari cara kerja CSS, karena saya belum pernah mempelajari CSS sebelumnya. Tetapi, saya juga melampirkan _logic_ penerapan saya juga pada file txt yang saya sediakan di folder, jika barangkali diperlukan.  (_All credits to Daniel for the great table design, if he sees this message, thanks!_)
### Melakukan deployment ke Heroku
Membuat file `Procfile` berisi _command_ yang harus dijalankan untuk melakukan build dan file `dpl.yml` berisi konfigurasi untuk deployment pada heroku. Nantinya kita hanya perlu membuat app pada heroku, menambah secrets pada github, dan melakukan _deploy_-nya secara otomatis.
