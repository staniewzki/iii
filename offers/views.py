from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

def index(request):
    template = loader.get_template('index.html')
    context = {'data': 'lubie placki'}
    return HttpResponse(template.render(context, request))

@login_required(login_url="/accounts/login/")
def manage(request):
    template = loader.get_template('manage.html')
    context = {'data': 'zarządzam placki'}
    return HttpResponse(template.render(context, request))