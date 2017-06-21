from django.conf.urls import url

from . import views

app_name = 'questions'
urlpatterns = [
    # ex: /questions/
    url(r'^$', views.QuestionIndexView.as_view(), name='questions'),
    # ex: /questions/5/
    url(r'^(?P<pk>[0-9]+)/$', views.AnswerView.as_view(), name='answer'),
    # ex: /questions/ask/
    url(r'^vote/$', views.ask, name='ask')
]
