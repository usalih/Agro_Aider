from . import views
from django.urls import path

app_name = "core"
urlpatterns = [
    # Homepage
    path("",views.index, name='index'),

    path("contact",views.contact_view, name='contact'),
    path("aboutus/",views.about_us_view, name='aboutus'),
    path("checkout/",views.checkout_view, name='checkout'),
    path("single_product/<pid>/",views.single_product_view, name='single_product'),
    path('products/',views.product_view, name='products'),

    path("search/",views.search_view, name='search'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
   # path('products/<int:pid>/', views.view_article, name='view_article'),


    path("product-list/", views.category_view, name="category-all"),
    path("product-list/<name>/", views.category_view, name="category-one"),
    path("order_summary/", views.checkout_order, name="order_summary"),
    path("place-order/", views.list_page_view, name="place_order"),
    path('article/<int:article_id>/', views.view_article, name='view_article'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:product_id>/add_comment/', views.add_comment, name='add_comment'),
    path('', views.index, name='index'),


     # path('add_comment', views.add_comment, name='add_comment'),
    # path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
]
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    # path("products/",views.get_product_list_view, name='products-list'),
    




