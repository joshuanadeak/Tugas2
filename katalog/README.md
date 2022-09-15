# Tugas 2: Pengenalan Aplikasi dan MVT pada Django
---
Tautan URLnya dapat diklik di link [berikut](https://tugas2pbpjoshuanadeak.herokuapp.com/katalog/)
## Bagan _Request-Response Client_
---
![](../katalog/bagan.png?raw=true)
Pertama-tama, _client_ mengirim suatu _request_ ke server, nantinya server akan meneruskan _request_ tersebut ke Django. Setelah sampai di Django, _request_ tersebut akan melakukan _parse_ URL yang diterima dan melakukan _routing_ berdasarkan _path_ URL ke _view function_ di file urls.py, di mana hal tersebut diproses ke views.py. Setelah itu, akan dilakukan proses _query_ ke database melalui model yang telah dibuat di models.py. Nantinya, HTML tersebut akan di-_render_ berdasarkan template yang ada pada template.html. Terakhir, hasil yang telah dirender tersebut akan "diberikan" ke views.py dan nantinya akan dikirim dan tampilkan ke _client_.
## _Virtual Environment_
---
Suatu _Virtual environment_ merupakan sebuah _development environment_/infrastruktur _environment_ yang digunakan oleh framework, seperti pada kasus ini adalah Django, di mana fungsinya adalah menjaga konsistensi dari _dependency_ yang ada di proyek tersebut, hal ini dilakukan dengan memisahkan satu proyek dengan proyek lain. Tujuan dari hal tersebut adalah sehingga tidak terjadi konflik antarproyek yang bisa menimbulkan kerusakan data ataupun _error_, karena suatu project seringkali memiliki _dependency_ yang berbeda dengan proyek lain. Sehingga pada kasus ini, _virtual environment_ bisa mendukung proses pengembangan suatu produk/aplikasi, seperti _web_.
## Implementasi
---
### Bagian Pertama

### Bagian Kedua

### Bagian Ketiga

### Bagian Keempat
