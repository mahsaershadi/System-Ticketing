from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm
from .models import Ticket


@login_required
def ticket_list(request):
    if request.user.is_staff:
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(
            created_by=request.user
        )
    status = request.GET.get("status")
    priority = request.GET.get("priority")
    sort = request.GET.get("sort")

    if status:
        tickets = tickets.filter(status=status)

    if priority:
        tickets = tickets.filter(priority=priority)

    if sort == "oldest":
        tickets = tickets.order_by("created_at")

    elif sort == "priority":
        from django.db.models import Case, IntegerField, Value, When

        tickets = tickets.annotate(
            priority_order=Case(
                When(priority="HIGH", then=Value(1)),
                When(priority="MEDIUM", then=Value(2)),
                When(priority="LOW", then=Value(3)),
                output_field=IntegerField(),
            )
    ).order_by("priority_order")

    else:
        tickets = tickets.order_by("-created_at")

    return render(
        request,
        "ticket_list.html",
        {
            "tickets": tickets,
            "selected_status": status,
            "selected_priority": priority,
            "selected_sort": sort,
        },
    )


@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    return render(
        request,
        "ticket_detail.html",
        {"ticket": ticket},
    )


@login_required
def ticket_create(request):

    if request.method == "POST":
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()

            return redirect(
                "ticket_detail",
                pk=ticket.pk,
            )

    else:
        form = TicketForm()

    return render(
        request,
        "ticket_form.html",
        {"form": form},
    )


@login_required
def ticket_update(request, pk):

    ticket = get_object_or_404(
        Ticket,
        pk=pk,
    )

    if request.method == "POST":
        form = TicketForm(
            request.POST,
            instance=ticket,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "ticket_detail",
                pk=ticket.pk,
            )

    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        "ticket_form.html",
        {
            "form": form,
            "ticket": ticket,
        },
    )


@login_required
def ticket_delete(request, pk):

    ticket = get_object_or_404(
        Ticket,
        pk=pk,
    )

    if request.method == "POST":
        ticket.delete()

        return redirect("ticket_list")

    return render(
        request,
        "ticket_confirm_delete.html",
        {"ticket": ticket},
    )