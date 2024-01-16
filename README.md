# Deploy Django project with Docker, Nginx and Gunicorn

## Why are we going to do this?

- When the process of a Django project is finished, in order to publish this project, we must load it on a host or VPS (virtual private server).

## Why do we use Nginx and Gunicorn?

- Django not serving your static files in debug False. you need to serve it with web server like nginx, apache or etc.
- debug False used in production environment. in production environment you used another tools to run django.

## What is Nginx?

- Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy, and HTTP cache.
- Static files ->Files that are not affected by the server code. For example, CSS and Image files used in a landing page.
- Media files -> Files uploaded by users.

# let's start

## Setup Django

### 1. Install Django and create an app

- create virtual environment
```markdown
python3 -m venv venv
```

- activation virtual environment (The following command is for activation in ubuntu.)
```markdown
source venv/bin/activate
```

- install django
```markdown
pip install django
```

- install gunicorn - python WSGI HTTP server
```markdown
pip install gunicorn
```

- create project
```markdown
django-admin startproject project .
```

- create app
```markdown
python manage.py startapp myapp
```


### The structure of the project so far is as follows :
