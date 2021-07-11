from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

messages = [
    {
        'sender' : 'John Doe',
        'title' : 'Inquiry 1',
        'content' : 'Lorem Ipsum',
        'sender' : '1 jan 2002',
    },
    {
        'sender' : 'Mary Jane',
        'title' : 'Inquiry 2',
        'content' : 'Lorem Ipsum',
        'sender' : '1 jan 2004',
    }
]

def base(request):
    context = {
        'messages' : Message.objects.all(),
    }
    return render(request,'base.html', context)

def register(request):
    form = UserCreationForm()
    return render(request, 'partials/_register.html')
