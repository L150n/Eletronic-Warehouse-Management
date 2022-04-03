from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


from .models import Brand, Category, Product

# Create your views here.

	
@login_required(login_url="/account/signin/")
def index(request):
	return render(request, "product.html", {})

def signin(request):
	if request.method == "POST":
		pass
		user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
		if user:
			login(request, user)
			return redirect("/products/")
		else:
			messages.error(request, "Username or password error!")
			return redirect("/account/signin/")
	return render(request, "login.html", {})



def logout_view(request):
	logout(request)
	return redirect("/account/signin/")



@csrf_exempt
@login_required(login_url="/account/signin/")
def products(request):
	return render(request, "product.html", {})

@login_required(login_url="/account/signin/")
def categories(request):
	return render(request, "categories.html", {})

def categories_list(request):
	categories_lists = Category.objects.all()
	html = render_to_string('modules/tables_categories.html', {"categories": categories_lists})
	return JsonResponse({"message": "Ok", "html": html})

@csrf_exempt
def create_product(request):
	data = dict()
	if request.method == "GET":
		categories_lists = Category.objects.all()
		brands_lists = Brand.objects.all()
		data['html'] = render_to_string('modules/add_product.html', {"categories": categories_lists, "brands": brands_lists})
	else:
		print(request.FILES)
		Product.objects.create(
			name=request.POST["name"],
			brand=Brand.objects.get(id=request.POST["brand"]),
			category=Category.objects.get(id=request.POST["category"]),
			code=request.POST["code"],
			quantity=request.POST["quantity"],
			rate=request.POST["rate"],
			status=request.POST["status"],
		)
		products_lists = Product.objects.all()
		data['html'] = render_to_string('modules/tables_products.html', {"products": products_lists})
	return JsonResponse(data)

@csrf_exempt
def products_list(request):
	products_lists = Product.objects.all()
	html = render_to_string('modules/tables_products.html', {"products": products_lists})
	return JsonResponse({"message": "Ok", "html": html})
@csrf_exempt
def create_brand(request):
	data = dict()
	brand_name = request.POST.get("brandName")
	brand_status = request.POST.get("brandStatus")
	Brand.objects.create(name=brand_name, status=brand_status)
	brands_list = Brand.objects.all()
	data['html'] = render_to_string('modules/tables.html', {"brands": brands_list})
	return JsonResponse(data)

@csrf_exempt
def create_categories(request):
	data = dict()
	category_name = request.POST.get("categoryName")
	category_status = request.POST.get("categoryStatus")
	Category.objects.create(name=category_name, status=category_status)
	categories_lists = Category.objects.all()
	data['html'] = render_to_string('modules/tables_categories.html', {"categories": categories_lists})
	return JsonResponse(data)
	
@login_required(login_url="/account/signin/")
def brand_list(request):
	brands_list = Brand.objects.all()
	html = render_to_string('modules/tables.html', {"brands": brands_list})
	return JsonResponse({"message": "Ok", "html": html})

@csrf_exempt
@login_required(login_url="/account/signin/")
def brands(request):
	return render(request, "brand.html", {})
@csrf_exempt
@login_required(login_url="/account/signin/")
def search(request):
	if request.method == 'GET':
		q = request.GET.get('q')
		if q:
			product= Product.objects.filter(name__icontains=q)
			return render(request,'search.html', {"products": product})	
		else:
			print("No result to show")
			return render(request, "search.html", {})
