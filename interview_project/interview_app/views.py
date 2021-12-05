from django.shortcuts import render
from django.http import HttpResponse
from .models import PhysicalPort
# Create your views here.

def physicalport(request, physicalport_id):
    return HttpResponse(PhysicalPort.objects.get(id=physicalport_id))

def users(request, physicalport_id):
    return HttpResponse(PhysicalPort.objects.get(id=physicalport_id).user_set.all())