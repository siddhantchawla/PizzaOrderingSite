from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login


from .forms import UserRegistrationForm, UserLoginForm
from .models import Size,Pizza,Topping,Type,Order,OrderManager

# User = settings.AUTH_USER_MODEL

# Create your views here.

@login_required(login_url='login/')
def home(request):
    context = {
            'offers' : "None for Now!"
    }
    
    return render(request, 'home.html', context)

@login_required(login_url='login/')
def menu(request):
    context = {
                    'menu': Pizza.objects.all(),
                    "toppings" : Topping.objects.all(),
                }
    # # print(context["menu"])
    # for item in context["menu"]:
    #     print(item)

    return render(request, 'menu.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            request.session['message'] = ''
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                messages.success(request, 'Registered Succesfully!')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Looks like the Username or Email is already taken!')
                # request.session['message'] = 'Looks like a username with that email or password already exists! Please Try again!'
                return HttpResponseRedirect('/register')
                # raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
      	form = UserRegistrationForm()

   
    return render(request, 'registration.html', {'form' : form})


def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            # email =  userObj['email']
            password =  userObj['password']

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request, 'Logged in Succesfully!')
                return HttpResponseRedirect('/')
             	
            else:
                messages.error(request, 'Password or Username is incorrect!')    
                return HttpResponseRedirect('/login')
                # raise forms.ValidationError('Looks like a username or password is wrong!')
    else:
        
      	form = UserLoginForm()
    
    return render(request, 'login.html', {'form' : form})



@login_required(login_url='login/')
def logout_page(request):
    messages.success(request, 'Logged Out Succesfully!')
    logout(request)
    return redirect('/login')



@login_required(login_url='login/')
def add_to_cart(request,product_id):
    p = int(product_id)
    print(p)
    if p is not None:
        product_obj = Pizza.objects.filter(id = p)
        print(product_obj)
        c,n = Order.objects.get_or_new(request)
        c.order.add(p)

        placed = c.order.all()
        # print(placed)
        total=0
        product_obj = product_obj.first()
        request.session['toppings'] = product_obj.toppings
        request.session['count'] = 0
        total += product_obj.price
        order_obj = Order.objects.filter(id=c.id)
        order_obj = order_obj.first()
        order_obj.subtotal = total
        q = Pizza.objects.filter(id=p)
        q = q.first()
        order_obj.name = str(q)
        print(q)
        order_obj.save()
        if q.toppings > 0:
            request.session['key'] = int(c.id)
            print(request.session['key'])
            order_obj.name += " ( "
            order_obj.save()
            if q.toppings==1:
                messages.success(request, f'Select your topping!')
            else:
                messages.success(request, f'Select your {q.toppings} toppings!')
            return redirect('/toppings')
    messages.success(request, 'Your order was added to the Cart!')
    return redirect("/menu")

@login_required(login_url='login/')
def get_cart(request):
    orders = Order.objects.filter(user = request.user)
    total = 0
    pizza = []
    # topp1 = []
    # topp2 = []
    # topp3 = []
    # print(orders)
    for order in orders:
        
        total += order.subtotal
        
    context = {
        'total' : total,
        'orders' : orders,
        'pizza' : pizza,
    }


    return render(request, "cart_home.html", context)


@login_required(login_url='login/')
def topping_menu(request):
    # print(request.session['key'])
    context = {
                    "toppings" : Topping.objects.all(),
                    
                }

    
    return render(request, 'toppings.html', context)


@login_required(login_url='login/')
def add_toppings(request,topping_id):
    
    t = int(topping_id)
    order = Order.objects.filter(id = request.session['key'])
    order = order.first()
    

    # print(order)
    # print(order.toppings)
    if(request.session['count'] == request.session['toppings']):

        order.name += " ) "
        order.save()
        messages.success(request, 'Your order was added to the Cart!')
        return redirect('/menu')

        

    else:
        request.session['count'] += 1

        order.toppings.add(t)
        
        q = Topping.objects.filter(id = t)
        q = q.first()

        order.name += str(q)
        if(request.session['toppings']-request.session['count']):
            order.name += " , "
        order.save()

        if(request.session['count'] == request.session['toppings']):

            order.name += " ) "
            order.save()
            messages.success(request, 'Your order was added to the Cart!')
            return redirect('/menu')
        messages.success(request, 'Select the next topping!')
        return redirect('/toppings')

@login_required(login_url='login/')
def remove_order(request,order_id):

    t = int(order_id)
    order = Order.objects.filter(id = t)
    order.delete()
    messages.success(request, 'Cart updated!')
    return redirect('/cart')




    




