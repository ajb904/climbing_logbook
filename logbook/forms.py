from django import forms

from logbook.models import Sector, Route, Partner, Guidebook_area

class NewRouteForm(forms.Form):
	route_name = forms.CharField(max_length=100)
	sector = forms.ModelChoiceField(queryset=Sector.objects.all())
	num_pitches = forms.IntegerField()
	system = forms.ChoiceField(choices = ( ('Fr', 'french'),
											('UK', 'UK trad'),
											('UIAA', 'UIAA'),
											('Alp', 'Alpine'),
											) )
	grade = forms.CharField(max_length=10)
	notes = forms.CharField(max_length=100)
	
class NewLogForm(forms.Form):
	date_climbed = forms.DateField()
	route_name = forms.ModelChoiceField(queryset=Route.objects.all())
	partner = forms.ModelMultipleChoiceField(queryset=Partner.objects.all())
	
class NewClimbForm(forms.Form):
	route_name = forms.CharField(max_length=100)
	sector = forms.ModelChoiceField(queryset=Sector.objects.all())
	num_pitches = forms.IntegerField()
	system = forms.ChoiceField(choices = ( ('Fr', 'french'),
											('UK', 'UK trad'),
											('UIAA', 'UIAA'),
											('Alp', 'Alpine'),
											) )
	grade = forms.CharField(max_length=10)
	notes = forms.CharField(max_length=100)
	date_climbed = forms.DateField()
	partner = forms.ModelMultipleChoiceField(queryset=Partner.objects.all())

