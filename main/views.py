from django.shortcuts import render
from .models import *

# Create your views here.


def main_view(request):
    main_images = KayanFotograf.objects.all()
    return render(request, 'main.html', {"images": main_images})


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
