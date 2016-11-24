# Django Order Management System (DOMS)

## About this application

This application is created by MD INZAMUL HAQUE for INFORTECH Solutions. This is a simple order management system. <br>
##### Framework: Django 1.10.1
##### Language : Python 3.6

## Demo
Link: https://www.youtube.com/watch?v=L5GLK_GmQ2g

## Install
- To change Database go to "DOMS/settings.py" and find "DATABASE = " then change database (visit here for more https://docs.djangoproject.com/en/1.10/ref/settings/#databases). Default Database is SQLite.

- Migrate Database by typing this:
```
python manage.py migrate
```
- Login:
	Username: inzamul36 <br>
	Password: 123456asdfgh

- To Add new user go to "DOMS/urls.py" uncomment this line:
```
# url(r'^admin/', admin.site.urls),
```
by deleting "#". Then login into admin(Django administration). click Users -> add and add user. 
- Again comment this line:
```
url(r'^admin/', admin.site.urls),
``` 
to hide admin(Django administration).

## Features
- Add order
- Export Order (pdf, excel, csv and etc)
- Edit / Delete Order
- Search Order
- Print Invoice
- Easy interface
- Mobile view

## Uses
* Restaurant Order
* Facebook Commerce
* etc...

### Contact me 
Facebook: facebook.com/inzamul36 <br>
Email: inzamul36@gmail.com, inzamuk36@live.com, inzamul36@yahoo.com    