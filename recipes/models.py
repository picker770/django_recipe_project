from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.title
