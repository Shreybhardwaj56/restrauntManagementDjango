from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_discount = models.FloatField()
    item_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.item_name

    # def get_absolute_url(self):
    #     return reverse("restraunt:detail", kwargs={"pk": self.pk})