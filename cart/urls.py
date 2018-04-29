from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),

]
