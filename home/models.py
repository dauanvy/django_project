from django.db import models
from django import forms
from datetime import date
from django.template.defaultfilters import slugify
#Event
#python3 manage.py migrate --fake home zero
class Category(models.Model):
	name = models.CharField(max_length=30)
	class Meta:
		db_table = "categorys"
		ordering = ['-id']
	def __str__(self):
		return "%s" % (self.name)
		
class CategoryForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	class Meta:
		model = Category
		fields = ['name']

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
	phone = models.CharField(max_length=256, default='')
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)
	slug = models.SlugField(default='')
	class Meta:
		db_table = "events"
		ordering = ['-id']
	def __unicode__(self):
		return '%s-%s' % (self.name,self.city)
	def get_absolute_url(self):
		return "/%s/" % (self.slug)
	def save(self):
		self.slug = slugify(self.name)
		super(Events,self).save()
		
	# def _get_name2(self):
		# "Returns the person's name2."
		# return self.name
	# name2 = property(_get_name2)
	
class EventsForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	organizer = forms.CharField(label='Organizer', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))	
	phone = forms.CharField(label='Phone', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	start_date = forms.DateField(label='Start Date', input_formats = [ '%Y-%m-%d' ], required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	end_date = forms.DateField(label='End Date', input_formats = [ '%Y-%m-%d' ], required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="----------")
	category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="----------")
	class Meta:
		model = Events
		fields = ['name', 'phone', 'location','organizer','category', 'start_date', 'end_date']
