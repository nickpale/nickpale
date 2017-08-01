"""nickpale URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^ask/', include('questions.urls')),
    # url(r'^donate/$', views.DonatePageView.as_view(), name='donate'),
    url(r'^loops/', include('loops.urls')),
    url(r'^me/$', views.AboutPageView.as_view(), name='about'),
    url(r'^music/', include('music.urls')),
    # url(r'^news/$', views.NewsPageView.as_view(), name='news'),
    url(r'^social/$', views.SocialPageView.as_view(), name='social'),
    url(r'^thoughts/', include('journal.urls')),
    url(r'^google45bddbda066f4df6\.html$',
        views.GoogleValidPageView.as_view()),
    url(r'^robots\.txt$',
        views.RobotsPageView.as_view(content_type="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
