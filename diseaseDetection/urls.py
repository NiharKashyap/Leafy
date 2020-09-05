"""diseaseDetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

handler403 = 'potato.views.handler403'
handler404 = 'potato.views.handler404'
handler500 = 'potato.views.handler500'

urlpatterns = [
    path('Django_admin/', admin.site.urls),
    path('', include('potato.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('media/<path:path>', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)