from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect, render
from . import models

def form_pinjam(request):
    if request.POST:
        models.pinjam.objects.create(
            nmr_anggota = request.POST ['na'],
            nama = request.POST ['np'],
            buku = request.POST ['nb'],
            jml_buku = request.POST ['jb'],
            tgl_pinjam = request.POST ['tp'],
            tgl_kembali = request.POST ['tk'],
            ) 
        return redirect('/')
    data2 = models.pinjam.objects.all()
    return render(request, 'form_pinjam.html', {
            'isi':data2
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
            nama = request.POST ['nama'],
            buku = request.POST ['buku'],
            jml_buku = request.POST ['jml_buku'],
            tgl_pinjam = request.POST ['tgl_pinjam' ],
            tgl_kembali = request.POST ['tgl_kembali'],
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
    return render(request, 'index.html')

