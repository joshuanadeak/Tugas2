from django.test import TestCase
from django.urls import reverse, resolve
from katalog.models import CatalogItem
from katalog.views import show_katalog

# Credits to Daniel for the idea, because I really don't understand this before
class KatalogTest(TestCase):
    def test_new_catalog(self):
        CatalogItem.objects.create(
            item_name = "Permen Uranium", 
            item_price = 110000000, 
            item_stock = 3, 
            description = "Tubuhmu bisa bernyala-nyala", 
            rating = 5, 
            item_url = "https://r.mtdv.me/permenuranium"
        )
        uraniumpermen = CatalogItem.objects.get(item_url="https://r.mtdv.me/permenuranium")
        self.assertEquals(uraniumpermen.item_url, "https://r.mtdv.me/permenuranium")
