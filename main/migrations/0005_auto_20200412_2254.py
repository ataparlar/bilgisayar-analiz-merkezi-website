# Generated by Django 2.2.12 on 2020-04-12 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_sliderimages_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='KayanFotograf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Kayan Fotoğraf İsmi')),
                ('img', models.ImageField(upload_to='', verbose_name='Kayan Fotoğraf')),
                ('query', models.SmallIntegerField(default=0, verbose_name='Kayan Fotoğraf Sırası')),
            ],
        ),
        migrations.CreateModel(
            name='Sayfa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=120, verbose_name='Sayfa adı')),
            ],
        ),
        migrations.DeleteModel(
            name='SliderImages',
        ),
        migrations.AddField(
            model_name='post',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Sayfa', verbose_name='Bu post, hangi sayfada yer alacak?'),
        ),
    ]
