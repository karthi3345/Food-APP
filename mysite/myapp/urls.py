from django.urls import path
from .import views
app_name="myapp"

urlpatterns = [
    path('',views.IndexClassView.as_view(), name="index"),
    path('item/',views.item),
    path('<int:pk>/',views.FoodDetail.as_view(),name="detail"),
    path("add/", views.ItemCreateView.as_view(),name="create_item"),       
    path("update/<int:pk>/",views.ItemUpdateView.as_view(), name="update_item",),
    path("delete/<int:pk>",views.ItemDeleteView.as_view(), name="delete_item"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("addresss/", views.address, name="address"),

]
