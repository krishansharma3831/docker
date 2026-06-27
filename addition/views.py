from django.shortcuts import render

def home(request):
    result = None

    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        result = a + b

    return render(request, "index.html", {"result": result})
