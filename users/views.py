from django.shortcuts import render, redirect
#Built-in Registration Form of django
# Python classes that generates HTML forms
from django.contrib import messages
#Importing costumized forms created
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Messages class -> tags
# messages.debug/success/warning/info...
#


#Built-in login/logout views modules
#Password Reset View
from django.contrib.auth.views import PasswordResetView
# -----
# Personalized Password Reset View:
# subject_template_name -> txt file to include into subject
# html_email_template_name -> html text to be sent on email body
# -----
# https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.views.PasswordResetView

class PswResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    subject_template_name = 'users/password_reset.txt'
    html_email_template_name = 'users/password_email.html'


#Restriction to access HTML pages/views to users logged in
#   Note that if page is restricted, server redirect user to LOGIN_URL (settings.py)
from django.contrib.auth.decorators import login_required

def register(request):
    #Treat data passed through POST request
    #Note that at first page laod, the request method would be empty. Hence, return render executed
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #Sa ve form info to DB
            username = form.cleaned_data.get('username')    #Get user.usernam
            messages.success(request, f'Your acount has been created under {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})


#Decorator forcing a login to execute/access method
@login_required
#Profile template view once logged in on Blog
def profile(request):
    if request.method == 'POST':
                                # Get user info and populate into forms
        user_form = UserUpdateForm(request.POST, instance=request.user)
                                # request.POST/FILES -> Gets data info on input fields
        profile_form = ProfileUpdateForm(request.POST, 
                                        request.FILES,
                                        instance=request.user.profile )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f"Your account has been updated")
            return redirect('profile')
    
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }

    return render(request, 'users/profile.html', context)
