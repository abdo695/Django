from django.shortcuts import render, redirect,get_object_or_404


from .models import *
from .forms import BookForm, CategoryForm, CreateForm

def abdo(request):
    return render(request,'pages/abdo.html')

def index(request):

    if request.method == 'POST':   #لو البيانات اللي مبعوته post
        add_book= BookForm(request.POST,request.FILES)
        if add_book.is_valid(): #لو صحيحه 
            add_book.save()
            return redirect('index') 


        add_category= CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save() 

    context = {
        'category':Category.objects.all(),#عشان امرر ال class هنا 
        'books': Book.objects.all(),
        'form':BookForm(),#عشان امرر الفورم هنا 
        'formcat': CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),# عشان تجيب اجمالي عدد الكتب
        'booksold':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavailble':Book.objects.filter(status='availble').count(),

         
    }
    return render(request,'pages/index.html',context)



def delete(request,id):
    book_delete = get_object_or_404(Book,id=id)
    if request.method =='POST':
        book_delete.delete()
        return redirect('index')


    return render(request,'pages/delete.html')



def books(request):
    search = Book.objects.all()

    title= None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    x =  {
        'category':Category.objects.all(),
        'books': search,
        'formcat': CategoryForm(),
            }
    return render(request,'pages/books.html',x)



def update(request,id):
    book_id =Book.objects.get(id=id)
    if request.method =='POST':
        book_save= BookForm(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            

    else:
        book_save= BookForm(instance=book_id)  

    context = {
        'form':book_save,
    }          
    return render(request,'pages/update.html',context)



def signup(request):
    return render(request,'pages/signup.html')

def login(request):
    # if request.method == 'POST':
    #     login_form = Create(request.POST)
    #     if login_form.is_valid():
    #         username = login_form.cleaned_data['username']
    #         password = login_form.cleaned_data['password']
    #         # منطق التحقق من صحة المستخدم
    # else:
    #     login_form = Create()
   






   
   
    return render(request,'pages/login.html')
def home(request):
    return render(request,'pages/home.html')
def courses(request):
    return render(request,'pages/courses.html')
def tasks(request):
    return render(request,'pages/tasks.html')
def account(request):
    return render(request,'pages/account.html')


# Create your views here.
