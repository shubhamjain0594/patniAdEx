import datetime

from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# defining a save method and thus it validates the data before saving it
class ValidateOnSaveMixin(object):
	def save(self, force_insert = False, force_update = False, **kwargs):
		if not force_insert or force_update:
			self.full_clean()
		super(ValidateOnSaveMixin, self).save(force_insert,force_update,**kwargs)

# Create your models here.
class Patient(ValidateOnSaveMixin, models.Model):
	username = models.CharField(unique=True,max_length=50) # username of patient to login 
	password = models.CharField(max_length=50, blank=False) # password currently saved as it is without any encoding

	def check_password(self, password):
		return self.password == password

	def clean(self):
		from django.core.exceptions import ValidationError
		if self.username.strip() == '':
			raise ValidationError('Empty username error')
		if self.password.strip() == '':
			raise ValidationError('Empty password error')

	class Meta:
		ordering = ['username']
	# validator that determines the uniqueness of username

class PatientDetails(ValidateOnSaveMixin, models.Model):
	ip = models.GenericIPAddressField() # patient to which this configuration belongs
	url = models.URLField() # cough for which the ad is defined
	class Meta:
		ordering = ['ip']