from django.db import models
from django.utils import timezone

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
        return self.store_name

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

class Inventories(models.Model):
    store_id = models.ForeignKey('Store', on_delete=models.CASCADE)
    entity_id = models.AutoField(primary_key=True)
    count = models.IntegerField()
    created_at = models.DateTimeField(
        default=timezone.now)
    updated_at = models.DateTimeField(
         auto_now=True)

    def __str__(self):
        return self.count
