from django.shortcuts import render, redirect, get_object_or_404
from .models import BookLoan
from .forms import BookLoanForm


# Create your views here.

def display_bookloan(request):
    bookloan_list = BookLoan.objects.all()
    context = {'bookloan_list':bookloan_list}
    return render(request, 'bookloan_list.html', context)


def add_bookloan(request):  
    if request.method == 'POST':
        form = BookLoanForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bookloan_list')
    else:
        form = BookLoanForm()
        print("GAGAL")
    return render(request, 'add_bookloan.html', {'form':form})


def edit_bookloan(request, bookloan_id):
    bookloan = get_object_or_404(BookLoan, id = bookloan_id)
   
    if request.method == "POST":
        form = BookLoanForm(request.POST, instance=bookloan)
        if form.is_valid():
            form.save()
            return redirect('bookloan_list')
    else:
        form = BookLoanForm(instance=bookloan)
    return render(request, 'edit_bookloan.html', {'form':form})


def delete_bookloan(request, bookloan_id):
    bookloan = get_object_or_404(BookLoan, id = bookloan_id)
    if request.method == 'POST':
        bookloan.delete()
        return redirect('bookloan_list')
    return render(request, 'delete_bookloan.html', {'bookloan':bookloan})
    