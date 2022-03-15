from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import datetime
import json

# Create your views here.

def index(request):
    #query all rides
    rides = Ride.objects.all().order_by("date")
    context = {"rides":rides}
    return render(request, "rides/index.html", context)

def myTickets(request):
    #check who is logged in
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer).order_by("-date_ordered")


    else:
        orders = []

    context = {"orders":orders,}
    return render(request, "rides/my-tickets.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        tickets = order.orderticket_set.all()
    else:
        tickets = []

    context = {"tickets":tickets}
    return render(request, "rides/cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        tickets = order.orderticket_set.all()
    else:
        tickets = []

    context = {"tickets":tickets}
    return render(request, "rides/checkout.html", context)


def updateTicket(request):
    data = json.loads(request.body)
    rideId = data['rideId']
    action = data['action']

    print('Action:', action)
    print('rideId:', rideId)

    customer = request.user.customer
    ride = Ride.objects.get(id=rideId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderTicket, created = OrderTicket.objects.get_or_create(order=order, ride=ride)

    if action == 'remove':
        orderTicket.delete()

    if action == 'add':
        orderTicket.save()

    return JsonResponse('ticket added to cart', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id
        order.complete = True
        order.save()
    else:
        print('Not logged in')
    return JsonResponse('ticket ordered', safe=False)