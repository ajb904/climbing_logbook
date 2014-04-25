from django.shortcuts import render, get_object_or_404
from logbook.models import Log_entry, Route
from django.http import HttpResponse


def homepage(request):
	
	latest = Log_entry.objects.select_related().all()
	
	return render(request, 'home.html', {'latest': latest})
	

def my_image(request):
    image_data = open("/home/ali/Documents/Django/climbing/climbing/staticfiles/images/allExp.png", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")
    
def about(request):
	return render(request, 'about.html')
	

