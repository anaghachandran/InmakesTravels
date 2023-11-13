from django.http import HttpResponse
from django.shortcuts import render
from .models import Place

# def demo(request):
    # return HttpResponse("Hello World")#create views
#     return render(request,"index.html")#render
#
# def about(request):
#     return render(request, "about.html")
#
# def contact(request):
#     return HttpResponse("Hello Iam Contact")
#def demo(request):
#     name="india"
#     return render(request, "index1.html", {'obj':name})
# def demo(request):
#     return render(request,"index2.html")

# def addition(request):
#     return render(request, "result.html")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request, "result.html", {'result':res})


# def demo(request):
#     return render(request,"index3.html")

def demo(request):
    obj = Place.objects.all()
    return render(request, "index3.html", {'result': obj})

