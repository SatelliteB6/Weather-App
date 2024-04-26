from rest_framework import serializers
from .models import Weather, Forecast

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

    def create(self, validated_data):
        return Weather.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.temperature = validated_data.get('temperature', instance.temperature)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.wind_speed = validated_data.get('wind_speed', instance.wind_speed)
        instance.description = validated_data.get('description', instance.description)
        instance.date_time = validated_data.get('date_time', instance.date_time)
        instance.save()
        return instance

class ForecastSerializer(serializers.Serializer):
    city_name = serializers.CharField(source='city.name')
    date = serializers.DateField()
    min_temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
    max_temperature = serializers.DecimalField(max_digits=5, decimal_places=2)
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Forecast.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.min_temperature = validated_data.get('min_temperature', instance.min_temperature)
        instance.max_temperature = validated_data.get('max_temperature', instance.max_temperature)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class WeatherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class ForecastModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = ['city', 'date', 'min_temperature', 'max_temperature', 'description']
