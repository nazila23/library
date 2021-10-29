# Generated by Django 3.2.8 on 2021-10-28 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmr_anggota', models.IntegerField(default='')),
                ('nik', models.IntegerField()),
                ('nama_anggota', models.TextField(max_length=200)),
                ('alamat', models.TextField(max_length=200)),
                ('no_tlp', models.IntegerField()),
                ('tgl_lahir', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_buku', models.IntegerField()),
                ('judul', models.TextField(max_length=200)),
                ('pengarang', models.TextField(max_length=200)),
                ('tahun_terbit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pinjam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmr_pinjam', models.IntegerField(blank=True)),
                ('buku', models.TextField(max_length=200)),
                ('jml_buku', models.IntegerField()),
                ('tgl_pinjam', models.DateField(auto_now_add=True)),
                ('tgl_kembali', models.DateField()),
                ('nmr_anggota', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='uhuy', to='main.anggota')),
            ],
        ),
    ]
