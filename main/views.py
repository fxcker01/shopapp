from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from .serializers import ItemSerializer, OrderSerializer
from .models import Item
from django.views.generic import TemplateView


class FrontendAppView(TemplateView):
    template_name = "index.html"


class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})
        return Response(serializer.data)


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all().order_by('-id')
    serializer_class = ItemSerializer

class OrderAdd(APIView):
    def post(self, request):
        print("Отримано запит:", request.data)  # Логування

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': 'Замовлення успішно оформлене!'}, status=status.HTTP_201_CREATED)

        print("Помилка валідації:", serializer.errors)
        return Response({'result': 'Помилка в формі', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


