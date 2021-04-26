# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Posts


# Create your views here.

class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
