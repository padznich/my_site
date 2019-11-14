from django.conf.urls import url

from products.views import product_view


urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', product_view, name='product'),
    ]