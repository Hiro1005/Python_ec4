from django.db import models


class Product(models.Model):
    """ 製品
    """
    name = models.CharField("商品名", max_length=128)
    price = models.PositiveIntegerField("価格")
