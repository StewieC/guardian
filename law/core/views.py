from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Incident, Article, Case, Lawyer
from .forms import IncidentForm, CaseForm

def home(request):
    incidents = Incident.objects.all().order_by('-created_at')[:5]
    return render(request, 'core/home.html', {'incidents': incidents})

@login_required
def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reported_by = request.user
            incident.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'core/report_incident.html', {'form': form})

def incident_list(request):
    incidents = Incident.objects.all().order_by('-created_at')
    return render(request, 'core/incident_list.html', {'incidents': incidents})

def article_list(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'core/article_list.html', {'articles': articles})

def contact_authorities(request):
    return render(request, 'core/contact_authorities.html')

@login_required
def file_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.filed_by = request.user
            case.save()
            return redirect('home')
    else:
        form = CaseForm()
    return render(request, 'core/file_case.html', {'form': form})

def find_lawyer(request):
    lawyers = Lawyer.objects.all()
    return render(request, 'core/find_lawyer.html', {'lawyers': lawyers})