**Event Registration System – Django**

A web-based application built with Django that allows users to register for events and enables hosts to manage them. 
The project utilizes PostgreSQL for data storage and is structured to support future Docker integration.

**Features**

User Authentication: Secure registration and login functionalities.

Event Management: Hosts can create, update, and delete events.

Participant Registration: Users can register for available events.

Admin Dashboard: Superusers can oversee users and events via Django Admin.

PostgreSQL Integration: Robust database management with Django ORM.

**Technologies Used**

Backend: Django 4.x

Database: PostgreSQL

Frontend: HTML, CSS

Environment Management: Python Virtual Environment (eventenv)

Version Control: Git & GitHub

**Installation & Setup**

1.Clone the Repository:
git clone https://github.com/Sagargowda1605/Event-Registration-Django.git
cd Event-Registration-Django

2.Create and Activate Virtual Environment:
  python -m venv eventenv
eventenv\Scripts\activate   # For Windows

3.Install Dependencies:
	pip install -r requirements.txt

4. Alter the Database Settings in settings.py
   DB_NAME=your_db_name
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432

5. Apply Migrations:
   python manage.py makemigrations
	 python manage.py migrate


6. Run the Development Server:
   python manage.py runserver



Project Structure:
Event-Registration-Django/
├── EventRegistration/        # Project settings
├── events/                   # Core application
├── templates/                # HTML templates
├── static/                   # Static files (CSS, JS, images)
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── .gitignore                # Git ignore file
└── .env                      # Environment variables (excluded from Git)
