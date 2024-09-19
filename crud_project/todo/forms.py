# forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description'] 
        labels = {
            'title': '제목',  
            'description': '설명',
        }
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 300px;'}),
            'description': forms.Textarea(attrs={'style': 'width: 500px; height: 150px;'}),
        }