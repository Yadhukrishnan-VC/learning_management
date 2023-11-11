# Learning_management


# Learning_management - Django Project
## Overview

short course management is a Django web application that allows you to manage and organize information about some courses. It provides features for adding, editing,deleting and filtering course's details. This README provides essential information about setting up, running, and customizing the project.

## Features

- Add, List, edit, and delete Courses
- Filter courses by the title.
- User authentication for admin access.
- Use of SqLite3 as the database backend.
- AJAX-based filtering.
- Pagination

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x) and pip installed on your development environment.
- Git installed to clone the project repository.
- SQlite database setup.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Yadhukrishnan-VC/learning_management.git

1. Create a Virtual env:
     Enter the directory (cd learning_management)
     pipenv shell
2. Install project dependencies:
      pip install -r requirements.txt
   
3. Apply Migrations :
     python manage.py makemigrations
     python manage.py migrate

4. Start the server:
     python manage.py runserver
     Access the project at http://localhost:8000/ in your web browser.


### Credentials

     Use login Credentials for testing purpose

     username/email:
          admin@gmail.com
     password:
          admin12345678





   