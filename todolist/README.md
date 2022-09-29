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
