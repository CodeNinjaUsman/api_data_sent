# API using Token and IP Address Based Authentication
This API is built with Django Rest Framework and provides Token and IP Address Based Authentication. It receives data in JSON format and saves it to a database.

## Requirements
To run this API, you need the following software installed on your system:

- Python 3.x
- Django 3.x
- Django Rest Framework
- XAMPP
## Installation
- Clone the repository:
```
git clone https://github.com/codeninjausman/api_data_sent
cd api_data_sent
```
- Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate
```
- Install the required packages:
```
pip install -r requirements.txt
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
## Usage
To use this API, you can make requests to the available endpoints using a tool like curl or httpie, or you can use a web interface like Postman or Insomnia.

Before making requests, ensure that you have a token by sending a POST request to **/api/obtain_token/** with your credentials in the payload. To include the token in subsequent requests to the endpoints, add an **Authorization header** with the value **Token <your_token_here>**.

For more details on how to use the API endpoints, please refer to the documentation provided in the Postman collection, which you can access here: [Collection Link..](https://red-crater-662608.postman.co/workspace/Team-Workspace~2822bb94-cce7-4f85-863e-3a7eee0dff1b/collection/25933712-c8e022c3-d06a-4118-b546-8f22511efe29?action=share&creator=25933712).

## Endpoints
The collection includes the following endpoints:
- Create User
1. **Endpoint:** /api/create_user/
2. **Method:** POST
3. **Description:** Creates a new user with the specified username and password.
- Obtain Token
1. **Endpoint:** /api/obtain_token/
2. **Method:** POST
3. **Description:** Obtains a token for a given user and IP address. Requires a JSON payload containing the username, password, and IP address.
- Change User IP
1. **Endpoint:** /api/ip_reset/
2. **Method:** POST
3. **Description:** Changes the IP address saved in the user object to the IP address from where the API endpoint is requested.
- Make User Staff
1. **Endpoint:** /api/change_user_status/
2. **Method:** POST
3. **Description:** Changes the user status to staff and requires the request.user to be a superuser.
- Retrieve All Data Sent
1. **Endpoint:** /api/data/
2. **Method:** GET
3. **Description:** Retrieves all the objects of data_sent related to the user with the specified ID.
- Save Data
1. **Endpoint:** /api/data/
2. **Method:** POST
3. **Description:** Saves data related to the request user. The IP address from where the API **Endpoint** is requested must match the IP address saved in the user object.
- Delete Data Sent
1. **Endpoint:** /api/data_delete_id/
2. **Method:** POST
3. **Description:** Deletes a specific data_sent object that has an ID matching the one in the request and is related to the request user.
- Remove All Data Sent
1. **Endpoint:** /api/data_delete/
2. **Method:** POST
3. **Description:** Removes all the objects of data_sent related to the user with the specified ID.
## Authorization
All Endpoints require a token obtained from **/api/obtain_token/** in the Authorization header of the request.
## Error Handling
If there is an error, the response will have an appropriate status code and an error message in the response body.
## Note
Before making requests, ensure that you have installed and configured the necessary dependencies and databases.
# THE END

