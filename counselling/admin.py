from decimal import Clamped
from django.contrib import admin
from .models import Client, Counsellor, Article, Issue, Appointment
from django.contrib.auth.models import Group

# Register your models here.
admin.site.site_header = 'Eger Counsel Admin'
class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    list_filter = ('username', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')

    def has_add_permission(self, request, obj=None):
        return False

class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')
    list_filter = ('username', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')
    list_per_page = 10
    def has_add_permission(self, request, obj=None):
        return False

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'categories', 'date_published', 'approved', 'article_image', 'article')
    list_filter = ('categories',)
    search_fields = ('title', 'categories')
    list_per_page = 5

class IssueAdmin(admin.ModelAdmin):
    search_fields = ('client',)
    list_display = ('client', 'anxiety', 'troumatic_experience', 'relationship', 'stress', 'depression', 'addiction', 'other')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'counsellor', 'date', 'time', 'expired',)
    search_fields = ('client','counsellor',)

class ImportAdmin(admin.ModelAdmin):
    change_list_template = 'admin/counselling/client/change_list.html'

admin.site.register(Client, ClientAdmin)
admin.site.register(Counsellor, CounsellorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Issue)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.unregister(Group)