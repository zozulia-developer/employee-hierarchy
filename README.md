# Django Employee Management System

This is a Django project for managing employees. It includes features for adding, editing, and deleting employees, as well as managing their positions.

---

## Installation

1. Clone the repository:
```sh
git clone https://github.com/zozulia-developer/employee-hierarchy.git
```

2. Navigate to the project directory:
```sh
cd employee-hierarchy
```

3. Create a virtual environment:
```sh
python -m venv venv
```

4. Activate the virtual environment:
- On Windows:
```sh
venv\Scripts\activate
```
- On macOS and Linux:
```sh
source venv/bin/activate
```

5. Install the required packages:
```sh
pip install -r requirements.txt
```

6. Run database migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser:
```sh
 python manage.py createsuperuser
```

8. Collect static files:
```sh
python manage.py collectstatic
```

---

## Usage

1. Start the development server:
```sh
python manage.py runserver
```

2. Open your web browser and go to http://127.0.0.1:8000/ to access the application.
3. Use the admin interface to manage employees and positions:
- `http://127.0.0.1:8000/admin/`
