from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Mail
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Main page display
def base(request):
    context = {
        'messages' : Mail.objects.all(),
    }
    return render(request,'base.html', context)

# Messaging
class PostListView(ListView):
    model = Mail
    template_name = 'home.html'
    context_object_name = 'messages'
    ordering = ['-date_sent']

class PostDetailView(DetailView):
    model = Mail

# Create new message
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Mail
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update - Modify message
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Mail
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Delete message
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mail
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Profiles management
# Create account
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

#  Login to account
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account as been updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'partials/_profile.html', context)



