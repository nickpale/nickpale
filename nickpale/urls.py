from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    # path(r'^donate/$', views.DonatePageView.as_view(), name='donate'),
    path('email/', views.EmailPageView.as_view(), name='email'),
    path('loops/', include('loops.urls')),
    path('me/', views.AboutPageView.as_view(), name='about'),
    path('music/', include('music.urls')),
    # path(r'^news/$', views.NewsPageView.as_view(), name='news'),
    path('pro/', include('pro.urls')),
    path('questions/', include('questions.urls')),
    path('social/', views.SocialPageView.as_view(), name='social'),
    path('thoughts/', include('journal.urls')),
    path('google45bddbda066f4df6.html',
        views.GoogleValidPageView.as_view()),
    path('google2b7fe076baa2fa0c.html',
        views.GSuiteValidPageView.as_view()),
    path('robots.txt',
        views.RobotsPageView.as_view(content_type="text/plain")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
