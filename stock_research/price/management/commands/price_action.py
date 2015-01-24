# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	# args, help変数はヘルプメッセージを出力した時に使われる
	help = "[Description]\nHere is help..."

	def handle(self, *args, **options):
		print "Test"
