from django import forms
from core.models import Snippet
from django.core.validators import MaxLengthValidator

class NewSnippetForm(forms.Form):
    title = forms.CharField(
        validators=[MaxLengthValidator(150, message='Title exceeds 150 character limit')],
        widget=forms.TextInput(attrs={'placeholder': 'title', 'class': 'form-control form-control-lg','required': True}),
        label='',
    )
    post_content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'add a new snippet', 'class': 'form-control form-control-lg','required': True}),
    )
    language = forms.ChoiceField(
        choices=Snippet.LANG_CHOICES, 
        required=True,
        label='',
    )
    public = forms.BooleanField(
        initial=False,
        required=False,
        label='make public',
        widget=forms.CheckboxInput(attrs={'title': 'public?', 'class': 'form-check form-check-inline'}),
    )

    def save(self, user, *args, **kwargs):
        if self.is_valid():
            data = {
                'title': self.cleaned_data['title'], 
                'language': self.cleaned_data['language'], 
                'post_content': self.cleaned_data['post_content'],
                'public': self.cleaned_data['public'],
                }
            data.update(kwargs)
            return Snippet.objects.create(user=user, **data)
        return None
