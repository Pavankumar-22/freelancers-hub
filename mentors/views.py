# mentors/views.py
from django.shortcuts import render

def mentor_list(request):
    # Example data
    mentors = [
        {'id': 1, 'name': 'John Doe', 'expertise': 'Web Development'},
        {'id': 2, 'name': 'Jane Smith', 'expertise': 'Data Science'},
    ]
    return render(request, 'mentors/mentor_list.html', {'mentors': mentors})

def mentor_detail(request, id):
    # Example data
    mentor = {'id': id, 'name': f'Mentor {id}', 'expertise': 'Sample Expertise'}
    return render(request, 'mentors/mentor_detail.html', {'mentor': mentor})
