from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FirstScreenForm, ConcreteForm, SearchForm
from complaints_manager import service


def main(req):
    if req.method == 'POST':
        form = FirstScreenForm(req.POST)
        if form.is_valid():
            req.session['_old_post'] = req.POST
            return HttpResponseRedirect('/concrete')
        search_form = SearchForm(req.POST)
        if search_form.is_valid():
            req.session['_old_post'] = req.POST
            return HttpResponseRedirect('/search')
    else:
        form = FirstScreenForm()
        search_form = SearchForm()

    return render(req, 'http_front/main/index.html', {
        'form': form,
        'search_form': search_form
    })


def concrete(req):
    old_post = req.session.pop('_old_post')
    initial_identity = ''

    if req.method == 'POST':
        form = ConcreteForm(req.POST)
        if form.is_valid():
            service.make_complaint(
                form.cleaned_data['identity'],
                form.cleaned_data['content'],
                form.cleaned_data['category']
            )
            req.session['_old_post'] = {'template': form.cleaned_data['identity']}

            return HttpResponseRedirect('/search')

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


def search(req):
    if req.method == 'POST':
        post = req.POST
    else:
        post = req.session.pop('_old_post')

    search_form = SearchForm(post)
    complaints = []

    if search_form.is_valid():
        complaints = service.search_complaints(search_form.cleaned_data['template'])

    return render(req, 'http_front/main/search.html', {
        'form': search_form,
        'complaints': complaints
    })
