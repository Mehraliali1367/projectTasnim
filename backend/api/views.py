from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from account.models import Images, User
from .serializers import ImagesSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from django.http import JsonResponse
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import extensions.jalali as jalali
from kavenegar import *
from account.mixins import AdminAccessMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Images(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
    
    
    def perform_create(self, serializer):
        print('*'*100)
        print(self.request.POST.get('user'))
        try:
            serializer.save(user=User.objects.get(serial=self.request.POST.get('user')))
        except:
            return JsonResponse(status=401,data={"error":"not found user"})    
    
    # lookup_field=User.objects.get()
    # def get_queryset(self):
    #     # videoName = self.kwargs['videoName']
    #     serial=self.request.POST.get("user")o
    #     user=User.objects.get(serial=serial)
    #     print(user.first_name)
    #     return user

# class Images(APIView):
#     # queryset = Images.objects.all()
#     serializer_class = ImagesSerializer
#     def post(self,*args,**kwargs):
#         print('1'*100)
#         img=self.request.FILES["image"]
#         serial=self.request.POST.get("user")
#         if img and serial:
#             try:
#                 # code zir dar windows neveshteshode va bain format daste site miresad
#                 #   response = requests.post(url + url_post_image, data=data, files=files, headers=headers)
#                 print("2"*100)
#                 # user=User.objects.get(serial=serial)
#                 # data_ser={'user':user,'image':img}
#                 ImagesSerializer()
#                 print(user.first_name)
#                 obj=Images(user=user,image=img)
#                 print('3'*100)
#                 obj.save()
#                 print('4'*100)
#                 # print(self.request.data)
#                 # ImagesSerializer(user.id,data=self.request.data)
#                 return  JsonResponse(status=201,data={'serial':serial,'status':'true'})
#             except :
#                 return Response({"message": "Deal doesnt exist"},status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return  JsonResponse(status=501,data={'error':'سرور نتوانست تصویر را ذخیره کند شاید سریال تصویر درست نمی باشد'})

class UsersList(AdminAccessMixin,LoginRequiredMixin,ListAPIView):
    # filter_backends = (DynamicSearchFilter,)
    serializer_class = UserSerializer

    search_fields = [
        '^melli',
        '^serial',
        '^tel',
        '^first_name',
        '^last_name',
    ]

    def get_queryset(self, *args, **kwargs):
        try:
            req = self.request.GET.get("date", None)
            if req:
                date = date_register(req)
                if date:
                    convert_date = str(date).split('-')
                    if len(str(convert_date[1])) == 1:
                        convert_date[1] = "0" + convert_date[1]
                    if len(str(convert_date[2])) == 1:
                        convert_date[2] = "0" + convert_date[2]
                    d = str.format("{}-{}-{}", convert_date[0], convert_date[1], convert_date[2])
                    return User.objects.filter(date__startswith=d).order_by('-date')
                else:
                    return User.objects.all().order_by('-date')[:1000]
            else:
                search = self.request.GET.get("search", None)
                if search:
                    return User.objects.filter(is_admin=0).order_by('-date')
                else:
                    return User.objects.filter(is_admin=0).order_by('-date')[:1000]
        except:
            return User.objects.all().order_by('-date')[:1000]


def date_register(date):
    return jalali.Persian(date).gregorian_string()

class DeleteAccount(AdminAccessMixin,LoginRequiredMixin,RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        melli = self.request.GET.get('obj', None)
        user = User.objects.get(melli=melli)
        user.delete()

        return Response({status.HTTP_200_OK})

class CountUsers(LoginRequiredMixin,View):
    def get(self, request):
        count = User.objects.filter(is_admin=False).count()
        return JsonResponse({'users': count})

    def post(self):
        pass


class ListUsers(AdminAccessMixin,LoginRequiredMixin,ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_list = User.objects.filter(is_admin=False, ).order_by("-date")
        page = self.request.GET.get('obj', 1)
        paginator = Paginator(user_list, 200)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return users


class SendMessage(AdminAccessMixin,LoginRequiredMixin,View):
    def get(self):
        pass

    def post(self, request):
        description = (request.POST.get('arry_description')).split(',')
        arry = (request.POST.get('arry_tell')).split(',')
        sender = (request.POST.get('arry_sender')).split(',')
        print("t" * 100)
        # test=arry.split(',')
        print(arry)
        # print(test)
        print(description)
        print(sender)
        try:
            api = KavenegarAPI(
                '4C6A7A6F556F6A68766F444466794278494C3738383433727239755636732B4831786E2B7653516C376C493D')
            params = {
                'receptor': f'{arry}',
                'sender': f'{sender}',
                'message': f'{description}',
            }
            print("a" * 100)
            response = api.sms_sendarray(params)
            print(response)
            print("b" * 100)
            if response:
                print("#" * 100)
                print(response)
            return JsonResponse({"status": 'Success'})

        except Exception as e:
            print("c" * 100)
            print(e)
            return JsonResponse({"status": 'Error'})


# ddfdfd

#   '^' Starts-with search.
#   '=' Exact matches.
#  '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
#  '$' Regex search.

# filterset_fields = {
#     'start_date': ['gte', 'lte', 'exact', 'gt', 'lt'],
#     'id': ['exact'],
#     'event_name': ['exact'],
#     'start_time': ['exact'],
#     'end_date': ['exact'],
#     'end_time': ['exact'],
#     'age_max': ['gte', 'lte', 'exact', 'gt', 'lt'],
#     'age_min': ['gte', 'lte', 'exact', 'gt', 'lt'],
#     'event_organizer__name': ['exact'],
#     'event_type__name': ['exact'],
#     'event_city__name': ['exact'], 'event_tag__name': ['exact']
# }

# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         list = request.GET.getlist('search_fields', [])
#         return list
#
#         def date_register(date):
#             print("*" * 100)
#             return jalali.Persian(date).gregorian_string()
