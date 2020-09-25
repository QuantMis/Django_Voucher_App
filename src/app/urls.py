from django.contrib import admin
from django.urls import path
from app import main

# controller import
from app import voucher, product

admin.autodiscover()

urlpatterns = [
	# page renderer
	path('',main.home,name='main_page'),
	path('user/',main.user,name='user_page'),
	path('admin/',main.admin,name='admin_page'),

	# voucher resource
	path('admin/voucher/post',voucher.create_voucher,name='create_voucher'),
	path('admin/voucher/get',voucher.load_voucher,name='load_voucher'),
	path('admin/voucher/del',voucher.del_voucher,name='del_voucher'),
	path('admin/voucher/apply',voucher.apply_voucher,name='apply_voucher'),

	# products resource
	path('admin/product/post',product.create_product,name='create_product'),
	path('admin/product/get',product.load_product,name='load_product'),
	path('admin/product/del',product.del_product,name='del_product'),
	path('admin/product/cart/post',product.cart,name='add_cart'),
	path('admin/product/cart/del',product.reset_cart,name='del_cart'),
]

