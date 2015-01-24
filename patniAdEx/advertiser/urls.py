from django.conf.urls import url
from advertiser import views

urlpatterns = [
	url(r'^advertiser/$', views.advertiser_list),
	url(r'^advertiser_details/(?P<pk>[0-9]+)/$', views.advertiser_details),
	url(r'^advertiser_bid/(?P<cough>[0-5]+)/$', views.advertiser_bid_winner),
	url(r'^advertiser_login/$', views.advertiser_login),
]