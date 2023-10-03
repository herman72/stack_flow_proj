from django import forms

from .models import Tag


class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox'}),
    )


class AnswerForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'max_length': 500}))

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if body.count('\n') > 4:
            raise forms.ValidationError("The body can have a maximum of 5 lines.")
        return body


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search...'}))


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tag name...'}),
        }
