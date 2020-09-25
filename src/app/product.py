from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Product, CltCart
from django.http import JsonResponse

# temp only 
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_product(request):
	r = Product(
		title = request.POST.get("title",""), 
	    price = request.POST.get("price",""),
	)
	r.save()
	data = {"status_code":"success"}
	return JsonResponse(data)

@csrf_exempt
def load_product(request):
	if Product.objects.count()==0:
		res = []
	else:
		res = list(Product.objects.values())
	data = {"res":res,"status_code":"success"}
	return JsonResponse(data)

@csrf_exempt
def del_product(request):
	title = request.POST.get("title","")
	Product.objects.filter(title=title).delete()
	data = {"status_code":"success"}
	return JsonResponse(data)

# for client operations
@csrf_exempt
def cart(request):
	client = request.POST.get("client","")
	new_item = request.POST.get("item","")
	new_price = request.POST.get("price",'')
	
	try:
		item = (CltCart.objects.get(client_tag=client).client_item,new_item)
		item = ",".join(item)
		payable = CltCart.objects.get(client_tag=client).client_payable + float(new_price)

	except CltCart.DoesNotExist:
		item = new_item
		payable = new_price

	print(f"item: {item}")# update_item: {update_item}")
	print(f"payable: {payable}") # update_payable: {update_payable}")
	cart, created = CltCart.objects.update_or_create(
        client_tag=client, defaults={
        	"client_item": item,
        	"client_payable":payable,
        	"client_fee":25
        }
	)
	res = list(CltCart.objects.values())
	# print(f"Cart: {cart}")
	print(res)
	return JsonResponse({"res":res,"status_code":"success"})

@csrf_exempt
def reset_cart(request):
	CltCart.objects.filter().delete()
	return JsonResponse({"status_code":"cart reset"})