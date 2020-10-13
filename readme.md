# Modules included :

1. Forgot password Api
2. Create/update/delete module 
3. admin, teacher,student based permissions based on groups and permission
4. customized permissions based on groups 
5. signup module.
6. Database setup is there 
7. login module using jwt is there 
8. token based authentcation is provided.


### database setup

#### For development phase , used the db.sqlite database
#### For production phase , used the postgresql database

### steps to setup project

run these commands after opening project

1. pip install virtualenv
2. virtualenv vnv
3. pip install -r requirements.txt

##### Now set the credentials of database and email address in settings.py

4. python manage.py migrate 
5. python manage.py createsuperuser
6.  python manage.py runserver


### urls:
##### http://127.0.0.1:8000/api/
##### http://127.0.0.1:8000/api/password_reset/
##### http://127.0.0.1:8000/signup/
##### http://127.0.0.1:8000/login/


install packages provided in requirements.txt file
