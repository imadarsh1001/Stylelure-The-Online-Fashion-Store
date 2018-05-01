from decimal import Decimal
from django.db import models
from django.conf import settings
from Products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed
from colorfield.fields import ColorField

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)

    product_list=[]
    def item_list(self,id):        
        item_count = Cart.objects.filter(id=4).first().items.all().count()
        for i in range(item_count):
            product_list.append(Cart.objects.filter(id=4).first().items.all()[i].product_id)
        return product_list


class Cart(models.Model):
    user           = models.ForeignKey(User, null=True, blank=True)
    #products       = models.ManyToManyField(Product, blank=True)
    subtotal       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total          = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated        = models.DateTimeField(auto_now=True)
    created_date   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class CartItem(models.Model):
    product = models.ForeignKey(Product,related_name='products')
    cart = models.ForeignKey(Cart,related_name='items',null=True)
    selected_color = ColorField(default=None)
    quantity = models.PositiveIntegerField(default=1)
    selected_size  = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.product.discounted_price * self.quantity


# def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
#     if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
#         products = instance.products.all()
#         total = 0
#         for x in products:
#             total += x.price
#         if instance.subtotal != total:
#             instance.subtotal = total
#             instance.save()

# m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.08) 
    else:
        instance.total = 0.00

pre_save.connect(pre_save_cart_receiver, sender=Cart)
