from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout and auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash as update_session
from django.views.decorators.http import require_POST


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method = "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = UserCreationForm()
    context = {'form': form, }
    return render(request, 'articles/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = AuthenticationForm(request.POST, request)
        if form.is_valid():
            auth_login(request, form.get.user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    request.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)


@login_required
def change_password(request):
    if request.method = 'POST':
        form = PasswordChangeForm(request, request.POST)
        if form.is_valid():
            user = form.save()
            update_session(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm()
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)
