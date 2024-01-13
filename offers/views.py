from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .models import *
from datetime import datetime, timedelta

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
    begin = datetime.strptime(request.POST['begin'], '%Y-%m-%d')
    end = datetime.strptime(request.POST['end'], '%Y-%m-%d')
    day = timedelta(days=1)
    frame = get_object_or_404(Availability,
        offer_id=offer_id,
        begin__lte=begin.date(),
        end__gte=end.date(),
    )
    new_frame = Availability(offer=frame.offer, begin=(end + day).date(), end=frame.end)
    frame.end = (begin - day).date()
    frame.save(), new_frame.save()
    Booking(owner=request.user.appuser, offer=frame.offer, begin=begin.date(), end=end.date()).save()
    return redirect('manage')

@login_required(login_url="/accounts/login/")
def manage(request):
    template = loader.get_template('manage.html')
    context = {
        'bookings': Booking.objects.filter(owner=request.user.appuser),
    }
    return HttpResponse(template.render(context, request))