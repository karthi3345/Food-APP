from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from .forms import ItemForm
from django.shortcuts import render, redirect
from .forms import ItemForm


# Create your views here.
def index(request):  # ✅ Correct
    item=Items.objects.all()
    context={
        "item":item
    }
    return render(request,"myapp/index.html",context)

def detail(request,id):
    detail_item=Items.objects.get(id=id)
    context={
        "detail_item":detail_item
    }
    return render(request,"myapp/detail.html",context)
    # return HttpResponse(f"This is detail with item as id as {detail_item}")

def item(request):
    return HttpResponse("this is my item")

def create_item(request):
    form=ItemForm(request.POST or None)
    if request.method == "POST":

        if form.is_valid():
            form.save()
        return redirect("myapp:index")
    context={
         "form":form
    }
    return render(request,"myapp/item-form.html",context)

def update_item(request, id):
    item= Items.objects.get(id=id)
    form = ItemForm( request.POST or None ,instance=item)
    if form.is_valid():
        form.save()
        return redirect("myapp:index")
    context={
         "form":form
    }
    return render (request,"myapp/item-form.html",context)

def delete_item(request,id ):
    item=Items.objects.get(id=id)
    if request.method=="POST":
       item.delete()
       return redirect("myapp:index")
    return render(request,"myapp/item-delete.html")
    
    from django.shortcuts import render

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")
def address(request):
    return render (request,"myapp/address.html")