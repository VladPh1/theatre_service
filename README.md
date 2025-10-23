# Theatre-Service Project

Django Project for managing theatre, which allows theatergoers to make 
reservations online and choose their desired seats without having to 
physically go to the theater.

## Installation

Python3 must be already installed

```shell

Install PosrgresSQL and create db

git clone https://github.com/VladPh1/theatre_service
cd theatre-service
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set DB_HOST = <your db hostname>
set DB_NAME = <your db name>
set DB_USER = <your db username>
set DB_PASSWORD = <your db user password>
set SECRET_KEY = <your secret key>
python manage.py migrate
python manage.py runserver # starts Django server
```

```Run with docker
Docker should be installed

docker-compose build
docker-compose up
```

## Getting access

* create user via /api/user/register
* get access token via /api/user/token

## Features

* Customer/User Authentication Feature
* Ticket Booking
* Convenient Admin Panel for Advanced Management
* JWT authenticated
* Documentation is located at /api/v1/doc/swagger
* Managing order and tickets
* Creating plays with genre, actors
* Creating theatre halls
* Adding Performance

Test User
```
User:
email: user_1@example.com
password: user_123

SuperUser:
email: admin@admin.com
password: 1qazcde3

```

## DB structure

[theatre_diagram.webp](theatre_diagram.webp)
