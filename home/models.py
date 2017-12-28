from django.db import models
from django import forms
from datetime import date
from django.template.defaultfilters import slugify
#Event
#python3 manage.py migrate --fake home zero
class Location(models.Model):
	name = models.CharField(max_length=30)
	street = models.CharField(max_length=30,default='')
	city = models.CharField(max_length=30,default='')
	country = models.CharField(max_length=30,default='')
	class Meta:
		db_table = "locations"
		ordering = ['-id']
	def __str__(self):
		return "%s" % (self.name)
		
class LocationForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	street = forms.CharField(label='Street', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	city = forms.CharField(label='City', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	country = forms.CharField(label='Country', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	class Meta:
		model = Location
		fields = ['name', 'street', 'city', 'country']
		
class Events(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=256)
	organizer = models.CharField(max_length=256, default='')
	category = models.CharField(max_length=256, default='')
	location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
	start_date = models.DateTimeField( null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)
	slug = models.SlugField(default='')
	def __unicode__(self):
		return '%s' % self.name
	def get_absolute_url(self):
		return "/%s/" % (self.slug)
	def save(self):
		self.slug = slugify(self.name)
		super(Events,self).save()

	class Meta:
		db_table = "events"
		ordering = ['-id']
		
class EventsForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	organizer = forms.CharField(label='Organizer', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	category = forms.CharField(label='Category', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	start_date = forms.DateField(label='Start Date', input_formats = [ '%Y-%m-%d' ], required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	end_date = forms.DateField(label='End Date', input_formats = [ '%Y-%m-%d' ], required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="----------")
	class Meta:
		model = Events
		fields = ['name', 'location','organizer','category', 'start_date', 'end_date']