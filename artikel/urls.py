from django.urls import path ,include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('artikel',artikel, name='tabel_artikel'),
    path('resep',resep, name='tabel_resep'),
    path('users/',users, name='tabel_users'),
    path('artikel/tambah',tambah_artikel, name='tambah_artikel'),
    path('artikel/lihat/<str:id>',lihat_artikel, name='lihat_artikel'),
    path('artikel/edit/<str:id>',edit_artikel, name='edit_artikel'),
    path('artikel/delete/<str:id>',delete_artikel, name='delete_artikel'),
    path('sinkron',sinkron_resep, name='sinkron_resep'),
    path('resep/lihat/<str:id>',lihat_resep, name='lihat_resep'),
    path('resep/edit/<str:id>',edit_resep, name='edit_resep'),
    path('resep/delete/<str:id>',delete_resep, name='delete_resep'),
    path('user/delete/<str:id>',delete_user, name='delete_user'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, decument_root=settings.MEDIA_ROOT)

