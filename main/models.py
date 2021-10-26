from django.db import models

# Create your models here.
class pinjam(models.Model):
    nmr_anggota = models.IntegerField()                              
    buku = models.TextField(max_length=200)
    jml_buku = models.IntegerField()
    tgl_pinjam = models.DateField(auto_now_add=True)
    tgl_kembali = models.DateField()
    
class anggota(models.Model):
    nmr_anggota = models.IntegerField()                              
    nama_anggota = models.TextField(max_length=200)
    jenis_kelamin = models.TextField(max_length=200)
    alamat = models.TextField(max_length=200)
    no_tlp = models.IntegerField()
    tgl_lahir = models. DateField(auto_now_add=True)


    def tgl_pinjam_format(self):
        return self.tgl_pinjam.strftime('%Y-%m-%d')

    def tgl_kembali_format(self):
        return self.tgl_kembali.strftime('%Y-%m-%d')