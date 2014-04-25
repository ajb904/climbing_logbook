from django.db import models

# Create your models here.

class Guidebook_area(models.Model):
	country = models.CharField(max_length=30)
	region = models.CharField(max_length=30)
	area = models.CharField(max_length=30)
	
	def __unicode__(self):
		return '%s, %s, %s' % (self.area, self.region, self.country)

class Rock_type(models.Model):
	rock_type = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.rock_type

class Crag(models.Model):
	name = models.CharField(max_length=50)
	area = models.ForeignKey(Guidebook_area)
	rock_type = models.ForeignKey(Rock_type)
	
	def __unicode__(self):
		return self.name

class Sector(models.Model):
	name = models.CharField(max_length=50)
	crag = models.ForeignKey(Crag)

	def __unicode__(self):
		return self.name

class Grade_system(models.Model):
	system = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.system

class Route(models.Model):
	route_name = models.CharField(max_length=100)
	sector = models.ForeignKey(Sector)
	num_pitches = models.IntegerField()
	system = models.CharField(max_length=10,
								choices = ( ('Fr', 'french'),
											('UK', 'UK trad'),
											('UIAA', 'UIAA'),
											('Alp', 'Alpine'),
											) )
	grade = models.CharField(max_length=10)
	pitch_grades = models.CharField(max_length=20, blank=True)
	notes = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.route_name

class Partner(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	gender = models.CharField(max_length=1, choices=( ('M','male'),('F','female')))
	
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class Log_entry(models.Model):
	date_climbed = models.DateField()
	route_name = models.ForeignKey(Route)
	partner = models.ManyToManyField(Partner)
	rope_end = models.CharField(max_length=10, 
								choices = ( ('L', 'lead'),
											('S', 'second'),
											('TR', 'toprope'),
											('ALT', 'alternate leads'),
											('UNK', 'other'),
											) )
	style = models.CharField(max_length=10,
								choices = ( ('OS','onsight'),
											('FL','flash'),
											('RP','redpoint'),
											('DOG','dog'),
											('DNF','backed off'),
											('GU','ground up'),
											) )
	notes = models.CharField(max_length=500)
	
	def __unicode__(self):
		return str(self.date_climbed)
