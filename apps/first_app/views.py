from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
	try:
		request.session['time'] 
	except:
		request.session['time'] = 0
	return render(request,'first_app/index.html')
def generate(request):
	if request.method == "POST":
		print "*"*50
		request.session['time'] += 1
		request.session['string'] = get_random_string(length=14)

		return redirect('/')
def startover(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		request.session['time'] = 0

		return redirect('/')
