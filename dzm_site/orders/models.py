from django.db import models
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Status name:%s' %self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Order(models.Model):
    total_amount = models.DecimalField(decimal_places=2, max_digits=15, default=0) #total price for all products
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=256, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return 'Order id:%s %s' %(self.id, self.customer_name)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ProductInOrder(models.Model):
    num_order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, blank=True, null=True, default=None)
    count = models.IntegerField(default=1)
    price_per_item = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_price = models.DecimalField(decimal_places=2, max_digits=15, default=0) #price*count
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return '%s' % self.product.name


    class Meta:
        verbose_name = 'Product in order'
        verbose_name_plural = 'Products in order'


    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.count*self.price_per_item
        super(ProductInOrder, self).save(*args,**kwargs)

    # переопределять метод save лучше так:
    """from django.db.models.signals import pre_save
    from django.dispatch import receiver

    @receiver(pre_save, sender=Accessories)
    def calc_ac_total(sender, instance, **kwargs):
        instance.ac_total = instance.period_duration()"""


def total_price_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.num_order
    all_products_in_order = ProductInOrder.objects.filter(num_order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.num_order.total_amount = order_total_price
    instance.num_order.save(force_update=True)

post_save.connect(total_price_in_order_post_save, sender=ProductInOrder)

class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128,blank=True, null=True, default=None)
    num_order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, blank=True, null=True, default=None)
    count = models.IntegerField(default=1)
    price_per_item = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    total_price = models.DecimalField(decimal_places=2, max_digits=15, default=0) #price*count
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return '%s' % self.product.name


    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'







# Create your models here.
