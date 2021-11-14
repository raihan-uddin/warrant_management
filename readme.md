## Prerequisites
1. Python
2. Pycharm
## Installation
```bash
git clone  git@gitlab.com:raihan-uddin/warrant_management.git
```
## Create a virtual environment using pycharm

Press Ctrl+Alt+S to open the project Settings/Preferences and go to Project <project name> | Python Interpreter. Then click the The Configure project interpreter icon and select Add.

In the left-hand pane of the Add Python Interpreter dialog, select Virtualenv Environment. The following actions depend on whether the virtual environment existed before.

## Installing framework & Dependencies
Open terminal on project folder & run this command to install dependencies
```
pip install -r requirements.txt
```

## Database Migration
```
python manage.py migrate
```

##### Create SuperUser

`python manage.py createsuperuser` Enter your desired username and press enter.

`Username: admin`. You will then be prompted for your desired email address:

`Email address: admin@example.com`. ...

`Password: **********` 

`Password (again): *********` Superuser created successfully.


### Runserver
```
python manage.py runserver
```


### Create APP
``` 
python manage.py startapp warrant 
```
Add new created app on `settings.py` file
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'warrant',
]
```

### Django Shell
`python manage.py shell`

 _note: for autocomplete install `pip install ipython` using terminal_ 



