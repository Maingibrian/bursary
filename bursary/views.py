import os

from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import  UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from projectalfa import settings
from .decorators import *
from .form import *
from .models import  *


@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        form1 = universityform(request.POST)

        if form.is_valid() and form1.is_valid():
            # Save the userform independently
            user = form.save()
            group = Group.objects.get(name='institutions')
            user.groups.add(group)

            # Save the universityform and associate it with the user
            university_instance = form1.save(commit=False)
            university_instance.user = user
            university_instance.save()

            messages.success(request, "User and University details saved successfully.")
            return redirect("login_user")  # Redirect to the same page after registering the user and saving universityform

    else:
        form = CreateUserForm()
        form1 = universityform()

    context = {
        "form": form,
        "form1": form1,
    }
    return render(request, "registration.html", context)



@unauthenticated_user
def login_user(request):

        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or Password is not correct.")
                return redirect('login_user')
        else:
            return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('login_user')

@login_required(login_url="login_user")
@admin_only
def home(request):
    return render(request, "home.html")


@login_required(login_url="login_user")
@allowed_users(allowed_roles=["cdfofficials"])
def cdfofficial(request):
    institutions = institution.objects.all()
    form = chequeform()

    if request.method == 'POST':
        form = chequeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cdfofficial")

    for institution_obj in institutions:
        show_download_link = False
        download_path = ""

        # Check if there's a valid file for the current institution
        if institution_obj.Cheque:
            show_download_link = True
            download_path = institution_obj.Cheque.url

        institution_obj.show_download_link = show_download_link
        institution_obj.download_path = download_path

    context = {
        "form": form,
        "institutions": institutions
    }
    return render(request, "cdfofficial.html", context)


@login_required(login_url="login_user")
@allowed_users(allowed_roles=["institutions"])
def eduinstitution(request):
        institutions = request.user.university.institution_set.all()

        for institution_obj in institutions:
            show_download_link = False
            download_path = ""

            # Check if there's a valid file for the current institution
            if institution_obj.Cheque:
                show_download_link = True
                download_path = institution_obj.Cheque.url

            institution_obj.show_download_link = show_download_link
            institution_obj.download_path = download_path

        context = {
            "institutions": institutions
        }

        return render(request, "eduinstitution.html", context)


@login_required(login_url="login_user")
def beneficiary(request):
    show_download_link = False
    download_path = ""  # Add this line

    if request.method == 'POST':
        entered_phone = request.POST.get('phone')

        # Check if there's a matching phone in the institution model
        institution_obj = institution.objects.filter(phone=entered_phone).first()
        if institution_obj:
            show_download_link = True
            download_path = institution_obj.Cheque.url  # Adjust this line

    return render(request, "beneficiary.html", {'show_download_link': show_download_link, 'download_path': download_path})

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response ['Content-Disposition'] = 'inline;filename ='+os.path.basename(file_path)
            return response
    raise Http404


