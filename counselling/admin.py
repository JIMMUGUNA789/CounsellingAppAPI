from decimal import Clamped
from django.contrib import admin
from .models import Client, Counsellor, Article

# Register your models here.
admin.site.register(Client)
admin.site.register(Counsellor)
admin.site.register(Article)
