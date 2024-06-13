from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from trails.models import Park
from trails.serliazers import ParkSerializer
from trails.utils import parse_cluster_info


class ClusterInfoNalichevoView(APIView):
    """Получение информации о парке Налычево"""

    def get(self, request):
        url = "https://www.vulcanikamchatki.ru/territoriya/klaster_nalychevskij/"
        parsed_data = parse_cluster_info(url)
        if parsed_data:
            park, created = Park.objects.get_or_create(
                title=parsed_data['title'],
                defaults={'description': parsed_data['description']}
            )
            serializer = ParkSerializer(park)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ошибка при получении данных'}, status=status.HTTP_400_BAD_REQUEST)


class ParkListView(APIView):
    """Вывод списка парков"""

    def get(self, request):
        parks = Park.objects.all()
        serializer = ParkSerializer(parks, many=True)
        return Response(serializer.data)
