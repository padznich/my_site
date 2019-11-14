from django.shortcuts import render
from django.http import HttpResponse
from .forms import Subscriber_form
from .models import Subscriber
from products.models import ImageProduct

def first_view(request):
    return HttpResponse('это сайт сержа')

def start_html(request):
    print(request.method)
    form = Subscriber_form(request.POST or None)
    data_users = list(Subscriber.objects.values('email'))
    print(data_users)
    print(f'request {request}')
    print(f'request_get {request.GET}')
    print(f'request_post {request.POST}')

    if request.method == "POST" and form.is_valid():
        if {'email': form.cleaned_data['email']} in data_users:
            print('SOVPALO')
            return render(request, 'landing/no_submit.html', locals())
        print(f'form print:\n{form}')
        print(f'request.POST:\n{request.POST}')
        print(f'form.cleaned_data:\n{form.cleaned_data}')
        print(f'form.cleaned_data["email"]:\n{form.cleaned_data["email"]}')
        print(f'form.cleaned_data["name"]:\n{form.cleaned_data["name"]}')
        print(type(form.cleaned_data))
        new_form = form.save()
    return render(request, 'landing/start_page.html', locals())


def home(request):
    product_images = ImageProduct.objects.filter(is_active =True, is_main=True)
    product_images_phones = ImageProduct.objects.filter(is_active =True, is_main=True, product__category__name='Телефоны')
    product_images_laptops = ImageProduct.objects.filter(is_active=True, is_main=True, product__category__name='Ноутбуки')
    product_images_page = product_images[0:4]
    product_images_phones_page = product_images_phones[0:4]
    product_images_laptops_page = product_images_laptops[0:4]



    return render(request, 'landing/home.html', locals())
# Create your views here.
