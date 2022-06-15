from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, permissions,status
from knox.models import AuthToken


from counselling.models import Client, Counsellor, Article,Issue
from .serializers import ArticleSerializer, ClientSerializer, RegisterClientSerializer, CounsellorSerializer, RegisterCounsellorSerializer, ChangePasswordSerializer, ChangeCounsellorPasswordSerializer, ArticleSerializer, RegisterIssueSerializer, UploadArticleSerializer
from .serializers import IssueSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated


# Create your views here.

#admin dashboard

def admin(request):
  return render(request, 'admin/index.html')

@api_view(['GET'])
def routes(request):
    routes=[
        {'routeURL':'/counselling',
        'instruction':'all urls should pre-append this'

        },
        {'path':'routes/',
        'method':'GET',
        'description':'Returns all routes',},
        {
        'path':'client/register/',
        'method':'POST',
        'description':'Register a new client',
        'response':'client details and a token'
            
        },
          {
        'path':'client/login/',
        'method':'POST',
        'description':'login client',
        'response':'token'
            
        },
          {
        'path':'client/logout/',
        'method':'POST',
        'description':'logout client',
        'response':''
            
        },
          {
        'path':'client/logoutall/',
        'method':'POST',
        'description':'logout client on all devices',
        'response':''
            
        },
         {
        'path':'counsellor/register/',
        'method':'POST',
        'description':'Register a new counsellor',
        'response':'client details and a token'
            
        },
         {
        'path':'counsellor/login/',
        'method':'POST',
        'description':'login counsellor',
        'response':'token'
            
        },
          {
        'path':'counsellor/logout/',
        'method':'POST',
        'description':'logout counsellor',
        'response':''
            
        },
          {
        'path':'client/logoutall/',
        'method':'POST',
        'description':'logout client on all devices',
        'response':''
            
        },
        {
        'path':'clients/',
        'method':'GET',
        'description':'list of all clients',
        'response':''
        },
          {
        'path':'clients/detail/<int:id>/',
        'method':'GET',
        'description':'client detail',
        'response':''
        },
          {
        'path':'clients/delete/<int:id>/',
        'method':'DELETE',
        'description':'delete',
        'response':''
        },
          {
        'path':'counsellors/',
        'method':'GET',
        'description':'list of all clients',
        'response':''
        },
          {
        'path':'counsellors/detail/<int:id>/',
        'method':'GET',
        'description':'counsellor detail',
        'response':''
        },
          {
        'path':'counsellors/delete/<int:id>/',
        'method':'DELETE',
        'description':'delete',
        'response':''
        },
         {
        'path':'client/changePassword/',
        'method':'PUT',
        'description':'Change client password',
        'response':'success message',
        'expected_data':{
          'old_password':"",
          'new_password':"",
          'token':'',
        }
        },
         {
        'path':'client/password_reset/',
        'method':'POST',
        'description':'reset client password',
        'response':'a token',
        'expected_data':{
          
          'email':'',
        }
        },
          {
        'path':'client/password_reset/confirm/',
        'method':'POST',
        'description':'reset client password confirmation',
        'response':'a token',
        'expected_data':{
          
          'token':'',
          'password':''
        }
        },
        {
        'path':'articles/',
        'method':'GET',
        'description':'get a list of all article details ',
        'response':'all articles'
        },
        {
        'path':'articles/upload/',
        'method':'POST',
        'description':'Upload an article',
        'response':'returns the uploaded article'
        },
        {
        'path':'articles/<int:id>/',
        'method':'GET',
        'description':'GET details of a particular article',
        'response':'article details'
        },
        {
        'path':'articles/update/<int:id>/',
        'method':'PUT',
        'description':'update details of an article',
        'response':'updated article'
        },
        {
        'path':'articles/delete/<int:id>/',
        'method':'DELETE',
        'description':'delete article',
        'response':'article deleted'
        },
         {
        'path':'articles/approve/<int:id>/',
        'method':'PUT',
        'description':'approve an article. Only an admin should be able to do this',
        'response':'approved article'
        },
        

    ]
    return Response(routes)
