from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .models import *

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def offers(request):
    template = loader.get_template('offers.html')
    context = {
        'kind': request.GET['kind'],
        'begin': request.GET['begin'],
        'end': request.GET['end'],
        'offers': Offer.objects.filter(
            kind=request.GET['kind'],
            availability__begin__lte=request.GET['begin'],
            availability__end__gte=request.GET['end'],
        ),
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def book(request, offer_id):
    frame = get_object_or_404(Availability,
        offer_id=offer_id,
        begin__lte=request.POST['begin'],
        end__gte=request.POST['end'],
    )
    new_frame = Availability(offer=frame.offer, begin=request.POST['end'])
    # todo: implement logic
    return redirect('manage')

@login_required(login_url="/accounts/login/")
def manage(request):
    template = loader.get_template('manage.html')
    context = {}
    return HttpResponse(template.render(context, request))