from django.db import models

# Create your models here.


class Event(models.Model):
    event_title=models.CharField(max_length=120)
    location=models.CharField(max_length=40)
    date=models.CharField(max_length=40)
    description=models.TextField()

    def __str__(self):
        return self.event_title
    
class Registration(models.Model):
    full_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    pno=models.CharField(max_length=10)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name