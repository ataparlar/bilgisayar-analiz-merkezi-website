from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name="Post Başlığı:")
    text = models.TextField(verbose_name="Post Metni:")
    img = models.ImageField(blank=True, null=True, verbose_name="Post Fotoğrafı:")
    date = models.DateField(blank=True, null=True)
    page = models.ForeignKey(
        "Sayfa",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Bu post, hangi sayfada yer alacak?",
    )

    def __str__(self):
        return self.title

class KayanFotograf(models.Model):
    title = models.CharField(max_length=120, verbose_name="Kayan Fotoğraf İsmi")
    img = models.ImageField(verbose_name="Kayan Fotoğraf")
    query = models.SmallIntegerField(blank=False, null=False, default=0, verbose_name="Kayan Fotoğraf Sırası")

    def __str__(self):
        return self.title

class Sayfa(models.Model):
    page_name = models.CharField(max_length=120, verbose_name="Sayfa adı")
    atomic = False

    def __str__(self):
        return self.page_name