from django.shortcuts import render, redirect
from .import forms
from .import models
# Create your views here.
# def add_categorie(request):
#     if request.method == 'POST':
#         category_form = forms.CategoryForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return redirect('add_categorie')
#     else:
#         category_form = forms.CategoryForm()
#     return render(request, 'add_category.html' ,{'form':category_form})
def add_category(request):
    category = models.Category.objects.all()
    return render(request, 'home.html', {'category':category})