# Generated by Django 3.2.8 on 2021-10-29 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_pinjam_nmr_pinjam'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cari', to='main.pinjam')),
            ],
        ),
    ]
