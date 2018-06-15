from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
def hello(request):
    # text = "<h1>Hello World</h1>"
    # return HttpResponse(text)
    return render(request, "hello.html", {})