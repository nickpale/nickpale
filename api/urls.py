from django.urls import include, path

from pro.views import BlurbView, DescriptionListView, ResumeView

urlpatterns = [
    # ex: /api/pro/
    path('pro/', include([
        # ex: /api/pro/blurb
        path('blurb', BlurbView.as_view(), name='blurb'),
        # ex: /api/pro/descriptions
        path('descriptions', DescriptionListView.as_view(), name='descriptions'),
        # ex: /api/pro/resume
        path('resume', ResumeView.as_view(), name='resume')
    ]))
]
