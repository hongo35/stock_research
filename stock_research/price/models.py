from django.db import models

# Create your models here.
class Price(models.Model):
	ccode      = models.IntegerField(primary_key=True)
	date       = models.DateField(primary_key=True)
	#open       = models.FloatField()
	#high       = models.FloatField()
	#low        = models.FloatField()
	#close      = models.FloatField()
	#volume     = models.FloatField()
	#created_at = models.DateTimeField()
	#updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'prices'
