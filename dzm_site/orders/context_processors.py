from .models import ProductInBasket

def basket_items(request):
    print('______orders.context_processors________def basket_items___________')
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, num_order__isnull=True)
    total_count_items_in_basket = 0
    for item_in_basket in products_in_basket:
        total_count_items_in_basket += item_in_basket.count

    count_in_basket = total_count_items_in_basket
    print(f'products in basket: {products_in_basket}')
    print(f'count in basket = {count_in_basket}')


    return locals()