#-# Class #15 - Installation & Configuration Django

## 1. Create & Active Virtual Environment
#- Creating Project Folder
#- Creating and Activating Virtual Environment


## 2. Install Necessary Package
#- Installing Django
#- Checking List Command: pip list


## 3. Create Project and App
#- Creating Project Command: django-admin startproject eshop .
#- Running Server: python manage.py runserver
#- Migrating admin, auth, contenttypes, sessions: python manage.py migrate
#- Creating Superuser: python manage.py createsuperuser
#- username: admin, email: admin@gmail.com, password: #abcd1234
#- Creating App: py manage.py startapp store


## 4. Configuration App with Project
#- adding 'store' appat INSTALLED_APPS in Project's settings.py (Same for others apps)
#- Including 'store.urls' in urls.py of Project (Same for others apps)
#- Creating urls.py in store app folder (Same for others apps)



## 5. Write some Function and run the Project