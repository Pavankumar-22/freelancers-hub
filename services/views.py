from django.shortcuts import render, get_object_or_404
from .models import Service  # Ensure you have a Service model

# View to list all services
def service_list(request):
    services = Service.objects.all()  # Fetch all services from the database
    return render(request, 'services/service_list.html', {'services': services})

# View for service detail
def service_detail(request, id):
    service = get_object_or_404(Service, id=id)  # Fetch service by id
    return render(request, 'services/service_detail.html', {'service': service})
