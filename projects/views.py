from django.shortcuts import render, get_object_or_404
from .models import Project, MetaData

def project_list(request):
    projects = Project.objects.all()
    meta = MetaData.objects.first()
    return render(request, 'projects/project_list.html', {'projects': projects, 'meta': meta})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})
