from django.urls import path
from .import views
app_name="myapp"

urlpatterns = [
    path('',views.IndexClassView.as_view(), name="index"),
    path('item/',views.item),
    path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),
    path("add/", views.ItemCreateView.as_view(),name="create_item"),       
    path("update/<int:id>/",views.update_item, name="update_item",),
    path("delete/<int:id>",views.delete_item, name="delete_item"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("addresss/", views.address, name="address"),

]
