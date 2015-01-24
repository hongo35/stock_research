# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stock_research.price.models import Price
import jsm
import datetime

class Command(BaseCommand):
	# args, help変数はヘルプメッセージを出力した時に使われる
	help = "[Description]\nHere is help..."

	def handle(self, *args, **options):
		q = jsm.Quotes()

		prices = Price.objects.filter(ccode = 1301)
		print prices
