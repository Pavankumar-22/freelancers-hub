# blogs/views.py
from django.shortcuts import render

def blog_list(request):
    # Example data - replace with actual queryset or logic later
    blogs = [
        {'id': 1, 'title': 'First Blog', 'content': 'This is the first blog.'},
        {'id': 2, 'title': 'Second Blog', 'content': 'This is the second blog.'},
    ]
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    # Example logic for blog detail view
    blog = {'id': id, 'title': f'Blog {id}', 'content': f'This is blog {id}.'}
    return render(request, 'blogs/blog_detail.html', {'blog': blog})
