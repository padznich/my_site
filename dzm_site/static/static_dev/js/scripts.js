$ (document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data('product_id');
        var product_name = submit_btn.data('product_name');
        var product_price = submit_btn.data('product_price')
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        var data_prod = {}
        data_prod["prod_id"] = product_id; // синтаксис добавления в словарь или через точку или через []
        data_prod.number = nmb;
        console.log(data_prod);
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data_prod["csrfmiddlewaretoken"] = csrf_token;
        console.log(data_prod);
        var form_url = form.attr("action");
        console.log(form_url)

        $.ajax({
            url: form_url,
            type: 'POST',
            data: data_prod,
            cache: true,
            success: function(data_prod){
                console.log("OK")
                console.log(data_prod.products_total_count)
                if (data_prod.products_total_count){
                    $('#basket_total_count').text("("+data_prod.products_total_count+")")
                }
            },

            error: function(){
                console.log("error")

            }

        })


        $('.basket-item ul').append('<li>' + product_name + ' x ' + nmb +' шт. '+ product_price+'   руб.' +
        '<a class="delete-item" href="">x</a>'+
        ' </li>')

    });

    function showingBasket() {
        $('.basket-item').toggleClass('hidden');
//        $('.basket-item').removeClass('hidden');

    }

    $('.basket-container').on('click', function(e){
        e.preventDefault();
        showingBasket()
    })



    $('.basket-container').mouseover(function(){
        showingBasket()
    })


    $('.basket-container').mouseout(function(){
//        $('.basket-item').addClass('hidden')
        showingBasket()
    })

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        $(this).closest('li').remove();

    })




})