from django.urls import path

from .views import (
    ticket_create,
    ticket_delete,
    ticket_detail,
    ticket_list,
    ticket_update,
)


urlpatterns = [
    path("", ticket_list, name="ticket_list"),

    path(
        "create/",
        ticket_create,
        name="ticket_create",
    ),

    path(
        "<int:pk>/",
        ticket_detail,
        name="ticket_detail",
    ),

    path(
        "<int:pk>/edit/",
        ticket_update,
        name="ticket_update",
    ),

    path(
        "<int:pk>/delete/",
        ticket_delete,
        name="ticket_delete",
    ),
]