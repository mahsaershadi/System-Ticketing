# Tickify — Ticket Management System

A full-stack ticket management web application built with **Django** and **PostgreSQL**.

Tickify allows authenticated users to create, view, edit, and delete tickets while providing filtering and sorting functionality. The interface was designed from scratch with HTML and CSS and uses a dark indigo/lavender visual style.

---

## Preview

> Added screenshots of the application here to showcase the UI.

### Dashboard

![Tickify Dashboard](docs/screenshots/dashboard.jpg)

### Create Ticket

![Create Ticket](docs/screenshots/create-ticket.jpg)

### Ticket Details

![Ticket Details](docs/screenshots/ticket-detail.jpg)

### Edit Ticket

![Edit Ticket](docs/screenshots/edit-ticket.jpg)

### Delete Confirmation

![Delete Ticket](docs/screenshots/delete-ticket.jpg)

---

## Features

### Authentication
- User registration
- User login
- User logout
- Django's built-in authentication system
- Password hashing handled by Django

### Ticket Management
- Create tickets
- View ticket details
- Edit tickets
- Delete tickets
- Ticket status management:
  - Open
  - In Progress
  - Closed
- Ticket priority:
  - Low
  - Medium
  - High

### Filtering & Sorting
- Filter tickets by status
- Filter tickets by priority
- Sort by newest
- Sort by oldest
- Sort by priority

### Authorization
- Regular users can access their own tickets
- Staff/admin users can access all tickets
- Ticket ownership is enforced on detail, edit, and delete operations

### Frontend
- Responsive HTML5/CSS3 interface
- Dark UI
- Indigo/lavender accent color system
- Responsive ticket forms
- Ticket status and priority badges
- Confirmation UI for destructive actions
- Consistent navigation and reusable base template

### Database
- PostgreSQL database
- Django ORM
- User-to-ticket relationship through `created_by`
- Django migrations for database schema management

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Django | Web framework |
| PostgreSQL | Database |
| psycopg | PostgreSQL driver |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| Git | Version control |

---

## Project Structure

```text
System Ticketing/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       └── register.html
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── tickets/
│   ├── migrations/
│   ├── templates/
│   │       ├── ticket_list.html
│   │       ├── ticket_detail.html
│   │       ├── ticket_form.html
│   │       └── ticket_confirm_delete.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│       └── style.css
│
├── templates/
│   └── base.html
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Database Model

The main application model is `Ticket`.

Each ticket contains:

```text
Ticket
├── title
├── description
├── priority
├── status
├── created_by
├── created_at
└── updated_at
```

The `created_by` field is a foreign key to Django's built-in `User` model.

```text
User
  │
  └── creates
       │
       ├── Ticket
       ├── Ticket
       └── Ticket
```

---

## Main Routes

| Route | Description |
|---|---|
| `/` | Ticket dashboard |
| `/accounts/register/` | User registration |
| `/accounts/login/` | User login |
| `/accounts/logout/` | User logout |
| `/create/` | Create a ticket |
| `/<id>/` | View ticket |
| `/<id>/edit/` | Edit ticket |
| `/<id>/delete/` | Delete ticket |
| `/admin/` | Django admin panel |
