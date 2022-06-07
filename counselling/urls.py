from django.urls import path, include
from knox import views as knox_views
from . import views


urlpatterns=[
    path('routes/', views.routes, name='routes'),
    path('client/register/', views.RegisterClient.as_view(), name='registerClient'),
    path('client/login/', views.ClientLogin.as_view(), name='clientLogin'),
    path('client/logout/', knox_views.LogoutView.as_view(), name='clientLogout'),
    path('client/logoutall/', knox_views.LogoutAllView.as_view(), name='clientlogoutall'),
    path('counsellor/register/', views.RegisterCounsellor.as_view(), name='registerCounsellor'),
    path('counsellor/login/', views.CounsellorLogin.as_view(), name='counsellorLogin'),
    path('counsellor/logout/', knox_views.LogoutView.as_view(), name='counsellorLogout'),
    path('counsellor/logoutall/', knox_views.LogoutAllView.as_view(), name='counsellorlogoutall'),
    path('clients/', views.getClients, name='getClients'),
    path('clients/detail/<int:id>/', views.getClientDetail, name='getClientDetail'),
    path('clients/delete/<int:id>/', views.deleteClient, name='deleteClient'),
    path('counsellors/', views.getCounsellors, name='getCounsellors'),
    path('counsellors/detail/<int:id>/', views.getCounsellorDetail, name='getCounsellorDetail'),
    path('counsellors/delete/<int:id>/', views.deleteCounsellor, name='deleteCounsellor'),
    path('client/changePassword/', views.ChangePassword.as_view(),name='changePassword'),
    path('client/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('counsellor/changePassword/', views.ChangeCounsellorPassword.as_view(),name='changeCounsellorPassword'),

]