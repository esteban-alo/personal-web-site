from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request: HttpResponse) -> render:
    return render(request, "core/home.html")


def about(request: HttpResponse) -> HttpResponse:
    return render(request, "core/about.html")


def portfolio(request: HttpResponse) -> HttpResponse:
    return render(request, "core/portfolio.html")


def contact(request: HttpResponse) -> HttpResponse:
    return render(request, "core/contact.html")

