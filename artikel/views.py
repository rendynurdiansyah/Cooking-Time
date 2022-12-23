from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel,Kategori,Resep
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
import requests
from .forms import ArtikelForms

def is_creator(user):
    if user.groups.filter(name='Creator').exists():
        return True
    else:
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Creator').exists():
        request.session['is_creator'] = 'creator'
    list_user = User.objects.all()
    template_name = "pengurus/dashboard.html"
    context = {
        'title' : 'dashboard',
        'list_user' : list_user,
    } 
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "pengurus/tabel_artikel.html"
    artikel = Artikel.objects.all()
    context = {
        'title' : 'dashboard',
        'artikel': artikel,
    }
    return render(request, template_name, context)
@login_required
def resep(request):
    template_name = "pengurus/tabel_resep.html"
    resep = Resep.objects.all()
    context = {
        'resep': resep,
    }
    return render(request, template_name, context)


@login_required
@user_passes_test(is_creator)
def users(request):
    template_name = "pengurus/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' : 'dashboard',
        'list_user' : list_user
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "pengurus/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        forms_artikel =ArtikelForms(request.POST)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect (artikel)
    else:
        forms_artikel = ArtikelForms()
    context = {
        'title':'Tambah Artikel',
        'kategori':kategori,
        'forms_artikel' : forms_artikel

    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "pengurus/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request ,id ):
    template_name = 'pengurus/tambah_artikel.html'
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        forms_artikel = ArtikelForms(request.POST, instance=a)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
            return redirect(artikel)
    else:
        forms_artikel = ArtikelForms(instance=a)
    context = {
        'title':'Edit Artikel',
        'artikel' : a,
        'forms_artikel' : forms_artikel,

    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

def sinkron_resep(request):
        url = "https://masak-apa-tomorisakura.vercel.app/api/recipes"
        data = requests.get(url).json()
        for d in data['results']:
            cek_berita = Resep.objects.filter(porsi=d['serving'])
            if cek_berita:
                print('data sudah ada')
                c = cek_berita.first()
                c.porsi=d['serving']
                c.save()
            else: 
                #jika belum ada maka tulis baru kedatabase
                b = Resep.objects.create(
                    porsi = d['serving'],
                    title = d['title'],
                    kunci = d['key'],
                    tingkat = d['difficulty'],
                    waktu = d['times'],
                    # gambar = d['thumb'],
                )
        return redirect(resep)

def edit_resep(request ,id ):
    template_name = 'pengurus/edit_resep.html'
    resep = Resep.objects.all()
    a = Resep.objects.get(id=id)
    if request.method == "POST":
        
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')

        #input Kategori Dulu
        

        #simpan produk karena ada relasi ke tabel kategori 
        a.nama = nama
        a.judul = judul
        a.body = body
        a.save() 
        return redirect(resep)
    context = {
        'title':'Edit Resep',
        'resep' : resep,

    }
    return render(request, template_name, context)


@login_required
def lihat_resep(request, id):
    template_name = "pengurus/lihat_resep.html"
    resep = Resep.objects.get(id=id)
    context = {
        'title' : 'View Artikel',
        'resep' :resep,
    }
    return render(request, template_name, context)

@login_required
def delete_resep(request,id):
    Resep.objects.get(id=id).delete()
    return redirect(resep)

def delete_user(request,id):
    User.objects.get(id=id).delete()
    return redirect(users)

