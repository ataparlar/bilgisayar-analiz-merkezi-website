from django.shortcuts import render
from django.views.generic import TemplateView
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
    hizmetler_dict = {
        "hizmetlers": hizmetler_post,
        "yazicis": yazici_post,
        "monitors": monitor_post,
        "kasa-pcs": kasa_pc_post,
        "laptops": laptop_post,
        "satiss": satis_post,
    }
    return render(request, 'hizmetler.html', hizmetler_dict)
