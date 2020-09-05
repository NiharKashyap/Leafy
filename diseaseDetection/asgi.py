"""
ASGI config for diseaseDetection project.

It exposes the ASGI callable as a module-level variable named ``application``.
#Just putting it out there that this project was created by Nihar Kashyap and Prachurjya Gogoi
For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diseaseDetection.settings')

application = get_asgi_application()
