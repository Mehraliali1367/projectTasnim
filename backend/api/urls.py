from django.urls import path
from . import views
from rest_framework import routers

# from rest_framework import routers

app_name = "api"

# router = routers.SimpleRouter()
# router.register('', views.ImagesViewSet)

# router = routers.SimpleRouter()
# router.register('users', views.UsersViewSet, basename="users")

urlpatterns = [
    # path('', include(router.urls)),
    path('img/', views.Images.as_view()),
    path('userdelete/', views.DeleteAccount.as_view()),
    path('users/', views.UsersList.as_view()),
    path('countusers/', views.CountUsers.as_view()),
    path('ListUsers/', views.ListUsers.as_view()),
    path('sendmessage/', views.SendMessage.as_view()),

]
