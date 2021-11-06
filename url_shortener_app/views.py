import random
import string

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Url


class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url']

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith(('http:', 'https:', 'ftp:')):
            raise forms.ValidationError('Invalid URL. Allowed schemes: https,http,ftp')
        return url


def generate_random_key(length):
    letters = string.ascii_letters
    digits = string.digits
    random_key = ''.join(random.choice(letters + digits) for i in range(length))
    return random_key


def homepage(request):
    return render(request, 'homepage.html')


def create_user(request):
    form = UserCreationForm(request.POST or None)
    if form.is_bound and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('./url-tool')
    return render(request, 'register.html', {'form': form})


@login_required
def get_url_tool_page(request):
    form = UrlForm(request.POST or None)
    page_params = {
        'form': form,
    }
    if form.is_bound and form.is_valid():
        url = form.save(commit=False)
        url.user_id = request.user.id
        url.url_short = generate_random_key(5)
        url.save()
        page_params['url_short'] = url.url_short
    return render(request, 'url_tool_page.html', page_params)


def perform_redirect(request, url_key):
    url_info = Url.objects.get(pk=url_key)
    url_info.redirect_count += 1
    url_info.save()
    return redirect(url_info.url)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('./login')
