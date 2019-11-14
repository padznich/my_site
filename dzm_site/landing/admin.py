from django.contrib import admin
from .models import Subscriber

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ['name', 'email'] # здесь все поля
    list_display = [field.name for field in Subscriber._meta.fields]  # все поля из модели Subscriber
    # print(f'this DZM print: {Subscriber._meta.fields[2].name}')
    list_filter = ['email', 'name']
    #exclude = ['email'] #исключает отображение поля в админке при просмотре конкретной записи
    #fields = ['name'] # отображает только указанные поля в админке при просметре конкретной записи
    search_fields = ['name','email']





    class Meta:
        model = Subscriber



admin.site.register(Subscriber, SubscriberAdmin)