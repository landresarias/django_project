
Step 1: Django Installation --

1. Make sure to have Python 3 installed

2. Create a virtual environment by navigating to the folder you want to create it in and entering: 
py -m venv project-name

3. Start(activate) the virtual environment: project-name\Scripts\activate.bat

4. You’ll now see “(project-name)” next to the command prompt to designate that you’re in your virtual 
environment.

Note: You must activate the virtual environment every time you open the command prompt to work on your project.

5. Install Django: py -m pip install Django (Remember to install Django while you are in the virtual environment!)

6. Verify installation with: django-admin --version

Step 2: Initialize Project --

1. In your virtual environment command line, run: django-admin startproject first_project. This creates 
the workspace that will encapsulate all of your applications and your config files.

2. cd into first_project.

3. Run: py manage.py runserver and open up localhost:8000 to see if you get 
a site with an animated rocket that tells you your install worked!

Paso 3: Crear aplicación --

1. Run: py manage.py startapp first_app

2. Configure application in project. Look for the INSTALLED_APPS variable in the settings.py file of the 
first_project folder. After the final application in the list, add the name of our application as a string.

3. Import the HttpResponse package from the HTTP Django module to create a view.
from django.http import HttpResponse

4. Create a view function:
def index(request):
    return HttpResponse(“Hello World!”)

5. Use Project URL Mapper to route to application view:
Navigate to first_project/urls.py
Import from first_app import views at the top of the file
In the urlpatterns list, add the following:
path('',views.index,name="index")       

6. Execute Project: Run (Mac) python3 manage.py runserver or (Windows) py manage.py runserver and open up 
port 8000 to see the result of our example!



