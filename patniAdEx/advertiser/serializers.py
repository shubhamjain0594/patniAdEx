from django.forms import widgets
from rest_framework import serializers
from rest_framework import validators
from advertiser.models import Advertiser, AdvertiserDetails

class AdvertiserSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	username = serializers.CharField(max_length=50, validators=[validators.UniqueValidator(queryset=Advertiser.objects.all(), message="An advertiser with same username already exists")]
	)
	password = serializers.CharField(max_length=50)

	def create(self, validated_data):
		"""
		Create and return a new advertiser given the validated data 
		"""
		return Advertiser.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing advertiser instance, given the validated data	
		"""
		instance.username = validated_data.get('name',instance.username)
		instance. password = validated_data.get('password', instance.password)
		instance.save()
		return instance	

class AdvertiserDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = AdvertiserDetails
		fields = ('id','advertiser','cough','rates','total_displays','advertise_url')