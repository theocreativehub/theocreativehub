from django.shortcuts import render
from .models import Order, Portfolio, Comment
from datetime import date


def home(request):

    if request.method == "POST":

        client_name = request.POST.get("client_name")
        service = request.POST.get("service")

        order_count = Order.objects.count() + 1
        order_id = f"THC-{order_count:04d}"

        Order.objects.create(
            order_id=order_id,
            client_name=client_name,
            project_name=service,
            status="Pending",
            progress=0,
            delivery_date=date.today()
        )

        portfolios = Portfolio.objects.all()

        return render(request, "home.html", {
            "success": f"Order Submitted successfully! Your Order ID is {order_id}",
            "portfolios": portfolios
        })

    portfolios = Portfolio.objects.all()

    return render(request, "home.html", {
        "portfolios": portfolios
    })

def tracking(request):

        order = None
        error = None

        if request.method == "POST":

            if "order_id" in request.POST:

                order_id = request.POST.get("order_id")

                try:
                    order = Order.objects.get(order_id=order_id)

                except Order.DoesNotExist:
                    error = "Order not found"

            elif "comment" in request.POST:

                order_id = request.POST.get("hidden_order_id")

                order = Order.objects.get(order_id=order_id)

                Comment.objects.create(
                    order=order,
                    message=request.POST.get("comment")
                )

        return render(request, "tracking.html", {
            "order": order,
            "error": error
})
