from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class JobsApply(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    present_address = models.CharField(max_length=100)
    
    university = models.CharField(max_length=50, blank=True, null=True)

    resume = models.FileField(upload_to='nimusoft/resume/')
    cover_letter = models.TextField()

    def __str__(self):
        return self.name