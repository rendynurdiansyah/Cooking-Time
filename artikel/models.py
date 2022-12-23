from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
         return self.nama
    
    class meta :
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    judul = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True, null=True,
                                    config_name='special',
                                    external_plugin_resources=[(
                                        'youtube',
                                        '/static/ckeditor_plugins/youtube/youtube/',
                                        'plugin.js',
                                    )],
                                    )
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class meta :
        ordering = ['-id']
        verbose_name_plural = "Artikel"

class Resep(models.Model):
    porsi = models.CharField(max_length=50,blank=True,null=True)
    title = models.CharField(max_length=1000)
    kunci = models.CharField(max_length=100)
    tingkat = models.CharField(max_length=100)
    waktu = models.TextField()
    gambar = models.ImageField()

    def __str__(self):
        return "{} - {}".format(self.title, self.kunci)