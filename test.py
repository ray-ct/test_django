import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_new.settings")# project_name 项目名称
django.setup()

from django.contrib.auth.models import User

User.objects.create(username='hansuo',password='123')