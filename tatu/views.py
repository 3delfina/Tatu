import os
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tatu.models import *
from tatu.forms import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.conf import settings

# Create your views here.

def index(request):
    context_dict = {}
    image_list = os.listdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media'))[1:4]
    context_dict['images'] = image_list
    return render(request, 'tatu/index.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request,
                  'tatu/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                    'registered': registered
                   })


def login(request):
    return HttpResponse("""Login page
    <a href="/tatu/">Index</a>""")

def artists(request):
    return HttpResponse("""Artists page
    <a href="/tatu/">Index</a>""")

def tattoos(request):
    return HttpResponse("""Tattoos page
    <a href="/tatu/">Index</a>""")

#def about(request):
#    return HttpResponse("""About page
#    <a href="/tatu/">Index</a>""")


    #user = UserProfile.objects.get(pk=1)
    #image_list = user.images.all()

def contact(request):
    return HttpResponse("""Contact us page
    <a href="/tatu/">Index</a>""")

def faq(request):
    return HttpResponse("""FAQ page
    <a href="/tatu/">Index</a>""")


