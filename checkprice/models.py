from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255,default='')
    cn_official_price = models.IntegerField(default=0)
    pic = models.CharField(max_length=1024,default='')
    other_people_price = models.CharField(max_length=255,default='')
    hk_official_price = models.IntegerField(default=0)
    our_price = models.IntegerField(default=0)

class SaleRecord(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,default='',related_name="item_record")
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    location = models.CharField(max_length=255,default='')
    date = models.DateField()
    sell_person = models.CharField(max_length=255,default='')



