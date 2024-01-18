from django.db import models

# makemigration = create change and store in file 
# migrate =applt the pending changes created by make migration 
# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=122)
    contact=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    date=models.DateField()
