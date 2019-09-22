from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContact
# Create your views here.

def index(request):
    #return HttpResponse('Chao cac ban')
    return render(request,"Office/index.html")
def about(request):
    #return HttpResponse('Chao cac ban')
    return render(request,"Office/about.html")
def contact(request):
    #return HttpResponse('Chao cac ban')
    registered = False
    if request.method=="POST":
        form_contact = FormContact(data = request.POST)
        if form_contact.is_valid():
            register = form_contact.save()
            register.save()
            registered=True
    else:
        form_contact = FormContact()
    return render(request, "Office/contact.html",{'contact_form':form_contact, 'registered': registered})