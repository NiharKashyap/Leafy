# Generated by Django 2.2.5 on 2020-04-22 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('potato', '0009_auto_20200421_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='histimage',
            name='user',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_expert',
            field=models.BooleanField(default=False),
        ),
    ]