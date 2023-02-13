from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class menuIteam(models.Model):
    Item_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='menu')
    desc = models.TextField()

    def __str__(self):
        return self.Item_name
