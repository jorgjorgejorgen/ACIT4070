from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("update-ticket/", views.updateTicket, name="update-ticket"),
    path("process-order/", views.processOrder, name="process-order"),
    path("my-tickets/", views.myTickets, name="my-tickets"),
]