# Generated by Django 3.2.8 on 2021-10-29 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_pinjam_nmr_pinjam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinjam',
            name='nmr_pinjam',
        ),
    ]
