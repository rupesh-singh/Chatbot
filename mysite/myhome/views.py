from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import intent, answers, questions

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
	#fill();
	return HttpResponse(xa[20:])

'''
import json


def fill():
	with open('/home/rupesh/Desktop/project/mysite/myhome/int.json') as data_file:
		data = json.load(data_file)
	for  i in data['intents']:
		#a=intent(intent_name=i['tag'])
		#a.save();
		for j in i['patterns']:
			p = intent.objects.get(intent_name=i['tag'])
			a=questions(intent_id=p,questions=j)
			a.save()
			
		for j in i['responses']:
			p = intent.objects.get(intent_name=i['tag'])
			a=answers(intent_id=p,answer=j)
			a.save()



'''