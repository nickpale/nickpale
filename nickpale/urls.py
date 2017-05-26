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
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^me$', views.AboutPageView.as_view(), name='about'),
    url(r'^loops$', views.LoopPageView.as_view(), name='loops'),
    url(r'^albums$', views.AlbumPageView.as_view(), name='albums'),
    url(r'^donate$', views.DonatePageView.as_view(), name='donate'),
    url(r'^ask$', views.QuestionPageView.as_view(), name='question'),
    url(r'^news$', views.NewsPageView.as_view(), name='news'),
    url(r'^thoughts/', include('journal.urls')),
    url(r'^admin/', admin.site.urls),
]
