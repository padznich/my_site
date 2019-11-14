from django.conf.urls import url

from .views import start_html, home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^start/$',start_html, name='start_page'),
    ]