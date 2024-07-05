from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q
from turtle import title
from book.models import Book
from member.models import Member
from bookloan.models import BookLoan
from datetime import timedelta
# Create your views here.

def lobby(request):
    context = {
        'title' : title
    }
    return render(request, 'index.html', context)

def home(request):
    today =  timezone.now().date()
    h3day = today + timedelta(days=3)

    overdue_loans = BookLoan.objects.filter(Q(due_date__lte=today) &  Q(return_date__isnull = True))
    outstand_loans = BookLoan.objects.filter(due_date__range=(today, h3day))
    bookloan_list = BookLoan.objects.all()
    count_book = Book.objects.all().count()
    count_member = Member.objects.all().count()
    count_bookloan = BookLoan.objects.all().count()
    count_overdue = overdue_loans.count()
    count_outstand = outstand_loans.count()
    count_all_over = count_overdue + count_outstand

    if 'username' in request.session:
        username = request.session['username']
        librarian_user = username
        
    else: 
        return redirect('librarian_login')
    
    context = {
        'librarian_user': librarian_user,
        'count_all_over': count_all_over,
        'overdue_loans': overdue_loans,
        'outstand_loans': outstand_loans,
        'bookloan_list': bookloan_list,
        'count_book': count_book,
        'count_member': count_member,
        'count_bookloan': count_bookloan

        }
    return render(request, 'home.html',context)




