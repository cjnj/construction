from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Review
from .forms import CreateForm
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request,'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def services(request):
    return render(request, 'blog/services.html')



# create/ list

class CreateReviewView(CreateView):
    model = Review
    template_name = "blog/create.html"
    form_class = CreateForm
    
    def get_success_url(self) -> str:
        return reverse('reviews')

# View / modify

class ListReviews(ListView):
    model = Review
    template_name = "blog/reviews.html"
    context_object_name = 'reviews'
    
    def get_queryset(self):
        return Review.objects.all()