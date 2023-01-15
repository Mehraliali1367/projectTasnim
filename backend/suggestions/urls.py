from django.urls import path
from .views import QuestionView

app_name = "suggestions"
urlpatterns = [
    path('',QuestionView.as_view(), name='Question')
]
