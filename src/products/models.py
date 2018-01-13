from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    discription = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title