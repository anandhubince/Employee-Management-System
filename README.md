# Employee Management System

A web-based Employee Management System developed using Python and Django. This project helps manage employee information through a simple interface with user authentication and CRUD operations.

## Project Overview

The Employee Management System allows registered users to manage employee records. Users can add new employees, view employee details, update existing information, and delete employee records.

The project also includes a Django Admin Panel for administrative management.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Tools:** Visual Studio Code, Git, GitHub

## Features

### User Authentication
- User Registration
- User Login
- User Logout
- Login-protected employee management pages

### Employee Management
- Add new employees
- View employee details
- Edit employee information
- Delete employee records

### Django Admin Panel
- Manage employee records
- Search employees
- Filter employee records by department and joining date
- View customized employee details

### User Interface
- Responsive page design
- Custom CSS styling
- Loading animation

## Application URLs

After starting the Django development server, access the application using these URLs:

| Page | URL |
|---|---|
| User Registration | http://127.0.0.1:8000/employees/register/ |
| User Login | http://127.0.0.1:8000/employees/login/ |
| View Employees | http://127.0.0.1:8000/employees/view/ |
| Add Employee | http://127.0.0.1:8000/employees/add/ |
| Django Admin | http://127.0.0.1:8000/admin/ |

**Note:** Employee management pages require user login. Register or log in before accessing them.

These are local development URLs. They work when the project is running on your computer.

## Project Structure

```text
employee_management/
│
├── employee_project/
│   ├── settings.py
│   ├── urls.py
│
├── employees/
│   ├── migrations/
│   ├── templates/
│   │   ├── add_employee.html
│   │   ├── view_employees.html
│   │   ├── edit_employees.html
│   │   ├── delete_employee.html
│   │   ├── register.html
│   │   └── login.html
│   │
│   ├── static/
│   │   └── employees/
│   │       └── style.css
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

## Installation and Setup

Follow these steps to run the project on your local computer.

### 1. Clone the Repository

```bash
git clone https://github.com/anandhubince/Employee-Management-System.git
```

### 2. Navigate to the Project Folder

```bash
cd Employee-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

To access the Django Admin Panel:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your admin account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/employees/register/

## Learning Outcomes

Through this project, I gained practical experience in:

- Python and Django web development
- Django MVT architecture
- Database operations using Django ORM
- CRUD functionality
- User authentication and authorization
- Django Admin customization
- HTML and CSS integration
- Git and GitHub

## Future Improvements

- Improve responsive design.
- Add employee profile images.
- Add employee search and pagination.
- Add dashboard statistics.
- Deploy the application online.

## Author

**Anandhu Bince**

- GitHub: https://github.com/anandhubince
- LinkedIn: https://linkedin.com/in/anandhubince

---

*Developed as a learning project using Python and Django.*
