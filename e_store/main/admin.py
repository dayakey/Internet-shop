from django.contrib import admin
from .models import Goods, Order, Comment, Rating

admin.site.register(Goods)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Rating)
