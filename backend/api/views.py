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


class Images(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


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

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        list = request.GET.getlist('search_fields', [])
        return list

        def date_register(date):
            print("*" * 100)
            return jalali.Persian(date).gregorian_string()


class UsersList(ListAPIView):
    # filter_backends = (DynamicSearchFilter,)
    serializer_class = UserSerializer

    search_fields = [
        '^serial',
        '^tel',
        '^full_name',

    ]

    def get_queryset(self):
        try:
            date = date_register(self.request.GET.get("date"))
            print(date)
            if date:
                convert_date = str(date).split('-')
                if len(str(convert_date[1])) == 1:
                    convert_date[1] = "0" + convert_date[1]
                if len(str(convert_date[2])) == 1:
                    convert_date[2] = "0" + convert_date[2]
                d = str.format("{}-{}-{}", convert_date[0], convert_date[1], convert_date[2])
                return User.objects.filter(date__startswith=d)
            else:
                return User.objects.all()
        except:
            print("error in return request Search")
            return User.objects.all()


def date_register(date):
    return jalali.Persian(date).gregorian_string()


# queryset = User.objects.all().order_by("-date")[:500]
# queryset = User.objects.all()
# serializer_class = UserSerializer
# search_fields = [
#     '^serial',
#     '^tel',
#     '^full_name',
#     '^date'
# ]
# filterset_fields = {
#     'date': ['lte', ]
# }


class DeleteAccount(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        serial = self.request.GET.get('obj', None)
        user = User.objects.get(serial=serial)
        user.delete()

        return Response({status.HTTP_200_OK})


class CountUsers(View):
    def get(self, request):
        count = User.objects.filter(is_admin=False).count()
        return JsonResponse({'users': count})

    def post(self):
        pass


class ListUsers(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user_list = User.objects.filter(is_admin=False, ).order_by("-date")
        page = self.request.GET.get('obj', 1)
        paginator = Paginator(user_list, 99)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return users
