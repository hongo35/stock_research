# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stock_research.price.models import Price
from stock_research.brand.models import Brand
import jsm
import datetime

class Command(BaseCommand):
	# args, help変数はヘルプメッセージを出力した時に使われる
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		q = jsm.Quotes()

		dt = datetime.date
		start_date = dt.today() - datetime.timedelta(days = 2)
		end_date   = dt.today() - datetime.timedelta(days = 1)

		brands = Brand.objects.select_related("ccode")
		for b in brands:
			data = q.get_historical_prices(b.ccode, jsm.DAILY, start_date = start_date, end_date = end_date)
			ts = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S+09:00")
			
			for d in data:
				try:
					p = Price.objects.create(
						ccode = b.ccode,
						date = d.date,
						open = d.open,
						high = d.high,
						low = d.low,
						close = d.close,
						volume = d.volume,
						created_at = ts,
						updated_at = ts
					)
					#p.save(force_insert=True)
				except:
					pass
