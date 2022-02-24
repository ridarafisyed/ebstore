from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=255)
    imageFile =models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name + ": " + str(self.imageFile)

class Video(models.Model):
   name = models.CharField(max_length=255)
   videoFile =models.FileField(upload_to='videos/', null=True, blank=True)

   def __str__(self):
        return self.name + ": " + str(self.videoFile)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.email + ": " + self.subject