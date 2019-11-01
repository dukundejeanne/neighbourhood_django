from .models import Neighbour,Post,Profile,User,Rates
from django import forms
from django.forms import ModelForm,Textarea,IntegerField

class NewNeighbourForm(forms.ModelForm):
    class Meta:
        model=Neighbour
        exclude=['user','likes',]
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','date_posted']

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user','followers','following']
class VotesForm(forms.ModelForm):
    class Meta:
        model=Rates
        fields=('design','usability','content')

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model=Comment
#         fields=('comment',)

class NewsLetterForm(forms.Form):
    your_name=forms.CharField(label='First Name', max_length=40)
    email=forms.EmailField(label='Email')