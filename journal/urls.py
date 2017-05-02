from django.conf.urls import url

from . import views

app_name = 'journal'
urlpatterns = [
    # ex: /journal/
    url(r'^$', views.JournalIndexView.as_view(), name='index'),
    # ex: /journal/5/
    url(r'^(?P<pk>[0-9]+)/$', views.JournalEntryView.as_view(), name='entry')
]
