from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Finch, Toy
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
    current_toy_ids = finch.toys.all().values_list('id')
    available_toys = Toy.objects.exclude(id__in=current_toy_ids)
    feeding_form = FeedingForm()
    return render (request, 'finches/detail.html', {
        'finch': finch,
         "feeding_form": feeding_form,
         'available_toys': available_toys
    })

def add_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def remove_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
  # validate the form
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'