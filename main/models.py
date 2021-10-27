from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField, IntegerField
# Create your models here.

class anggota(models.Model):
    nmr_anggota = models.IntegerField()
    nama_anggota = models.TextField(max_length=200)
    alamat = models.TextField(max_length=200)
    no_tlp = models.IntegerField()
    tgl_lahir = models. DateField(auto_now_add=True)

    def __str__(self):
        return self.nmr_anggota
    
class buku(models.Model):
    no_buku = models.IntegerField()                              
    judul = models.TextField(max_length=200)
    pengarang = models.TextField(max_length=200)
    tahun_terbit = models.IntegerField()



class Pinjam(models.Model):
    nmr_pinjam = models.IntegerField()
    nmr_anggota = models.ForeignKey(anggota, on_delete=models.CASCADE, related_name='uhuy')                              
    buku = models.TextField(max_length=200)
    jml_buku = models.IntegerField()
    tgl_pinjam = models.DateField(auto_now_add=True)
    tgl_kembali = models.DateField()
       