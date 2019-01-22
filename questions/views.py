import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Answer
from notifications.models import PushNotification


class QuestionIndexView(generic.ListView):
    template_name = 'questions/questions.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all()


class AnswerView(generic.DetailView):
    model = Answer
    template_name = 'questions/answer.html'
    context_object_name = 'answer'

    def get_queryset(self):
        return Answer.objects.all()


def ask(request):
    new_question = Question(question=request.POST['askaquestion'], pub_date=timezone.now())
    new_question.save()

    responses = PushNotification.send()

    for list in responses:
        for response in responses[list]:
            print(datetime.datetime.now().strftime("[%d/%b/%Y %H:%M:%S]"),
                  '"POST',
                  list,
                  'HTTP/Custom"',
                  response.status_code,
                  response.text)

    return HttpResponseRedirect(reverse('questions:index'))
