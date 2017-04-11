from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /journal/
    url(r'^$', views.index, name='index'),
    # ex: /journal/5/
    url(r'^(?P<journal_entry_id>[0-9]+)/$', views.entry, name='entry')
]
