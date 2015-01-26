from django.db import models

# Create your models here.
class Brand(models.Model):
	ccode = models.IntegerField(primary_key=True)
	industory_code = models.IntegerField()
	industory_name = models.CharField(max_length=31)
	market = models.CharField(max_length=31)
	name = models.CharField(max_length=255)
	info = models.CharField(max_length=255)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'brands'
