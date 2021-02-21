from django.shortcuts import render

from .models import Participants,ParticipantsAdmin
# Create your views here.
def home(request):
    context={}
    return render(request,"eventapplication/home.html",context)

def register(request):
    context={}
    if request.method == 'POST':
        p1 = Participants()
        p1.username = request.POST.get('username','-')
        p1.email= request.POST.get ('email','-')
        p1.contnum=request.POST.get('contnum','000') 
        p1.inst= request.POST.get('inst','-')

        if len(Participants.objects.all())>15: 
            return render(request,'eventapplication/fail.html') 
        else:
            p1.save()
            return render(request,'eventapplication/success.html',context)  
    if request.method == 'GET':
        context['username']=''
        context['email']=''
        context['contnum']=''
        context['inst']=''

    return render(request,"eventapplication/register.html",context)
    
def listofparticipants(request):
    context={}
    context['participants']= Participants.objects.all()
    return render(request,"eventapplication/listofparticipants.html",context)

def success(request):
    context={}
    return render(request,"eventapplication/success.html",context)

