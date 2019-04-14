
# coding=utf-8
# from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    thumbnail = models.ImageField(upload_to='thumbnails/category/', null=True, blank=False)
    slug = models.SlugField(editable=False, unique=True, max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coursefrom_category', args=[str(self.slug)])

    def get_unique_slug(self):
        slug = slugify(
            self.name.replace('ı', 'i').replace('ə', 'e').replace('ö', 'o').replace('ğ', 'g').replace('ç', 'c').replace('ş', 's'))

        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Category, self).save(*args, **kwargs)



class Videos(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=False)
    altname = models.CharField(max_length=100, null=True, blank=False)
    video = models.FileField(upload_to='videos/', null=True, blank=False)
    place = models.PositiveIntegerField(default=1, blank=False)
    videoslug = models.SlugField(unique=True, editable=False, max_length=3, null=True)
    # duration = models.DurationField(help_text='duration', null=True)


    def __str__(self):
        return self.altname + str(self.place)


    # def get_watchvideo_url(self):
     #   return reverse('watch', args=[str(self.videoslug)])


    def get_unique_slug(self):
        videoslug = slugify(self.place)+slugify(self.altname)
        return videoslug
    
    def save(self, *args, **kwargs):
        self.videoslug = self.get_unique_slug()
        
        return super(Videos, self).save(*args, **kwargs)


class Course(models.Model):
    SKILLS = (('Beginner', 'beginner'), ('Intermediate', 'intermediate'), ('Expert', 'expert'))

    title = models.CharField(max_length=100, blank=False)
    teacher = models.ForeignKey(User, default=1, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill = models.CharField(max_length=12, choices=SKILLS, default='beginner')
    price = models.FloatField(default=10, blank=False)
    description = models.TextField(max_length=2000, null=True, blank=False)
    # whatwillilearn = ArrayField(models.CharField(max_length=200), blank=False, null=False, default='list')
    thumbnail = models.ImageField(upload_to='thumbnails/course/', null=True, blank=False)
    promotion = models.FileField(upload_to='promotions/', null=True, blank=False)
    video = models.ManyToManyField(Videos)
    # publish_date = models.DateTimeField(auto_now_add=True)
    purchased = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, editable=False, max_length=120)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.slug)])

    def get_watch_url(self):
        return reverse('watch', args=[str(self.slug)])


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















