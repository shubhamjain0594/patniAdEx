from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.db.models import Q
from advertiser.models import Advertiser, AdvertiserDetails
from advertiser.serializers import AdvertiserSerializer, AdvertiserDetailsSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def advertiser_login(request):
	"""
	Login for advertiser
	"""	
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = AdvertiserSerializer(data=data)
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
				advertiser = Advertiser.objects.get(username=serializer.data['username'])
				if advertiser.check_password(password=serializer.data['password']):
					status = 0
					username=serializer.data['username']
				else:
					status = 1
			except Advertiser.DoesNotExist:
				status = 2
		else:
			status = 3
		data = {}
		data['username'] = username	
		if status==0:
			data['status'] = "success"
			data['message'] = "Successfully logged in."
			data['pk'] = advertiser.id
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
def advertiser_list(request):
	"""
	List all Advertiser
	"""
	if request.method == 'GET':
		advertiser = Advertiser.objects.all()
		serializer = AdvertiserSerializer(advertiser, many = True)
		return JSONResponse(serializer.data)

@csrf_exempt
def advertiser_details(request,pk):
	"""
	List all Advertiser
	"""	
	if request.method == 'GET':
		advertiserDetails = AdvertiserDetails.objects.filter(advertiser__id=pk)
		serializer = AdvertiserDetailsSerializer(advertiserDetails, many = True)
		return JSONResponse(serializer.data, status=201)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = AdvertiserDetailsSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)


def advertiser_bid_winner(request,cough):
	"""
	Gets the bidder with highest value amongst the ones with default and given cough value
	"""
	if request.method == 'GET':
		try:
			bidWinner = AdvertiserDetails.objects.filter(Q(cough=-1)|Q(cough=cough)).order_by('-rates')[0]
			serializer = AdvertiserDetailsSerializer(bidWinner)
			return JSONResponse(serializer.data, status=201)
		except IndexError:
			data = {}
			data['status'] = "failure"
			data['message'] = "No advertiser available"
			return JSONResponse(data, status=201)