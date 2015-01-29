# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from stock_research.article.models import Article
import requests
import datetime
from bs4 import BeautifulSoup

class Command(BaseCommand):
	help = "[Description] Here is help..."

	def handle(self,*args, **options):
		res = requests.get("http://news.yahoo.co.jp/hl?c=biz")
		soup = BeautifulSoup(res.text)

		news_list = soup.find("ul", class_="listBd").find_all("li")
		for li in news_list:
			news = li.find("p", class_="ttl").find("a")
			
			subject = news.text
			url     = news.get("href")
			news_id = url.split("a=")[1]
			source  = li.find("p", class_="source").find("span", class_="cp").text
			ts      = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

			try:
				Article.objects.create(
					id         = news_id,
					subject    = subject,
					url        = url,
					source     = source,
					created_at = ts,
					updated_at = ts
				)
			except:
				pass

