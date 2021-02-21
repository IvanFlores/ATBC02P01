from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
# Models imports
from endpoints.models import Project
# Forms imports
from endpoints.forms import ProjectForm


def hello(request):
    return HttpResponse("Hello, you.")


def hello_name(request, name):
    return HttpResponse("Hello: " + name)


def index(request):
    return render(request, 'menu.html', {})


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    post = Project.objects.get(pk=pk)

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                lang=form.cleaned_data["lang"],
                code=form.cleaned_data["code"],
                post=post
            )
            project.save()

    projects = Project.objects.filter(post=post)
    context = {
        "post": post,
        "projects": projects,
        "form": form,
    }
    return render(request, "project_detail.html", context)


def project_new(request):

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                lang=form.cleaned_data["lang"],
                code=form.cleaned_data["code"],
            )
            project.save()
            return redirect('project_index')
    #context = {
    #    "projects": project,
    #    "form": form,
    #}

    return render(request, "project_edit.html", {'form': form})
