from django import forms
from .models import Feedback


class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'first_name', 'last_name', 'number', 'email', 'message'}


# class FeedbackForm(forms.Form):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Имя')
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Фамилия')
#     e_mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input'}), label='E-mail')
#     number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input'}), label='Телефон')
#     message = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), label='Имя')
#
#     class Meta:
#         model = Feedback
#         fields = ['first_name', 'last_name', 'e_mail', 'number', 'message']

