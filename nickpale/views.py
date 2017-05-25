from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "nickpale/home.html"


class AboutPageView(TemplateView):
    template_name = "nickpale/about.html"
