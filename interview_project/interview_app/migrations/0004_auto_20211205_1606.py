# Generated by Django 3.2.9 on 2021-12-05 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview_app', '0003_alter_physicalport_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physicalport',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='physicalport',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='interview_app.physicalport'),
            preserve_default=False,
        ),
    ]
