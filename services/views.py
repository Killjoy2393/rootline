from django.shortcuts import render, get_object_or_404
from .models import Service
from website.models import ServicesBlock, MetaData

def service_list(request):
    services = Service.objects.all()
    services_block = ServicesBlock.objects.last()
    meta = MetaData.objects.first()
    # return
    return render(request, 'services/service_list.html', {'services': services, 'services_block': services_block, 'meta': meta})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'services/service_detail.html', {'service': service})
