from django import forms


class FirstScreenForm(forms.Form):
    identity = forms.CharField(label="На кого жалуемся?", widget=forms.TextInput(attrs={'placeholder': 'На кого жалуемся?'}))


class ConcreteForm(forms.Form):
    identity = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'На кого жалуемся?'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': ''}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': ''}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': ''}))