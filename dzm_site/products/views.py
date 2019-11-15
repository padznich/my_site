from django.shortcuts import render
from .models import Product


# Create your views here.

def product_view(request, product_id):

    print("______products.views.py___________def product_view____________")
    this_product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(f'session_key: {request.session.session_key}')
    print(f'request_get {request.GET}')
    print(f'request_post {request.POST}')


    return render(request, 'products/product.html', locals())
