from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic  import DetailView, ListView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from .models import Profile, Article

# Create your views here.
# class Profile():
#     def __init__(self, name, email, age):        
#         self.name = name 
#         self.email = email
#         self.age = age

# profiles = [
#     Profile('Austin', 'austin@example.com', 33),
#     Profile('Dom', 'Dom@example.com', 28),
#     Profile('Diego', 'Diego@example.com', 30),
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profiles_index(request):
    profiles = Profile.objects.all()
    # profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/index.html', {'profiles': profiles})

def profiles_detail(request, profile_id):
  profile = Profile.objects.get(id=profile_id)
  return render(request, 'profiles/detail.html', { 'profile': profile })
# def profiles_detail(request, profile_id):
#     profile = Profile.objects.get(id=profile_id)
#     return render(request, 'profiles/detail.html', {
#         'profile': profile,
#     })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class ProfileCreate( CreateView):
    model = Profile
    fields = '__all__' 

class ProfileUpdate( UpdateView):
    model = Profile
    fields = ['bio', 'location', 'age']    

class ProfileDelete( DeleteView):
    model = Profile
    success_url = '/profiles/'