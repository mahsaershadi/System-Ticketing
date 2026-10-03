from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TicketForm
from .models import Ticket


@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by("-created_at")

    return render(
        request,
        "tickets/ticket_list.html",
        {"tickets": tickets},
    )


@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    return render(
        request,
        "tickets/ticket_detail.html",
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
        "tickets/ticket_form.html",
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
        "tickets/ticket_form.html",
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
        "tickets/ticket_confirm_delete.html",
        {"ticket": ticket},
    )