from core import models
from .models import Product
from django.db.models import Q
from googletrans import Translator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

translator = Translator()

def index(request):
    products = models.Product.objects.all()

    context = {"products": products}
    return render(request, "core/index.html", context)

def about_us_view(request):
    return render(request, "core/aboutus.html")

def checkout_view(request):
    return render(request, "core/checkout.html")

def product_view(request):
    categories = ['article', 'video', 'file']
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'core/product.html', context)

#return render(request, "core/product.html",)


def single_product_view(request, pid):
    product = get_object_or_404(models.Product, pid=pid)

    context = {"product": product}
    return render(request, "core/product-single.html", context)





def add_to_cart(request, product_id):
    if request.method == "POST":
        attr = {"user": request.user}
        amount = int(request.POST.get("amount", 1))

        product = models.Product.objects.get(id=product_id)
        cart, _ = models.Cart.objects.get_or_create(**attr, defaults=attr)

        cart_item = cart.cartitem_set.filter(product=product).first()

        if cart_item:
            cart_item.quantity += amount
            cart_item.save()
        else:
            models.CartItem.objects.create(cart=cart, quantity=amount, product=product)

    return redirect(request.META.get("HTTP_REFERER"))


def remove_from_cart(request, item_id):
    if request.method == "POST":
        cart_item = models.CartItem.objects.filter(id=item_id).first()

        if cart_item:
            cart_item.delete()
    return redirect(request.META.get("HTTP_REFERER"))


def contact_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        message = request.POST["message"]
        phone_no = request.POST["phone_no"]
        full_name = request.POST["full_name"]
        models.Contact.objects.create(
            full_name=full_name, email=email, phone_no=phone_no, message=message
        )

        return render(request, "core/contact.html", {"full_name": full_name})
    else:
        return render(request, "core/contact.html", {})


def search_view(request):
    query = request.GET.get("q")
    products = models.Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    context = {"products": products, "query": query}
    return render(request, "core/search.html", context)


# logic
def view_article(request, pid):
    product = get_object_or_404(pk=pid)
    return render(request, 'view_article.html', {'product': product})

def category_view(request, name="all"):
    products = models.Product.objects.all()
    categories = models.Category.objects.all()

    if name != "all":
        products = products.filter(category__title=name)

    context = {"products": products, "categories": categories}
    return render(request, "core/shop.html", context)


def list_page_view(request):
    cart_items = request.user.cart.cartitem_set.all()
    context={"cart_items":cart_items}
    return render(request,"core/order_summary.html",context)

def checkout_order(request):
    # get all the cart items
    cart_items = request.user.cart.cartitem_set.all()

    if cart_items.count():
        # first create an order
        order = models.Order.objects.create(user=request.user)

        # replicate the cart items to order items and delete them from the cart
        for item in cart_items:
            models.OrderItem.objects.create(
                order=order, product=item.product, amount=item.quantity, price=item.product.price
            )
            item.delete()
    
    return redirect("userauths:index")

