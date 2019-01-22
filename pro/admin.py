from django.contrib import admin

from .models import Blurb, Description, Resume


@admin.register(Blurb)
class BlurbAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'active')


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'order_rank')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
