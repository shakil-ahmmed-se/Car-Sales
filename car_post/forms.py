from django import forms
from .models import CarPosts,Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = CarPosts
        fields = '__all__'

        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
    