from django.shortcuts import render,redirect
from car_post.models import CarPosts
from categories.models import Category
def home(request, category_slug = None):
    data = CarPosts.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = CarPosts.objects.filter(category = category)
    categories = Category.objects.all()
    return render(request,'home.html' ,{'data':data,'category':categories})