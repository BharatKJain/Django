from django.shortcuts import render
#--------------------part15
from .models import Product


def product_detail_view(request):
    obj = Product.objects.get(id=5)
    object_context = {"object": obj}
    # return render(request, "product/detail.html ", object_context)
    # ---------------------part16
    return render(request,"product/products_details.html",object_context)
    
    #part16----------------------
#part15-----------------------