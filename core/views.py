from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

from .models import Product


def home(request):
    products = Product.objects.filter(is_sold=False)
    context = {'products':products,'page_obj':products}
    return render(request,'core/front-page.html',context)

@login_required(login_url='signup')
def product_like(request,pk):
    if request.user.is_authenticated:
        products = Product.objects.get(id=pk)
        if products.likes.filter(id=request.user.id):
            products.likes.remove(request.user.id)
            return redirect('home')
        else:
            products.likes.add(request.user.id)
            return redirect('home')
    else:
        return redirect('signup')

def search(request):
    query = request.GET.get('q','')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(discription__icontains=query))
    context = {'query':query,'products':products}
    return render(request,'core/search.html',context)


@login_required(login_url='signup')
def product_detail(request,pk):
    product = get_object_or_404(Product,id=pk)
    host  = request.get_host()
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,#PAYPAL_RECEIVER_EMAIL
        'amount': product.price,
        'item_name': product.name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('success',kwargs={'pk':pk})}",
        'cancel_url': f"http://{host}{reverse('failed',kwargs={'pk':pk})}",
    }
    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout) 
    context = {'product':product,'paypal':paypal_payment}
    return render(request,'core/detail.html',context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        email = request.POST.get('email').lower()
        password = request.POST.get('password').lower()
        password2 = request.POST.get('password2').lower()
        users = User.objects.filter(username=username,email=email).exists()
        if users:
            messages.info(request,'User Exists')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('signup')
        # if username and password is  None:
        #     messages.error(request,'Something went wrong')
        #     return redirect('signup')
        if password == password2:
            user = User.objects.create_user(username=username,email=email,password=password)
            login(request,user)
            return redirect('home')
        if password is None:
            return redirect('signup')
        else:
            messages.info(request,'Something went wrong')
            return redirect('signup')
            
    context = {}
    return render(request,'core/signup.html',context)


def userlogin(request):
     if request.user.is_authenticated:
        return redirect('home')
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        # if user is not User:
        #     messages.info(request,'Password is not valid')
        #     return redirect('login')
        login(request,user)
        return redirect('home')
        if username and password is None:
         messages.info(request,'Something went wrong')
         return redirect('login')
        else:
          return redirect('login')
     context = {}
     return render(request,'core/login.html',context)

@login_required(login_url='signup')
def userlogout(request):
    logout(request)
    return redirect('login')


def paymentsuccess(request,pk):
    product = get_object_or_404(Product,id=pk)
    context = {'product':product}
    return render(request,'core/success.html',context)

def paymentfailed(request):
    context = {}
    return render(request,'core/failed.html',context)