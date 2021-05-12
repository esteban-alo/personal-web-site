from django.shortcuts import render, HttpResponse
from .models import Project


# Create your views here.
def portfolio(request: HttpResponse) -> HttpResponse:
    projects = Project.objects.all()  # Return all objects
    portfolio_context = {
        'projects': projects
    }
    return render(request, "portfolio/portfolio.html", context=portfolio_context)

