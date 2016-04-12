from django import forms


class FirstScreenForm(forms.Form):
    identity = forms.CharField(label="На кого жалуемся?",
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'На кого жалуемся?', 'autofocus': ''}))


class ConcreteForm(forms.Form):
    identity = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'На кого жалуемся?', 'autofocus': ''}))
    category = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Категория действия'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Подробное описание проблемы'}))
