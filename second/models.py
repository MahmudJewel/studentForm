from django.db import models

# Create your models here.

class stform(models.Model):
	id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	sid=models.CharField(max_length=25, unique=True)
	name=models.CharField(max_length=50)
	DOB=models.DateField()
	gender=models.CharField(max_length=15)
	addess=models.TextField(max_length=100)
	zip_code=models.IntegerField()
		