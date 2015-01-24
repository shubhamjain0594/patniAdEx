from django.forms import widgets
from rest_framework import serializers
from rest_framework import validators
from patient.models import Patient, PatientDetails

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ('id','username','password')

class PatientDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientDetails
		fields = ('id','ip','url')