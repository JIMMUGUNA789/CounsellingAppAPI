from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
# Create your models here.
class Counsellor(User):
    phone_number = models.IntegerField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images')

    
class Client(User):
    phone_number = models.IntegerField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images')
    counsellor_assigned = models.ForeignKey('Counsellor', on_delete=models.SET_NULL, null=True)

category_choices = (
    ("Anxiety", "Anxiety"),
    ("Troumatic Experience", "Troumatic Experience"),
    ("Relationship", "Relationship"),
    ("School or Work Stress", "School or Work Stress"),
    ("Depression", "Depression"),
    ("Addiction", "Addiction"),
    ("Other", "Other"),
) 

class Article(models.Model):
    author = models.ForeignKey('Counsellor', on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=255)
    approved = models.BooleanField(default=False)
    article_image = models.ImageField(null=True, blank=True, upload_to='images')
    categories = models.CharField(max_length=255, choices=category_choices, default="Other")
    article = models.FileField(upload_to='articles')

    class Meta:
        ordering = ['-date_published']






@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
