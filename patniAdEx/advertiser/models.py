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
class Advertiser(ValidateOnSaveMixin, models.Model):
	username = models.CharField(unique=True,max_length=50) # username of buyer to login 
	password = models.CharField(max_length=50, blank=False) # password currently saved as it is without any encoding

	def check_password(self, password):
		return self.password == password

	class Meta:
		ordering = ['username']
	# validator that determines the uniqueness of username
	def clean(self):
		from django.core.exceptions import ValidationError
		if self.username.strip() == '':
			raise ValidationError('Empty username error')
		if self.password.strip() == '':
			raise ValidationError('Empty password error')

class AdvertiserDetails(ValidateOnSaveMixin,
	models.Model):
	advertiser = models.ForeignKey(Advertiser) # advertiser to which this configuration belongs
	cough = models.IntegerField( # cough for which the ad is defined
		default = -1,
		validators = [
			MaxValueValidator(5),
			MinValueValidator(-1),
		],
	)
	rates = models.DecimalField( # rate of the ad
		default = 1,
		max_digits = 10,
		decimal_places = 2,
	)
	total_displays = models.IntegerField( # total number of times the ad has been displayed till now
		default = 0,
		validators = [
			MinValueValidator(0),
		]
	)
	advertise_url = models.URLField() # url of the ad to be displayed

	class Meta:
		unique_together = (('advertiser','cough'))
		ordering = ['advertiser']