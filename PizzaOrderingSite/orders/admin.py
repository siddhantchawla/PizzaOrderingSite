from django.contrib import admin

# Register your models here.
from .models import Size,Pizza,Topping,Type,Order

admin.site.register(Size)
admin.site.register(Pizza)
admin.site.register(Type)
admin.site.register(Topping)
admin.site.register(Order)


