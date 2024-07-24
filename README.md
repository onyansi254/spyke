Spyke
Spyke is a Django-based web application that tracks and displays geolocation data of clients using their IP addresses. It stores geolocation information and connection counts in a MySQL database, offering real-time insights into client locations.

Features
Client Location Detection: Retrieves geolocation data based on IP addresses.
Data Storage: Stores client addresses and connection counts in a MySQL database.
Index Page: Displays real-time geolocation data of the current client.
Django Integration: Utilizes Django framework and django-location library for geolocation services.
Technologies Used
Django: Web framework for building the application.
django-location: Library for geolocation services.
MySQL: Database for storing geolocation data.
Python: Programming language used for development.
Installation
Prerequisites
Python 3.6 or higher
MySQL
Git
Clone the Repository
Open Command Prompt or PowerShell.
Navigate to the directory where you want to clone the repository.
bash
Copy code
cd path\to\your\directory
Clone the repository:
bash
Copy code
git clone https://github.com/onyansi254/spyke.git
cd spyke
Create and Activate Virtual Environment
Create a virtual environment:
bash
Copy code
python -m venv venv
Activate the virtual environment:
bash
Copy code
.\venv\Scripts\activate
Install Dependencies
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Configure Database
Create a MySQL database and user using MySQL Workbench or Command Line.

Update the DATABASES section in spyke/settings.py with your MySQL credentials. Example configuration:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Apply Migrations
bash
Copy code
python manage.py migrate
Run the Development Server
bash
Copy code
python manage.py runserver
The application will be available at http://127.0.0.1:8000/.

Usage
Navigate to the index page to view the real-time geolocation data of the current client.
Access other endpoints as defined in your Django application.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Richard Otwoma - LinkedIn - GitHub
Email: ronyansi11@gmail.com
