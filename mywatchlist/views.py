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