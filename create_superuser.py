import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopapp.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "anriykushnir05@example.com"
password = "199126"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
