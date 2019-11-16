from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInBasket

# Create your views here.
def basket_adding(request):
    print('___orders.views.py___def basket_adding______')
    return_dict = {}
    session_key = request.session.session_key
    print(f'print_request_get {request.GET}')
    print(f'print_request_post {request.POST}')
    data = request.POST
    product_id = data.get('prod_id')
    nmb = data.get('number')
    is_delete = data.get('is_delete')

    if is_delete=='true':
        # если находимся в этом блоке кода то:
        # product_id = id корзины
        ProductInBasket.objects.filter(id=product_id).update(count=0, is_active=False)
    else:
        # если находимся в этом блоке кода то:
        # product_id = id продукта
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={'count':nmb})
        if not created:
            if ProductInBasket.objects.filter(product_id=product_id, is_active=False):
                new_product.is_active=True
            new_product.count +=int(nmb)
            new_product.save(force_update=True)

    prods_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    total_count_in_basket = 0
    for item_in_basket in prods_in_basket:
        total_count_in_basket += item_in_basket.count

    products_in_basket_count = total_count_in_basket

    return_dict['products_in_basket_count'] = products_in_basket_count


    return_dict["products"] = list()
    for item in prods_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.count
        return_dict["products"].append(product_dict)

    print(f'return_dict: {return_dict}')
            


    return JsonResponse(return_dict)

