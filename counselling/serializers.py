from rest_framework import serializers
from .models import Client, Counsellor, Article, Issue, Appointment

#Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'phone_number', 'profile_pic')

#client registration serializer
class RegisterClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'password', 'phone_number','profile_pic')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        client = Client.objects.create_user(
         validated_data['username'],
         validated_data['email'], 
         validated_data['password'], 
         phone_number=validated_data['phone_number'],
         profile_pic=validated_data['profile_pic'])
        return client
#counsellor seriallizer
class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ('id', 'username', 'email', 'phone_number','profile_pic')

class RegisterCounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ('id', 'username', 'email', 'password', 'phone_number', 'profile_pic')
        extra_kwargs = {'password':{'write_only':True}}

    
    def create(self, validated_data):
         counsellor = Counsellor.objects.create_user(
         validated_data['username'],
         validated_data['email'], 
         validated_data['password'], 
         phone_number=validated_data['phone_number'],
         profile_pic=validated_data['profile_pic'])
         return counsellor

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class RegisterIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'   

    
    def create(self, validated_data):
         issue = Issue.objects.create(
             anxiety = validated_data['anxiety'],
             troumatic_experience = validated_data['troumatic_experience'],
             relationship = validated_data['relationship'],
             stress = validated_data['stress'],
             depression = validated_data['depression'],
             addiction = validated_data['addiction'],
             other = validated_data['other'],
             client = validated_data['client']
                
         )
         return issue

class ChangePasswordSerializer(serializers.Serializer):
    model = Client

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ChangeCounsellorPasswordSerializer(serializers.Serializer):
    model = Counsellor
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'  

class UploadArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'article_image', 'categories', 'article')    

    
    def create(self, validated_data):
         article = Article.objects.create(
         author=validated_data['author'],
         title=validated_data['title'], 
         article_image=validated_data['article_image'], 
         categories=validated_data['categories'],
         article=validated_data['article'])
         return article
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'  

class CreateappointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'client', 'counsellor', 'date', 'time')    

    
    def create(self, validated_data):
         appointment = Appointment.objects.create(
         client=validated_data['client'],
         counsellor=validated_data['counsellor'], 
         date=validated_data['date'], 
         time=validated_data['time'],)
         
         return appointment
    