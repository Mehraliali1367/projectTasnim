from django.urls import path
from .views import QuizView,ErrorView,QuestionView

app_name = "suggestions"
urlpatterns = [
    path('quiz/',QuizView.as_view(), name='quiz'),
    path('create_question/',QuestionView.as_view(), name='question'),
    path('error/',ErrorView.as_view(), name='error')
]
