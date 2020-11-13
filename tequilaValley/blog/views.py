#from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post


""" posts = [
    {
        'author': 'Aby',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 18, 2020'
    },
    {
        'author': 'Dany',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 18, 2020'
    }
] """

# Create your views here.
def home(request):
    context = {
        # 'posts': posts
        'posts': Post.objects.all()
    }

    #return HttpResponse('<h1> Blog Home</h1>')
    #return render(request, 'blog/home.html')
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Order from latest to oldest

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):   # a form for creating a new post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): #Overwrite the user in the form
        form.instance.author = self.request.user
        return super().form_valid(form) # Verify the form

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #Only logged users can update a post
    def form_valid(self, form): #Overwrite the user in the form
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):    #Validate that only author can modify his post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog/'

    def test_func(self):    #Validate that only author can modify his post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    #return HttpResponse('<h1> This is about page </h1>')
    return render(request, 'blog/about.html', {'title': 'testingAbout'})
