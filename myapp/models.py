from django.db import models
from django.utils import timezone
import json

# Create your models here.
class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=200)
    store_owner = models.CharField(max_length=200)
    location = models.TextField()
    established_on = models.DateTimeField(
            blank=True, null=True)
    gst_in = models.CharField(max_length=64)

    #def publish(self):
     #   self.published_date = timezone.now()
      #  self.save()

    def __str__(self):
        return json.dumps({"store_id":self.store_id, "store_name":self.store_name, "store_owner":self.store_owner})

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    review = models.TextField()
    stars = models.IntegerField()
    created_at = models.DateTimeField(
            default=timezone.now)
    updated_at = models.DateTimeField(
             auto_now=True)

    def __str__(self):
        return self.review

class Entities(models.Model):
    entity_id = models.AutoField(primary_key=True)
    entity_name = models.CharField(max_length=200)
    price = models.IntegerField()
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
        auto_now=True)

    def __str__(self):
        return self.entity_name


class Inventories(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    entity_id = models.ForeignKey(Entities, on_delete=models.CASCADE, null = False)
    count = models.IntegerField()
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
         auto_now=True)

    def __str__(self):
        return self.store_id, self.entity_id
