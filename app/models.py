from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    
    def saludar(self, nombre):
        return "hola " + nombre

    def validador(self, postData):
        errors = {}

        if len(postData['title']) < 5:
            errors['largo_title'] = "El largo del titulo es menor a 5 caracteres."

        return errors
        

class Show(models.Model):
    title = models.CharField(max_length=150) # default null blank
    network = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __str__(self):
        return f"{self.title} ( {self.network} )"

    def __repr__(self):
        return f"{self.title} ( {self.network} )"
    