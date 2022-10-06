# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
---
Tautan URLnya dapat diklik di link [berikut](https://tugas2pbpjoshuanadeak.herokuapp.com/todolist/).
### Akun Dummy yang Telah Dibuat
1. Username: ayamgoreng1       Pass: testodesu2020
2. Username: ayamgoreng2       Pass: testodesu2020

## Apakah kegunaan {% csrf_token %} pada elemen <form>
### Dan, apa yang terjadi apabila tidak ada potongan kode tersebut tidak ada pada elemen <form>?
---
![](../todolist/csrf.png?raw=true)
---
Sebelum masuk ke dalam pemahaman akan kegunaan dari CSRF, tentunya perlu dipahami terlebih dahulu definisi dari CSRF itu sendiri. CSRF atau Cross-Site Request Forgery adalah suatu attack yang dilakukan terhadap seseorang yang sudah terautentikasi ke suatu website, di mana pengguna tersebut akan dibuat sang hacker melakukan hal yang ia tidak maksud (misalnya, mentransfer dana ke sang hacker untuk keuntungan pribadinya). Hal ini dapat terjadi karena _session user_ pada suatu _web_ yang terkait masih aktif, sehingga dibuat seolah-olah user benar-benar melakukan _request_ tersebut. Pada server yang tidak menggunakan proteksi CSRF, apabila user di-_click_ URL tersebut, akan langsung mentransfer ke target. Di sinilah sebenarnya fungsi dari CRS token terlihat, yakni untuk keamanan dari hal tersebut. CSRF token bekerja dengan server mengirim token tersebut ke client, dan client harus mengirim kembali token tersebut sebagai bagian dari request selanjutnya. Apabila token tidak ada atau tidak sesuai dengan apa yang dimiliki server, maka request tersebut akan di-_reject_, sehingga keamanan dari hal tersebut bisa terjamin.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
---
Ya, tentunya kita tetap dapat membuat elemen <form> secara manual, hal ini saya implementasikan setelah saya sedikit diskusi dengan teman saya, Daniel Christian Mandolang perihal permasalahan tidak bisa ganti tanggal karena formatnya {{ form.as_table }}.
Berikut inilah lampiran code yang saya buat secara manual, tanpa menggunakan form.as_table:
```
        <form method="POST">
            {% csrf_token %}
            <table>
                <tr>
                    <td>Title </td>
                    <td>
                        <input type="text" name="title" placeholder="Title" class="form-control rounded-md w-full">
                    </td>
                </tr>
                <tr>
                    <td>Description </td>
                    <td>
                        <textarea type="description" name="description" placeholder="Description" class="form-control rounded-md w-full"> </textarea>
                    </td>
                </tr>
                <tr>
                    <td>Date </td>
                    <td>
                        <input type="date" name="date" placeholder="Date" class="form-control rounded-md w-full">
                    </td>
                </tr>
            </table>
            <button class="submit mt-6 px-4 py-2 bg-gradient-to-r from-green-600 to-orange-600 text-white rounded-md">
                Save
            </button>
        </form>
```

## Penjelasan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
---
1. User melihat langsung suatu laman form yang berisi slot submisi tertentu.
2. User memberikan input data ke dalam form tersebut, tentunya dengan nilai-nilai yang sesuai. Jika ada kesalahan dalam format atau tipe nilai yang dimasukkan, maka sebaiknya user diberitahu agar memperbaikinya.
3. User melakukan submit pada form tersebut. Dan dari sinilah alur datanya akan lebih terlihat.
4. Nantinya client akan mengirim request POST ke server sesuai route yang terhubung pada atribut action dari form tersebut.
5. Request yang diterima akan di-parse dan di-handle oleh fungsi views yang bersesuaian.
6. Data yang diterima dari form tersebut akan dilakukan akses oleh server dengan cara mengkonversi data menjadi sebuah instance form.
7. Nantinya, data itu akan digunakan dalam pembuatan instance baru dari suatu models yang sudah ada, serta disimpan ke database.

## Implementasi yang saya lakukan
---
### Diawali dengan membuat proyek baru
Pertama-tama, kita perlu membuat suatu proyek baru pada program yang telah dibuat pada tugas sebelumnya ini, ini dilakukan dengan menjalankan kode berikut:
``` python manage.py startapp todolist ```
Setelah itu, daftarkan ke project-django/settings.py dan project_django/urls.py.
### Lalu, dibuat model data pada models.py
```
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    is_finished = models.BooleanField(default=False)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
```
Lalu, harus dilakukan pembuatan route dan fungsi-fungsi, masing-masing pada todolist/urls.py dan todolist/views.py
    
### Setelah itu, buatlah semua template data html yang akan digunakan untuk nantinya dipekerjakan laman _web_-nya
Contohnya pada saya adalah todolist.html
```
{% extends 'base.html' %}

{% block content %}
  <div class="title-container">
    <h1 class="title">My Own TodoList: PBP Assignment 4</h1>
  </div>

<p>
    Greetings, {{ user.get_username }}!
</p>

<button><a href="{% url 'todolist:create_todolist' %}">Create New Task</a></button>

<br></br>

  <table class="table">
    <tr class="table-header-row">
      <th class="table-header-cell">Date</th>
      <th class="table-header-cell">Title</th>
      <th class="table-header-cell">Description</th>
      <th class="table-header-cell">Is Finished</th>
      <th class="table-header-cell">Button Is Finished</th>
      <th class="table-header-cell">Button Delete</th>
    </tr>

    {% comment %} Add the data below this line {% endcomment %}
    
    {% for data in list_todolist %}
      <tr class="table-row">
        <th class="table-cell">{{ data.date }}</th>
        <th class="table-cell">{{ data.title }}</th>
        <th class="table-cell">{{ data.description }}</th>
        <th class="table-cell">
          {% if data.is_finished %}
            <p>
              Yes, It's Finished
            </p>
            {% else %}
            <p>
              No, It's Not Finished
            </p>
            {% endif %}
        </th>
        <th class="table-cell">
          <a class="button" href="{% url 'todolist:update_todolist' id=data.pk %}">
              Update Task
            </a>
          </form>
        </th>
        <th class="table-cell">
          <a class="button" href="{% url 'todolist:delete_todolist' id=data.pk %}">
            Delete Task
          </a>
        </th>
      </tr>
    {% endfor %}

{% if messages %}
<ul class="messages">
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
</ul>
{% endif %}

<button><a href="{% url 'todolist:logout' %}">Log Out</a></button>

{% endblock content %}
```
### Kaitkan fungsi pada todolist/views.py dengan model User yang sudah disediakan Django. Dan, atur laman login dan register, kemudian kunci halaman /todolist/ dan /todolist/create_task agar hanya dapat diakses oleh user yang sudah login. Serta, buat route dan fungsi yang sesuai untuk is_finished dan menghapus suatu task, kemudian hubungkan dengan tombol pada template.

### Melakukan migrasi data dan me-load data yang akan dipakai
Ini dilakukan dengan beberapa kode berikut ini:
```
python manage.py makemigrations
python manage.py migrate
```

### Melakukan deployment ke Heroku
Menambahkan kode pada file `Procfile` berisi _command_ yang harus dijalankan untuk melakukan build dan yang berkaitan dengan dpl.yml yang akan melakukan deployment pada heroku. Nantinya kita hanya perlu membuat app pada heroku, menambah secrets pada github, dan melakukan _deploy_-nya secara otomatis.
    
### Buatlah 2 buah dummy yang sesuai dengan masing-masing memiliki 3 buah task, sesuai dengan akun yang sudah dilampirkan di atas

---
---

# Tugas 5: Web Design Using HTML, CSS, and CSS Framework
---
Tautan URLnya dapat diklik di link [berikut](https://tugas2pbpjoshuanadeak.herokuapp.com/todolist/).
### Akun Dummy yang Telah Dibuat
1. Username: ayamgoreng1       Pass: testodesu2020
2. Username: ayamgoreng2       Pass: testodesu2020

## Apa perbedaan dari Inline, Internal, dan _External_ CSS?
### Apa saja kelebihan dan kekurangan dari masing-masing style?
---
![](../todolist/css.png?raw=true)
---
Untuk lebih memahami perbedaan antara Inline, Internal, dan Eksternal CSS perlu ditinjau langsung berdasarkan definisinya. Penjelasannya adalah sebagai berikut:
### Inline
Inline CSS adalah salah satu cara styling pada CSS yang digunakan langsung untuk suatu tag html secara spesifik. Atribut ```<style>``` digunakan untuk memberikan style ke suatu tag html. Contohnya adalah sebagai berikut:
```
<!DOCTYPE html>
<html>
<body style="background-color:black;">
 
<h1 style="color:white;padding:30px;">Hostinger Tutorials</h1>
<p style="color:white;">Something usefull here.</p>
 
</body>
</html>
```
Kelebihannya: Dalam melakukan perbaikan relatif cepat dan permintaan HTTP yang relatif kecil.
Kekurangannya: Hanya dapat mengatur sebuah tag, akan sangat melelahkan untuk diterapkan pada tiap tag di sebuah laman.
### Internal
Internal CSS adalah salah satu cara styling CSS yang ditaruh di dalam bagian ```<head>``` pada sebuah halaman. Dalam kasus ini, Class dan ID dapat digunakan untuk merujuk kode pada CSS, namun hanya akan aktif pada halaman tersebut. Contohnya adalah sebagai berikut:
```
<head>
  <style type="text/css">
    p {color:white; font-size: 10px;}
    .center {display: block; margin: 0 auto;}
    #button-go, #button-back {border: solid 1px black;}
  </style>
</head>
```
Kelebihannya: Berbagai kelas dan ID dapat dipergunakan oleh _stylesheet_ yang ada di dalamnya dan untuk perubahan satu halaman, tidak perlu buat beberapa file jadinya.
Kekurangannya: Tidak efisien untuk mengubah style css yang ingin sama diterapkan pada beberapa halaman dan meningkatkan waktu pada saat akses web.
### Eksternal
Eksternal CSS adalah salah satu cara styling CSS yang ditaruh pada file yang terpisah dengan file HTMLnya. Nantinya file dari CSSnya ini akan dilink di dalam file HTML pada bagian ```<head>``` untuk bisa digunakan stylenya. Contohnya adalah sebagai berikut:
```
Pada HTML:
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>

Pada CSS:
.xleftcol {
   float: left;
   width: 33%;
   background:#809900;
}
.xmiddlecol {
   float: left;
   width: 34%;
   background:#eff2df;
}
```
Kelebihannya: Dalam satu file CSS bisa dipergunakan untuk berbagai halaman HTML, waktu akses ke website lebih cepat dari Internal, dan ukuran file HTML lebih kecil.
Kekurangannya: Halaman tidak akan tampil sempurna bila file CSS belum selesai dipanggil.
## Jelaskan tag HTML5 yang kamu ketahui!
---
```
<a> = Memberikan definisi hyperlink
<b> = Memberikan tampilaan text dalam bentuk bold
<body> = Memberikan definisi Body dokumen
<br> = Menghasilkan sebuah line break
<button> = Membuat sebuah tombol yang bisa dipencet
<div> = Menjelaskan sebuah divisi atau bagian di sebuah dokumen
<form> = Mendefinisikan sebuah form HTML untuk input user
<head> = Mendefiniskan bagian head dari sebuah dokumen yang mengandung informasi mengenai dokumennya seperti judul/title
<h1> - <h6> = Mendefinisikan Heading/judul pada HTML
<input> = Mendefinisikan input control
<label> = Mendefinisikan label untuk <input> control
<li> = Mendefinisikan list item
<meta> = Menyajikan metadata terstruktur mengenai kontek dokumennya
<p> = Mendefinisikan sebuah paragraf
<span> = Mendefinisikan sebuah inline bagian tanpa style di sebuah dokumen
<style> = Memasukkan informasi style (Biasanya CSS) ke dalam Head sebuah dokumen
<table> = Mendefiniskan sebuah tabel data
<td> = Mendefinisikan sebuah cell di dalam tabel
<textarea> = Tempat user dapat memasukkan text (multi line)
<th> = Mendefinisikan header cell dalam sebuah tabel
<title> = Mendefinisikan judul dari sebuah dokumen
<tr> = Mendefinisikan sebuah baris cell di dalam tabel
<ul> = Mendefinisikan list tak berurut
```

## Jelaskan tipe-tipe CSS selector yang kamu ketahui!
---
1. Element Selector, ini menggunakan tag HTML sebagai selector untuk mengubah properti yang ada di dalam tag tersebut.
2. ID Selektor, ini menggunakan ID pada tag HTML sebagai selector-nya (ID harus unik). Pada CSS-nya, menggunakan format #id.
3. Class Selector, ini menggunakan class pada tag HTML sebagai selector-nya. Pada CSS-nya, menggunakan format .class.
4. Selector, secara umum ini mengatur semua elemen yang ada di dokumen. Selector ini juga bisa seluruh elemen di dalam sebuah elemen lainnya.

## Implementasi yang saya lakukan
---
### Melakukan _customization_ pada bagian HTML yang telah dibuat pada Tugas 4, di mana digunakan CSS atau frameworknya seperti Bootstrap
Pada kesempatan kali ini, saya memiliki untuk menggunakan Bootstrap sebagai CSS framework saya dalam pembuatan tugas kali ini. Ini dapat saya lakukan dengan menambahkan link bootstrap pada head yang ada di ```templates/base.html```, seperti berikut (saya juga menambahkan 2 scripts lagi pada bagian bodynya untuk keperluan aplikasi saya):
```
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
  {% block meta %}
  {% endblock meta %}
</head>

<body>
  {% block content %}
  {% endblock content %}
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
    integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js"
    integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz"
    crossorigin="anonymous"></script>
</body>
```

### Mengubah implementasi dari HTML pada file yang ada di ```todolist/templates```
Ini saya lakukan pada masing-masing file, yakni ```create_task.html```, ```login.html```, ```register.html```, ```todolist.html```.
---
#### ```create_task.html```
Pada bagian ```create_task.html```, saya melakukan mengimport font dan melakukan styling. Saya juga mengubah tempate ```{{form.as_table}}``` dengan membuat fungsi-fungsi masing-masing secara manual. Setelah itu saya memasukkan ke dalam suatu container dan menaruhnya pada _center_. Karena di bootstrap terdapat beberapa template bentuk, seperti _button_, yang bisa diubah, saya mengutilisasi hal tersebut.
#### ```register.html```
Pada dasar konsepnya sama dengan ```create_task.html```, saya juga melakukan styling dan mengimport font. Saya mengubah template ```{{form.as_table}}``` dengan membuat fungsi-fungsi masing-masing secara manual. Setelah itu saya memasukkan ke dalam suatu container dan menaruhnya pada _center_. Pada bagian ini, saya mengimplementasi button secara manual. (Hal ini dengan bantuan dari GSGS, yakni melalui video Youtube yang telah saya pelajari, Coding Nepal Video https://www.youtube.com/watch?v=eeHqZeJ9Vqc)
#### ```login.html```
Tidak jauh beda juga dari register, saya juga melakukan styling dan mengimport font. Setelah itu saya memasukkan ke dalam suatu container dan menaruhnya pada _center_. Pada bagian ini, saya mengimplementasi button secara manual. (Hal ini dengan bantuan dari GSGS, yakni melalui video Youtube yang telah saya pelajari, Coding Nepal Video https://www.youtube.com/watch?v=eeHqZeJ9Vqc)
#### ```todolist.html```
Pada bagian todolist, saya juga melakukan implementasi yang sama, tetapi pada bagian ini saya terinspirasi dari pembuatan Rendy Arya Kemal untuk cara pembuatan _card_-nya sehingga saya juga bisa menyelesaikannya dengan cukup baik. Saya mengubah yang dari tadinya berbentuk tabel yang cetak langsung, menjadi yang bentuknya kartu, sehingga jauh lebih bagus secara tampilan, serta lebih interaktif dengan user dan sedap dipandang, ketimbang sebelumnya.

### Mengubah satu fungsi pada todolist/views.py
Saya melakukan ini untuk bisa kembali memasukkan data dari ```list_todolist``` yang saya implementasikan, yang tadinya dapat melayani yang berbentuk tabel cetak langsung, menjadi yang bentuknya kartu.

### Membuat aplikasi web tersebut menjadi responsif
Karena yang saya pakai adalah _framework_ Bootstrap versi 5.2 dalam aplikasi ini, sudah terdapat _media query_ yang berlandaskan _breakpoint-breakpoint_ yang telah disediakan oleh Bootstrap langsung. Juga, sudah terdapat kelas _grid_ dan _container_ yang memanfaatkan _breakpoint-breakpoint_ ini sehingga bentuknya dapat menjadi responsif dengan penyesuaian _breakpoint_-nya.
Maka dari itu nantinya halamannya akan responsif dengan melakukan pembungkusan akan elemen-elemen HTML di dalam _grid_ juga _container_ jika ada. Dan juga, ukuran beberapa elemennya juga akan menyesuaikan dengan ukuran halamannya untuk membantu proses responsif tersebut.

### Melakukan deployment ke Heroku
Menambahkan kode pada file `Procfile` berisi _command_ yang harus dijalankan untuk melakukan build dan yang berkaitan dengan dpl.yml yang akan melakukan deployment pada heroku. Nantinya kita hanya perlu membuat app pada heroku, menambah secrets pada github, dan melakukan _deploy_-nya secara otomatis.
    
### Buatlah 2 buah dummy yang sesuai dengan masing-masing memiliki 3 buah task

---
---
