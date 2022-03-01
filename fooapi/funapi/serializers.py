from rest_framework import serializers
from funapi import models



class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drink
        fields = ['title','description','time_posted']