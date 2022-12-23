from django import forms
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"placeholder": _('Имя')}))
	email = forms.EmailField(max_length = 150, widget=forms.TextInput(attrs={"placeholder": _('Почта')}))
	phone = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={"placeholder": _('Номер')}))
	theme = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={"placeholder": _('Тема обращения')}))
	message = forms.CharField(max_length = 2000, widget=forms.Textarea(attrs={"placeholder": _('Коментарий')}))