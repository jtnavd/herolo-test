from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message
from .forms import UserRegisterForm

def base(request):
    context = {
        'messages' : Message.objects.all(),
    }
    return render(request,'base.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} account's created!")
            return redirect('base-page')
    else:
        form = UserRegisterForm()
    return render(request, 'partials/_register.html', {'form':form})

def profile(request):
    return render(request, 'partials/_profile.html')

