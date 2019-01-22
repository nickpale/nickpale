from django.urls import include, path

from . import views


app_name = 'pro'
urlpatterns = [
    # ex: /pro/
    path('', views.ProfessionalHomeView.as_view(), name='home'),
    # ex: /pro/api/ in case of pro subdomain usage
    path('api/', include('api.urls'))
]
