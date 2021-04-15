from django.db import models

# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo/%y/%m/%d')
    is_nvp = models.BooleanField(default=False)
    desc = models.TextField(blank=True, verbose_name='Description')
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    contract_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-contract_date']
