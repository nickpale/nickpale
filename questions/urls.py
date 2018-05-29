from django.urls import path

from . import views


app_name = 'questions'
urlpatterns = [
    # ex: /questions/
    path('', views.QuestionIndexView.as_view(), name='index'),
    # ex: /questions/5/
    path('<int:pk>/', views.AnswerView.as_view(), name='answer'),
    # ex: /questions/ask/
    path('ask/', views.ask, name='ask')
]
