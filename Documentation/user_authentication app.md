Setup
---
"python3 manage.py (app name)" is a general command, used to create apps.
Flynarc API use one app for each data model.
1. Run in terminal:
- `python3 manage.py startapp user_authentication`
2. Add `'user_authentication',`to the bottom of the installed apps in settings.py
3. Create a `urls.py` and `serializers.py` file to the `user_authentication` directory

User Authentication app
---
In models, import:
- `from django.contrib.auth.models import User`
- `from django.db.models.signals import post_save`