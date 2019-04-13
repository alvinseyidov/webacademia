
from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    purchasedcourses = models.ManyToManyField(Course)
    photo = models.ImageField(default='profilephotos/default.png', upload_to='profilephotos', blank=False)
    headline = models.CharField(max_length=30, null=True, blank=False)
    bio = models.TextField(max_length=400, null=True, blank=False)


    def __str__(self):
        return self.user.username