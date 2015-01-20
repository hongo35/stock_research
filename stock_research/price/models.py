from django.db import models

# Create your models here.
class Price(models.Model):
	ccode      = models.IntegerField('ccode')
	date       = models.DateField()
	open       = models.DecimalField(max_digits=10, decimal_places=2)
	high       = models.DecimalField(max_digits=10, decimal_places=2)
	low        = models.DecimalField(max_digits=10, decimal_places=2)
	close      = models.DecimalField(max_digits=10, decimal_places=2)
	volume     = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		db_table = 'price'
