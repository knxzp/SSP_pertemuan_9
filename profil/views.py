from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def activities(request):
    return render(request, "act.html")

def contact(request):
    return render(request, "contactme.html")

def hobby(request):
    return render(request, "hobby.html")            