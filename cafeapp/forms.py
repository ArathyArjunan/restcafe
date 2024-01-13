from django import forms
from cafeapp.models import User,Category,Subcategory,Items


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model=Category
        fields=["category_name"]


class SubCategoryCreateForm(forms.ModelForm):

    class Meta:
        model=Subcategory
        fields=["Subcategory_name"]


class ItemCreateForm(forms.ModelForm):

    class Meta:
        model=Items
        fields=["items_name","price","description","image"]