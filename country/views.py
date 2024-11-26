from django.http import JsonResponse
from .models import Country
from django.shortcuts import render

def search(request):
   query = request.GET.get('q', '').lower()
   countries = Country.objects.filter(name__icontains=query)
   country_names = [country.name for country in countries]
   return JsonResponse(country_names, safe=False)
    
def index(request):
    return render(request,'index.html')

