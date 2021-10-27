from django.core.checks import messages
from django.http import request
from django.http.response import Http404
from django.shortcuts import redirect, render
from.import models


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
    return render(request, 'form_pinjam.html', {
            'isi':data2,
             })


def deleteindex(request,id):
    models.pinjam.objects.filter(pk=id).delete()
    return redirect ('form_pinjam')
    
def detailindex(request,id):
    detail = models.pinjam.objects.filter(pk=id).first()
    return render (request,'detail.html', {
        'data': detail,
    })
def updateindex(request,id):
    if request.POST:
        models.pinjam.objects.filter(id=id).update(
            nmr_anggota = request.POST ['nmr_anggota'],
            nama_anggota = request.POST ['na'],
            buku = request.POST ['nb'],
            jml_buku = request.POST ['jb'],
            tgl_pinjam= request.POST ['tp'],
            tgl_kembali = request.POST ['tk'],
            )
    data = models.pinjam.objects.filter(pk=id).first()
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

def dftr(request):
    if request.POST:
        models.anggota.objects.create(
            nama_anggota = request.POST ['na'],
            tgl_lahir = request.POST ['tl'],
            alamat = request.POST ['almt'],
            no_tlp = request.POST ['no_tlp'],
            ) 
        return redirect('/')
    data = models.anggota.objects.all()
    return render(request, 'dftr.html', {
            'isi':data,
            })
