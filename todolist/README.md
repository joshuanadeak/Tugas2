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


## Penjelasan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
---


## Implementasi yang saya lakukan
---
### Diawali dengan membuat proyek baru
Pertama-tama, kita perlu membuat suatu proyek baru pada program yang telah dibuat pada tugas sebelumnya ini, ini dilakukan dengan menjalankan kode berikut:
``` python manage.py startapp mywatchlist ```
### Lalu, dibuat model data pada models.py
```
from django.db import models

class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()
```
### Setelah itu, tambahkan data yang terdapat pada _fixtures_
Contohnya dari hal ini seperti berikut:
```
{
        "model": "mywatchlist.mywatchlist",
        "pk": 1,
        "fields": {
            "watched": true,
            "title": "Mr. Bean's Holiday",
            "rating": 5,
            "release_date": "2007-03-24",
            "review": "Mr Bean's Holiday is an excellent family movie! It has the usual slapstick moments which are funny and sometimes inappropriate behaviour."
        }
}
```
### Menambahkan beberapa hal pada views.py
Ini dilakukan dengan menambah _show_json, show_html, dan show_xml_ seperti berikut:
```
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


def show_json_watchlist(request):
    data_json = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_json), content_type="application/json")

def show_xml_watchlist(request):
    data_xml = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_xml), content_type="application/xml")

def show_html_watchlist(request):
    data_html = MyWatchList.objects.all()
    count_watched = MyWatchList.objects.filter(watched = True).count()
    count_not_watched = MyWatchList.objects.filter(watched = False).count()
    if count_watched >= count_not_watched:
        watch_bigger = True
    elif count_not_watched > count_watched:
        watch_bigger = False
    context = {
        'list_watchlist': data_html,
        'nama': 'Joshua Mihai Daniel Nadeak',
        'NPM': '2106635285',
        'watch_bigger': watch_bigger,
    }
    return render(request, "mywatchlist.html", context)
```
### Melakukan migrasi data dan me-load data yang akan dipakai
Ini dilakukan dengan beberapa kode berikut ini:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_watchlist.json
```
### Melakukan deployment ke Heroku
Menambahkan kode pada file `Procfile` berisi _command_ yang harus dijalankan untuk melakukan build dan yang berkaitan dengan dpl.yml yang akan melakukan deployment pada heroku. Nantinya kita hanya perlu membuat app pada heroku, menambah secrets pada github, dan melakukan _deploy_-nya secara otomatis.
