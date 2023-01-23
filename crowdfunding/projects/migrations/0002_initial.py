# Generated by Django 4.1.5 on 2023-01-17 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pledge',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.project'),
        ),
        migrations.AddField(
            model_name='pledge',
            name='supporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporter_pledges', to=settings.AUTH_USER_MODEL),
        ),
    ]
