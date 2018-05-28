from django.urls import path

from . import views


app_name = 'journal'
urlpatterns = [
    # ex: /journal/
    path('', views.JournalIndexView.as_view(), name='index'),
    # ex: /journal/5/
    path('<int:pk>/', views.JournalEntryView.as_view(), name='entry')
]
