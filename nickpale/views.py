from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "nickpale/home.html"


class AboutPageView(TemplateView):
    template_name = "nickpale/about.html"


class DonatePageView(TemplateView):
    template_name = "nickpale/donate.html"


class NewsPageView(TemplateView):
    template_name = "nickpale/news.html"


class SocialPageView(TemplateView):
    template_name = "nickpale/social.html"


class RobotsPageView(TemplateView):
    template_name = "nickpale/robots.txt"

class GoogleValidPageView(TemplateView):
    template_name = "nickpale/google45bddbda066f4df6.html"
