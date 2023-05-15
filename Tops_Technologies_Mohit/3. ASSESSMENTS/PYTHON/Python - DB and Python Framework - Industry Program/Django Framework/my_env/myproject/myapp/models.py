from django.db import models

# Create your models here.
class costomer(models.Model):
    Username = models.CharField(max_length=30)
    Email    = models.EmailField(max_length=30,unique=True)
    Password = models.IntegerField(max_length=30)
    Confirm_Password = models.CharField(max_length=30)
    Frish_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Phome_Number = models.IntegerField(max_length=30)
    
    # def __str__(self):
    #     return self.name
    
    
