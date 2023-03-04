from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()


class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    offer = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['-date_added', 'offer']
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    def __str__(self):
        return self.user.username

def post_save_create_cart(sender, instance, created, *args, **kwargs):
    if created:
        Cart.objects.create(user=instance)

post_save.connect(post_save_create_cart, sender=User)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        cost = self.product.price*self.quantity
        return cost
    
    def __str__(self):
        return self.product.name


class ItemReviews(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.PositiveBigIntegerField(default=0)
    comment = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Item Review'
        verbose_name_plural = 'Item Reviews'

    def __str__(self):
        return self.item.name

    def get_review(self):
        return self.review

