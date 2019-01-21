from django.contrib import admin

from .models import Blurb, Description, Resume


@admin.register(Blurb)
class BlurbAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'active')


admin.site.register(Description)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
