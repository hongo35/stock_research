#from django.http import HttpResponse
from django.shortcuts import render_to_response

from stock_research.price.models import Price

def index(request):
	prices = Price.objects.all()[:5]
	context = {'prices': prices}
	return render_to_response('price/index.html', context)

def detail(request, ccode):
	return HttpResponse("You're looking at price %s." % ccode)
