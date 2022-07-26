from django.urls import path, include
from . import views
from rest_framework import routers

# from rest_framework import routers

app_name = "api"

# router = routers.SimpleRouter()
# router.register('', views.ImagesViewSet)

router = routers.SimpleRouter()
router.register('users', views.UsersViewSet, basename="users")

urlpatterns = [
    path('', include(router.urls)),
    path('t/', views.ImagesViewSet.as_view()),
    path('userdelete/', views.DeleteAccount.as_view()),

]
