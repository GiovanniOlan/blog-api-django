from django.contrib import admin
from apps.categories.models import *

# Register your models here.

admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "published"]
