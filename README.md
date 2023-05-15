## API using Token and IP Address Based Authentication
This API is built with Django Rest Framework and provides Token and IP Address Based Authentication. It receives data in JSON format and saves it to a database.

# Requirements
To run this API, you need the following software installed on your system:

- Python 3.x
- Django 3.x
- Django Rest Framework
- XAMPP
# Installation
- Clone the repository:
```
git clone https://github.com/your_username/your_project.git
cd your_project
```
- Setup the database:
1. Install and start XAMPP.
2. Start Apache and MySQL services from the XAMPP control panel.
3. Open a web browser and go to http://localhost/phpmyadmin.
4. Create a database named "django".
5. Edit the database settings in settings.py to match your local configuration:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Run the migrations:
```
python manage.py migrate
```
- Create a superuser:
```
python manage.py createsuperuser
```
- Start the development server:
```
python manage.py runserver
```
# Usage
To use this API, you can make requests to the available endpoints using a tool like curl or httpie, or you can use a web interface like Postman or Insomnia.

Before making requests, ensure that you have a token by sending a POST request to /api/obtain_token/ with your credentials in the payload. To include the token in subsequent requests to the endpoints, add an Authorization header with the value **Token <your_token_here>**.

For more details on how to use the API endpoints, please refer to the documentation provided in the Postman collection, which you can access here: [insert your Postman collection link here].
