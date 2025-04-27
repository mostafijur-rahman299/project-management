# Project Management - Project Setup Guide

This guide provides step-by-step instructions to set up the Project Management project.

## Prerequisites

- Python 3.10 or higher
- PostgreSQL (optional; SQLite used for development)

## Setup Instructions
### 1. Clone the Repository

```bash
git clone <repository-url>
cd ProjectManagement
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL (Optional)
For production, configure PostgreSQL:

```bash
brew install postgresql
brew services start postgresql
psql -U $USER
```

> For development, you can skip this step to use SQLite

### 5. Configure Environment Variables
Copy .env.example to .env and update with your settings:

```bash
cp .env.example .env
```

### 6. Run Database Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 7. Create a Superuser (Optional)
To access the admin panel:

```bash
python3 manage.py createsuperuser
```

### 8. Start the Development Server
```bash
python3 manage.py runserver
```

### Access the Application
Admin Panel: `http://127.0.0.1:8000/admin/`
