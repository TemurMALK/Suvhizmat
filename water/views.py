from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class SuvlarAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        suvlar = Suv.objects.all()
        serializer = SuvSerializer(suvlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"True", "data":serializer.data})
        return Response("xabar","False")

class SuvAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request,pk):
        suvlar = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suvlar)
        return Response(serializer.data)

    def put(self, request, pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv, data = request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "qoshilgan malumot": serializer.data}
            return Response(natija, status = status.HTTP_201_CREATED)
        return Response({"xabar":"Ma'lumotda xatolik bor!", "detail":serializer.errors}).objects

    def delete(self, reuqest, pk):
        suv = Suv.objects.get(id=pk)
        suv.delete()
        return Response({"xabar":"Ma'lumot o'chdi!"})

class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        mijoz = Mijoz.objects.all()
        serializer = MijozSerializer(mijoz, many=True)
        return Response(serializer.data)

    def post(self, request):
        mijoz = request.data
        serializer = MijozSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"True", "data":serializer.data})
        return Response("xabar","False")

class MijozAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)

    def put(self, request, pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz, data = request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "qoshilgan malumot": serializer.data}
            return Response(natija, status = status.HTTP_201_CREATED)
        return Response({"xabar":"Ma'lumotda xatolik bor!", "detail":serializer.errors}).objects

    def delete(self, reuqest, pk):
        mijoz = Mijoz.objects.get(id=pk)
        mijoz.delete()
        return Response({"xabar":"Ma'lumot o'chdi!"})




class BuyurtmalarAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        buyurtma = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data)

    def post(self, request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response({"xabar":"True", "data":serializer.data})
        return Response("xabar","False")

class BuyurtmaAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, pk):
        buyurtma = Buyurtma.objects.get(id=pk)
        serializer = BuyurtmaSerializer(buyurtma)
        return Response(serializer.data)

class HaydovchilarAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        haydovchi = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchi, many=True)
        return Response(serializer.data)

class HaydovchiAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)

class AdminlarAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class AdminAPIView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

