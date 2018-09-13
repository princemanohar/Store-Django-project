from django.db import models
from django.utils import timezone
import json
# Create your models here.

INFRA_TYPES = [
        ("HW",'HARDWARE'),
        ("SW","SOFTWARE"),
        ("LG", "LOGISTICS")
]

class Infrastructure(models.Model):
    infra_id            = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=1024)
    deptt               = models.ForeignKey('Department', on_delete=models.CASCADE, null = False)
    infra_type          = models.CharField(max_length=64, choices = INFRA_TYPES)
    brand               = models.CharField(max_length=264)
    SKU_id              = models.CharField(max_length=264)

    licence_id          = models.CharField(max_length=264, blank=True)
    model_id            = models.CharField(max_length=264, blank=True)

    procurement_cost    = models.FloatField(blank=True, default=0)
    maintanence_cost    = models.FloatField(blank=True, default=0)
    running_cost        = models.FloatField(blank=True, default=0)

    procurement_date    = models.DateTimeField(default=timezone.now)
    last_upgraded_on    = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name+" ( "+self.infra_type+" )"


class Department(models.Model):
    deptt_id   = models.AutoField(primary_key=True)
    name       = models.CharField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name








