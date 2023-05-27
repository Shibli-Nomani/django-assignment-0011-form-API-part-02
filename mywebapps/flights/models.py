from django.db import models

# Create your models here.
#table name
#inherit the models into Model
class Flight(models.Model):
    client_id = models.IntegerField()
    client_name = models.CharField(max_length = 50)
    client_email = models.EmailField(max_length = 35)
    batch = models.IntegerField()
    destination = models.CharField(max_length = 25)


    

