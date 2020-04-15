from django.shortcuts import render
from .models import *

# Create your views here.


def main_view(request):
    main_images = KayanFotograf.objects.all()
    main_posts = Post.objects.filter(page=Sayfa.objects.all()[11])
    main_dict = {
        "images": main_images,
        "posts": main_posts,
    }
    return render(request, 'main.html', main_dict)


def hizmetler_view(request):
    hizmetler_post = Post.objects.filter(page=Sayfa.objects.all()[5])
    yazici_post = Post.objects.filter(page=Sayfa.objects.all()[4])
    monitor_post = Post.objects.filter(page=Sayfa.objects.all()[3])
    kasa_pc_post = Post.objects.filter(page=Sayfa.objects.all()[2])
    laptop_post = Post.objects.filter(page=Sayfa.objects.all()[1])
    satis_post = Post.objects.filter(page=Sayfa.objects.all()[0])
    urls = {
        "satis": "pieces/hizmetler/satis.html",
        "yazici": "pieces/hizmetler/yazici.html",
        "monitor": "pieces/hizmetler/monitor.html",
        "laptop": "pieces/hizmetler/laptop.html",
        "kasa-pc": "pieces/hizmetler/kasa-pc.html"
    }

    # hizmetler_dict hizmetler.html'e gönderilecek, tüm bilgiler onun içinde
    hizmetler_dict = {
        "urls": urls,
        "hizmetlers": hizmetler_post,
        "yazicis": yazici_post,
        "monitors": monitor_post,
        "kasa-pcs": kasa_pc_post,
        "laptops": laptop_post,
        "satiss": satis_post,
    }
    return render(request, 'hizmetler.html', hizmetler_dict)


def kurumsal_view(request):
    kurumsal_post = Post.objects.filter(page=Sayfa.objects.all()[6])
    misyon_vizyon_post = Post.objects.filter(page=Sayfa.objects.all()[7])
    hakkimizda_post = Post.objects.filter(page=Sayfa.objects.all()[8])
    basin_post = Post.objects.filter(page=Sayfa.objects.all()[9])
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
