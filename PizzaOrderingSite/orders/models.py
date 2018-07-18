from django.db import models
from django.conf import settings


# Create your models here.

User = settings.AUTH_USER_MODEL

class Size(models.Model):
	size = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.size}"

class Type(models.Model):
	pizza_type = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.pizza_type}"


class Pizza(models.Model):
	pizza = models.ForeignKey(Type, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	toppings = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=6,decimal_places=2,default=0)

	def __str__(self):

		if self.toppings == 0:
			return f"{self.pizza} with Cheese ({self.size})"
		else:
			return f"{self.pizza} with {self.toppings} toppings ({self.size})"

	


class Topping(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return f"{self.name}"


# class Order(models.Model):
# 	user = models.ForeignKey(User,on_delete=models.CASCADE, default=0)
# 	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
# 	toppings = models.ManyToManyField(Topping, blank = True)
# 	subtotal = models.DecimalField(default = 0.00, max_digits= 12, decimal_places=2)
# 	updated = models.DateTimeField(auto_now =True)
    # timestamp = models.DateTimeField(auto_now_add  = True)
    # objects  = CartManager()
	




class OrderManager(models.Manager):
    def get_or_new(self,request):
        new_obj = True
        cart_obj = Order.objects.create(user = request.user)
        request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order = models.ManyToManyField(Pizza, blank= True, null=True)
    name = models.CharField(max_length=128,default=0)
    toppings = models.ManyToManyField(Topping, blank= True, null=True)
    # topping_name = models.CharField(max_length=128,blank = True)
    subtotal = models.DecimalField(default = 0.00, max_digits= 12, decimal_places=2)
    # pizza_id = models.IntegerField(default=0)
    
    objects  = OrderManager()

    def __str__(self):
        return f"{self.name}"







	


	
