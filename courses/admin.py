
from django.contrib import admin
from .models import Category, Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'slug']


    class Meta:
        model = Course

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    class Meta:
        model = Category


admin.site.register(Category)
admin.site.register(Course)
