from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

from .models import Order
from products.models import Product
from .forms import OrderForm

import pathlib
from wsgiref.util import FileWrapper
from mimetypes import guess_type
from django.http import Http404,HttpResponse

# Create your views here.
@login_required
def my_order_view(request):
    qs = Order.objects.filter(user=request.user, status = 'paid')
    context = {
        'object_list': qs
    }
    return render(request,'orders/my_order.html',context)


@login_required
def order_checkout_view(request):
    product_id = request.session.get('product_id') or None
    if product_id == None:
        return redirect('/')
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except:
        # message success
        return redirect('/success')
    # if product.has_inventory == 0:
    #     return redirect('/no-inventory')
    user = request.user
    order_id = request.session.get('order_id')  # CART
    order_obj = None
    new_creation = False
    try:
        order_obj = Order.objects.get(id=order_id)
    except:
        order_id = None
    if order_id == None:
        new_creation = True
        order_obj = Order.objects.create(product=product, user=user)
    if order_obj != None and new_creation == False:
        if order_obj.product.id != product.id:
            order_obj = Order.objects.create(product=product, user=user)
    request.session['order_id'] = order_obj.id
    # initialize the form
    form = OrderForm(request.POST or None, product=product, instance=order_obj) # dealing with forms
    if form.is_valid():
        order_obj.shipping_address = form.cleaned_data.get('shipping_address')
        order_obj.billing_address = form.cleaned_data.get('billing_address')
        order_obj.mark_paid(save=False)
        order_obj.save()
        del request.session['order_id']
        request.session['checkout_success_order_id'] = order_obj.id
        return redirect("/success")
    context = { 
        'form': form,
        'object': order_obj,
        'is_digital': product.is_digital
    }
    #print(order_id)
    return render(request,'orders/checkout.html',context)

@login_required
def download_order(request, order_id = None, *args, **kwargs):
    ''' 
    Dowload our order product media, if it exists.
    '''
    if order_id ==None:
        return redirect('/orders')
    qs = Order.objects.filter(id = order_id,user = request.user,status = 'paid', product__media__isnull= False)
    if not qs.exists():
        return redirect("/orders")
    order_obj = qs.first()
    product_obj = order_obj.product
    if not product_obj.media:
        raise Http404
    media = product_obj.media
    product_path = media.path   # abc/asdf/media/cdfsd/adsf.csv
    path = pathlib.Path(product_path)
    pk = product_obj.pk
    ext = path.suffix   # .csv , .png , .mov
    fname = f"my-product-{order_id}-{pk}{ext}"
    if not path.exists():
        raise Http404
    with open(path, 'rb') as f:
        wrapper = FileWrapper(f)
        content_type = 'application/force-download'
        guessed_ = guess_type(path)[0]
        if guessed_:
            content_type = guessed_
        response = HttpResponse(wrapper, content_type = content_type)
        response['Content-Disposition'] = f"attachment;filename={fname}"
        response['X-SendFile'] = f"{fname}"
        return response

