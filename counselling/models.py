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

    

    class Meta:
        verbose_name_plural = 'Counsellors'

    
class Client(User):
    phone_number = models.IntegerField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images')
    counsellor_assigned = models.ForeignKey('Counsellor', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'Clients'
    

class Issue(models.Model):
    anxiety = models.BooleanField(default=False)
    troumatic_experience = models.BooleanField(default=False)
    relationship = models.BooleanField(default=False)
    stress = models.BooleanField(default=False)
    depression = models.BooleanField(default=False)
    addiction = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.client.
    class Meta:
        verbose_name_plural = 'Issues'

    

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
        verbose_name_plural = 'Articles'

time_choices = (
    ("8-9am", "8-9am"),
    ("9-10am", "9-10am"),
    ("10-11am", "10-11am"),
    ("11-12pm", "11-12pm"),
    ("12-1pm", "12-1pm"),
    ("1-2pm", "1-2pm"),
    ("2-3pm", "2-3pm"),
    ("3-4pm", "3-4pm"),
    ("4-5pm", "4-5pm"),
) 

class Appointment(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    counsellor = models.ForeignKey('Counsellor', on_delete=models.SET_NULL,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.CharField(max_length=255, choices=time_choices, default="8-9am" )
    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.client
    
    class Meta:
        ordering = ['-date']





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
