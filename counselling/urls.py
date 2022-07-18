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

    path('clients/registerissue/', views.RegisterClientIssue.as_view(), name='registerClientIssue'),


    path('counsellors/', views.getCounsellors, name='getCounsellors'),
    path('counsellors/detail/<int:id>/', views.getCounsellorDetail, name='getCounsellorDetail'),
    path('counsellors/delete/<int:id>/', views.deleteCounsellor, name='deleteCounsellor'),
    path('client/changePassword/', views.ChangePassword.as_view(),name='changePassword'),
    path('client/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('counsellor/changePassword/', views.ChangeCounsellorPassword.as_view(),name='changeCounsellorPassword'),

    path('articles/', views.getArticles, name='getArticles'),
    path('articles/<int:id>/', views.getArticleDetails, name='getArticleDetails'),
    path('articles/upload/', views.UploadArticle.as_view(), name='uploadArticle'),
    path('articles/update/<int:id>/', views.updateArticle, name='updateArticle'),
    path('articles/delete/<int:id>/', views.deleteArticle, name='deleteArticle'),
    path('articles/approve/<int:id>/', views.approveArticle, name='articleApproved'),

    path('book-appointment/', views.BookAppointment.as_view(), name='book-appointment'),
    # path('bookappointment/<int:clientId>/', views.bookAppointment, name='bookappointment'),
    path('appointments/', views.getAppointments, name='getAppointments'),
    path('appointments/<int:id>/', views.appointmentDetail, name='appointmentDetail'),
    path('appointments/delete/<int:id>/', views.deleteAppointment, name='deleteAppointment'),
    path('appointments/counsellor/<int:id>/', views.counsellorAppointment, name='counsellorAppointment'),
    path('appointments/client/<int:id>/', views.clientAppointment, name='clientAppointments'),

    

]