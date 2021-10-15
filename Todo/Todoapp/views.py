from django.shortcuts import render,redirect,get_object_or_404
from .models import *

from .forms import taskform


# Create your views here.




def homepage(request):
    
    

    form = taskform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    todo = Todo.objects.all()

    


    

    
    


    return render(request,'index.html',{'form':form,'todo':todo})
def delete(request,pk):
    tod = Todo.objects.get(id=pk)
    tod.delete()
    return redirect('/')

    
    return render(request,'delete.html',{'tod':tod})

def update(request,pk):
    upgrade = get_object_or_404(Todo,id=pk)
    
    form = taskform(request.POST or None, instance=upgrade)
    if form.is_valid():
        upgrade = form.save(commit= False)
        upgrade.save()
        return redirect('/')
        
    return render(request,'update.html',{'form':form})
    
def details(request):
    
    return render(request,'details.html')    