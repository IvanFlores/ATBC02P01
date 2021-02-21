# ATBC02P01
Jalasoft Automation BootCamp 01 - Project 01

## Requirements

1. Python 3.9

## Steps you should follow:

1. Install Django framework:
```sh
pip install Django --user
```

2. Install mysqlclient: (verify with development team)
```sh
pip pip install mysqlclient
```
3. (Option 1) When working with an MySQl database:
Install XAMPP: [Download from here](https://www.apachefriends.org/download.html)![Step 3 image](ATBC02P01\resources\img-step3.png)
![XAMPP installer used](ATBC02P01\resources\xampp_installer_used.png)

3. (Option 2) When working with an SQlLite3 database:
   [working]

4. Make sure that MySQL is running in port 3306:
![Step 4 image](ATBC02P01\resources\img-step3.png)
   
5. Create a database named: atbc02_project
![Step 5 image](ATBC02P01\resources\img-step4.png)
   
6. Run migrations to create de tables in the DataBase
```sh
python manage.py migrate
```
This will create the following tables:
- auth_group
- auth_group_permissions
- auth_permission
- auth_user
- auth_user_groups
- auth_user_user_poermissions
- django_admin_log
- django_content_type
- django_migrations
- django_session

7. Create a Super User:
```sh
python manage.py createsuperuser

User: [register the user name you want to create]
Email address: [register your email address]
Password: [register your password and its confirmation]
```
8. Run the application:
```sh
python manage.py runserver
```
