from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from account.models import Images, User
from .serializers import ImagesSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets


class ImagesViewSet(CreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

 #ddfdfd

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
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = [
        '^serial',
        '^tel',
        '^full_name'

    ]
    filterset_fields = {
        'date': ['gte', 'exact', 'lte']
    }

    # def get_queryset(self):
    #     if self.request.method == 'GET':
    #         queryset = User.objects.all()
    #         type = self.request.GET.get('obj', None)
    #         print("type:"+type)
    #         return queryset


class DeleteAccount(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        serial = self.request.GET.get('obj', None)
        user = User.objects.get(serial=serial)
        user.delete()

        return Response({status.HTTP_200_OK})
