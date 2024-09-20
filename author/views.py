from django.shortcuts import render,redirect
from .import forms
from django.contrib import messages
from .import models
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from car_post.models import CarPosts
# Create your views here.
def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            messages.success(request,'Account Created Successfuly')
            signup_form.save()
            return redirect('signup')
    else:   
        signup_form = forms.SignUpForm()
    return render(request,'sign_up.html',{'form':signup_form ,'type': 'Sign Up'})

#class base view
#user login class base view
class UserLoginView(LoginView):
    template_name = 'sign_up.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Incorrect Information')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context



def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            messages.success(request,'Profile Updated Successfuly')
            profile_form.save()
            return redirect('profile')
    else:   
        profile_form = forms.ChangeUserData(instance = request.user)
    return render(request,'edit_profile.html',{'form':profile_form })
    

@login_required
def profile(request):
    cars = CarPosts.objects.all()
    buy_history = models.BuyNow.objects.filter(user=request.user)
    return render(request,'profile.html', {'buy_history':buy_history,'cars':cars})
 

