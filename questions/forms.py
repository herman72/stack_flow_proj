from django import forms

from .models import Question, Answer, Tag


class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
    )


class AnswerForm(forms.ModelForm):
    pass


class SearchForm(forms.Form):
    pass


class TagForm(forms.ModelForm):
    pass
