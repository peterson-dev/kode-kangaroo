from django import forms
from core.models import Snippet


class NewSnippetForm(forms.Form):
    title = forms.CharField(
        label='Title',
        max_length=55,
        widget=forms.TextInput(attrs={'required': True}),
    )
    language = forms.ChoiceField(
        label='Language',
        choices=Snippet.LANG_CHOICES, 
        required=True,
    )
    post_content = forms.CharField(
        label='',
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'add a new snippet','required': True}),
    )
    public = forms.BooleanField(
        initial=False,
        required=False,
        label='Public?',
        widget=forms.CheckboxInput
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
            print(data)
            return Snippet.objects.create(user=user, **data)
        return None
