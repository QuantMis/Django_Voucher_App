from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Voucher,CltCart
from django.http import JsonResponse

# temp only 
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_voucher(request):
	r = Voucher(
		title = request.POST.get("title",""), 
	    description = request.POST.get("description",""),
	    capacity  = request.POST.get("capacity",""),
	    vouchtype = request.POST.get("vouchtype",""),
	    vouchvalue = request.POST.get("vouchvalue","")
	)
	r.save()
	data = {"status_code":"success"}
	return JsonResponse(data)

@csrf_exempt
def load_voucher(request):
	if Voucher.objects.count()==0:
		res = []
	else:
		res = list(Voucher.objects.values())
	data = {"res":res,"status_code":"success"}
	return JsonResponse(data)

@csrf_exempt
def del_voucher(request):
	title = request.POST.get("title","")
	Voucher.objects.filter(title=title).delete()
	data = {"status_code":"success"}
	return JsonResponse(data)

@csrf_exempt
def apply_voucher(request):
	code = request.POST.get("code","")
	client = request.POST.get("client","")
	vouchers = list(Voucher.objects.values())
	titles = [i['title'] for i in vouchers]
	cobj = CltCart.objects.get(client_tag=client)
	if code in titles:
		vobj = Voucher.objects.get(title=code) 
		# voucher attr
		capacity = vobj.capacity
		vouch_type = vobj.vouchtype
		vouch_value = float(vobj.vouchvalue)

		# cart attr
		payable = cobj.client_payable
		fee = cobj.client_fee

		if int(capacity) == 0:
			status = "max reach"
			res = []
		else:
			if vouch_type == "FEE REDUCTION":
				print("FEE PATH")
				fee = 0

			elif vouch_type == "OFF":
				payable = payable - vouch_value

			elif vouch_type == "DISCOUNT": 
				payable = payable - (vouch_value/100)*payable

			cart, created = CltCart.objects.update_or_create(
        		client_tag=client, defaults={
		        	"client_payable":payable,
		        	"client_fee":fee
		        }
			)

			voucher, created = Voucher.objects.update_or_create(
				title=code, defaults={
					"capacity":(int(capacity)-1)
				}
			)

			res = list(CltCart.objects.values())
			status = "voucher applied"
			print(f"res: {res}")
		data = {"res":res,"status_code":status}
		print(f"data: {data}")
		return JsonResponse(data)
	else:
		status = "not exist"
		data = {"code":code,"status_code":status}
		return JsonResponse(data)