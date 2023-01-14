from django.urls import path
from . import views

app_name = 'take_turns'
urlpatterns = [
    path('doctordifinit/', views.DoctorDifinit.as_view(), name='doctordifinit'),
    path('servicesdifinit/', views.ServicesDifinit.as_view(), name='servicesdifinit'),
    path('getdoctorapi/', views.GetDoctorApi.as_view(), name='getdoctorapi'),
    path('deletedoctor/', views.DeleteDoctor.as_view(), name='deletedoctor'),
    path('getdoctordateapi/', views.GetDoctorDateApi.as_view(), name='getdoctordateapi'),
    path('getserviceapi/', views.GetServiceApi.as_view(), name='getserviceapi'),
    path('presencedoctor/', views.PresenceDoctor.as_view(), name='presencedoctor'),
    path('gethourvisit/', views.GetHourVisitApi.as_view(), name='gethourvisitapi'),
    path('visit/', views.Visit.as_view(), name='visit'),
    path('getdoctors/', views.GetDoctors.as_view(), name='getdoctors'),
    path('searchـtakeـturns/', views.SearchTakeTurns.as_view(), name='searchـtakeـturns'),
    path('get_all_take_turns_api/', views.GetAllTakeTurns.as_view(), name='get_all_take_turns'),
    path('del_take_turns_api/', views.DeleteTakeTurns.as_view(), name='DeleteTakeTurns'),
]
