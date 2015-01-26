from django.db import models

# Create your models here.
class Finances(models.Model):
	ccode = models.IntegerField(primary_key=True)
	market_cap = models.FloatField()
	shares_issued = models.FloatField()
	dividend_yield = models.FloatField()
	dividend_one = models.FloatField()
	per = models.FloatField()
	pbr = models.FloatField()
	eps = models.FloatField()
	bps = models.FloatField()
	price_min = models.FloatField()
	round_lot = models.FloatField()
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'finances'
