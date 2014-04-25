from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from logbook.models import Route, Log_entry, Guidebook_area
from logbook.forms import NewRouteForm, NewLogForm, NewClimbForm

# Create your views here.

class LatestView(generic.ListView):
	template_name = 'logbook/home.html'
	context_object_name = 'latest'
	
	def get_queryset(self):
		'''
		return the latest 20 logbook entries
		'''
		return Log_entry.objects.order_by('-date_climbed')[:20]
		
class RouteView(generic.DetailView):
	model = Route
	template_name = 'logbook/route.html'
	
#class RouteEntryView(generic.DetailView):
#	model = Route
#	template_name = 'logbook/route_entry.html'

def new_route(request):
	form = NewRouteForm()
	
	return render(request, 'logbook/route_entry.html', {'form': form})
	
def log_climb(request):
	form = NewLogForm()
	
	return render(request, 'logbook/log_entry.html', {'form': form})
	
def new_route_and_climb(request):

	if request.method == 'POST':
		form = NewClimbForm(request.POST)
		if form.is_valid():
			### do stuff ###
			return HttpResponseRedirect('/logbook/thanks/')
	else:
		form = NewClimbForm()
	
	return render(request, 'logbook/route_entry.html', {'form': form})

def new_route_at_crag(request, crag_id):

	if request.method == 'POST':
		form = NewClimbForm(request.POST)
		if form.is_valid():
			### do stuff ###
			return HttpResponseRedirect('/logbook/thanks/')
	else:
		form = NewClimbForm()
	
	return render(request, 'logbook/route_entry.html', {'form': form})


def thanks(request):
	return render(request, 'logbook/thanks.html')

#def choose_crag(request)@:

class CragView(generic.ListView):
	template_name = 'logbook/choose_crag.html'
	context_object_name = 'areas'
	
	def get_queryset(self):

		return Guidebook_area.objects.order_by('country')
	
