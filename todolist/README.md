# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
---
Tautan URLnya dapat diklik di link [berikut](https://tugas2pbpjoshuanadeak.herokuapp.com/todolist/).

## Apakah kegunaan {% csrf_token %} pada elemen <form>
---
![](../mywatchlist/image.png?raw=true)
---
Pertama-tama, kita tentunya telah mengerjakan berbagai bentuk latihan maupun tugas yang berkaitan dengan ketiga hal ini. Ini dilakukan melalui pengerjaan dari Lab 2 dan juga pada Tugas 3 ini. Pengenalan berkaitan dengan _JSON, XML, HTML_ merupakan suatu hal yang sangat krusial untuk dipahami, sehingga kemampuan kita yang bersifat praktikal langsung pada pengerjaan tidak ketinggalan dari segi teoretisnya.

### Apa yang terjadi apabila tidak ada potongan kode tersebut tidak ada pada elemen <form>?

## Perbedaan antara _JSON, XML,_ dan _HTML_
---
### _HTML_
Dalam pengerjaan berbagai pemrograman _web_, pemahaman akan _HTML_ merupakan suatu hal yang sangat krusial untuk dipahami, karena _base_ dari pemrograman _web_ itu sendiri diawali oleh _HTML_ ini. HTML merupakan suatu akronim dari _Hypertext Markup Language_, di mana _HTML_ ini dipergunakan dalam penampilan tiap halaman _web_. Di dalam pemrograman _web_ terdapat berbagai bentuk elemen, baik itu statis maupun dinamis. Elemen-elemen statis misal, hyperlink, button, image dan juga elemen dinamis biasa berupa data dari database dapat ditampilkan pada halaman _HTML_. Dalam pembuatan halaman web dengan _HTML_, perlu digunakan _format tags_.
Contoh _HTML_:
```
<tr>
   <th>Item Name</th>
   <th>Item Price</th>
   <th>Item Stock</th>
   <th>Rating</th>
   <th>Description</th>
   <th>Item URL</th>
</tr>
```
### _XML_
Kita telah mengenal _HTML_ pada bagian sebelumnya. Sekarang kita akan membahas lebih lanjut berkaitan dengan _XML_ dan juga _JSON_ pada bagian selanjutnya. _XML_ merupakan akronim dari _eXtensible Markup Language_. _XML_ ini memiliki fungsi di dalam pelaksanaan _data-delivery_, begitu juga dengan _JSON_. Namun, hal yang membedakan antara _XML_ dengan _JSON_ adalah formatnya yang cukup serupa dengan _HTML_. _XML_ menggunakan _tags_ yang memiliki format yang mirip dengan _HTML_, misal <produk>SumpitTerbang</produk>. Karena adanya format ini, nantinya data yang ditampung pun akan memiliki ukuran yang relatif lebih besar dibandingkan pada _JSON_.
Contoh _XML_:
```
<django-objects version="1.0">
    <object model="mywatchlist.mywatchlist" pk="1">
        <field name="watched" type="BooleanField">True</field>
        <field name="title" type="CharField">Mr. Bean's Holiday</field>
        <field name="rating" type="IntegerField">5</field>
        <field name="release_date" type="DateField">2007-03-24</field>
        <field name="review" type="TextField">Mr Bean's Holiday is an excellent family movie! It has the usual slapstick moments which are funny and sometimes inappropriate behaviour.</field>
    </object>
```
### _JSON_
_JSON_ merupakan salah satu bentuk umum dalam pertukaran data atau _data-delivery_. _JSON_ itu sendiri merupakan akronim dari _JavaScript Object Notation_, di mana _JSON_ melakukan penampungan data dari _app_ yang bersangkutan dalam bentuk _key-value pair_. Secara format, data-data yang berbeda dipisah dengan karakter koma (,). Bila ditaksir berdasarkan besar _file_-nya, ukuran data pada _JSON_ lebih kecil dibandingkan ukuran data yang ditampung dalam _XML_.
Contoh _JSON_:
```
[
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
]
```
Jadi, secara singkat perbedaannya adalah sebagai berikut:
- Suatu _HTML_ dipergunakan dalam penampilan dokumen web pada suatu browser, sedangkan XML dan JSON digunakan untuk _data-delivery_.
- Suatu file _HTML_ dan juga file _XML_ akan memiliki ukuran yang lebih besar daripada _JSON_ secara umum.
- _XML_ dan _HTML_ bisa diakses menggunakan DOM, sementara _JSON_ diakses dengan key-value pair.

## Mengapa diperlukan _data-delivery_ dalam pengimplementasian sebuah _platform_?
Pada proses pembuatan suatu aplikasi yang pada kasus ini menggunakan suatu platform, sistem _data-delivery_ merupakan suatu hal yang sangat krusial untuk dapat dilakukan, karena melalui proses inilah dilaksanakan pertukaran data dengan server yang berkaitan. Jika seandainya tidak terdapat mekanisme ini maka nantinya data yang berasal dari _database_ tidak bisa ditampilkan secara nyata (_front-end_). Kerap dalam pembuatan suatu aplikasi terdapat data yang dinamis, yang berarti bahwa data ini dapat berubah dengan waktu karena terdapat _user_ yang mengganti data tersebut, baik itu melalui servernya maupung langsung secara interaktif di _app_ tersebut. Dengan konsep _data-delivery_ ini nantinya data terbaru itu dapat ditampilkan secara nyata di _app_ tersebut.

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

## _Checking Routes Using Postman_
### _HTML_
![](../mywatchlist/html.png?raw=true)
---
### _JSON_
![](../mywatchlist/json.png?raw=true)
---
### _XML_
![](../mywatchlist/xml.png?raw=true)
---
