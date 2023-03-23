from django.shortcuts import render, redirect
from .forms import ProfileForm, UserForm, UserUpdateForm
from .models import Profile

def create_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'profiles/create_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'profiles/update_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def delete_profile(request):
    user = request.user
    user.delete()
    return redirect('home')

