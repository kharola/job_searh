from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .forms import JobForm
import requests

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

@login_required
def job(request):
    result = {}

    if request.method == 'GET':
        form = JobForm(request.GET)
        if form.is_valid():
            description = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            endpoint = 'https://jobs.github.com/positions.json?{description}&{location}'
            url = endpoint.format(description=description, location=location)
            try:
                response = requests.get(url, headers={"Accept":"application/json"})
                result = response.json()
            except:
                result = {'internet':'internet connection error'}

    return render(request, "list_view.html", {'form':form,'data':result})

@login_required
def jobdetail(request, pk):
    detail_result = {}
    endpoint = 'https://jobs.github.com/positions/{pk}.json'
    url = endpoint.format(pk=pk)
    response = requests.get(url, headers={"Accept":"application/json"})
    detail_result = response.json()
    return render(request, 'detail.html',{'detail_data':detail_result})
