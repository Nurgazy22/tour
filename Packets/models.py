from django.db import models
# from Reviews.models import Rating, Comment





class Packet(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='packets') #change to category(7 seasons)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/packet_image/')  #Imagefield correct
    price = models.IntegerField() # цена
    description = models.TextField() # описание
    date_start = models.DateTimeField() # начало
    date_end = models.DateTimeField() # конец 
    availability = models.IntegerField() # cвободные места
    # packets_rating = models.ForeignKey('Reviews.Rating', on_delete=models.CASCADE, related_name='packetrating') #рейтинг
    # packets_comments = models.ForeignKey('Reviews.Comment', on_delete=models.CASCADE, related_name='packets') # комменты
    in_stock = models.BooleanField() # в наличии
    quantity = models.IntegerField()  # общее кол-во
    schedule = models.FileField()  #план тура

    def __str__(self):
        return f"{self.title}, {self.category}" 


class Category(models.Model):
    name = models.CharField(max_length=200)

    

class PacketImage(models.Model):
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/packet_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    udated_at = models.DateTimeField(auto_now=True)

    
class Hotel(models.Model):
    title = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    hotels_rating = models.IntegerField()
    season = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title}, {self.country}" 



    
