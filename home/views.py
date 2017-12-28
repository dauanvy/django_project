# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from home.models import Location
from home.models import LocationForm
from home.models import Events
from home.models import EventsForm

def event_ft(request):
	data = {}
	list_item = Events.objects.all()
	data['list_item'] = list_item
	return render(request,'home/event_ft.html',data)
#Location
def location_bk(request):
	form = LocationForm(request.POST)
	data = {}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location_bk')
	else :
		form = LocationForm()
	list_item = Location.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'home/location_bk.html',data)
def location_bk_update(request, id):
	data = {}
	try:
		selected_item = Location.objects.get(pk=id)
		form = LocationForm(instance=selected_item)
	except Location.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = LocationForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location_bk')
	list_item = Location.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'home/location_bk.html',data)

def location_bk_remove(request, id):
	data = {}
	try:
		selected_item = Location.objects.get(pk=id)
		selected_item.delete()
		form = LocationForm()
	except Location.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Location.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/location_bk', data)
#Event
def event_bk(request):
	form = EventsForm(request.POST)
	data = {}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/event_bk')
	else :
		form = EventsForm()
	list_item = Events.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'home/event_bk.html',data)

def event_bk_update(request, id):
	data = {}
	try:
		selected_item = Events.objects.get(pk=id)
		form = EventsForm(instance=selected_item)
	except Events.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = EventsForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/event_bk')
	list_item = Events.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'home/event_bk.html',data)

def event_bk_remove(request, id):
	data = {}
	try:
		selected_item = Events.objects.get(pk=id)
		selected_item.delete()
		form = EventsForm()
	except Events.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Events.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/event_bk', data)
