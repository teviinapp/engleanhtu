from django.shortcuts import render
from first_app.models import Topic, Webpage
from django.http import HttpResponse
from . import forms
# Create your views here.

def webpage(request):
    webpage_list = Webpage.objects.order_by('name')
    web_dict={'webpages':webpage_list}
    return render(request,'first_app/webpage.html', context=web_dict)
def topic(request):
    topic_list = Topic.objects.all()
    top_dict={'topics':topic_list}
    return render(request,'first_app/topic.html', context=top_dict)

def detail(request, maso):
    
    return HttpResponse(str(maso))

def register(request):
    registered = False
    if request.method == "POST":        
        form_user = forms.UserForm(data = request.POST)
        form_por = forms.UserProfileInfoForm(data = request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()
            
            profile = form_por.save(commit = False)
            profile.user = user            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']            
            profile.save()
            
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = forms.UserForm()
        form_por = forms.UserProfileInfoForm()    
            
    return render(request, "first_app/registration.html", {'user_form':form_user, 'profile_form': form_por, 
                                                           'registered': registered})
