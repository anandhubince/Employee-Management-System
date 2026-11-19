# Employee Management System

A web-based Employee Management System developed using Python and Django to manage employee information efficiently.

## Features

- User Registration and Login
- User Authentication
- Add Employee Details
- View Employee Records
- Edit Employee Information
- Delete Employee Records
- Django Admin Panel
- Employee Search and Filtering

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
employee_management/
├── employee_project/
├── employees/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anandhubince/Employee-Management-System.git
```

### 2. Navigate to the Project

```bash
cd Employee-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Django Admin

Create an administrator account:

```bash
python manage.py createsuperuser
```

Admin URL: http://127.0.0.1:8000/admin/

## Learning Outcomes

- Django MVT Architecture
- CRUD Operations
- User Authentication
- Django ORM
- Database Management
- Django Admin Customization

## Author

**Anandhu Bince**

GitHub: [anandhubince](https://github.com/anandhubince)

LinkedIn: [Anandhu Bince](https://linkedin.com/in/anandhubince)

---

Developed as part of my Python and Django learning journey.
