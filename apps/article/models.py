from django.db import models

# Create your models here
class Article(models.Model):
	id = models.CharField(primary_key=True, max_length=127)
	subject = models.CharField(max_length=255)
	url = models.CharField(max_length=1023)
	source = models.CharField(max_length=255)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'articles'
