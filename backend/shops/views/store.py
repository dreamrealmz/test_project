from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Store


class StoresApiView(APIView):
    authentication_classes = []

    def get(self, request, phone_number):
        if request.method == 'GET':
            return Response(
                {
                    'stores': Store.objects.filter(employee__phone_number=phone_number).values('pk', 'name')
                },
                status=status.HTTP_200_OK
            )
