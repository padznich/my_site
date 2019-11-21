$ (document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);



    function basket_updating(product_id, nmb, is_delete=false){
        var data_prod = {}
        data_prod["prod_id"] = product_id; // это может быть id продукта или id корзины (все обусловлено тем, кто вызвал событие)
        // ключевым разграничением будет отправлять параметр is_delete=false для "купить" и is_delete=true для "удалить"000000
        data_prod.number = nmb;
        console.log(data_prod);
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data_prod["csrfmiddlewaretoken"] = csrf_token;
        console.log(data_prod);

        if(is_delete){
            data_prod['is_delete']=true
        }

        var form_url = form.attr("action");
        console.log(form_url)

        $.ajax({
            url: form_url,
            type: 'POST',
            data: data_prod,
            cache: true,
            success: function(data_response){
                console.log("OK")
                console.log(data_response.products_in_basket_count)
                if (data_response.products_in_basket_count){
                    $('#basket_total_count').text("("+data_response.products_in_basket_count+")");
                    console.log(data_prod);
                    console.log(data_response);


                     $('.basket-item ul').html(""); // очищаем корзину
                     $.each(data_response.products, function(k, v){   // проходимся по каждому элементу массива
                        console.log('ind: '+ k +" "+ 'val.name:'+ v.name);
                        $('.basket-item ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'руб. ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                            '</li>');
                     });


//                    if (data_response.was_created){
//                        $('.basket-item ul').append('<li id="'+product_id+'">' +
//                        product_name + ' x ' + nmb +
//                        ' шт. '+ product_price+'   руб.'+
//                        '<a class="delete-item" href="" data-product_id="'+product_id+
//                        ' </li>')
//
//
//                    } else {
//                        console.log('in else')
//                        $('#'+product_id).text(product_name + ' x ' + data_response.prod_id_count +
//                        ' шт. '+ product_price+'   руб.')
//                        var prod_el = document.getElementById(product_id);
//                        //добавляем в html крестик - удалить элемент
//                        prod_el.insertAdjacentHTML('beforeEnd', '<a class="delete-item" href="" data-product_id="'+
//                            product_id+'>x</a>');
//                    }
                }
            },

            error: function(){
                console.log("error")

            }
        })
    }


    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val(); //считываем значение с поля ввода input c id="number" в product.html
        console.log(nmb);
        var submit_btn = $('#submit_btn'); // Кнопка КУПИТЬ с id="submit_btn" в product.html
        var product_id = submit_btn.data('product_id'); // считываем аттрибуты data-product_id с кнопки КУПИТЬ
//        var product_name = submit_btn.data('product_name'); //data-product_name
//        var product_price = submit_btn.data('product_price'); // data-product_price
//        console.log(product_id);
//        console.log(product_name);
//        console.log(product_price);
        basket_updating(product_id, nmb, is_delete=false)
    });

    function showingBasket() {
        $('.basket-item').toggleClass('hidden');
//        $('.basket-item').removeClass('hidden');
    }


    $('.basket-container').on('click', function(e){
        e.preventDefault();
        showingBasket()
    });



    $('.basket-container').mouseover(function(){
        showingBasket()
    });


    $('.basket-container').mouseout(function(){
//        $('.basket-item').addClass('hidden')
        showingBasket()
    });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id=$(this).data("product_id");
        basket_updating(product_id, nmb=0, is_delete=true);


//        $(this).closest('li').remove();

    });
    function total_amount_in_order(){
        var total_money = 0;
        $('.product-total-amount').each(function(){
            total_money += parseFloat($(this).text())
            console.log('in each')
        });
        console.log('total_am: '+total_money)
        $('#total-order-amount').text(total_money.toFixed(2)+' руб.');
        $('#total_sum_span').text(total_money.toFixed(2));

    }

    $(document).on('change', '.product_num_in_basket', function(){
        var new_prod_num = $(this).val();
        current_tr=$(this).closest('tr');
        current_price=parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        console.log("cur_price: "+current_price);
        current_total_amount = parseFloat(new_prod_num*current_price).toFixed(2);
        console.log("cur_total_amount: "+current_total_amount);
        current_tr.find('.product-total-amount').text(current_total_amount)
        total_amount_in_order();
    });

    total_amount_in_order();

})