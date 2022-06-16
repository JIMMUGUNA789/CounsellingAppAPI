from decimal import Clamped
from django.contrib import admin
from .models import Client, Counsellor, Article, Issue
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Eger Counsel Admin Panel'
class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    list_filter = ('username', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    list_filter = ('username', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')
    list_per_page = 10

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'categories', 'date_published', 'approved', 'article_image', 'article')
    list_filter = ('categories',)
    search_fields = ('title', 'categories')
    list_per_page = 5

class IssueAdmin(admin.ModelAdmin):
    search_fields = ('client',)
    list_display = ('client', 'anxiety', 'troumatic_experience', 'relationship', 'stress', 'depression', 'addiction', 'other')

admin.site.register(Client, ClientAdmin)
admin.site.register(Counsellor, CounsellorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Issue)
admin.site.unregister(Group)