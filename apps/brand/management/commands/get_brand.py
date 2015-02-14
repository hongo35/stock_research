# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from brand.models import Brand

import jsm
import datetime

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self, *args, **options):
		q = jsm.Quotes()

		# Brandの取得
		brand = jsm.Brand()
		ids   = brand.IDS

		for industory_code in ids.keys():
			industory_name = ids[industory_code]
			brand_data = q.get_brand(industory_code)

			for data in brand_data:
				ts = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

				Brand(
					ccode = data.ccode,
					industory_code = industory_code,
					industory_name = industory_name,
					market = data.market,
					name = data.name,
					info = data.info,
					created_at = ts,
					updated_at = ts
				)
				Brand.save()
