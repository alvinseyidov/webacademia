from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False)
    # tutor = models.ForeignKey()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'
