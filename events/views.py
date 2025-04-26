from django.shortcuts import render,redirect
#from django.http import HttpResponse
from .models import User,Event,Submission
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import submission_form
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        # Try to authenticate directly
        user = authenticate(request, username=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            # Add some error message here for invalid credentials
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'login.html', {})

def user_logout(request):
    logout(request)
    return redirect('Home')

def user_register(request):

    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')


         
        user=User(name=username,email=email)
        user.username = email 
        user.set_password(password)
        user.save()

        login(request,user)
        return redirect('Home')


    return render(request,'register.html',{})


@login_required(login_url='/login_user/')
def user_profile(request,pk):
    user=User.objects.get(id=pk)

    context={
        'user':user
    }

    return render(request,'user_profile.html',context)



def home_page(request):
    Events=Event.objects.all()
    participants=User.objects.filter(participant=True)

    context={
        'events':Events,
        'participants':participants
    }

    return render(request,'Home.html',context)


@login_required(login_url='/login')
def event_details(request,pk):
    event=Event.objects.get(id=pk)
    submitted=Submission.objects.filter(user=request.user,event=event).exists()

    context={
        'event':event,
        'submitted':submitted
    }
    return render(request,'Event_details.html',context)

@login_required(login_url='/login')
def event_confirmation(request,pk):
    event=Event.objects.get(id=pk)
    if request.method=="POST":
        #print('getting')
        event = Event.objects.get(id=pk)  # Or get it from the form or URL
        event.participants.add(request.user)
        #print(request.user)
        return redirect('Home')
    
    context={
        'event':event
    }
    
    return render(request,'confirmation.html',context)


@login_required(login_url='/login')
def project_submission(request,pk):
    event=Event.objects.get(id=pk)
    form=submission_form()
     

    if request.method=='POST':
        form=submission_form(request.POST)
        if form.is_valid():
            Submission=form.save(commit=False)
            Submission.user=request.user
            Submission.event=event
            Submission.save()
            return redirect('Home')

    context={
        'event':event,
        'form':form
    }

    return render(request,'project_submission.html',context)


@login_required(login_url='/login')
def project_update(request,pk):
    sub=Submission.objects.get(id=pk)
    print(sub)
    event=sub.event
    form=submission_form(instance=sub)


    if request.method=="POST":
        form=submission_form(request.POST,instance=sub)
        if form.is_valid():
            form.save()
            return redirect('user_profile',request.user.id)
    context={
        'form':form,
        'event':event
    }

    return render(request,'project_submission.html',context)


