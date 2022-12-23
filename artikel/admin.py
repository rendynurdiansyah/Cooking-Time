from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategori','date')

admin.site.register(Artikel, ArtikelAdmin)


class ResepAdmin(admin.ModelAdmin):
    list_display = ('porsi','title','kunci','tingkat','waktu','gambar')

admin.site.register(Resep, ResepAdmin)
