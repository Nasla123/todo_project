from django.shortcuts import render,redirect
from .models import task
from .forms import ModelForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model=task
    template_name='home.html'
    context_object_name='obj'
    success_url=reverse_lazy('taskList')

class TaskDetailView(DetailView):
    model=task
    template_name='detail.html'
    context_object_name='i'

class TaskUpdateView(UpdateView):
    model=task
    template_name='update.html'
    context_object_name='task'
    fields=('name','priority','date')
    def get_success_url(self):
         return reverse_lazy('taskdetail', kwargs={'pk': self.object.id})




class TaskDeleteView(DeleteView):
    model=task
    template_name='delete.html'
    success_url=reverse_lazy('taskList')


def home(request):
    obj1=task.objects.all()

    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj = task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'home.html',{'obj':obj1})

# def delete(request,task_id):
#     tasks=task.objects.get(id=task_id)
#     if request.method=='POST':
#         tasks.delete()
#         return redirect('/')
#     return render(request,'delete.html',{'task':task})

# def update(request,id):
#     task1=task.objects.get(id=id)
#     form=ModelForm(request.POST or None,instance=task1)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'update.html',{'form':form,'tasks':task1})
