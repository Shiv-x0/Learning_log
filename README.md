# Learning Log

Learning Log is a simple Django web application that helps users create and manage personal learning topics and journal entries. It is designed to be easy to use, clean, and practical for tracking what you learn over time.

The project includes user registration and login, topic creation, entry management, and a polished interface built with Django and Bootstrap.

## Demo

You can view the deployed project here:

- https://learning-logs-tr17.onrender.com/

## Features

- User registration and login
- Create, view, and manage learning topics
- Add detailed journal entries under each topic
- Clean, responsive UI with Bootstrap styling
- Ready for deployment using Render

## Tech Stack

- Python
- Django
- Bootstrap 5
- SQLite for local development
- Render for deployment

## Project Structure

- Learning_Logs/ — main app for topics and entries
- accounts/ — user authentication and registration
- templates/ — shared templates
- LL_project/ — Django project settings and URLs

## Screenshots

You can add screenshots here once you have them ready:

![Django Logo](https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Shiv-x0/Learning_log.git
   cd Learning_log
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations
   ```bash
   python manage.py migrate
   ```

5. Start the development server
   ```bash
   python manage.py runserver
   ```

## Deployment

This project is prepared for deployment on Render.

### Render setup

- Build Command:
  ```bash
  pip install -r requirements.txt
  ```

- Start Command:
  ```bash
  bash start.sh
  ```

## Notes

This project was built as a practical learning project to strengthen Django skills, especially around authentication, forms, models, templates, and deployment.

## Author

Built with care by Shiv.
