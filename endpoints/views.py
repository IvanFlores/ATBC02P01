import logging
import os

from endpoints.core.factory import Factory
from endpoints.core.python_parameters import PythonParameters
from endpoints.core.java_parameters import JavaParameters

from django.core.files import File
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
# Models imports
from endpoints.models import Project
# Forms imports
from endpoints.forms import ProjectForm, ProjectEditForm, ProjectTestForm, ProForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'menu.html', {})


def hello(request):
    return HttpResponse("Hello, you.")


def hello_name(request, name):
    return HttpResponse("Hello: " + name)


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "project_index.html", context)


def project_new(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                name=form.cleaned_data["name"],
                lang=form.cleaned_data["lang"],
                code_challenge=form.cleaned_data["code_challenge"],
            )
            project.save()
            return redirect('project_index')
    return render(request, "project_new.html", {'form': form})


def edit(request, pk=None, template_name='project_template.html'):
    if pk:
        project = get_object_or_404(Project, pk=pk)
    else:
        project = Project(pk=pk)
    form = ProForm(request.POST or None, instance=project)
    if request.POST and form.is_valid():
        form.save()
        return redirect('/../endpoints/index')
    return render(request, template_name, {
        'form': form
    })


def delete(request, pk):
    # Retrieve de project instance an delete it.
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('/../endpoints/index')


def project_solve(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "project_solve.html", {'project': project})


def project_run(request):
    typ = ''
    if 'lang' in request.GET:
        lang = request.GET['lang']
        if lang.lower() == 'java':
            file = 'endpoints/projects/main.java'
            typ = 'java'
        else:
            file = 'endpoints/projects/main.py'
            typ = 'python'
    else:
        lang = "No lang"
        file = 'main.py'
    logger.error(file)
    if 'code' in request.GET:
        code = request.GET['code']
        if len(code) is 0:
            if lang.lower() == 'java':
                code = 'package projects;\npublic class main{public static void main(String[] args) ' \
                       '{\n\t\tSystem.out.println("No code submitted in Java!");\n\t}\n}'
            else:
                code = 'print("No code submitted in python!")'
    else:
        code = 'Error reading the code.'
    #logger.error(file+": "+code)
    f = open(file, 'w')
    my_file = File(f)
    my_file.write(code)
    f.close()
    result = run_factory(typ)
    return render(request, 'message.html', {"message": result.get_result()})

    #return render(request, 'message.html', {'message': 'Save ' + lang + ' code complete: ' + code})


def project_edit(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectEditForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(
                name=form.cleaned_data["name"],
                lang=form.cleaned_data["lang"],
                code_challenge=form.cleaned_data["code_challenge"],
            )
            project.save()
    context = {
        "project": project,

        "form": form,
    }
    return render(request, "project_edit.html", context)


def run_factory(typ):
    factory = Factory()
    if typ == 'java':
        parameters = JavaParameters(r'C:\Program Files\Java\jdk1.8.0\bin\java',
                                     r'E:\Git\ATBC02P01\endpoints', 'projects')
    else:
        parameters = PythonParameters(r'C:\Python\Python39\python',
                                     r'endpoints', 'projects')

    result = factory.run_project(parameters, typ)
    print("Result:\n\t " + result.get_result())
    return result

