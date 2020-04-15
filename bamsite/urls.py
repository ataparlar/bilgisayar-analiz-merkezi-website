"""bamsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),

    path('hizmetler', hizmetler_view),
    path('hizmetler/satis', hizmetler_view),
    path('hizmetler/yazici', hizmetler_view),
    path('hizmetler/monitor', hizmetler_view),
    path('hizmetler/laptop', hizmetler_view),
    path('hizmetler/kasa-pc', hizmetler_view),

    path('kurumsal', kurumsal_view),
    path('kurumsal/misyon-vizyon', kurumsal_view),
    path('kurumsal/hakkimizda', kurumsal_view),
    path('kurumsal/basin', kurumsal_view),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
