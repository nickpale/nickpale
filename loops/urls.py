from django.urls import path

from . import views

app_name = 'loops'
urlpatterns = [
    # ex: /loops/
    path('', views.LoopIndexView.as_view(), name='index'),
    # ex: /loops/5/
    path('<int:pk>/', views.LoopView.as_view(), name='loop')
]
