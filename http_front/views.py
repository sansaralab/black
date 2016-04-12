from django.shortcuts import render, redirect
from .forms import FirstScreenForm


def main(req):
    if req.method == 'POST':
        form = FirstScreenForm(req.POST)
        if form.is_valid():
            return redirect('/concrete', identity=form.cleaned_data["identity"])
    else:
        form = FirstScreenForm()
    return render(req, 'http_front/main/index.html', {
        'form': form
    })


def concrete(req):
    pass
