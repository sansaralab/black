from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FirstScreenForm, ConcreteForm


def main(req):
    if req.method == 'POST':
        form = FirstScreenForm(req.POST)
        if form.is_valid():
            req.session['_old_post'] = req.POST
            return HttpResponseRedirect('/concrete')
    else:
        form = FirstScreenForm()

    return render(req, 'http_front/main/index.html', {
        'form': form
    })


def concrete(req):
    old_post = req.session.pop('_old_post')
    initial_identity = ''

    if req.method == 'POST':
        form = ConcreteForm(req.POST)
        if form.is_valid():
            # TODO: make complaint
            return redirect('/')

    first_form = FirstScreenForm(old_post)
    if first_form.is_valid():
        initial_identity = first_form.cleaned_data['identity']

    try:
        form
    except NameError:
        form = ConcreteForm(initial={'identity': initial_identity})

    return render(req, 'http_front/main/concrete.html', {
        'form': form
    })
