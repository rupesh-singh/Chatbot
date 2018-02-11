from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sys 
sys.path.append('/home/rupesh/Desktop/tensor')

#from response import response,bow,classify,clean_up_sentence

#response();

def index(request):
	template = loader.get_template('chatwindow/index.html')
	return HttpResponse(template.render({},request))




# Create your views here.
