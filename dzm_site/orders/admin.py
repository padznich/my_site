from django.contrib import admin
from .models import Status, Order, ProductInOrder, ProductInBasket


# Register your models here.
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]  # все поля из модели Status


    class Meta:
        model = Status


class OrderAdmin(admin.ModelAdmin):
    #list_display = ['name', 'email'] # здесь все поля
    list_display = [field.name for field in Order._meta.fields]  # все поля из модели Subscriber
    # print(f'this DZM print: {Subscriber._meta.fields[2].name}')
    #list_filter = ['email', 'name']
    #exclude = ['email'] #исключает отображение поля в админке при просмотре конкретной записи
    #fields = ['name'] # отображает только указанные поля в админке при просметре конкретной записи
    #search_fields = ['name','email']
    inlines = [ProductInOrderInline]


    class Meta:
        model = Order


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]


    class Meta:
        model = ProductInOrder


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]


    class Meta:
        model = ProductInBasket



admin.site.register(Status, StatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInBasket, ProductInBasketAdmin)