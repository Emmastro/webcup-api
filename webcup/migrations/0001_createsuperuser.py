import os

from django.contrib.auth.models import User
from django.db import migrations


from django.contrib.auth import get_user_model
User = get_user_model()

def createsuperuser(apps, schema_editor):
    admin_password = os.environ["ADMIN_PASSWORD"] 
    User.objects.create_superuser("admin", password=admin_password)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(createsuperuser)
    ]