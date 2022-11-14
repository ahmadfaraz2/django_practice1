from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from .forms import ContactForm
from .models import Page

# Create your views here.
def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink = pagename)
    ctx = {
        'title' : pg.title,
        'content' : pg.bodytext,
        'last_updated' : pg.update_date,
        'page_list' : Page.objects.all(),
    }
    return render(request, 'pages/page.html', ctx)







def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'koibemail@example.com'),
                ['siteowner@example.com'],
                connection=con
                
            )

            return HttpResponseRedirect('/contact?submitted=True')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
                

    ctx_cnt = {
        'form' : form,
        'submitted' : submitted,
        'page_list' : Page.objects.all(),
    }
    return render(request, 'pages/contact.html', ctx_cnt)    
