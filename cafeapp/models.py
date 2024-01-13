from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=100)

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.category_name


class Subcategory(models.Model):
    Subcategory_name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)



    def __str__(self):
        return self.Subcategory_name


class Items(models.Model):
    items_name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    subcategory=models.ForeignKey(Subcategory,null=True,on_delete=models.SET_NULL)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.items_name



class Offers(models.Model):
    items=models.ForeignKey(Items,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)



class Carts(models.Model):
    item=models.ForeignKey(Items,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


from django.core.validators import MinValueValidator,MaxValueValidator

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cloths=models.ForeignKey(Items,null=True,on_delete=models.SET_NULL)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)


