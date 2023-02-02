from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#null=True rakhyo vane naam navako data halyo vane error nadekhauna 
class Customer(models.Model):
	#user can have one costomer and one customer have one user
	#blank=True we can add a customer without a user attached to it
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #one to one relationship
	name = models.CharField(max_length=200, null=True) # CASCADE le chai user delete vayo vane customer sangako relation delete garxa
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)
#one to many relationships
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL) #customer delete vayo vane pani order chai db bata delete nahos
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL) #every time manually type garna naparos vanera
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product



	