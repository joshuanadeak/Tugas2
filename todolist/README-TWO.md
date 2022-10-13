# Tugas 6: Javascript dan AJAX
---
Tautan URLnya dapat diklik di link [berikut](https://tugas2pbpjoshuanadeak.herokuapp.com/todolist/).
### Akun Dummy yang Telah Dibuat
1. Username: ayamgoreng1       Pass: testodesu2020
2. Username: ayamgoreng2       Pass: testodesu2020

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!
---
![](../todolist/avsp.png?raw=true)
---
Dalam pemrograman berbasis platform, synchronous dan asynchronous merupakan dua kata yang sudah tidak asing lagi terdengar. 
### Asynchronous Programming
Secara umum, asynchronous secara umum berarti operasi-operasi dapat dikerjakan secara tidak terurut. Asynchronous programming merupakan cara programming dengan multithread yang paling cocok digunakan untuk networking dan komunikasi. Asynchronous secara definisi adalah arsitektur non-blocking yang artinya tidak akan memblokir eksekusi lebih lanjut apabila satu atau lebih operasi sedang berjalan.
Dengan asynchronous programming, beberapa operasi yang saling bersangkutan dapat berjalan di saat yang bersamaan tanpa perlu menunggu satu sama lain selesai. Dalam komunikasi asynchronous, para pihak menerima dan memroses pesan ketika itu memungkinkan, bukannya langsung direspon ketika diterima.
Dengan begitu, penerapan asynchronous programming pada sebuah website sangat tepat, karena user tidak perlu menunggu suatu operasi selesai untuk menjalankan operasi lainnya.

### Synchronous Programming
Sementara itu, synchronous berarti operasi-operasi dikerjakan secara terurut. Artinya, pada synchronous programming komputer harus menunggu suatu operasi selesai untuk mulai menjalankan operasi berikutnya. Synchronous dikenal juga sebagai arsitektur blocking dan ideal untuk sistem programming reactive. Sebagai model single-thread, model ini mengikuti suatu urutan secara runtut yang artinya operasi dilakukan satu per satu, dalam urutan yang sempurna. Ketika sebuah operasi sedang dijalankan, instruksi operasi lainnya ditahan. Penyelesaian _task_ pertama akan menjalankan _task_ berikutnya dan seterusnya.

| Asynchronous | Synchronous |
| ----------- | ----------- |
| Digunakan untuk task yang bersifat independen | Digunakan untuk task yang bersifat dependen|
| Non-blocking (beberapa request ke server)   | Blocking (request satu per satu)        |
| Multi-thread (bisa paralel)      | Single-thread (satu persatu)       |
| Meningkatkan throughput (bisa beberapa operasi di saat yang sama)   | Lebih lambat dan metodis        |

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini!
---
_Event-driven programming_ adalah suatu paradigma di mana alur yang dijalankan suatu program didasarkan atas event atau perilaku yang dilakukan antar user dan client. Sehingga, di terjadi pengiriman "pesan" yaitu event yang ingin diproses, lalu program akan memanggil perintah-perintah berdasarkan event yang didapat.
Pada Tugas kali ini, contoh sederhananya adalah ketika diterapkan ```onReady``` document untuk inisialisasi, ```onClick``` untuk button form baru, serta ```onSuccess``` yang dipanggil setelah pemanggilan AJAX berhasil.

## Jelaskan penerapan asynchronous programming pada AJAX!
---
Pada AJAX, asynchronous programming ini diterapkan pada pengiriman request. Pada saat AJAX request dilakukan, request yang diberikan itu akan berjalan di background sehingga user masih dapat melakukan operasi lain tanpa harus menunggu request tersebut selesai. Kemudian, setelah request tersebut selesai diproses, dikirim, dan berhasil mendapatkan respon, terdapat fungsi yang dihubungkan untuk menangani respon yang didapat.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
---
### Pembuatan fungsi baru pada ```views.py``` untuk memperoleh data semua task dalam bentuk json dan menghubungkannya dengan url ```/todolist/json```.

### Mengubah beberapa hal pada django template untuk menampilkan hasil proses AJAX setelah laman di-load.

### Membuat task baru modal pada ```todolist.html``` dan dihubungkan fungsi tersebut pada tombol untuk memunculkan modal.

### Pembuatan fungsi baru pada ```views.py```  untuk membuat task baru dan menghubungkannya dengan url ```/todolist/add```.

### Membuat fungsi yang akan diproses ketika task form baru dimasukkan menggunakan AJAX secara _asynchronous_.

### Dibuat funsi delete sebagai bonus untuk task, sehingga bisa menghapus secara _asynchronous_.

### Melakukan deployment ke Heroku
Menambahkan kode pada file `Procfile` berisi _command_ yang harus dijalankan untuk melakukan build dan yang berkaitan dengan dpl.yml yang akan melakukan deployment pada heroku. Nantinya kita hanya perlu membuat app pada heroku, menambah secrets pada github, dan melakukan _deploy_-nya secara otomatis.

---
---