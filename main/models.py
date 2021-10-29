from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
# Create your models here.

class anggota(models.Model):
    nik = models.IntegerField()
    nama_anggota = models.TextField(max_length=200)
    alamat = models.TextField(max_length=200)
    no_tlp = models.IntegerField()
    tgl_lahir = models.DateField(auto_now_add=True)

 
    
class buku(models.Model):                 
    no_buku = models.IntegerField()                              
    judul = models.TextField(max_length=200)
    pengarang = models.TextField(max_length=200)
    tahun_terbit = models.IntegerField()



class Pinjam(models.Model):
    nmr_pinjam = models.IntegerField(blank=True)
    nmr_anggota = models.IntegerField()                              
    buku = models.TextField(max_length=200)
    jml_buku = models.IntegerField()
    tgl_pinjam = models.DateField(auto_now_add=True)
    tgl_kembali = models.DateField()
       
       