#client registration
class RegisterClient(generics.GenericAPIView):
    serializer_class = RegisterClientSerializer

    def post(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()
        return Response({
            'client':ClientSerializer(client, context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(client)[1]
        })


#Register client issues

class RegisterClientIssue(generics.GenericAPIView):
    serializer_class = RegisterIssueSerializer

    def post(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        issue = serializer.save()
        return Response({
            'issue':IssueSerializer(issue, context=self.get_serializer_context()).data
            
        })

  


#client login
class ClientLogin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.validated_data['user']
        login(request, client)
        return super(ClientLogin, self).post(request, format=None)

#counsellor registration
class RegisterCounsellor(generics.GenericAPIView):
    serializer_class = RegisterCounsellorSerializer

    def post(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        counsellor = serializer.save()
        return Response({
            'counsellor':CounsellorSerializer(counsellor, context=self.get_serializer_context()).data,
            'token':AuthToken.objects.create(counsellor)[1]
        })

#counsellor login
class CounsellorLogin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        counsellor = serializer.validated_data['user']
        login(request, counsellor)
        return super(CounsellorLogin, self).post(request, format=None)

#get all clients
@api_view(['GET'])
def getClients(request):
    clients=Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)
#get particular client
@api_view(['GET'])
def getClientDetail(request, id):
    client = Client.objects.get(id=id)
    serializer = ClientSerializer(client, many=False)
    return Response(serializer.data)
#delete client
@api_view(['DELETE'])
def deleteClient(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return Response('Client deleted')

#get all counsellors
@api_view(['GET'])
def getCounsellors(request):
    counsellors=Counsellor.objects.all()
    serializer = CounsellorSerializer(counsellors, many=True)
    return Response(serializer.data)
#get particular counsellor
@api_view(['GET'])
def getCounsellorDetail(request, id):
    counsellor = Counsellor.objects.get(id=id)
    serializer = CounsellorSerializer(counsellor, many=False)
    return Response(serializer.data)
#delete counsellor
@api_view(['DELETE'])
def deleteCounsellor(request, id):
    counsellor = Counsellor.objects.get(id=id)
    counsellor.delete()
    return Response('Counsellor deleted')

#change client password

class ChangePassword(generics.UpdateAPIView):
  serializer_class = ChangePasswordSerializer
  model = Client
  pagination_class = (IsAuthenticated,)

  def get_object(self, queryset=None):
        obj = self.request.user
        return obj

  def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Change Counsellor Password

class ChangeCounsellorPassword(generics.UpdateAPIView):
  serializer_class = ChangeCounsellorPasswordSerializer
  model = Counsellor
  pagination_class = (IsAuthenticated,)

  def get_object(self, queryset=None):
        obj = self.request.user
        return obj

  def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#article management
#get all article
@api_view(['GET'])
def getArticles(request):
  articles = Article.objects.all()
  serializer = ArticleSerializer(articles, many=True)
  return Response(serializer.data)

#article detail

@api_view(['GET'])
def getArticleDetails(request, id):
  article = Article.objects.get(id=id)
  serializer = ArticleSerializer(article, many=False)
  return Response(serializer.data)



#Upload article
class UploadArticle(generics.GenericAPIView):
    serializer_class = UploadArticleSerializer

    def post(self, request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        return Response({
            'article':ArticleSerializer(article, context=self.get_serializer_context()).data
            
        })




#update an article
@api_view(['PUT'])
def updateArticle(request, id):
  data = request.data
  article = Article.objects.get(id=id)
  serializer = ArticleSerializer(instance=article, data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def deleteArticle(request, id):
  article = Article.objects.get(id=id)
  article.delete()
  return Response('Article deleted')

#Approve articles
@api_view(['PUT'])
def approveArticle(request, id):
  article = Article.objects.get(id=id)
  article.approved = True
  approved_article = article.save()
  serializer = ArticleSerializer(article, many=False)
  return Response({
    'approved_article':serializer.data
  })



  




