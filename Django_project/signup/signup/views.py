from django.contrib.auth import get_user_model
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from .tokens import account_activation_token
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import SignupForm

from .tokens import account_activation_token


def sign_up(request):
    if not request.user.is_authenticated:
        _next = request.GET.get("next")
        # breakpoint()
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                # save form in the memory not in database
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                # to get the domain of the current site
                current_site = get_current_site(request)
                mail_subject = "Activation link has been sent to your email id"
                message = render_to_string(
                    "acc_activate.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                )
                to_email = form.cleaned_data.get("email")
                # email = EmailMessage(
                email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
                email.attach_alternative(message, "text/html")
                email.send()
                messages.success(
                    request,
                    "Please check your email and confirm your email address to complete the registration",
                )
                if _next:
                    return HttpResponseRedirect(_next)
                return HttpResponseRedirect("/signup/")

        else:
            form = SignupForm()
        return render(request, "signup.html", {"form": form})
    else:
        return HttpResponseRedirect("/profile/")


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        messages.success(
            request,
            "Thank you for your email confirmation. Now you can login your account.",
        )
        return HttpResponseRedirect("/login/")
    else:
        return HttpResponseRedirect("/invalid/")
