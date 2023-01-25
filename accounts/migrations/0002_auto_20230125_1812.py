# Generated by Django 2.2.28 on 2023-01-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='department',
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=30, verbose_name='住所'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tel_number',
            field=models.CharField(blank=True, max_length=30, verbose_name='電話番号'),
        ),
    ]
