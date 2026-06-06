from django.shortcuts import render
from .models import Order, Portfolio, Comment
from datetime import date


def home(request):
    if request.method == "POST":
        client_name = request.POST.get("client_name")
        service = request.POST.get("service")

        order = Order.objects.create(
            client_name=client_name,
            project_name=service,
            status="Pending Payment",
            progress=0,
            delivery_date=date.today()
        )

        portfolios = Portfolio.objects.all()

        return render(request, "home.html", {
            "success": True,
            "order_id": order.order_id,
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
