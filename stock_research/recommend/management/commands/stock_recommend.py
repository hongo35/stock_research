# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stock_research.price.models import Price
from stock_research.brand.models import Brand
from stock_research.finance.models import Finance
import datetime

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		span = 30
		
		brands = Brand.objects.all()
		for b in brands:
			data = {
				'open': [],
				'high': [],
				'low': [],
				'close': []
			}

			prices = Price.objects.filter(ccode = b.ccode).order_by("date")
			for p in prices:
				data['open'].append(p.open)
				data['high'].append(p.high)
				data['low'].append(p.low)
				data['close'].append(p.close)

			highest      = 0
			lowest       = 0
			latest_close = 0
			try:
				highest      = max(data['high'][(len(data['high']) - span):])
				lowest       = min(data['low'][(len(data['low']) - span):])
				latest_close = data['close'][-1]
			except:
				pass

			if (highest - lowest) != 0:
				finance = Finance.objects.filter(ccode = b.ccode)

				wr    = (highest - latest_close) * 100 / (highest - lowest)
				per   = finance[0].per
				pbr   = finance[0].pbr
				price = finance[0].price_min
				
				# 条件
				if wr == 100 and per < 20 and price < 100000:
					print "%s,%s,%s,%s,%s,%s" % (b.ccode, b.name, per, pbr, price, latest_close)
