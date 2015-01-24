import logging
import json
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response

from stock_research.price.models import Price

logger = logging.getLogger(__name__)

def index(request):
	#data = {
	#	"hoge": "hoge"
	#}
	#json_str = json.dumps(data, ensure_ascii=False, indent=2)
	#return HttpResponse(json_str, content_type='application/json')
	prices = Price.objects.all()[:10]
	context = {'prices': prices}
	#json_r = serializers.serialize('json', json_str, ensure_ascii=False)
	return render_to_response('price/index.html', context)

def detail(request, ccode):
	return HttpResponse("You're looking at price %s." % ccode)
