from django import forms
from .models import Parent, Children, Leader, Post, Squad, Camp

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ('last_name', 'first_name', 'middle_name', 'contact_phone')

class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ('last_name', 'first_name', 'middle_name', 'contact_phone', 'birthday')

class LeaderForm(forms.ModelForm):
    class Meta:
        model = Leader
        fields = ('last_name', 'first_name', 'middle_name', 'contact_phone')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'created_date', 'published_date')

class SquadForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ('nick', 'slogan')

class CampForm(forms.ModelForm):
    class Meta:
        model = Camp
        fields = ('title', 'label')