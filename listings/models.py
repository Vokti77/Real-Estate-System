from django.db import models
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, verbose_name='Description')
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    garage = models.BooleanField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(decimal_places=2, max_digits=5)
    is_published = models.BooleanField()
    photo_main = models.ImageField(upload_to='photos/%d/%m/%y')
    photo_1 = models.ImageField(upload_to='photos/%d/%m/%y')
    photo_2 = models.ImageField(upload_to='photos/%d/%m/%y')
    photo_3 = models.ImageField(upload_to='photos/%d/%m/%y')
    photo_4 = models.ImageField(upload_to='photos/%d/%m/%y')
    photo_5 = models.ImageField(upload_to='photos/%d/%m/%y')
    photo_6 = models.ImageField(upload_to='photos/%d/%m/%y')
    list_date = models.DateTimeField(auto_now_add=False)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-list_date',)