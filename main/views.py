from django.shortcuts import render
from .models import *

# Create your views here.
"""
Environment setup yapılıp localhost üzerinden websitesi'ne ulaşıldıktan sonra
sayfaların açılması için /admin panelinden Sayfas altında sayfa eklenmesi gerekmektedir.
Sayfaların sırası aşağıdaki gibi olmalıdır. Aksi takdirde Postların yerleri karışacaktır.

1 - 2. el satış sayfası
2 - laptop tamiri sayfası
3 - kasa-pc tamiri sayfası
4 - monitör tamiri sayfası 
5 - yazıcı tamiri sayfası 
6 - hizmetler sayfası
7 - misyon-vizyon sayfası
8 - hakkımızda sayfası
9 - basında biz sayfası
10 - çalışma sistemimiz sayfası
11 - anasayfa
 
"""


def main_view(request):
    main_images = KayanFotograf.objects.all()
    main_posts = Post.objects.filter(page=Sayfa.objects.all()[11]).order_by('query')
    main_dict = {
        "images": main_images,
        "posts": main_posts,
    }
    return render(request, 'main.html', main_dict)


def hizmetler_view(request):
    hizmetler_post = Post.objects.filter(page=Sayfa.objects.all()[5]).order_by('query')
    yazici_post = Post.objects.filter(page=Sayfa.objects.all()[4]).order_by('query')
    monitor_post = Post.objects.filter(page=Sayfa.objects.all()[3]).order_by('query')
    kasa_pc_post = Post.objects.filter(page=Sayfa.objects.all()[2]).order_by('query')
    laptop_post = Post.objects.filter(page=Sayfa.objects.all()[1]).order_by('query')
    satis_post = Post.objects.filter(page=Sayfa.objects.all()[0]).order_by('query')
    urls = {
        "satis": "pieces/hizmetler/satis.html",
        "yazici": "pieces/hizmetler/yazici.html",
        "monitor": "pieces/hizmetler/monitor.html",
        "laptop": "pieces/hizmetler/laptop.html",
        "kasa_pc": "pieces/hizmetler/kasa-pc.html"
    }

    # hizmetler_dict hizmetler.html'e gönderilecek, tüm bilgiler onun içinde
    hizmetler_dict = {
        "urls": urls,
        "hizmetlers": hizmetler_post,
        "yazicis": yazici_post,
        "monitors": monitor_post,
        "kasa_pcs": kasa_pc_post,
        "laptops": laptop_post,
        "satiss": satis_post,
    }
    return render(request, 'hizmetler.html', hizmetler_dict)


def kurumsal_view(request):
    kurumsal_post = Post.objects.filter(page=Sayfa.objects.all()[6]).order_by('query')
    misyon_vizyon_post = Post.objects.filter(page=Sayfa.objects.all()[7]).order_by('query')
    hakkimizda_post = Post.objects.filter(page=Sayfa.objects.all()[8]).order_by('query')
    basin_post = Post.objects.filter(page=Sayfa.objects.all()[9]).order_by('query')
    urls = {
        "misyon-vizyon": "pieces/kurumsal/misyon-vizyon.html",
        "hakkimizda": "pieces/kurumsal/hakkimizda.html",
        "basin": "pieces/kurumsal/basin.html",
    }
    kurumsal_dict = {
        "urls": urls,
        "kurumsals": kurumsal_post,
        "misyon_vizyons": misyon_vizyon_post,
        "hakkimizdas": hakkimizda_post,
        "basins": basin_post,
    }
    return render(request, "kurumsal.html", kurumsal_dict)


def calisma_sistemi_view(request):
    calisma_post = Post.objects.filter(page=Sayfa.objects.all()[10]).order_by('query')
    return render(request, 'calisma_sistemi.html', {"calismas": calisma_post})


def iletisim_view(request):
    return render(request, 'iletisim.html', {})
