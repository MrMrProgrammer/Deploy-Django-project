# Deploy Django project with Docker, Nginx and Gunicorn



### 1. Clone this repository in your project folder.


### 2. Install the gunicorn package.

```markdown
pip install gunicorn
```

### 3. Make the settings for the static and media files in the settings.py file. For this, add the following code in the settings.py file to your project.

```markdown
STATIC_URL = "static/"   # e.g. localhost:80/static/styles.css
MEDIA_URL = "media/"     # e.g. localhost:80/media/image.jpg

# directory where all static files of the app are going to be put
STATIC_ROOT = "/vol/static"

# directory where all files uploaded by users(media files) are going to be put
MEDIA_ROOT = "/vol/media"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
```

### 4. Change the name of the project in the ' ./scripts/start.sh ' file. The project name is in the settings.py file.

### 5. Access the start.sh file.

```markdown
chmod +x scripts/start.sh
```

### 6. Build Docker Image :
```markdown
docker-compose build --no-cache
```

### 7. Build Docker Containers :
```markdown
docker-compose up
```

---

### Enjoy your project :)

---
