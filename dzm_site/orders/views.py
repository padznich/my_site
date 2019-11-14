from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket

# Create your views here.
def basket_adding(request):
    return_dict = {}
    session_key = request.session.session_key
    print (f'print_request_get {request.GET}')
    print(f'print_request_post {request.POST}')
    data = request.POST
    product_id = data.get('prod_id')
    nmb = data.get('number')

    new_product = ProductInBasket.objects.create(session_key=session_key, product_id=product_id, count=nmb)
    products_total_count = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
    return_dict['products_total_count'] = products_total_count

    return JsonResponse(return_dict)

