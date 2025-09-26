from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from .forms import ItemForm
from django.shortcuts import render, redirect
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy



# # Create your views here.
# def index(request):  # ✅ Correct
#     item=Items.objects.all()
#     context={
#         "item":item
#     }
#     return render(request,"myapp/index.html",context)

class IndexClassView(ListView):
    model= Items
    template_name="myapp/index.html"
    context_object_name= "item"

# def detail(request,id):
#     detail_item=Items.objects.get(id=id)
#     context={
#         "detail_item":detail_item
#     }
#     return render(request,"myapp/detail.html",context)
#     # return HttpResponse(f"This is detail with item as id as {detail_item}")

class FoodDetail(DetailView):
     model=Items
     template_name= "myapp/detail.html"
     context_object_name="detail_item"
    

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

class ItemCreateView(CreateView):
    model=Items
    fields=["item_name","item_des", "item_price","item_image"]
    template_name = "myapp/item-form.html"  # ✅ This must match the template file name
    def form_valid(self, form):
        self.request.user
        return super().form_valid(form)
    
   




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

class ItemUpdateView(UpdateView):
    model=Items
    fields=["item_name","item_des", "item_price","item_image"]
    # template_name_suffix= "_update_form.html"  #determine the /item/update/form
    template_name = "myapp/item-form.html" 


def delete_item(request,id ):
    item=Items.objects.get(id=id)
    if request.method=="POST":
       item.delete()
       return redirect("myapp:index")
    return render(request,"myapp/item-delete.html", {"item": item})

class ItemDeleteView(DeleteView):
    model=Items
    template_name="myapp/item-delete.html"
    success_url = reverse_lazy('myapp:index') 
    


 

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")
def address(request):
    return render (request,"myapp/address.html")



from django.http import JsonResponse
from django.db import connection

def db_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'details': str(e)})

def get_object(request):
    for item in Items.objects.all():
        print(item.item_name)