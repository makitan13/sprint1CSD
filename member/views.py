from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm

# Create your views here.

def member_list(request):
    member_list = Member.objects.all()
    context = {'member_list':member_list}
    return render(request, 'member_list.html',context)

def member_login(request):
    
    return render(request, 'member_login.html')

def member_register(request):
   
    return render(request, 'member_register.html')


def add_member(request):  
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
        print("GAGAL")
    return render(request, 'add_member.html', {'form':form})


def edit_member(request, member_id):
    member = get_object_or_404(Member, id = member_id)
   
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'edit_member.html', {'form':form})


def delete_member(request, member_id):
    member = get_object_or_404(Member, id = member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'delete_member.html', {'member':member})