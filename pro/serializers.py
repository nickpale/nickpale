from rest_framework import serializers

from .models import Blurb, Description, Resume


class BlurbSerializer(serializers.ModelSerializer):
    """Serialize blurbs"""
    class Meta:
        model = Blurb
        fields = ('title', 'text')
        read_only_fields = ('title', 'text')


class DescriptionSerializer(serializers.ModelSerializer):
    """Serialize Descriptions"""
    class Meta:
        model = Description
        fields = ('title', 'text')
        read_only_fields = ('title', 'text')


class ResumeSerializer(serializers.ModelSerializer):
    """Serialize Resumes"""
    class Meta:
        model = Resume
        fields = ('title', 'file')
        read_only_fields = ('title', 'file')
