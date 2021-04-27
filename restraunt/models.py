from django.db import models
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    food_name = models.CharField(max_length=200)
    food_price = models.IntegerField()
    food_discount = models.FloatField()
    food_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return reverse("restraunt:details", kwargs={"pk": self.pk})