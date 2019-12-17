"""kilankodaniel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from update_site import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from update_site.views import Update_SiteViewset

routers = routers.DefaultRouter()
routers.register(r'updateblog',Update_SiteViewset)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^single/(?P<blog_id>[0-9]+)/$', views.blog_single, name='single'),
    url(r'^category/(?P<cat_id>[\w\-]+)/$', views.category_blog, name='category_blog'),
    url(r'^blogs', views.blog, name='blogs'),
    url(r'^api/',include(routers.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
