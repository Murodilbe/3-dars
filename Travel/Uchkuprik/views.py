from django.shortcuts import render
from django.forms import model_to_dict
from django.shortcuts import render
from .models import Travel, Class, Hotel
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import HotelSerializers, ClassSerializers, TravelSerializers


# Create your views here.
class TravelAPIView(APIView):

    def get(self, request: Request, pk=None) -> Response:
        if pk is None:
            return Response({'error': "Malumotlar topilmadi"})
        try:
            travels = Travel.objects.get(pk=pk)
            return Response({"travels": TravelSerializers(travels).data})
        except:
            return Response({'succes': "Malumotlar muvaffaqiyatli olindi"})

    def post(self, request: Request):

        serializer = TravelSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        travels = serializer.save()

        return Response({'travels': TravelSerializers(travels).data, 'message': "Sayohat haqida malumot qo'shildi!!!"})

    def put(self, request: Request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        try:
            travels = Travel.objects.get(pk=pk)
            serializer = TravelSerializers(travels, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_travels = serializer.save()
            return Response({'travels': TravelSerializers(updated_travels).data})
        except:
            return Response({'error': "Bu id da birorta chipta  mavjud emas"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            travels = Travel.objects.get(pk=pk)
            travels.delete()
            return Response({'success': "Sizning malumotlaringiz  o'chirildi"})
        except:
            return Response({'error': "Bu id da chipta mavjud emas"})


class HotelAPIView(APIView):

    def get(self, request: Request, pk=None) -> Response:
        if pk is None:
            return Response({'error': "Malumotlar topilmadi"})
        try:
            hotels = Hotel.objects.get(pk=pk)
            return Response({"hotels": HotelSerializers(hotels).data})
        except:
            return Response({'success': "Malumotlar muvaffaqiyatli olind"})


    def post(self, request: Request):

        serializer = HotelSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        hotels = serializer.save()

        return Response({'hotels':HotelSerializers(hotels).data, "message": "xona malumotlari muvaffaqiyatli saqlandi"})
    def put(self, request: Request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        try:
            hotels = Hotel.objects.get(pk=pk)
            serializer = HotelSerializers(hotels, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_hotels = serializer.save()
            return Response({'hotels': HotelSerializers(updated_hotels).data})
        except:
            return Response({'error': "Bu qavatda birorta xona  mavjud emas"})

    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            hotels = Hotel.objects.get(pk=pk)
            hotels.delete()
            return Response({'success': "Sizning malumotlaringiz  o'chirildi"})
        except:
            return Response({'error': "Bu id da chipta mavjud emas"})

class ClassAPIView(APIView):


    def delete(self, request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"DELETE\" not allowed."})
        try:
            klass = Class.objects.get(pk=pk)
            klass.delete()
            return Response({'success': "Sizning malumotlaringiz  o'chirildi"})
        except:
            return Response({'error': " mavjud emas"})

    def put(self, request: Request, pk=None):
        if pk is None:
            return Response({"detail": "Method \"PUT\" not allowed."})
        try:
            klass = Class.objects.get(pk=pk)
            serializer = ClassSerializers(klass, data=request.data)
            serializer.is_valid(raise_exception=True)
            updated_klass = serializer.save()
            return Response({'klass': ClassSerializers(updated_klass).data})
        except:
            return Response({'error': "mavjud emas"})

    def get(self, request:Request, pk=None) -> Response:
        if pk is None:
            return Response({'error': "Malumot yuq ekan"})
        try:
            klass = Class.objects.get(pk=pk)
            return Response({'klass': ClassSerializers(klass).data})
        except:
            return Response({'success': "Malumotlar muvaffaqiyalti olindi"})

    def post(self, request: Request):
        serializer = ClassSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        klass = serializer.save()
        return Response({'klass': ClassSerializers(klass).data, 'message': "Malumot saqlanid"})
