from django.db import models
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=125, blank=True, null=True, verbose_name="Наименование продукта")
    price = models.IntegerField(blank=True, null=True, verbose_name="Цена")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

