# Django Project (Doggy Daycare)

## Description

This is my Django project for Capstone 1 in Hyperion Dev's Software Engineering Boot Camp.
This site is insipred by Trello© (but for pets!)

It allows logged in users to view bookings that have been added by a receptionist (admin user for the Django site)

### Unsigned In User
  - Cannot view anything except for the home/login page

### Regular User
  - Can view bookings

### Admin User
  - Can view and add bookings on the web page

## Installation

In order to install this site, I will assume a few things:
1. You are on a Windows device (if not check the commands for your system instead [it will be the same commands just different syntax]).

1. You have Pip installed.

1. You have Python installed.

1. You have a code editor installed (my project was created in VSC)

## Bash commands
1. Open a CMD/Powershell terminal

   win + "cmd"

1. Chnage into your working directory

   ```bash
   cd to/path/of/your/choice

1. Clone this GitHub repository to your local machine:

   ```bash
   git clone https://github.com/FinnlyFox/Doggy-Daycare.git

1. Change into the main project directory (The sturcure I created)

   ```bash
   cd Doggy-Daycare

1. (Optional but recommended) Set up a virtual environment

   ```bash
   python -m venv venv

1. Change into the django project directory

   ```bash
   cd MySite

1. (Optional if you wish to access the admin features of the site) Create an admin user
   To log into the admin section use [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) after the server is running.
   ```bash
   python manage.py createsuperuser
   
   - EXAMPLE -
   Username: admin
   Email address: admin@example.com
   Password: ********
   Password (again): ********

## Credits

   This project was created by Joel Whyle.
