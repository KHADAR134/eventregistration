from django.shortcuts import render
from .models import Participant
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)

def register(request):
    context = {}

    if request.method == 'POST':
        p1=Participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')
        p1.institution = request.POST.get('institution','-')

        if len(Participant.objects.all()) > 15:
            return render (request, 'eventappliction/failed.html',context)

        else:
            p1.save()
            return render (request, 'eventapplication/success.html',context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['institution'] = ''

    return render(request, 'eventapplication/register.html', context)

def listofparticipants(request):
    context = {}

    context['Participants'] = Participant.objects.all()

    return render(request, 'eventapplication/listofparticipants.html', context)

def success(request):
    context = {}
    return render(request, 'eventapplication/success.html', context)

def failed(request):
    context = {}
    return render(request, 'eventapplication/failed.html', context)