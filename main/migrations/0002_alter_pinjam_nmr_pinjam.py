# Generated by Django 3.2.8 on 2021-10-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinjam',
            name='nmr_pinjam',
            field=models.IntegerField(),
        ),
    ]