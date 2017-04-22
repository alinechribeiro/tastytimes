from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from account.forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def get_index(request):
    #variables to @media image
    pagetitle = "Tasty Times"
    subtitle = "Enjoy it."
    # now return the rendered template
    return render(request, 'index.html', {'pagetitle':pagetitle, 'subtitle':subtitle})

def register(request):
    pagetitle = "Register"
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                email=form.cleaned_data['email'],
                card=form.cleaned_data['stripe_id'],  # this is currently the card token/id
                plan='REG_MONTHLY',
        )
            except stripe.error.CardError as e:
                messages.error(request, "Your card was declined")

            if customer:
                    user = form.save()
                    user.stripe_id = customer.id
                    user.subscription_end = arrow.now().replace(weeks=+4).datetime
                    user.save()
            if user:
                    auth.login(request, user)
                    messages.success(request, "You have successfully reqistered")
                    return redirect(reverse('profile'))


            else:
                    messages.error(request, "unable to log you in at this time")
        else:

                messages.error(request, "We were unable to take a payment with that card!")

    else:
        today = datetime.date.today()
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, "pagetitle": pagetitle}
    args.update(csrf(request))

    return render(request, 'register.html', args)

def profile(request):
    pagetitle= "Profile"
    subtitle= "This page is available after login succeded."
    return render(request, 'profile.html', {'pagetitle': pagetitle, 'subtitle':subtitle})

def login(request):
    pagetitle="Login"
    subtitle="Enter your data"
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))
 
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")
 
    else:
        form = UserLoginForm()
 
    args = {'form':form, 'pagetitle': pagetitle, 'subtitle': subtitle}
    args.update(csrf(request))
    return render(request, 'login.html', args)

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

