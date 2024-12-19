from django import forms


class FeedbackForm(forms.Form):
    topic: forms.CharField = forms.CharField(error_messages={
        'required': 'Укажите тему обращения',
    }, min_length=3, max_length=100)
    email: forms.EmailField = forms.EmailField(error_messages={
        'required': 'Укажите E-mail',
    })
    text: forms.CharField = forms.CharField(widget=forms.Textarea, error_messages={
        'required': 'Укажите текст обращения',
    })
