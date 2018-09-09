from django.contrib import admin

# Register your models here.
from .models import Store,Reviews,Inventories

admin.site.register(Store)
admin.site.register(Reviews)
admin.site.register(Inventories)