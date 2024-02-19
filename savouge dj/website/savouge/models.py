from django.db import models

# Create your models here.

class Home(models.Model):
  image = models.ImageField()
  text =models.CharField(max_length=50)
  def __str__(self) -> str:
       return self.text

class Food_type(models.Model):
  name = models.CharField(max_length=50)
  def __str__(self) -> str:
       return self.name

class Menu(models.Model):
  images = models.ImageField()
  Food_type = models.ForeignKey(Food_type,on_delete=models.CASCADE)
  description= models.TextField()
  
  

class About(models.Model):
  image = models.ImageField()

class company_info(models.Model):

  name = models.TextField()
  def __str__(self) -> str:
       return self.name
  