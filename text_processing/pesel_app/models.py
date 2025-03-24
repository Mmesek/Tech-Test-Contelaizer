from django.db import models

# Create your models here.


class PESELForm(models.Model):
    pesel = models.CharField(max_length=11)
