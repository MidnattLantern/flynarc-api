from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAuthentication
from .serializers import UserAuthenticationSerializer


class UserAuthenticationList(APIView):
    """ List view for all the user authentications """
    def get(self, request):
        users = UserAuthentication.objects.all()
        serializer = UserAuthenticationSerializer(users, many=True)
        return Response(serializer.data)