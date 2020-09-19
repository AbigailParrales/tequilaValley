from django.shortcuts import render
#from django.http import HttpResponse

posts = [
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
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }

    #return HttpResponse('<h1> Blog Home</h1>')
    #return render(request, 'blog/home.html')
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1> This is about page </h1>')
    return render(request, 'blog/about.html', {'title': 'testingAbout'})
