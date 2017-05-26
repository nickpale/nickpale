from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "nickpale/home.html"


class AboutPageView(TemplateView):
    template_name = "nickpale/about.html"


class LoopPageView(TemplateView):
    template_name = "nickpale/loops.html"


class AlbumPageView(TemplateView):
    template_name = "nickpale/albums.html"


class DonatePageView(TemplateView):
    template_name = "nickpale/donate.html"


class QuestionPageView(TemplateView):
    template_name = "nickpale/question.html"


class NewsPageView(TemplateView):
    template_name = "nickpale/news.html"
