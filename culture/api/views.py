from rest_framework import viewsets
from api.models import Theatre
from api.serializers import TheatreSerializer


class TheatreViewSet(viewsets.ModelViewSet):
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


class SearchView(APIView):
    def get(self, request):
        query_param = request.query_params.get('search', None)
        if query_param:
            results = Theatre.objects.filter(name__icontains=query_param)
            serializer = TheatreSerializer(results, many=True)
            return Response(serializer.data)
        else:
            return Response("Поисковый запрос не был задан", status=400)
