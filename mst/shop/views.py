from django.shortcuts import render, redirect
from .models import *
from math import ceil
from .forms import productForm
from django.contrib.sessions.models import Session

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.session.has_key('is_logged'):
        allProds = []
        catprods = product.objects.values('category', 'id')  # category gulo nicche set wise
        cats = {item['category'] for item in catprods}  # category item theke ki ki value paisi oita nilam
        for cat in cats:
            prod = product.objects.filter(category=cat)  # specific ekta category te koyta product ase
            n = len(prod)
            nSlides = n // 4 + ceil((n / 4) - (n // 4))
            allProds.append(
                [prod, range(1, nSlides), nSlides])  # ek ekta carousel e ki ki product thakbe ar length ki hobe !!
        # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
        # allProds = [[products, range(1, nSlides), nSlides],
        #             [products, range(1, nSlides), nSlides]]
        params = {'allProds': allProds}
        return render(request, 'shop/index.html', params)
    return redirect('login')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def prodView(request, myid):
    products = product.objects.filter(id=myid)  # specific ekta id te product fetch
    params = {'product': products[0]}
    return render(request, 'shop/prodview.html', params)  # list akare ase bole index 0 dite hoy


def checkout(request):
    return render(request, 'shop/checkout.html')


def login(request):
    if request.session.has_key('is_logged'):
        return redirect('/shop/index')

    if request.POST:
        u_email = request.POST['email']
        u_password = request.POST['password']
        print(u_email)
        print(u_password)
        # search in database
        count = user.objects.filter(email=u_email, password=u_password).count()
        if count > 0:
            request.session['is_logged'] = True
            return redirect('/shop/index')
        else:
            return redirect('/shop/login')

    return render(request, 'shop/login.html')


def signup(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        obj = user(username=username, email=email, password=password)
        obj.save()
        return redirect('/shop/login')


def logout(request):
    del request.session['is_logged']
    return redirect('/shop/login')


def userInfo_form(request):
    if request.POST:
        userfull_name = request.POST['userfull_name']
        phone_no = request.POST['phone_no']
        user_email = request.POST['user_email']
        user_company = request.POST['user_company']
        user_position = request.POST['user_position']
        obj = userInformation(userfull_name=userfull_name, phone_no=phone_no, user_email=user_email,
                              user_company=user_company, user_position=user_position)
        obj.save()
        return render(request, 'shop/userInfo_form.html')
    else:
        return render(request, 'shop/userInfo_form.html')

def userInfo_list(request):
    users = userInformation.objects.all()
    params = {'users': users}
    return render(request,'shop/userInfo_list.html',params)

def edit_user_info(request,uid):
    users = userInformation.objects.filter(userInformation_id=uid)
    params = {'users': users}
    return render(request,'shop/edit_user_info.html',params)

def update_user_info(request,uid):
    userInformation.objects.filter(userInformation_id=uid).update(
        userfull_name=request.POST['userfull_name'],
        phone_no=request.POST['phone_no'],
        user_email=request.POST['user_email'],
        user_company=request.POST['user_company'],
        user_position=request.POST['user_position'],

    )
    return redirect('/shop/userInfo_list')



def delete_user_info(request,uid):
    user = userInformation.objects.filter(userInformation_id=uid)
    user.delete()
    return render(request, 'shop/delete.html')

def add_product(request):
    if request.method=='POST':
        form=productForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'shop/add_product.html')
        else:
            form=productForm()
    return render(request, 'shop/add_product.html', {
        'form': form
    })