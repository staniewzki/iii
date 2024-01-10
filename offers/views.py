from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from .models import *

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def offers(request):
    template = loader.get_template('offers.html')
    context = {'offers': Offer.objects.all(), 'kind': request.GET['kind']}
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def manage(request):
    template = loader.get_template('manage.html')
    context = {}
    return HttpResponse(template.render(context, request))