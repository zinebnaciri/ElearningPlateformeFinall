from django.db import models
from django.template.defaultfilters import slugify
class Niveaux(models.Model):
    nom = models.CharField( max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.nom
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Matiere(models.Model):
    matiere_id = models.CharField(unique=True)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    niveau = models.ForeignKey(Niveaux,on_delete=models.CASCADE, related_name ='matiere')
    image = models.ImageField(upload_to='matiere', blank=True)
    description = models.TextField(max_length= 500)

class lesson(models.Model):
    lesson_id = models.CharField(unique=True)
    niveau = models.ForeignKey(Niveaux,on_delete=models.CASCADE)
    




    
