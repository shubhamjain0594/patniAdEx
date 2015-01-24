import decimal
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db.models import Q
from patient.models import Patient, PatientDetails
from patient.serializers import PatientSerializer, PatientDetailsSerializer
from advertiser.models import Advertiser, AdvertiserDetails
from advertiser.serializers import AdvertiserSerializer, AdvertiserDetailsSerializer

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[-1].strip()
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def patient_login(request):
	"""
	Login for patient
	"""	
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PatientSerializer(data=data)
		"""
		A return status for login which returns the response according to Status Code
		0 - Successful
		1 - Password Mismatch
		2 - Username does not exist
		3 - Bad Request
		"""
		username = ""
		if serializer.data.has_key('username') and serializer.data.has_key('password'):
			try:
				patient = Patient.objects.get(username=serializer.data['username'])
				if patient.check_password(password=serializer.data['password']):
					status = 0
					username=serializer.data['username']
				else:
					status = 1
			except Patient.DoesNotExist:
				status = 2
		else:
			status = 3
		data = {}
		data['username'] = username	
		if status==0:
			data['status'] = "success"
			data['message'] = "Successfully logged in."
			data['pk'] = patient.id
			return JSONResponse(data, status=201)
		elif status==1:
			data['status'] = "error"
			data['message'] = "Password does not match."
			return JSONResponse(data, status=201)
		elif status==2:
			data['status'] = "error"
			data['message'] = "Invalid Username"
			return JSONResponse(data, status=201)
		else:
			data['status'] = "error"
			data['message'] = "Bad Request"
			return JSONResponse(data, status=400)

@csrf_exempt
def patient_details(request):
	"""
	Change the cough of the patient
	"""
	if request.method == 'POST':
		data = JSONParser().parse(request)
		data["ip"] = get_client_ip(request)
		serializer = PatientDetailsSerializer(data=data)
		print(data)
		if serializer.is_valid():
			serializer.save()
			visits = PatientDetails.objects.filter(ip=data["ip"]).filter(url__contains='cough').count()
			total = PatientDetails.objects.filter(ip=data["ip"]).count()
			cough = int(decimal.Decimal(visits/total))
			bidWinner = AdvertiserDetails.objects.filter(Q(cough=-1)|Q(cough=cough)).order_by('-rates')[0]
			serializer = AdvertiserDetailsSerializer(bidWinner)
			return JSONResponse(serializer.data, status = 201)
		else:
			return JSONResponse(serializer.errors, status = 400)