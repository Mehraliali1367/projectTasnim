from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogOut.as_view(), name='logout'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('edit/', views.Edit.as_view(), name='edit'),
    path('search/', views.Search.as_view(), name='search'),
    path('dashboard/<str:serial>/', views.Dashboard.as_view(), name='dashboard'),

]
