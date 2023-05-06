from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.db.models import Q
from PIL import Image

from .validators import ASCIIUsernameValidator

User = settings.AUTH_USER_MODEL

# LEVEL_COURSE = "Level course"
LP = "Licence"
MS = "Master"

LEVEL = (
    # (LEVEL_COURSE, "Level course"),
    (LP, "Licence"),
    (MS, "Master"),
)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_dep_head = models.BooleanField(default=False)
    phone = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pictures/%y/%m/%d/', default='default.png', null=True)
    email = models.EmailField(blank=True, null=True)

    username_validator = ASCIIUsernameValidator()

    # objects = UserManager()

    @property
    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

    def __str__(self):
        return '{} ({})'.format(self.username, self.get_full_name)

    @property
    def get_user_role(self):
        if self.is_superuser:
            return "Admin"
        elif self.is_student:
            return "Student"
        elif self.is_lecturer:
            return "Prof"
    def get_picture(self):
        try:
            return self.picture.url
        except:
            no_picture = settings.MEDIA_URL + 'default.png'
            return no_picture

    def get_absolute_url(self):
        return reverse('profile_single', kwargs={'id': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)
        except:
            pass

    def delete(self, *args, **kwargs):
        if self.picture.url != settings.MEDIA_URL + 'default.png':
            self.picture.delete()
        super().delete(*args, **kwargs)


class StudentManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(level__icontains=query) | 
                         Q(department__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() 
        return qs


class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=25, choices=LEVEL, null=True)

    objects = StudentManager()

    def __str__(self):
        return self.student.get_full_name

    def get_absolute_url(self):
        return reverse('profile_single', kwargs={'id': self.id})

    def delete(self, *args, **kwargs):
        self.student.delete()
        super().delete(*args, **kwargs)

