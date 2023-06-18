from blog.models import Blog
from django import forms
#Форма для створення блогу
class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'theme', 'description', 'all_description', 'image', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class':'blog_input all_title'}),
            'theme': forms.TextInput(attrs={'class':'theme_input all_title'}),
            'description': forms.TextInput(attrs={'class':'description_input all_title'}),
            'all_description': forms.TextInput(attrs={'class':'all_input all_title'}),
            'image': forms.FileInput(attrs={'class':'image_input all_title'}),
            'author': forms.TextInput(attrs={'class':'author_input all_title'}),
        }

