import logging
import json
import datetime
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response

from stock_research.price.models import Price

logger = logging.getLogger('application')

def index(request):
	#data = {
	#	"hoge": "hoge"
	#}
	#json_str = json.dumps(data, ensure_ascii=False, indent=2)
	#return HttpResponse(json_str, content_type='application/json')
	res = []
	
	prices = Price.objects.all()[:10]
	for p in prices:
		content = {
			'ccode': p.ccode,
		}

		res.append(content)
	#context = {'prices': prices}
	#json_r = serializers.serialize('json', json_str, ensure_ascii=False)
	#return render_to_response('price/index.html', context)
	json_str = json.dumps(res, ensure_ascii=False, indent=2)
	return HttpResponse(json_str, content_type='application/json')

def detail(request, ccode):
	res = []

	prices = Price.objects.filter(ccode = ccode)
	for p in prices:
		content = {
			'ccode': p.ccode,
			'date': p.date.strftime("%Y-%m-%d"),
			'open': p.open,
			'high': p.high,
			'low': p.low,
			'close': p.close,
			'volume': p.volume,
			'created_at': p.created_at.strftime("%Y-%m-%d %H:%M:%S"),
			'updated_at': p.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
		}
		res.append(content)

	json_str = json.dumps(res, ensure_ascii=False, indent=2)
	return HttpResponse(json_str, content_type='application/json')
