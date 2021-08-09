from django.shortcuts import render,redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    pizza = Pizza.objects.all()
    orders = Order.objects.filter(user = request.user)
    context = {'pizza' : pizza , 'orders' : orders}
    return render(request, 'index.html', context)

def order(request , order_id):
    order = Order.objects.filter(order_id=order_id).first()
    if order is None:
        return redirect('/')
    
    context = {'order' : order}
    return render(request , 'order.html', context)

@csrf_exempt
def order_pizza(request):
    user = request.user
    data=json.loads(request.body)
    try:
        pizza =Pizza.objects.get(id=data.get('id'))
        order = Order(user=user, pizza=pizza , amount = pizza.price)
        # print(order)
        order.save()
        new_order_id=Order.objects.values()
        order_list=list(new_order_id)[-1]
        return JsonResponse({'message':'Success','data':order_list})
    except Pizza.DoesNotExist:
        return JsonResponse({'error': 'Something went wrong'})
