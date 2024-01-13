from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import View,CreateView,ListView,DetailView
from cafeapp.forms import CategoryCreateForm,SubCategoryCreateForm,ItemCreateForm
from cafeapp.models import Category,Subcategory,Items


class CategoryCreateView(CreateView,ListView):
    model=Category
    template_name="category.html"
    form_class=CategoryCreateForm
    success_url=reverse_lazy("category-add")
    context_object_name="categories"



def remove_category(request,*args, **kwargs):
    id=kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    return redirect("category-add")

class SubCategoryView(CreateView,ListView):
    model=Subcategory
    template_name="subcategory.html"
    form_class=SubCategoryCreateForm
    success_url=reverse_lazy("category-add")
    context_object_name="sub"

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Category.objects.get(id=id)
        form.instance.category=obj
        messages.success(self.request,"sub category has been added")
        return super().form_valid(form)
    

def remove_subcategory(request,*args, **kwargs):
    id=kwargs.get("pk")
    Subcategory.objects.filter(id=id).update(is_active=False)
    return redirect("category-add")


class ItemCreateView(CreateView):
    model=Items
    template_name="Items.html"
    form_class=ItemCreateForm
    success_url=reverse_lazy("item-all")
    context_object_name="items"

    
    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Subcategory.objects.get(id=id)
        form.instance.subcategory=obj
        messages.success(self.request,"Items has been added")
        return super().form_valid(form)
    

class ItemListView(ListView):
    model=Items
    template_name="item_list.html"
    context_object_name="items"
    
    

def remove_items(request,*args, **kwargs):
    id=kwargs.get("pk")
    Items.objects.filter(id=id).delete()
    return redirect("category-add")


class ItemDetailView(DetailView):
    model=Items
    context_object_name="item"
    template_name="item_detail.html"



    




