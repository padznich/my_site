from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, ProductInOrder, ProductInBasket
from .forms import CheckoutContactForm
from django.contrib.auth.models import User

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
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, # для поля id работает одно нижнее
                                                                     product_id=product_id,   # подчеркивание _id для обращения к полю
                                                                     defaults={'count':nmb})  # связанной модели
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


def checkout(request):
    print("___________________checkout view")
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, num_order__isnull=True)
    total_amount_order = 0
    for product_in_basket in products_in_basket:
        total_amount_order+= product_in_basket.total_price
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        data = request.POST
        print(data)
        if form.is_valid():
            print("form is valid")
            name = data.get('cl_name', 'name if not data')
            phone = data['cl_phone']
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)
            for name, value in data.items():
                if name.startswith('product_in_basket_'):
                    pr_in_bask_id = name.split('product_in_basket_')[1]
                    prods_basket = ProductInBasket.objects.get(id=pr_in_bask_id)
                    prods_basket.count = value
                    prods_basket.num_order=order
                    prods_basket.save(force_update=True)
                    try:
                        ProductInOrder.objects.create(product=prods_basket.product, count=prods_basket.count,
                                                  price_per_item=prods_basket.price_per_item, total_price=prods_basket.total_price,
                                                  num_order=order)
                    except:
                        print('Произошел сбой')
                    else:
                        ProductInBasket.objects.filter(num_order=order).delete() # после добавление в ордер очищаем корзину
                        print('Заказ успешно обработан')
        else:
            print('form is not valid')

    return render(request, 'orders/checkout.html', locals())