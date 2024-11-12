from django.db import models

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)  # Add a description field
    ingredients = models.TextField(blank=True, null=True)  # Add an ingredients field
    category = models.CharField(max_length=100, blank=True, null=True)  # Category of the dish
    photo = models.ImageField(upload_to='menu_photos/', blank=True, null=True)  # Optional photo of the dish

    def __str__(self):
        return self.name



# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model