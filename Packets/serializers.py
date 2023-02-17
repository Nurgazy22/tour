from rest_framework import serializers
from .models import Packet, PacketImage, Category, Hotel


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'
    
    def validate_price(self, price):
        if price <=0:
            raise serializers.ValidationError(
                'price must be > 0'
            )
        return price
    

class PacketImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class HotelSerializer(serializers.ModelSerializer):

     class Meta:
        model = Hotel
        fields = '__all__'
