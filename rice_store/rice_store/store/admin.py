from django.contrib import admin
from .models import Rice, Order
# store/admin.py
from django.contrib import admin
from .models import Rice

# store/admin.py
from django.contrib import admin
from .models import Rice

class RiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand')  # Ensure 'brand' is a valid field
    def get_brand(self, obj):
        return obj.brand  # Ensure this method matches your needs
    get_brand.short_description = 'Brand'

admin.site.register(Rice, RiceAdmin)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'rice', 'quantity', 'created_at')
