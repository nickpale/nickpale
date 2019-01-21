from django.http import Http404
from django.views.generic.base import TemplateView
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blurb, Description, Resume
from .serializers import (BlurbSerializer, DescriptionSerializer,
                          ResumeSerializer)


class ProfessionalHomeView(TemplateView):
    template_name = "pro/home.html"


class BlurbView(APIView):
    """Return active blurb"""
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        blurb = Blurb.objects.filter(active=True).first()
        if not blurb:
            return Response('', status=404)
        return Response(BlurbSerializer(blurb).data, status=200)


class DescriptionListView(generics.ListAPIView):
    """List all blurbs"""
    parser_classes = (JSONParser,)

    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class ResumeView(APIView):
    """Return active resume"""
    parser_classes = (JSONParser,)

    def get(self, request, format=None):
        resume = Resume.objects.filter(active=True).first()
        if not resume:
            return Response('', status=404)
        return Response(ResumeSerializer(resume).data, status=200)
