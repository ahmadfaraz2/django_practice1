from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import QuoteForm
from .models import Quote

from pages.models import Page


def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  #method to save form data in our database.
            #assert False
            return HttpResponseRedirect('/quote/?submitted=True')

    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True

    ctxquote = {
        'submitted' : submitted,
        'form' : form, 
        'page_list' : Page.objects.all()
    }


    return render(request, 'quotes/quote.html', ctxquote)                


