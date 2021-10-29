from typing import List
from django.core.checks import messages
from django.http import request
from django.http.response import Http404
from django.shortcuts import redirect, render
from.import models
from django.db.models import Q
from django.views.generic import ListView
from .models import Pinjam

# fungsi pinjam buku
def form_pinjam(request):
    if request.POST:
        models.Pinjam.objects.create(
            nmr_anggota = request.POST ['choose'],
            buku = request.POST ['nb'],
            jml_buku = request.POST ['jb'],
            tgl_pinjam = request.POST ['tp'],
            tgl_kembali = request.POST ['tk'],
            ) 
        return redirect('/')
    data2 = models.Pinjam.objects.all()
    data1=models.anggota.objects.all()
    return render(request, 'form_pinjam.html', {
            'isi':data2,
            'data': data1,
             })
def deleteindex(request,id):
    models.Pinjam.objects.filter(pk=id).delete()
    return redirect ('form_pinjam')
    
def detailindex(request,id):
    detail = models.Pinjam.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def updateindex(request,id):
    if request.POST:
        models.Pinjam.objects.filter(id=id).update(
            nmr_anggota = request.POST ['nmr_anggota'],
            buku = request.POST ['buku'],
            jml_buku = request.POST ['jml_buku'],
            tgl_pinjam= request.POST ['tgl_pinjam'],
            tgl_kembali = request.POST ['tgl_kembali'],
            )
    data = models.Pinjam.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit.html',{
        "data": data,
    })


def sejarah(request):
        return render(request, 'sejarah.html')
def visi(request):
        return render(request, 'visi.html')

def buku_dipinjam(request,id):
    detail = models.pinjam.objects.filter(id=id).first()
    return render (request,'buku_dipinjam.html', {
        'data': detail,
    })

def index(request):
    return render(request,'index.html')

#fungsi kembali
def kembali(request,id):
    if request.POST:
        models.Pinjam.objects.filter(id=id).update(
            nmr_anggota = request.POST ['chosee'],
            buku = request.POST ['nb'],
            jml_buku = request.POST ['jb'],
            tgl_kembali = request.POST ['tk'],
            )
    data = models.Pinjam.objects.filter(id=id).first()
    print(data)
    return render (request,'kembali.html',{
        "data": data,
    })
def get_queryset(): # new
        # query = self.request.GET.get('q')
    object_list = Pinjam.objects.filter(id=id).first() 
    return object_list ('kembali')

# fungsi anggota(dftr)
def dftr(request):
    if request.POST:
        models.anggota.objects.create(
            nik = request.POST ['nik'],
            nama_anggota = request.POST ['na'],
            alamat = request.POST ['almt'],
            no_tlp = request.POST ['no_tlp'],
            tgl_lahir = request.POST ['tl'],
            ) 
        return redirect('/dftr')
    data = models.anggota.objects.all()
    # print(da  ta, "halo")
    return render(request, 'dftr.html', {
            'isi1':data,
            })

def delete_dftr(request,id):
    models.anggota.objects.filter(pk=id).delete()
    return redirect ('dftr')

def edit_dftr(request,id):
    if request.POST:
        models.anggota.objects.filter(id=id).update(
            nik = request.POST ['nik'],
            nama_anggota = request.POST ['nama_anggota'],
            alamat = request.POST ['alamat'],
            no_tlp= request.POST ['no_tlp'],
            tgl_lahir = request.POST ['tgl_lahir'],
        )
    data = models.anggota.objects.filter(pk=id).first()
    print(data)
    return render (request,'edit_dftr.html',{
        "data": data,
    })

def detail_dftr(request,id):
    detail = models.anggota.objects.filter(pk=id).first()
    return render (request,'detail_dftr.html', {
        'data': detail,
    })