from turtle import title
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormLogin, FormRegister
from .models import Librarian, LoginHistory
import secrets


# Create your views here.
def librarian_list(request):
    librarian_list = Librarian.objects.all()
    context = {
        'librarian_list':librarian_list
        }
    return render(request, 'librarian_list.html', context)

def librarian_register(request):
    if request.method == 'POST':
        form = FormRegister(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/librarian/login')
    else:
        form = FormRegister()
        print("GAGAL")
    return render(request, 'librarian_register.html', {'form':form})


def librarian_login(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                librarian = Librarian.objects.get(username = username)
                if password == librarian.password:
                    token = secrets.token_hex(20)
                    # Store Username
                    LoginHistory.objects.create(librarian=librarian)
                    request.session['token'] = token
                    request.session['username'] = username
                    print(username, token)
                    return redirect('/home')
                else:
                    form.add_error(None, 'Password Salah')
            except Librarian.DoesNotExist:
                form.add_error(None, 'Username Tidak ada')
    else:
        form = FormLogin()
    return render (request, 'librarian_login.html', {'form':form})

def librarian_profile(request):
    if 'username' in request.session:
        username = request.session['username']
      
    else: 
        return redirect('librarian_login')
    
    librarian_profile = Librarian.objects.get(username = username)
    context = {
        'librarian' : librarian_profile}
    return render(request, 'librarian_profile.html', context)



def librarian_logout(request):
    # Clear token and username from session
    if 'token' in request.session:
        del request.session['token']
        del request.session['username']
        print('deleting token')
    return redirect('librarian_login') 


def librarian_edit(request, librarian_id):
    librarian = get_object_or_404(Librarian, id = librarian_id)
    if request.method == "POST":
        form = FormRegister(request.POST, instance=librarian)
        if form.is_valid():
            form.save()
            token = secrets.token_hex(20)
            request.session['token'] = token
            request.session['username'] = librarian.username
            return redirect('librarian_profile')
    else:
        form = FormRegister(instance=librarian)

    context = {
        'form':form,
        'librarian':librarian
    }
    return render(request, 'edit_librarian.html', context)



def librarian_delete(request, librarian_id):
    librarian = get_object_or_404(Librarian, id = librarian_id)
    if request.method == 'POST':
        librarian.delete()
        del request.session['token']
        del request.session['username']
        print('deleting token')
        return redirect('librarian_login')
    
    context = {
        'librarian':librarian

    }
    return render(request, 'delete_librarian.html', context)

def librarian_login_history(request):
    librarian_login_history = LoginHistory.objects.all()
    librarian_login_history = librarian_login_history.order_by('-date_login')
    context = {'librarian_login_history':librarian_login_history}
    return render(request, 'login_history.html', context)
