# Generated by Django 3.2.8 on 2021-10-25 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211025_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinjam',
            name='tgl_kembali',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pinjam',
            name='tgl_pinjam',
            field=models.DateField(auto_now_add=True),
        ),
    ]