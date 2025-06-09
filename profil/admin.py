from django.contrib import admin
from . models import Barang,Jenis
# Register your models here.

class BarangAdmin(admin.ModelAdmin):
    list_display = ('kdbrg', 'nama', 'stok', 'harga', 'link_gbr', 'jenis_id')
    list_filter = ('jenis_id', )
    search_fields = ('nama', 'kdbrg', 'jenis_id__nama')
    list_per_page = 3

admin.site.register(Barang, BarangAdmin)
admin.site.register(Jenis)