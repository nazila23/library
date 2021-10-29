from django.contrib import admin

# Register your models here.
from.models import Pinjam

class PinjamAdmin(admin.ModelAdmin):
    list_display = ['nmr_anggota']

admin.site.register(Pinjam, PinjamAdmin)