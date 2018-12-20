from django.urls import path

from . import views


app_name = 'pro'
urlpatterns = [
    # ex: /pro/
    path('', views.ProfessionalHomeView.as_view(), name='pro')
]
