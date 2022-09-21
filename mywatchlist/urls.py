from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('json/', show_json_watchlist, name='show_json_watchlist'),
    path('xml/', show_xml_watchlist, name='show_xml_watchlist'),
    path('html/', show_html_watchlist, name='show_html_watchlist'),
]