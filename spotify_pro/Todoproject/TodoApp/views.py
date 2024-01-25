from django.shortcuts import render,redirect
from .models import Songs
from .forms import SongForm

def Home(req):
    songfile=Songs.objects.all()
    return render(req,'index.html',{'songfile':songfile})
def Form(req):
    if req.method=="POST": 
        name=req.POST.get('name','')
        language=req.POST.get('language','')
        duration=req.POST.get('duration','')
        image=req.FILES['image']
        description=req.POST.get('description','')        
        song=Songs(name=name,language=language,duration=duration,image=image,description=description)
        song.save()
        return redirect('home')
    return render(req,'form.html')

def Details(req,id):
    songfile=Songs.objects.get(id=id)
    return render(req,'details.html',{'song':songfile})
