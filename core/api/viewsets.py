from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontosTuristico.objects.filter(aprovado=True)
