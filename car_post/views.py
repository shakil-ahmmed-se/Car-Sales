from django.shortcuts import render,redirect
from .import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages

def detail_post_view(request, id):
    cars = models.CarPosts.objects.get(id=id)
    
    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.cars = cars
            new_comment.save()
    
    comments = cars.comments.all()
    comment_form = forms.CommentForm()
    
    context = {
        'cars': cars,
        'comments': comments,
        'comment_form': comment_form
    }
    
    return render(request, 'car_details.html', context)



@login_required
def buy_car(request, id):
    car = models.CarPosts.objects.get(id=id)
    cars = models.CarPosts.objects.all()
    if car.quantity > 0:
        models.BuyNow.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
        messages.success(request, 'Car Buy Successfully')
        return render(request, 'profile.html',{'cars':cars}) 
    else:
        messages.error(request, 'Car is out of stock')
    return render(request, 'profile.html',{'cars':cars})



