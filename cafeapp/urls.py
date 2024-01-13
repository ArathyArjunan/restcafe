from django.urls import path
from cafeapp import views


urlpatterns = [
    path("",views.CategoryCreateView.as_view(),name="category-add"),
    path("category/<int:pk>/",views.remove_category,name="category-remove"),
    path("category/<int:pk>/subcategory/",views.SubCategoryView.as_view(),name="subcategory-add"),
    path("subcategory/<int:pk>/",views.remove_subcategory,name="subcategory-remove"),
    path("subcategory/<int:pk>/items/",views.ItemCreateView.as_view(),name="item-add"),
    path("items/",views.ItemListView.as_view(),name="item-all"),
    path("items/<int:pk>/remove",views.remove_items,name="item-remove"),
    path("items/<int:pk>/",views.ItemDetailView.as_view(),name="item-detail"),




]
