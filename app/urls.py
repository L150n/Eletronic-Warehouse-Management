from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("account/signin/", views.signin, name="signin"),
	path("account/logout/", views.logout_view, name="logout"),
	path("brands/", views.brands, name="brand"),
	path("brands/list/", views.brand_list, name="brand-list"),
	path("brand/create/", views.create_brand, name="create-brand"),
	path("categories/", views.categories, name="categories"),
	path("categories/list/", views.categories_list, name="categories-list"),
	path("categories/create/", views.create_categories, name="create-categories"),
	path('search/', views.search, name='search'),
	path("products/", views.products, name="products"),
	path("products/list/", views.products_list, name="products-list"),
	path("products/create/", views.create_product, name="create-product"),
]