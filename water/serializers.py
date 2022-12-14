from rest_framework.exceptions import *
from .models import *
from rest_framework.serializers import ModelSerializer


class SuvSerializer(ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'



class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HaydovchiSerializer(ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class BuyurtmaSerializer(ModelSerializer):
    # suv = SuvSerializer()
    # mijoz = MijozSerializer()
    class Meta:
        model = Buyurtma
        fields = '__all__'
