from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(editable=False, unique=True, max_length=50)

    def __str__(self):
        return self.name


    def get_unique_slug(self):
        slug = slugify(
            self.name.replace('ı', 'i').replace('ə', 'e').replace('ö', 'o').replace('ğ', 'g').replace('ç', 'c').replace('ş', 's'))
        unique_slug = slug
        counter = 1
        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter = 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Category, self).save(*args, **kwargs)


class Course(models.Model):
    title = models.CharField(max_length=100, blank=False)
    # tutor = models.ForeignKey()
    category = models.ManyToManyField(Category)
    publish_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=120)

    def __str__(self):
        return self.title


    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i').replace('ə', 'e').replace('ö', 'o').replace('ğ', 'g').replace('ç', 'c').replace('ş', 's'))
        unique_slug = slug
        counter = 1
        while Course.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug


    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Course, self).save(*args, **kwargs)