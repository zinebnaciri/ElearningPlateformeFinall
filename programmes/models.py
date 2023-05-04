from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Niveaux(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)  


class Matiere(models.Model):
    matiere_id = models.CharField(unique=True, max_length=40)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, related_name='matiere')
    image = models.ImageField(upload_to='matiere', blank=True)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)  

class Lesson(models.Model):
    lesson_id = models.CharField(unique=True, max_length=40)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    creer_par = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='lesson',null=True)
    nom = models.CharField(max_length=100,null=True) 
    slug = models.SlugField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(verbose_name='chapitre no',null=True)  
    video = models.FileField(upload_to="Video", null=True, blank=True, verbose_name="cours en Video")
    fpe = models.FileField(upload_to="FPE", null=True, blank=True, verbose_name="fiche de presentation")
    pdf = models.FileField(upload_to="PDF", null=True, blank=True, verbose_name="Cours en pdf")

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.nom


    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)  
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("programmes:lessonlist", kwargs={"slug": self.matiere.slug, "niveau": self.niveau.slug})  

    


