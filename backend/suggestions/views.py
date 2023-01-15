from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import QuesModel


class QuestionView(LoginRequiredMixin, View):
    template_name = 'suggestions/quiz.html'

    def post(self, request):
        if request.method == 'POST':
            try:
                questions = QuesModel.objects.all()

                for q in questions:
                    if request.POST.get(q.question) == 'ans_op1':
                        q.ans_op1 = q.ans_op1+1
                    if request.POST.get(q.question) == 'ans_op2':
                        q.ans_op2 = q.ans_op2+1
                    if request.POST.get(q.question) == 'ans_op3':
                        q.ans_op3 = q.ans_op3+1
                    if request.POST.get(q.question) == 'ans_op4':
                        q.ans_op4 = q.ans_op4+1

                    q.save()
                return render(request, 'suggestions/result.html')
            except:
                return render(request, 'suggestions/error.html')

    def get(self, request):
        questions = QuesModel.objects.all()
        return render(request, self.template_name, {'questions': questions})


# https://data-flair.training/blogs/create-quiz-application-python-django/#google_vignette

# from django.shortcuts import redirect,render
# from django.contrib.auth import login,logout,authenticate
# from .forms import *
# from .models import *
# from django.http import HttpResponse

# # Create your views here.
# def home(request):
#     if request.method == 'POST':
#         print(request.POST)
#         questions=QuesModel.objects.all()
#         score=0
#         wrong=0
#         correct=0
#         total=0
#         for q in questions:
#             total+=1
#             print(request.POST.get(q.question))
#             print(q.ans)
#             print()
#             if q.ans ==  request.POST.get(q.question):
#                 score+=10
#                 correct+=1
#             else:
#                 wrong+=1
#         percent = score/(total*10) *100
#         context = {
#             'score':score,
#             'time': request.POST.get('timer'),
#             'correct':correct,
#             'wrong':wrong,
#             'percent':percent,
#             'total':total
#         }
#         return render(request,'Quiz/result.html',context)
#     else:
#         questions=QuesModel.objects.all()
#         context = {
#             'questions':questions
#         }
#         return render(request,'Quiz/home.html',context)

# def addQuestion(request):
#     if request.user.is_staff:
#         form=addQuestionform()
#         if(request.method=='POST'):
#             form=addQuestionform(request.POST)
#             if(form.is_valid()):
#                 form.save()
#                 return redirect('/')
#         context={'form':form}
#         return render(request,'Quiz/addQuestion.html',context)
#     else:
#         return redirect('home')

# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = createuserform()
#         if request.method=='POST':
#             form = createuserform(request.POST)
#             if form.is_valid() :
#                 user=form.save()
#                 return redirect('login')
#         context={
#             'form':form,
#         }
#         return render(request,'Quiz/register.html',context)

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#        if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/')
#        context={}
#        return render(request,'Quiz/login.html',context)

# def logoutPage(request):
#     logout(request)
#     return redirect('/')
