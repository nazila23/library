from django.db import models

# Create your models here.
class pinjam(models.Model):
    nmr_anggota = models.IntegerField()
    nama = models.TextField(max_length=200)
    buku = models.TextField(max_length=200)
    jml_buku = models.IntegerField()
    tgl_pinjam = models.DateField(auto_now_add=True)
    tgl_kembali = models.DateField()
    
    def tgl_pinjam_format(self):
        return self.tgl_pinjam.strftime('%Y-%m-%d')

    def tgl_kembali_format(self):
        return self.tgl_kembali.strftime('%Y-%m-%d')