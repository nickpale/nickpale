from django.conf.urls import url

from . import views

app_name = 'loops'
urlpatterns = [
    # ex: /loops/
    url(r'^$', views.LoopIndexView.as_view(), name='index'),
    # ex: /loops/5/
    url(r'^(?P<pk>[0-9]+)/$', views.LoopView.as_view(), name='loop')
]
