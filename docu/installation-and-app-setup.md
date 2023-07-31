# Installation and App Setup

1. Create a virtual environment

```console
mkdir django-crm-app
cd django-crm-app
python -m venv virt
source virt/Scripts/activate
```

2. Install Django

```console
pip install django
```

3. Install MySQL

```console
pip install mysql
pip install mysql-connector
pip install mysql-connector-python
```

4. Download MySQL
   Download MySQL [here](https://dev.mysql.com/downloads/installer/)

5. Starting a New Django Project
   To create a new Django project with the projectname dcrm run the following command:

```console
django-admin startproject dcrm
```

6. Start app

```console
cd dcrm
python manage.py startapp website
```
