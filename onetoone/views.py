from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import College, Principle
# Create your views here.

def onetoone(request):
    colleges = College.objects.all()
    context = {
        'allColleges' : colleges,
    }
    return render(request, 'onetoone/index.html',context)

def detail(request, college_id):
    college = College.objects.get(id=college_id)
    context = {
        'college' : college
    }
    return render(request, 'onetoone/detail.html', context)