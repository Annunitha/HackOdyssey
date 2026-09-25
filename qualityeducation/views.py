from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import bleach

from .models import qualityeducation
from .forms import SignUpForm, qualityeducationForm


def home_view(request):
    if request.user.is_authenticated:
        user_qualityeducation = qualityeducation.objects.filter(user=request.user)
        return render(request, 'home.html', {'user_qualityeducation': user_qualityeducation})
    return redirect('login')


@login_required
def qualityeducation_add(request):
    if request.method == 'POST':
        form = qualityeducationForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.user = request.user
            new_instance.save()
            return redirect('home')
    else:
        form = qualityeducationForm()
    return render(request, 'notes_add.html', {'form': form})


@login_required
def qualityeducation_detail(request, pk):
    qualityeducation_instance = get_object_or_404(qualityeducation, pk=pk)
    allowed_tags = [
        'a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'li', 'ol', 'strong', 'ul',
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'br', 'span'
    ]
    sanitized_description = bleach.clean(
        qualityeducation_instance.description,
        tags=allowed_tags,
        strip=True,
    )
    return render(
        request,
        'qualityeducation_detail.html',
        {'qualityeducation_instance': qualityeducation_instance, 'sanitized_description': sanitized_description},
    )


@login_required
def qualityeducation_edit(request, pk):
    qualityeducation_instance = get_object_or_404(qualityeducation, pk=pk)
    if request.method == 'POST':
        form = qualityeducationForm(request.POST, instance=qualityeducation_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes Saved!')
            return redirect('home')
    else:
        form = qualityeducationForm(instance=qualityeducation_instance)
    return render(request, 'notes_edit.html', {'form': form, 'qualityeducation_instance': qualityeducation_instance})


@login_required
def qualityeducation_delete(request, pk):
    qualityeducation_instance = get_object_or_404(qualityeducation, pk=pk)
    if request.method == "POST":
        qualityeducation_instance.delete()
        return redirect('home')
    return render(request, 'qualityeducation_delete.html', {'qualityeducation_instance': qualityeducation_instance})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in!')
            return redirect('home')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})