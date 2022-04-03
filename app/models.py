from django.db import models

# Create your models here.

CHOICES = (
	("1", "Available"),
	("2", "Not Available")
)

class Brand(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name

class Product(models.Model):
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=10)
	quantity = models.IntegerField()
	rate = models.FloatField(max_length=100)
	status = models.CharField(max_length=10, choices=CHOICES)

	def __str__(self):
		return self.name














