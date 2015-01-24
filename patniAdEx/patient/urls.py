from django.conf.urls import url
from patient import views

urlpatterns = [
	url(r'^patient_login/$', views.patient_login),
	url(r'^patient_details/$', views.patient_details),
]