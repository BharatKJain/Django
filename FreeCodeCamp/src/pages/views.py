from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# #part6
# def home_view(request,*args, **kwargs):
#     #request in args when not mentioned
#     print(request.user)
#     return HttpResponse("<h1>Hello World</h1>")
#     #part8
#     return render(request,"home.html",{})
# #part7
# def contact_view(*args,**kwargs):
#     return HttpResponse("<h1>Contact Page</h1>")

# def about_view(*args,**kwargs):
#     return HttpResponse("<h1>About Page</h1>")

# def social_view(*args,**kwargs):
#     return HttpResponse("<h1>Social Page</h1>")

#----------------part9
#Conversion from HttpResponse to html render
def home_view(request,*args, **kwargs):
    return render(request,"home.html",{})
def contact_view(request,*args, **kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args, **kwargs):
    #return render(request,"about.html",{})
    
    #--------------------part11
    # website_context={
    #     "my_text":"This is about coding",
    #     "my_number":123
    # }
    # return render(request,"about.html",website_context)
    #part11-----------------
    # #--------------------part12
    # website_context={
    #     "my_text":"This is about coding",
    #     "my_number":123,
    #     "my_list":['this','is','my','list']
    # }
    # return render(request,"about.html",website_context)
    # #part12-----------------
    #-------------------------part13
    website_context={
        "my_text":"This is about coding",
        "my_number":123,
        "my_list":[1313,4231,312,"Abc"],
        "my_html":"<p>testHTML</p>"
    }
    return render(request,"about.html",website_context)
    #part13-------------------------

def social_view(request,*args, **kwargs):
    return render(request,"social.html",{})
#part9-----------------