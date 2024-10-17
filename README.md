# Insurance Order Management System

## Overview

This project is an API and Admin panel-driven insurance order management system for an insurance company. It allows customers to create insurance orders for different insurance products and track the status of their orders. Administrators can manage the insurance products and orders via the Django admin panel.

## Features

- Customers can:
  - Register and log in to the system.
  - View available insurance products.
  - Place orders for insurance products.
  - Track the status of their orders.
  
- Administrators can:
  - Add, edit, and deactivate insurance products.
  - Approve or decline customer orders via the admin panel.

## Technologies Used

- **Python 3.11+**
- **Django 5.x**
- **Django Rest Framework** (for API)
- **PostgreSQL** (Database)
- **Docker** (for containerization)

## Project Structure

```
insurance-order-management/
│
├── insurance_management/         # Main Django project folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Project-level URL configuration
│   └── wsgi.py
│
├── insurance/                    # Insurance app
│   ├── __init__.py
│   ├── admin.py                  # Admin panel configuration
│   ├── apps.py
│   ├── migrations/               # Database migrations folder
│   │   └── __init__.py
│   ├── models.py                 # Models for insurance products, orders, and custom user
│   ├── serializers.py            # DRF serializers
│   ├── tests.py                  # API tests
│   ├── urls.py                   # App-level URL configuration
│   └── views.py                  # API views
│
├── Dockerfile                    # Docker setup for the app
├── docker-compose.yml            # Docker Compose configuration
└── README.md                     # This file
```

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Docker and Docker Compose
- Python 3.11+ (optional, but required if running without Docker)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/elmaraliyevdev/insurance-order-management.git
cd insurance-order-management
```

### 2. Environment Variables

Make sure to set up any necessary environment variables, including database credentials, in the docker-compose.yml file.

### 3. Build and Run the Application Using Docker

You can build and run the application using Docker by running the following commands:

```bash
docker-compose up --build
```

This will set up the database and the Django application inside Docker containers.

### 4. Apply Migrations

Once the containers are running, open a new terminal window and run:

```bash
docker-compose exec web python manage.py migrate
```

This will apply the necessary database migrations.

### 5. Create a Superuser

To access the Django admin panel, create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to set up the admin credentials.

### 6. Access the Application

* The Django development server will be running at: http://localhost:8000/

* The Django Admin panel can be accessed at: http://localhost:8000/admin/

Use the superuser credentials to log in.

## API Endpoints

The system exposes the following API endpoints:

GET /api/v1/products/: Fetch all active insurance products.

GET /api/v1/orders/: Fetch all orders for the logged-in user.

POST /api/v1/order/create/: Create a new insurance order.

GET /api/v1/order/`id`/status/: Get the status of a specific order.

### Sample API Requests

You can use tools like Postman or curl to test the API.

Fetch Active Products:

```bash
GET /api/v1/products/
```

Create a New Order (requires login):

```bash
POST /api/v1/order/create/
{
    "product": 1
}
```

## Running Tests

To run the tests:

```bash
docker-compose exec web python manage.py test
```

This will run the unit tests to ensure the API and models are functioning correctly.

## Docker Deployment

This project is containerized using Docker. The docker-compose.yml file contains the configurations to run the Django application and PostgreSQL database in separate containers.

### Commands

Build and run the app:

```bash
docker-compose up --build
```

Shut down the containers:

```bash
docker-compose down
```

## Conclusion

This project demonstrates a simple insurance order management system with API functionality and admin panel control. The system is built using Django, Django Rest Framework, and PostgreSQL, and containerized with Docker for easy deployment.