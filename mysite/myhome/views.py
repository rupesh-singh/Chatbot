from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

import subprocess

@csrf_exempt
def index(request):
	input = request.POST.get('message1',None).encode('ascii','ignore')
	#print(input)
	st= str(input)
	newst=st.replace("'","")
	newst=newst.replace("b","");
	#print(newst)
	xa = subprocess.check_output(['python3', '/home/rupesh/Desktop/Web-django/mysite/myhome/response1.py', newst])
	#print(xa)
	return HttpResponse(xa[20:])
