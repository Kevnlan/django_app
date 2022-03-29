from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # buildings = Building.objects.filter(owner=request.user)
    # tenants = Profile.objects.filter(is_tenant=True)

    # context = {
    #     "buildings" : buildings,
    #     "tenants" : tenants,
    # }
    return render(request, 'index.html')