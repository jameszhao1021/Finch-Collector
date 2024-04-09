from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Finch
from .forms import FeedingForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    
    return render(request, 'finches/index.html', {
        'finches': finches,
       
    })

def finches_detail(request, finch_id):
    finch = get_object_or_404(Finch, pk=finch_id)
    feeding_form = FeedingForm()
    return render (request, 'finches/detail.html', {
        'finch': finch,
         "feeding_form": feeding_form
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
 
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'