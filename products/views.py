from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductModelForm

# Create your views here.
def search_view(request, *args, **kwargs):
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains=query[0])
    print(query,qs)

    context = {
        "name": "Ajeet",
        "query" : query,
    }
    return render(request, "home.html", context)
    #return HttpResponse("<h1> Hello World  </h1>")

@staff_member_required
def product_create_view(request, *args, **kwargs):
    #print(request.POST)
    #print(request.GET)
    # if request.method == "POST":
    #     post_data = request.POST or None
    #     if post_data != None:
    #         my_form = ProductForm(request.POST)
    #         if my_form.is_valid():
    #             print(my_form.cleaned_data.get('title'))
    #             title_from_input = my_form.cleaned_data.get('title')
    #             Product.objects.create(title = title_from_input)
    #             #print("post_data", post_data)
    form = ProductModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False) # line 32 and 35 are equals to the lines 39, 40
        # do some stuff 
        image = request.FILES.get('images')
        if image:
            obj.image = image
        media = request.FILES.get('media')
        if media:
            obj.media = media    
        obj.user = request.user    #added after adding user field in models.py
        obj.save()
        print(request.POST)
        #print(form.cleaned_data)
        #data = form.cleaned_data
        #Product.objects.create(**data)
        #product(**data)
        form = ProductModelForm()
    context ={
        "form": form,
    }
    #return redirect("/success")   # go to new page saying success!
    return render(request,'forms.html',context)


def detail_home_view(request, id):
    obj = Product.objects.get(id=id)
    try:
        obj = Product.objects.get(id=id)
        content = {
            'object': obj,
        }
    except Product.DoesNotExist:
        raise Http404
    #return HttpResponse(f"Product ID: {obj.id}")
    return render(request,"products/detail.html", content)

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()  #list of products
    context = {
        'object_list':qs,
    }
    return render(request,'products/product_list.html', context)

#def bad_view(request, *args, **kwargs):
#    print(dict(request.GET))
#    new_product = my_request_data.get('new_product')
#    print(my_request_data, new_product)
#    if new_product[0].lower() == 'true':
#        print('new product')
#        Product.objects.create(title=my_request_data.get('title')[0],content=my_request_data.get('content')[0])
#    return HttpResponse("don't USE this.")


