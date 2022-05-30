from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Meet, Store
import logging
from datetime import datetime  # , timedelta

logger = logging.getLogger(__name__)


class MeetApiView(APIView):
    authentication_classes = []
    require_keys = ['pk', 'latitude', 'longitude']

    # не понимаю, зачем здесь нужен номер телефона, ну ладно

    def post(self, request, phone_number):
        if request.method == 'POST':
            data = request.data
            missed_keys = []

            for key in self.require_keys:
                if key not in data.keys():
                    missed_keys.append(key)

            if missed_keys:
                error_text = 'Нехватает ключей для формирования запроса, передай: ' + ', '.join(item for item in missed_keys)
                logger.error(error_text)
                return Response(
                    {
                        'error': error_text
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            store = Store.objects.filter(pk=data['pk']).first()
            if not store:
                error_text = f'Нет магазина с pk {data["pk"]}'
                logger.error(error_text)
                return Response(
                    {
                        'error': error_text
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif store.employee.phone_number != phone_number:
                error_text = f'{phone_number} некорректный'
                logger.error(error_text)
                return Response(
                    {
                        'error': error_text
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            meet_data = {
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'store': store,
                'date_of_meeting': datetime.now()  # + timedelta(hours=4)
            }

            instance = Meet.objects.create(**meet_data)

            logger.info(f'Создан инстанс "Посещение" {instance.pk}')

            return Response(
                {
                    'pk': instance.pk,
                    'datetime': instance.date_of_meeting,
                },
                status=status.HTTP_200_OK
            )
