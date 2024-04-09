from django.db import models
from userauths.models import User
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField


# Create your models here.

STATUS_CHOICE = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("Delivered", "Delivered"),
)

PRODUCT_CHOICE = (
    ("small", "Small"),
    ("medium", "Medium"),
    ("large", "Large"),
    ("extra_large", "Extra Large"),
)

STATUS = (
    ("draft", "Draft"),
    ("deliver", "Delivered"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.user.id, filename)

def user_file_directory_path(instance, filename):
    return "user_{0}/files/{1}".format(instance.user.id, filename)

# is it safe to flush the database? yes ok
class Category(models.Model):
    cid = ShortUUIDField(
        unique=True,
        length=10,
        max_length=20,
        prefix="cat_",
        alphabet="abcdefg1234",
    )
    title = models.CharField(max_length=100, default="Fresh Vege product.")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass


class Product(models.Model):
    pid = ShortUUIDField(
        unique=True,
        length=10,
        max_length=20,
        prefix="prd_",
        alphabet="abcdefg1234",
    )
    # slug = models.SlugField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100, default="Latest Update.")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    description = models.TextField(null=True, max_length=200, default="Make a brief description in 30 words.")

    file = models.FileField(blank=True, upload_to=user_file_directory_path, help_text="input attached file docs and videos")
    article = models.TextField( max_length=750, default="This is the text article section.")
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def product_image(self):
        return mark_safe('<img src="%s" width="50" hight="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price


class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-image.jpg", default="product.jpg")
    product = models.ForeignKey(
        Product,
        related_name="p_image",
        max_length=100,
        on_delete=models.SET_NULL,
        null=True,
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"

    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price



###################################################### ProductReview, Whishlist and Address #########################################################
###################################################### ProductReview, Whishlist and Address #########################################################
###################################################### ProductReview, Whishlist and Address #########################################################
###################################################### ProductReview, Whishlist and Address #########################################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def rating(self):
        return self.rating



class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_no = models.CharField(max_length=15)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Contact Us"
